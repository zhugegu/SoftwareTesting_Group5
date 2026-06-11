"""Member D marshal stability tests.

This script tests marshal stability and correctness for recursive structures,
deep nesting, unsupported objects, shared references, marshal version parameters,
and invalid byte-stream deserialization.

It writes one JSON result file per platform/Python version.
"""

from __future__ import annotations

import hashlib
import json
import marshal
import platform
import sys
import tempfile
from pathlib import Path
from typing import Any, Callable


REPEAT_COUNT = 100
BASE_DIR = Path(__file__).resolve().parent
RESULTS_DIR = BASE_DIR / "results"


def sha256_hex(data: bytes) -> str:
    """Return the SHA-256 hex digest for bytes."""
    return hashlib.sha256(data).hexdigest()


def slug(value: str) -> str:
    """Return a filesystem-friendly lowercase identifier."""
    cleaned = []
    for char in value.strip().lower():
        if char.isalnum():
            cleaned.append(char)
        else:
            cleaned.append("_")
    return "_".join("".join(cleaned).split("_")) or "unknown"


def result_file_stem() -> str:
    """Return a result stem with system, machine, and Python major/minor."""
    system = slug(platform.system())
    machine = slug(platform.machine())
    py_major = sys.version_info.major
    py_minor = sys.version_info.minor
    return f"{system}_{machine}_py{py_major}_{py_minor}"


def environment_info() -> dict[str, Any]:
    """Collect Python and OS environment details."""
    return {
        "platform_platform": platform.platform(),
        "platform_system": platform.system(),
        "platform_machine": platform.machine(),
        "python_implementation": platform.python_implementation(),
        "sys_version": sys.version,
        "python_version_major_minor": (
            f"{sys.version_info.major}.{sys.version_info.minor}"
        ),
        "marshal_version": marshal.version,
        "recursion_limit": sys.getrecursionlimit(),
    }


def safe_repr(value: Any, max_length: int = 200) -> str:
    """Return a shortened repr so JSON output stays readable."""
    try:
        text = repr(value)
    except Exception as exc:  # noqa: BLE001
        text = f"<repr failed: {type(exc).__name__}: {exc}>"
    if len(text) > max_length:
        return text[:max_length] + "...<truncated>"
    return text


def build_self_list() -> list[Any]:
    """Build a list that directly references itself."""
    value: list[Any] = []
    value.append(value)
    return value


def build_self_dict() -> dict[str, Any]:
    """Build a dict that directly references itself."""
    value: dict[str, Any] = {}
    value["self"] = value
    return value


def build_indirect_cycle() -> list[Any]:
    """Build an indirect cycle: a -> b -> a."""
    first: list[Any] = []
    second = [first]
    first.append(second)
    return first


def build_deep_list(depth: int) -> list[Any]:
    """Build a nested list with the given depth."""
    value: Any = 0
    for _ in range(depth):
        value = [value]
    return value


def build_deep_tuple(depth: int) -> tuple[Any, ...]:
    """Build a nested tuple with the given depth."""
    value: Any = 0
    for _ in range(depth):
        value = (value,)
    return value


def build_shared_list() -> list[Any]:
    """Build an object where the same list is referenced twice."""
    shared = [1, 2, 3]
    return [shared, shared]


def build_nested_shared_reference() -> list[Any]:
    """Build a nested structure containing the same object twice."""
    shared = {"x": [1, 2]}
    return [shared, {"again": shared}]


def check_self_list(value: Any) -> bool:
    """Check whether a loaded self-referential list keeps the cycle."""
    return isinstance(value, list) and len(value) == 1 and value[0] is value


def check_self_dict(value: Any) -> bool:
    """Check whether a loaded self-referential dict keeps the cycle."""
    return (
        isinstance(value, dict)
        and "self" in value
        and value["self"] is value
    )


def check_indirect_cycle(value: Any) -> bool:
    """Check whether a loaded indirect cycle keeps the reference relation."""
    try:
        return value[0][0] is value
    except Exception:  # noqa: BLE001
        return False


