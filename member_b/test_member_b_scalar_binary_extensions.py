"""Member B marshal stability tests for scalar and binary boundary inputs."""

from __future__ import annotations

import hashlib
import json
import marshal
import platform
import sys
from pathlib import Path
from typing import Any


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
        "marshal_version": marshal.version,
    }


def code_points(value: str) -> list[str]:
    """Return Unicode code points in U+XXXX notation."""
    return [f"U+{ord(char):04X}" for char in value]


def value_metadata(value: Any) -> dict[str, Any]:
    """Capture input metadata useful for byte-level comparisons."""
    if isinstance(value, str):
        encoded = value.encode("utf-8", errors="surrogatepass")
        return {
            "code_points": code_points(value),
            "utf8_length": len(encoded),
            "utf8_sha256": sha256_hex(encoded),
        }
    if isinstance(value, bytes):
        return {
            "bytes_length": len(value),
            "bytes_first_32_hex": value[:32].hex(),
            "bytes_sha256": sha256_hex(value),
        }
    return {}


def marshal_case(
    case_name: str,
    category: str,
    value: Any,
    logical_note: str,
) -> dict[str, Any]:
    """Marshal the same object repeatedly and record stability evidence."""
    hashes = []
    first_bytes = b""
    exception_type = None
    exception_message = None

    try:
        for index in range(REPEAT_COUNT):
            data = marshal.dumps(value)
            if index == 0:
                first_bytes = data
            hashes.append(sha256_hex(data))
    except Exception as exc:  # noqa: BLE001 - support probe records exceptions.
        exception_type = type(exc).__name__
        exception_message = str(exc)

    unique_hashes = sorted(set(hashes))
    result = {
        "case": case_name,
        "category": category,
        "repr": repr(value),
        "type": type(value).__name__,
        "logical_note": logical_note,
        "repeat_count": REPEAT_COUNT,
        "hashes": hashes,
        "unique_hashes": unique_hashes,
        "unique_hash_count": len(unique_hashes),
        "same_process_stable": len(unique_hashes) == 1 if hashes else None,
        "marshal_sha256": hashes[0] if hashes else None,
        "marshal_dumps_hex_prefix_160": first_bytes.hex()[:160],
        "exception_type": exception_type,
        "exception_message": exception_message,
    }
    result.update(value_metadata(value))
    return result


def unicode_cases() -> list[tuple[str, str, str]]:
    """Build unusual Unicode string cases without normalization."""
    return [
        ("ascii_plain", "hello", "Plain ASCII baseline string."),
        ("chinese_text", "中文测试", "Chinese BMP characters."),
        ("emoji_text", "emoji: 😀", "String containing an emoji."),
        ("nul_inside_string", "a\x00b", "String with embedded NUL."),
        ("crlf_string", "line\r\nbreak", "String containing CRLF."),
        ("non_bmp_character", "𐍈", "Single non-BMP character."),
        ("composed_e_acute", "é", "Precomposed Latin small e with acute."),
        ("decomposed_e_acute", "e\u0301", "Latin e plus combining acute mark."),
        ("lone_high_surrogate", "\ud800", "Lone high surrogate code point."),
        (
            "zero_width_joiner_sequence",
            "👩‍💻",
            "Emoji sequence joined by U+200D zero width joiner.",
        ),
    ]


def bytes_cases() -> list[tuple[str, bytes, str]]:
    """Build byte payload boundary cases."""
    return [
        ("bytes_empty", b"", "Empty bytes baseline."),
        ("bytes_single_nul", b"\x00", "Single embedded NUL byte."),
        (
            "bytes_high_values_with_ascii",
            b"\x00\xff\x80abc",
            "NUL, high byte values, and ASCII bytes.",
        ),
        ("bytes_all_byte_values", bytes(range(256)), "All byte values 0-255."),
        ("bytes_255_a", b"a" * 255, "Length boundary just below 256."),
        ("bytes_256_a", b"a" * 256, "Length boundary at 256."),
        ("bytes_65535_a", b"a" * 65535, "Length boundary just below 65536."),
        ("bytes_65536_a", b"a" * 65536, "Length boundary at 65536."),
    ]


def scalar_constant_cases() -> list[tuple[str, Any, str]]:
    """Build basic scalar constants."""
    return [
        ("constant_none", None, "None singleton scalar constant."),
        ("constant_true", True, "True boolean scalar constant."),
        ("constant_false", False, "False boolean scalar constant."),
        ("constant_ellipsis", Ellipsis, "Ellipsis scalar constant."),
    ]


def slice_cases() -> list[tuple[str, slice, str]]:
    """Build optional slice support probes."""
    return [
        (
            "slice_none_none_none",
            slice(None, None, None),
            "Optional marshal support probe for empty slice.",
        ),
        (
            "slice_1_10_2",
            slice(1, 10, 2),
            "Optional marshal support probe for positive stepped slice.",
        ),
        (
            "slice_neg10_none_neg1",
            slice(-10, None, -1),
            "Optional marshal support probe for negative stepped slice.",
        ),
    ]


def build_cases() -> list[dict[str, Any]]:
    """Run all scalar and binary extension cases."""
    cases: list[dict[str, Any]] = []
    for case_name, value, note in unicode_cases():
        cases.append(marshal_case(case_name, "unicode_string", value, note))
    for case_name, value, note in bytes_cases():
        cases.append(marshal_case(case_name, "bytes_payload", value, note))
    for case_name, value, note in scalar_constant_cases():
        cases.append(marshal_case(case_name, "basic_scalar_constant", value, note))
    for case_name, value, note in slice_cases():
        cases.append(marshal_case(case_name, "optional_slice_probe", value, note))
    return cases


def main() -> None:
    """Run extension tests and save the current platform result JSON."""
    RESULTS_DIR.mkdir(parents=True, exist_ok=True)

    output = {
        "member": "B",
        "topic": (
            "marshal byte-level stability for non-container, non-code scalar "
            "and binary boundary inputs"
        ),
        "environment": environment_info(),
        "repeat_count": REPEAT_COUNT,
        "cases": build_cases(),
    }

    result_path = RESULTS_DIR / f"scalar_binary_{result_file_stem()}_results.json"
    result_path.write_text(
        json.dumps(output, ensure_ascii=False, indent=2),
        encoding="utf-8",
    )
    print(f"Wrote scalar/binary result JSON: {result_path}")


if __name__ == "__main__":
    main()
