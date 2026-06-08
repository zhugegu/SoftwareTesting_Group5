"""Unified member B marshal stability tests.

This file consolidates the original float/complex suite and the later
scalar/binary extension suite into one executable test entrypoint.
"""

from __future__ import annotations

import hashlib
import json
import marshal
import math
import platform
import struct
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


def nan_from_bits(bits: int) -> float:
    """Construct a float from an IEEE-754 64-bit bit pattern."""
    return struct.unpack(">d", struct.pack(">Q", bits))[0]


def float_bits(value: float) -> str:
    """Return the IEEE-754 64-bit pattern for a float as hexadecimal."""
    return f"0x{struct.unpack('>Q', struct.pack('>d', value))[0]:016x}"


def code_points(value: str) -> list[str]:
    """Return Unicode code points in U+XXXX notation."""
    return [f"U+{ord(char):04X}" for char in value]


def value_metadata(value: Any) -> dict[str, Any]:
    """Capture metadata useful for cross-platform byte-level comparisons."""
    if isinstance(value, float):
        return {"float_bit_pattern": float_bits(value)}
    if isinstance(value, complex):
        return {
            "real_bit_pattern": float_bits(value.real),
            "imag_bit_pattern": float_bits(value.imag),
        }
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
    requirement_ids: list[str],
    value: Any,
    note: str,
    optional_support_probe: bool = False,
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
    except Exception as exc:  # noqa: BLE001 - support probes record exceptions.
        if not optional_support_probe:
            raise
        exception_type = type(exc).__name__
        exception_message = str(exc)

    unique_hashes = sorted(set(hashes))
    result = {
        "case": case_name,
        "category": category,
        "requirement_ids": requirement_ids,
        "type": type(value).__name__,
        "repr": repr(value),
        "note": note,
        "optional_support_probe": optional_support_probe,
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


def fixed_float_complex_cases() -> list[tuple[str, str, list[str], Any, str]]:
    """Build fixed float and complex test objects."""
    nan_payload_1 = nan_from_bits(0x7FF8000000000001)
    nan_payload_2 = nan_from_bits(0x7FF8000000000002)
    nan_payload_3 = nan_from_bits(0x7FF0000000000001)

    return [
        ("float_pos_zero", "float_complex", ["R1.1", "R3.1"], 0.0, "Ordinary float 0.0"),
        ("float_neg_zero", "float_complex", ["R1.1", "R3.1"], -0.0, "Ordinary float -0.0"),
        ("float_pos_one", "float_complex", ["R1.1"], 1.0, "Ordinary float 1.0"),
        ("float_neg_one", "float_complex", ["R1.1"], -1.0, "Ordinary float -1.0"),
        ("float_tiny_1e_minus_300", "float_complex", ["R1.1"], 1e-300, "Ordinary tiny float"),
        ("float_huge_1e300", "float_complex", ["R1.1"], 1e300, "Ordinary huge float"),
        ("float_pos_inf", "float_complex", ["R1.1", "R3.1"], float("inf"), "Positive infinity"),
        ("float_neg_inf", "float_complex", ["R1.1", "R3.1"], float("-inf"), "Negative infinity"),
        ("float_nan_constructor", "float_complex", ["R1.1", "R3.1", "R3.2"], float("nan"), "NaN from float('nan')"),
        ("float_math_nan", "float_complex", ["R1.1", "R3.1", "R3.2"], math.nan, "NaN from math.nan"),
        ("float_nan_payload_0x7ff8000000000001", "float_complex", ["R1.1", "R3.1", "R3.2"], nan_payload_1, "Quiet NaN payload 0x7ff8000000000001"),
        ("float_nan_payload_0x7ff8000000000002", "float_complex", ["R1.1", "R3.1", "R3.2"], nan_payload_2, "Quiet NaN payload 0x7ff8000000000002"),
        ("float_nan_payload_0x7ff0000000000001", "float_complex", ["R1.1", "R3.1", "R3.2"], nan_payload_3, "NaN payload 0x7ff0000000000001"),
        ("complex_regular", "float_complex", ["R1.1"], complex(1.5, -2.5), "Regular complex"),
        ("complex_zero_neg_zero", "float_complex", ["R1.1", "R3.1"], complex(0.0, -0.0), "Complex signed zero"),
        ("complex_inf_neg_inf", "float_complex", ["R1.1", "R3.1"], complex(float("inf"), float("-inf")), "Complex with infinities"),
        ("complex_nan_real", "float_complex", ["R1.1", "R3.1", "R3.2"], complex(float("nan"), 1.0), "Complex with NaN real part"),
        ("complex_nan_imag", "float_complex", ["R1.1", "R3.1", "R3.2"], complex(1.0, float("nan")), "Complex with NaN imaginary part"),
        ("complex_nan_both", "float_complex", ["R1.1", "R3.1", "R3.2"], complex(float("nan"), float("nan")), "Complex with NaN in both parts"),
        ("complex_payload_nan_real", "float_complex", ["R1.1", "R3.1", "R3.2"], complex(nan_payload_1, 1.0), "Complex with payload NaN real part"),
        ("complex_payload_nan_imag", "float_complex", ["R1.1", "R3.1", "R3.2"], complex(1.0, nan_payload_1), "Complex with payload NaN imaginary part"),
    ]


def recreated_float_nan_case() -> dict[str, Any]:
    """Marshal a freshly created float('nan') in every iteration."""
    hashes = []
    bit_patterns = []
    first_bytes = b""

    for index in range(REPEAT_COUNT):
        value = float("nan")
        data = marshal.dumps(value)
        if index == 0:
            first_bytes = data
        hashes.append(sha256_hex(data))
        bit_patterns.append(float_bits(value))

    unique_hashes = sorted(set(hashes))
    unique_bit_patterns = sorted(set(bit_patterns))
    return {
        "case": "recreated_float_nan",
        "category": "float_complex",
        "requirement_ids": ["R1.1", "R3.1", "R3.2"],
        "type": "float",
        "repr": "float('nan') recreated each iteration",
        "note": "Each iteration creates a new float('nan')",
        "repeat_count": REPEAT_COUNT,
        "hashes": hashes,
        "bit_patterns": bit_patterns,
        "unique_hashes": unique_hashes,
        "unique_bit_patterns": unique_bit_patterns,
        "unique_hash_count": len(unique_hashes),
        "unique_bit_pattern_count": len(unique_bit_patterns),
        "same_process_stable": len(unique_hashes) == 1,
        "stable_when_recreated": len(unique_hashes) == 1,
        "marshal_sha256": hashes[0],
        "marshal_dumps_hex_prefix_160": first_bytes.hex()[:160],
        "exception_type": None,
        "exception_message": None,
    }


def recreated_complex_nan_case() -> dict[str, Any]:
    """Marshal a freshly created complex(float('nan'), float('nan'))."""
    hashes = []
    combined_bit_patterns = []
    first_bytes = b""

    for index in range(REPEAT_COUNT):
        value = complex(float("nan"), float("nan"))
        data = marshal.dumps(value)
        if index == 0:
            first_bytes = data
        combined = f"{float_bits(value.real)}/{float_bits(value.imag)}"
        hashes.append(sha256_hex(data))
        combined_bit_patterns.append(combined)

    unique_hashes = sorted(set(hashes))
    unique_bit_patterns = sorted(set(combined_bit_patterns))
    return {
        "case": "recreated_complex_nan_both",
        "category": "float_complex",
        "requirement_ids": ["R1.1", "R3.1", "R3.2"],
        "type": "complex",
        "repr": "complex(float('nan'), float('nan')) recreated each iteration",
        "note": "Each iteration creates complex(float('nan'), float('nan'))",
        "repeat_count": REPEAT_COUNT,
        "hashes": hashes,
        "combined_bit_patterns": combined_bit_patterns,
        "unique_hashes": unique_hashes,
        "unique_bit_patterns": unique_bit_patterns,
        "unique_hash_count": len(unique_hashes),
        "unique_bit_pattern_count": len(unique_bit_patterns),
        "same_process_stable": len(unique_hashes) == 1,
        "stable_when_recreated": len(unique_hashes) == 1,
        "marshal_sha256": hashes[0],
        "marshal_dumps_hex_prefix_160": first_bytes.hex()[:160],
        "exception_type": None,
        "exception_message": None,
    }


def scalar_binary_cases() -> list[tuple[str, str, list[str], Any, str, bool]]:
    """Build extension cases for non-container, non-code scalar/binary values."""
    cases: list[tuple[str, str, list[str], Any, str, bool]] = [
        ("ascii_plain", "unicode_string", ["R1.1", "R1.2", "B-EXT"], "hello", "Plain ASCII baseline string.", False),
        ("chinese_text", "unicode_string", ["R1.1", "R1.2", "B-EXT"], "中文测试", "Chinese BMP characters.", False),
        ("emoji_text", "unicode_string", ["R1.1", "R1.2", "B-EXT"], "emoji: 😀", "String containing an emoji.", False),
        ("nul_inside_string", "unicode_string", ["R1.1", "R1.2", "B-EXT"], "a\x00b", "String with embedded NUL.", False),
        ("crlf_string", "unicode_string", ["R1.1", "R1.2", "B-EXT"], "line\r\nbreak", "String containing CRLF.", False),
        ("non_bmp_character", "unicode_string", ["R1.1", "R1.2", "B-EXT"], "𐍈", "Single non-BMP character.", False),
        ("composed_e_acute", "unicode_string", ["R1.1", "R1.2", "B-EXT"], "é", "Precomposed Latin small e with acute.", False),
        ("decomposed_e_acute", "unicode_string", ["R1.1", "R1.2", "B-EXT"], "e\u0301", "Latin e plus combining acute mark.", False),
        ("lone_high_surrogate", "unicode_string", ["R1.1", "R1.2", "B-EXT"], "\ud800", "Lone high surrogate code point.", False),
        ("zero_width_joiner_sequence", "unicode_string", ["R1.1", "R1.2", "B-EXT"], "👩‍💻", "Emoji sequence joined by U+200D zero width joiner.", False),
        ("bytes_empty", "bytes_payload", ["R1.1", "R1.2", "B-EXT"], b"", "Empty bytes baseline.", False),
        ("bytes_single_nul", "bytes_payload", ["R1.1", "R1.2", "B-EXT"], b"\x00", "Single embedded NUL byte.", False),
        ("bytes_high_values_with_ascii", "bytes_payload", ["R1.1", "R1.2", "B-EXT"], b"\x00\xff\x80abc", "NUL, high byte values, and ASCII bytes.", False),
        ("bytes_all_byte_values", "bytes_payload", ["R1.1", "R1.2", "B-EXT"], bytes(range(256)), "All byte values 0-255.", False),
        ("bytes_255_a", "bytes_payload", ["R1.1", "R1.2", "B-EXT"], b"a" * 255, "Length boundary just below 256.", False),
        ("bytes_256_a", "bytes_payload", ["R1.1", "R1.2", "B-EXT"], b"a" * 256, "Length boundary at 256.", False),
        ("bytes_65535_a", "bytes_payload", ["R1.1", "R1.2", "B-EXT"], b"a" * 65535, "Length boundary just below 65536.", False),
        ("bytes_65536_a", "bytes_payload", ["R1.1", "R1.2", "B-EXT"], b"a" * 65536, "Length boundary at 65536.", False),
        ("constant_none", "basic_scalar_constant", ["R1.1", "R1.2", "B-EXT"], None, "None singleton scalar constant.", False),
        ("constant_true", "basic_scalar_constant", ["R1.1", "R1.2", "B-EXT"], True, "True boolean scalar constant.", False),
        ("constant_false", "basic_scalar_constant", ["R1.1", "R1.2", "B-EXT"], False, "False boolean scalar constant.", False),
        ("constant_ellipsis", "basic_scalar_constant", ["R1.1", "R1.2", "B-EXT"], Ellipsis, "Ellipsis scalar constant.", False),
        ("slice_none_none_none", "optional_slice_probe", ["B-EXT"], slice(None, None, None), "Optional marshal support probe for empty slice.", True),
        ("slice_1_10_2", "optional_slice_probe", ["B-EXT"], slice(1, 10, 2), "Optional marshal support probe for positive stepped slice.", True),
        ("slice_neg10_none_neg1", "optional_slice_probe", ["B-EXT"], slice(-10, None, -1), "Optional marshal support probe for negative stepped slice.", True),
    ]
    return cases


def build_cases() -> list[dict[str, Any]]:
    """Run all member B required and extension cases."""
    results = [
        marshal_case(case_name, category, reqs, value, note)
        for case_name, category, reqs, value, note in fixed_float_complex_cases()
    ]
    results.append(recreated_float_nan_case())
    results.append(recreated_complex_nan_case())
    for case_name, category, reqs, value, note, optional_probe in scalar_binary_cases():
        results.append(
            marshal_case(
                case_name,
                category,
                reqs,
                value,
                note,
                optional_support_probe=optional_probe,
            )
        )
    return results


def main() -> None:
    """Run the unified member B suite and save the current platform JSON."""
    RESULTS_DIR.mkdir(parents=True, exist_ok=True)
    cases = build_cases()
    output = {
        "member": "B",
        "topic": "unified marshal stability tests for float/complex and scalar/binary extension cases",
        "environment": environment_info(),
        "repeat_count": REPEAT_COUNT,
        "case_count": len(cases),
        "cases": cases,
    }
    result_path = RESULTS_DIR / f"member_b_all_{result_file_stem()}_results.json"
    result_path.write_text(
        json.dumps(output, ensure_ascii=False, indent=2),
        encoding="utf-8",
    )
    stable = sum(
        1
        for case in cases
        if case.get("exception_type") is None
        and case.get("same_process_stable") is True
    )
    exceptions = sum(1 for case in cases if case.get("exception_type"))
    unstable = len(cases) - stable - exceptions
    print(f"Wrote unified result JSON: {result_path}")
    print(f"Cases: {len(cases)}; stable={stable}; unstable={unstable}; exceptions={exceptions}")


if __name__ == "__main__":
    main()