def check_shared_list(value: Any) -> bool:
    """Check whether shared list identity is preserved after loads."""
    return (
        isinstance(value, list)
        and len(value) == 2
        and value[0] is value[1]
    )


def check_nested_shared_reference(value: Any) -> bool:
    """Check whether nested shared identity is preserved after loads."""
    try:
        return value[0] is value[1]["again"]
    except Exception:  # noqa: BLE001
        return False


def run_dumps_case(
    case_id: str,
    case_name: str,
    requirement_ids: list[str],
    test_method: str,
    build_value: Callable[[], Any],
    note: str,
    correctness_check: Callable[[Any], bool] | None = None,
    marshal_version: int | None = None,
    optional_support_probe: bool = False,
) -> dict[str, Any]:
    """Run repeated marshal.dumps() for one case and record stability data."""
    hashes: list[str] = []
    first_bytes = b""
    exception_type = None
    exception_message = None
    roundtrip_success = None
    roundtrip_correct = None
    value_type = None
    value_repr = None

    value = build_value()
    value_type = type(value).__name__
    value_repr = safe_repr(value)

    try:
        for index in range(REPEAT_COUNT):
            if marshal_version is None:
                data = marshal.dumps(value)
            else:
                data = marshal.dumps(value, marshal_version)

            if index == 0:
                first_bytes = data

            hashes.append(sha256_hex(data))

        try:
            loaded = marshal.loads(first_bytes)
            roundtrip_success = True
            if correctness_check is not None:
                roundtrip_correct = correctness_check(loaded)
            else:
                roundtrip_correct = safe_repr(loaded) == safe_repr(value)
        except Exception as exc:  # noqa: BLE001
            roundtrip_success = False
            roundtrip_correct = False
            exception_type = type(exc).__name__
            exception_message = str(exc)

    except Exception as exc:  # noqa: BLE001
        if not optional_support_probe:
            # We still record the exception instead of stopping the whole suite.
            pass
        exception_type = type(exc).__name__
        exception_message = str(exc)

    unique_hashes = sorted(set(hashes))

    return {
        "case_id": case_id,
        "case_name": case_name,
        "requirement_ids": requirement_ids,
        "test_method": test_method,
        "note": note,
        "operation": "dumps",
        "marshal_version_argument": marshal_version,
        "value_type": value_type,
        "value_repr": value_repr,
        "repeat_count": REPEAT_COUNT,
        "hashes": hashes,
        "unique_hashes": unique_hashes,
        "unique_hash_count": len(unique_hashes),
        "same_process_stable": len(unique_hashes) == 1 if hashes else None,
        "marshal_sha256": hashes[0] if hashes else None,
        "marshal_dumps_hex_prefix_160": first_bytes.hex()[:160],
        "roundtrip_success": roundtrip_success,
        "roundtrip_correct": roundtrip_correct,
        "exception_type": exception_type,
        "exception_message": exception_message,
        "optional_support_probe": optional_support_probe,
    }


