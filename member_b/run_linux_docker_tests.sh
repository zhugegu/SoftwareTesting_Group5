#!/bin/sh

set -u

RESULTS_DIR="member_b/results"
TEST_SCRIPT="member_b/test_marshal_float_complex.py"
EXTRA_TEST_SCRIPT="member_b/test_member_b_scalar_binary_extensions.py"
UNIFIED_TEST_SCRIPT="member_b/test_member_b_all.py"
COMPARE_SCRIPT="member_b/compare_cross_platform.py"
EXTRA_COMPARE_SCRIPT="member_b/compare_scalar_binary_extensions.py"
UNIFIED_COMPARE_SCRIPT="member_b/compare_member_b_all_results.py"
PYTHON_IMAGE="python:3.12-slim"

error() {
    printf '%s\n' "$1" >&2
}

ensure_project_root() {
    if [ ! -f "$TEST_SCRIPT" ]; then
        error "Error: run this script from the project root."
        error "Expected to find: $TEST_SCRIPT"
        exit 1
    fi
}

ensure_docker() {
    if ! command -v docker >/dev/null 2>&1; then
        error "Error: Docker was not found."
        error "Install and start Docker Desktop, then rerun:"
        error "  sh tests/member_b_float_complex/run_linux_docker_tests.sh"
        exit 1
    fi
}

run_linux_test() {
    label="$1"
    platform_arg="$2"
    required="$3"

    before_files="$(mktemp)"
    after_files="$(mktemp)"

    find "$RESULTS_DIR" -maxdepth 1 -name 'linux_*_results.json' \
        -type f -print | sort >"$before_files"

    if [ -n "$platform_arg" ]; then
        docker run --rm \
            --platform "$platform_arg" \
            -v "$PWD:/work" \
            -w /work \
            "$PYTHON_IMAGE" \
            sh -c "python '$TEST_SCRIPT' && \
if [ -f '$EXTRA_TEST_SCRIPT' ]; then python '$EXTRA_TEST_SCRIPT'; fi && \
if [ -f '$UNIFIED_TEST_SCRIPT' ]; then python '$UNIFIED_TEST_SCRIPT'; fi"
    else
        docker run --rm \
            -v "$PWD:/work" \
            -w /work \
            "$PYTHON_IMAGE" \
            sh -c "python '$TEST_SCRIPT' && \
if [ -f '$EXTRA_TEST_SCRIPT' ]; then python '$EXTRA_TEST_SCRIPT'; fi && \
if [ -f '$UNIFIED_TEST_SCRIPT' ]; then python '$UNIFIED_TEST_SCRIPT'; fi"
    fi

    status=$?
    if [ "$status" -ne 0 ]; then
        rm -f "$before_files" "$after_files"
        if [ "$required" = "yes" ]; then
            error "Error: Docker test failed for $label."
            exit "$status"
        fi
        error "Warning: Docker test failed for optional $label."
        error "This can happen when linux/amd64 emulation needs Rosetta/QEMU."
        return 0
    fi

    find "$RESULTS_DIR" -maxdepth 1 -name 'linux_*_results.json' \
        -type f -print | sort >"$after_files"
    generated="$(comm -13 "$before_files" "$after_files" | tail -n 1)"

    if [ -z "$generated" ]; then
        generated="$(find "$RESULTS_DIR" -maxdepth 1 \
            -name 'linux_*_results.json' -type f \
            -exec ls -t {} + | head -n 1)"
    fi

    rm -f "$before_files" "$after_files"

    if [ -z "$generated" ] || [ ! -f "$generated" ]; then
        if [ "$required" = "yes" ]; then
            error "Error: could not find generated Linux result for $label."
            exit 1
        fi
        error "Warning: no generated Linux result found for optional $label."
        return 0
    fi

    printf 'Saved %s result: %s\n' "$label" "$generated"
}

main() {
    ensure_project_root
    ensure_docker
    mkdir -p "$RESULTS_DIR"

    run_linux_test \
        "default Linux platform" \
        "" \
        "yes"

    run_linux_test \
        "linux/amd64" \
        "linux/amd64" \
        "no"

    if command -v python >/dev/null 2>&1; then
        python "$COMPARE_SCRIPT"
        python "$EXTRA_COMPARE_SCRIPT"
        python "$UNIFIED_COMPARE_SCRIPT"
    elif command -v python3 >/dev/null 2>&1; then
        python3 "$COMPARE_SCRIPT"
        python3 "$EXTRA_COMPARE_SCRIPT"
        python3 "$UNIFIED_COMPARE_SCRIPT"
    else
        error "Error: neither python nor python3 was found on the host."
        exit 1
    fi
}

main "$@"