def run_unsupported_type_case() -> dict[str, Any]:
    """Run TC-D06: unsupported type exception consistency."""
    subcases = []

    class CustomClass:
        """Simple custom class for unsupported instance testing."""

    def normal_function() -> int:
        return 1

    unsupported_builders: list[tuple[str, Callable[[], Any], str]] = [
        ("object_instance", object, "Plain object instance"),
        ("custom_class_instance", CustomClass, "User-defined class instance"),
        ("normal_function", lambda: normal_function, "Function object"),
        ("lambda_function", lambda: (lambda x: x), "Lambda function object"),
        ("generator_object", lambda: (x for x in range(3)), "Generator object"),
    ]

    for name, builder, note in unsupported_builders:
        subcases.append(
            run_dumps_case(
                case_id=f"TC-D06-{name}",
                case_name=f"Unsupported type: {name}",
                requirement_ids=["R5.3"],
                test_method="Equivalence partitioning; exception-flow testing",
                build_value=builder,
                note=note,
                optional_support_probe=True,
            )
        )

    temp_file = tempfile.TemporaryFile()
    try:
        subcases.append(
            run_dumps_case(
                case_id="TC-D06-file_object",
                case_name="Unsupported type: file object",
                requirement_ids=["R5.3"],
                test_method="Equivalence partitioning; exception-flow testing",
                build_value=lambda: temp_file,
                note="Open file object should not be marshal-serializable.",
                optional_support_probe=True,
            )
        )
    finally:
        temp_file.close()

    exception_signatures = sorted(
        {
            f"{item.get('exception_type')}:{item.get('exception_message')}"
            for item in subcases
        }
    )

    return {
        "case_id": "TC-D06",
        "case_name": "Unsupported type exception consistency",
        "requirement_ids": ["R5.3"],
        "test_method": "Equivalence partitioning; exception-flow testing",
        "operation": "dumps",
        "repeat_count": REPEAT_COUNT,
        "subcases": subcases,
        "subcase_count": len(subcases),
        "all_subcases_rejected": all(
            item.get("exception_type") is not None for item in subcases
        ),
        "exception_signatures": exception_signatures,
        "note": (
            "Unsupported types are expected to be rejected. "
            "The goal is stable and non-crashing exception behavior."
        ),
    }


def run_version_parameter_case() -> dict[str, Any]:
    """Run TC-D09: marshal version argument stability."""
    version_results = []
    value_builder = lambda: {"numbers": [1, 2, 3], "text": "member_d"}

    for version in range(0, marshal.version + 1):
        version_results.append(
            run_dumps_case(
                case_id=f"TC-D09-version-{version}",
                case_name=f"marshal.dumps version={version}",
                requirement_ids=["R5.5"],
                test_method="Boundary value analysis; protocol parameter test",
                build_value=value_builder,
                note=(
                    "Different marshal format versions may produce different "
                    "bytes, but each version should be stable by itself."
                ),
                marshal_version=version,
                optional_support_probe=True,
            )
        )

    return {
        "case_id": "TC-D09",
        "case_name": "marshal version parameter stability",
        "requirement_ids": ["R5.5"],
        "test_method": "Boundary value analysis; protocol parameter test",
        "operation": "dumps",
        "repeat_count": REPEAT_COUNT,
        "tested_versions": list(range(0, marshal.version + 1)),
        "subcases": version_results,
        "all_versions_stable_or_rejected": all(
            item.get("same_process_stable") is True
            or item.get("exception_type") is not None
            for item in version_results
        ),
        "note": (
            "Cross-version byte equality is not required. "
            "The expected property is deterministic output within the same "
            "version argument."
        ),
    }


def run_loads_case(
    case_id: str,
    case_name: str,
    data_builder: Callable[[], bytes],
    expected_success: bool,
    expected_value: Any | None,
    note: str,
) -> dict[str, Any]:
    """Run repeated marshal.loads() for one byte-stream case."""
    exception_types = []
    exception_messages = []
    loaded_reprs = []
    success_count = 0
    correctness_count = 0

    data = data_builder()
    data_hash = sha256_hex(data)

    for _ in range(REPEAT_COUNT):
        try:
            loaded = marshal.loads(data)
            success_count += 1
            loaded_reprs.append(safe_repr(loaded))
            if expected_success and loaded == expected_value:
                correctness_count += 1
        except Exception as exc:  # noqa: BLE001
            exception_types.append(type(exc).__name__)
            exception_messages.append(str(exc))

    unique_exception_types = sorted(set(exception_types))
    unique_exception_messages = sorted(set(exception_messages))
    unique_loaded_reprs = sorted(set(loaded_reprs))

    if expected_success:
        stable_behavior = (
            success_count == REPEAT_COUNT
            and correctness_count == REPEAT_COUNT
            and len(unique_loaded_reprs) == 1
        )
    else:
        stable_behavior = (
            success_count == 0
            and len(unique_exception_types) == 1
            and len(unique_exception_messages) == 1
        )

    return {
        "case_id": case_id,
        "case_name": case_name,
        "requirement_ids": ["R5.6"],
        "test_method": "Exception-flow testing; deserialization correctness",
        "operation": "loads",
        "repeat_count": REPEAT_COUNT,
        "input_bytes_length": len(data),
        "input_bytes_sha256": data_hash,
        "input_bytes_hex_prefix_160": data.hex()[:160],
        "expected_success": expected_success,
        "success_count": success_count,
        "correctness_count": correctness_count,
        "exception_types": exception_types,
        "exception_messages": exception_messages,
        "unique_exception_types": unique_exception_types,
        "unique_exception_messages": unique_exception_messages,
        "unique_loaded_reprs": unique_loaded_reprs,
        "stable_behavior": stable_behavior,
        "note": note,
    }


def run_invalid_bytes_loads_case() -> dict[str, Any]:
    """Run TC-D10: invalid byte-stream deserialization behavior."""
    valid_value = [1, 2, 3]
    valid_data = marshal.dumps(valid_value)
    deterministic_noise = b"\xe3\x00\xffnot marshal data"

    subcases = [
        run_loads_case(
            case_id="TC-D10-empty-bytes",
            case_name="loads empty bytes",
            data_builder=lambda: b"",
            expected_success=False,
            expected_value=None,
            note="Empty input should fail consistently.",
        ),
        run_loads_case(
            case_id="TC-D10-single-null",
            case_name="loads single null byte",
            data_builder=lambda: b"\x00",
            expected_success=False,
            expected_value=None,
            note="Invalid single-byte input should fail consistently.",
        ),
        run_loads_case(
            case_id="TC-D10-random-noise",
            case_name="loads deterministic noise bytes",
            data_builder=lambda: deterministic_noise,
            expected_success=False,
            expected_value=None,
            note="Non-marshal bytes should fail consistently.",
        ),
        run_loads_case(
            case_id="TC-D10-truncated-valid-data",
            case_name="loads truncated valid marshal data",
            data_builder=lambda: valid_data[:-1],
            expected_success=False,
            expected_value=None,
            note="Truncated marshal data should fail consistently.",
        ),
        run_loads_case(
            case_id="TC-D10-valid-data-with-extra-bytes",
            case_name="loads valid marshal data with trailing extra bytes",
            data_builder=lambda: valid_data + b"extra",
            expected_success=True,
            expected_value=valid_value,
            note=(
                "marshal.loads() is expected to ignore trailing bytes after "
                "one valid marshal object."
            ),
        ),
    ]

    return {
        "case_id": "TC-D10",
        "case_name": "Invalid byte-stream deserialization behavior",
        "requirement_ids": ["R5.6"],
        "test_method": "Exception-flow testing; deserialization correctness",
        "operation": "loads",
        "repeat_count": REPEAT_COUNT,
        "subcases": subcases,
        "subcase_count": len(subcases),
        "all_subcases_stable": all(
            item.get("stable_behavior") is True for item in subcases
        ),
        "note": (
            "This case extends member D from serialization-only tests to "
            "deserialization exception-flow tests."
        ),
    }


def build_all_cases() -> list[dict[str, Any]]:
    """Build and run all member D cases."""
    cases: list[dict[str, Any]] = [
        run_dumps_case(
            case_id="TC-D01",
            case_name="Self-referential list cycle",
            requirement_ids=["R5.1"],
            test_method="Exception-flow testing; white-box guided recursion test",
            build_value=build_self_list,
            note="Direct list cycle: a = []; a.append(a).",
            correctness_check=check_self_list,
            optional_support_probe=True,
        ),
        run_dumps_case(
            case_id="TC-D02",
            case_name="Self-referential dict cycle",
            requirement_ids=["R5.1"],
            test_method="Exception-flow testing; equivalence partitioning",
            build_value=build_self_dict,
            note='Direct dict cycle: d = {}; d["self"] = d.',
            correctness_check=check_self_dict,
            optional_support_probe=True,
        ),
        run_dumps_case(
            case_id="TC-D03",
            case_name="Indirect cyclic reference",
            requirement_ids=["R5.1"],
            test_method="White-box guided recursion test",
            build_value=build_indirect_cycle,
            note="Indirect cycle: a -> b -> a.",
            correctness_check=check_indirect_cycle,
            optional_support_probe=True,
        ),
    ]

    for depth in [10, 100, 500, 900, 1000]:
        cases.append(
            run_dumps_case(
                case_id=f"TC-D04-depth-{depth}",
                case_name=f"Deep nested list depth {depth}",
                requirement_ids=["R5.2"],
                test_method="Boundary value analysis",
                build_value=lambda depth=depth: build_deep_list(depth),
                note=f"Nested list boundary test with depth={depth}.",
                optional_support_probe=True,
            )
        )

    for depth in [10, 100, 500, 900, 1000]:
        cases.append(
            run_dumps_case(
                case_id=f"TC-D05-depth-{depth}",
                case_name=f"Deep nested tuple depth {depth}",
                requirement_ids=["R5.2"],
                test_method="Boundary value analysis; equivalence partitioning",
                build_value=lambda depth=depth: build_deep_tuple(depth),
                note=f"Nested tuple boundary test with depth={depth}.",
                optional_support_probe=True,
            )
        )

    cases.append(run_unsupported_type_case())

    cases.append(
        run_dumps_case(
            case_id="TC-D07",
            case_name="Shared list reference determinism",
            requirement_ids=["R5.4"],
            test_method="Correctness testing; repeated stability testing",
            build_value=build_shared_list,
            note="shared = [1, 2, 3]; obj = [shared, shared].",
            correctness_check=check_shared_list,
            optional_support_probe=True,
        )
    )

    cases.append(
        run_dumps_case(
            case_id="TC-D08",
            case_name="Nested shared reference determinism",
            requirement_ids=["R5.4"],
            test_method="Structural complexity extension; correctness testing",
            build_value=build_nested_shared_reference,
            note='shared = {"x": [1, 2]}; obj = [shared, {"again": shared}].',
            correctness_check=check_nested_shared_reference,
            optional_support_probe=True,
        )
    )

    cases.append(run_version_parameter_case())
    cases.append(run_invalid_bytes_loads_case())

    return cases


def count_result_items(cases: list[dict[str, Any]]) -> dict[str, int]:
    """Count stable, unstable, and exception outcomes including subcases."""
    flat_items = []

    for case in cases:
        if "subcases" in case:
            flat_items.extend(case["subcases"])
        else:
            flat_items.append(case)

    stable = 0
    unstable = 0
    exceptions = 0

    for item in flat_items:
        if item.get("operation") == "loads":
            if item.get("stable_behavior") is True:
                stable += 1
            else:
                unstable += 1
        elif item.get("exception_type") is not None:
            exceptions += 1
        elif item.get("same_process_stable") is True:
            stable += 1
        else:
            unstable += 1

    return {
        "flat_case_count": len(flat_items),
        "stable_count": stable,
        "unstable_count": unstable,
        "exception_count": exceptions,
    }


def main() -> None:
    """Run member D test suite and save current platform JSON."""
    RESULTS_DIR.mkdir(parents=True, exist_ok=True)
    cases = build_all_cases()
    counts = count_result_items(cases)

    output = {
        "member": "D",
        "topic": (
            "marshal stability tests for recursive structures, exceptions, "
            "shared references, version parameters, and invalid loads input"
        ),
        "environment": environment_info(),
        "repeat_count": REPEAT_COUNT,
        "top_level_case_count": len(cases),
        "result_counts": counts,
        "cases": cases,
    }

    result_path = RESULTS_DIR / f"member_d_all_{result_file_stem()}_results.json"
    result_path.write_text(
        json.dumps(output, ensure_ascii=False, indent=2),
        encoding="utf-8",
    )

    print(f"Wrote member D result JSON: {result_path}")
    print(
        "Summary: "
        f"flat_cases={counts['flat_case_count']}; "
        f"stable={counts['stable_count']}; "
        f"unstable={counts['unstable_count']}; "
        f"exceptions={counts['exception_count']}"
    )


if __name__ == "__main__":
    main()