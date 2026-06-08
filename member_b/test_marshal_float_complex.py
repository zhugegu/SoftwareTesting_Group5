"""Member B marshal precision tests for float and complex values."""

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


def nan_from_bits(bits: int) -> float:
    """Construct a float from an IEEE-754 64-bit bit pattern."""
    return struct.unpack(">d", struct.pack(">Q", bits))[0]


def float_bits(value: float) -> str:
    """Return the IEEE-754 64-bit pattern for a float as hexadecimal."""
    return f"0x{struct.unpack('>Q', struct.pack('>d', value))[0]:016x}"


def value_metadata(value: Any) -> dict[str, Any]:
    """Capture useful precision metadata for supported tested values."""
    if isinstance(value, float):
        return {"float_bit_pattern": float_bits(value)}
    if isinstance(value, complex):
        return {
            "real_bit_pattern": float_bits(value.real),
            "imag_bit_pattern": float_bits(value.imag),
        }
    return {}


def environment_info() -> dict[str, Any]:
    """Collect the requested Python and OS environment details."""
    return {
        "platform_platform": platform.platform(),
        "platform_system": platform.system(),
        "platform_machine": platform.machine(),
        "python_implementation": platform.python_implementation(),
        "sys_version": sys.version,
        "marshal_version": marshal.version,
    }


def marshal_case(case_name: str, value: Any, note: str = "") -> dict[str, Any]:
    """Marshal the same object repeatedly and record every hash."""
    hashes = []
    first_bytes = b""

    for index in range(REPEAT_COUNT):
        data = marshal.dumps(value)
        if index == 0:
            first_bytes = data
        hashes.append(sha256_hex(data))

    unique_hashes = sorted(set(hashes))
    result = {
        "case": case_name,
        "type": type(value).__name__,
        "repr": repr(value),
        "note": note,
        "repeat_count": REPEAT_COUNT,
        "hashes": hashes,
        "unique_hashes": unique_hashes,
        "unique_hash_count": len(unique_hashes),
        "same_process_stable": len(unique_hashes) == 1,
        "first_hash": hashes[0],
        "first_marshal_hex": first_bytes.hex(),
    }
    result.update(value_metadata(value))
    return result


def fixed_cases() -> list[tuple[str, Any, str]]:
    """Build the fixed float and complex test objects."""
    nan_payload_1 = nan_from_bits(0x7FF8000000000001)
    nan_payload_2 = nan_from_bits(0x7FF8000000000002)
    nan_payload_3 = nan_from_bits(0x7FF0000000000001)

    return [
        ("float_pos_zero", 0.0, "Ordinary float 0.0"),
        ("float_neg_zero", -0.0, "Ordinary float -0.0"),
        ("float_pos_one", 1.0, "Ordinary float 1.0"),
        ("float_neg_one", -1.0, "Ordinary float -1.0"),
        ("float_tiny_1e_minus_300", 1e-300, "Ordinary tiny float"),
        ("float_huge_1e300", 1e300, "Ordinary huge float"),
        ("float_pos_inf", float("inf"), "Positive infinity"),
        ("float_neg_inf", float("-inf"), "Negative infinity"),
        ("float_nan_constructor", float("nan"), "NaN from float('nan')"),
        ("float_math_nan", math.nan, "NaN from math.nan"),
        (
            "float_nan_payload_0x7ff8000000000001",
            nan_payload_1,
            "Quiet NaN payload 0x7ff8000000000001",
        ),
        (
            "float_nan_payload_0x7ff8000000000002",
            nan_payload_2,
            "Quiet NaN payload 0x7ff8000000000002",
        ),
        (
            "float_nan_payload_0x7ff0000000000001",
            nan_payload_3,
            "NaN payload 0x7ff0000000000001",
        ),
        ("complex_regular", complex(1.5, -2.5), "Regular complex"),
        ("complex_zero_neg_zero", complex(0.0, -0.0), "Complex signed zero"),
        (
            "complex_inf_neg_inf",
            complex(float("inf"), float("-inf")),
            "Complex with infinities",
        ),
        (
            "complex_nan_real",
            complex(float("nan"), 1.0),
            "Complex with NaN real part",
        ),
        (
            "complex_nan_imag",
            complex(1.0, float("nan")),
            "Complex with NaN imaginary part",
        ),
        (
            "complex_nan_both",
            complex(float("nan"), float("nan")),
            "Complex with NaN in both parts",
        ),
        (
            "complex_payload_nan_real",
            complex(nan_payload_1, 1.0),
            "Complex with payload NaN real part",
        ),
        (
            "complex_payload_nan_imag",
            complex(1.0, nan_payload_1),
            "Complex with payload NaN imaginary part",
        ),
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
        "type": "float",
        "note": "Each iteration creates a new float('nan')",
        "repeat_count": REPEAT_COUNT,
        "hashes": hashes,
        "bit_patterns": bit_patterns,
        "unique_hashes": unique_hashes,
        "unique_bit_patterns": unique_bit_patterns,
        "unique_hash_count": len(unique_hashes),
        "unique_bit_pattern_count": len(unique_bit_patterns),
        "stable_when_recreated": len(unique_hashes) == 1,
        "first_hash": hashes[0],
        "first_marshal_hex": first_bytes.hex(),
    }


def recreated_complex_nan_case() -> dict[str, Any]:
    """Marshal a freshly created complex(float('nan'), float('nan'))."""
    hashes = []
    real_bit_patterns = []
    imag_bit_patterns = []
    combined_bit_patterns = []
    first_bytes = b""

    for index in range(REPEAT_COUNT):
        value = complex(float("nan"), float("nan"))
        data = marshal.dumps(value)
        if index == 0:
            first_bytes = data
        real_bits = float_bits(value.real)
        imag_bits = float_bits(value.imag)
        hashes.append(sha256_hex(data))
        real_bit_patterns.append(real_bits)
        imag_bit_patterns.append(imag_bits)
        combined_bit_patterns.append(f"{real_bits}/{imag_bits}")

    unique_hashes = sorted(set(hashes))
    unique_bit_patterns = sorted(set(combined_bit_patterns))
    return {
        "case": "recreated_complex_nan_both",
        "type": "complex",
        "note": "Each iteration creates complex(float('nan'), float('nan'))",
        "repeat_count": REPEAT_COUNT,
        "hashes": hashes,
        "real_bit_patterns": real_bit_patterns,
        "imag_bit_patterns": imag_bit_patterns,
        "combined_bit_patterns": combined_bit_patterns,
        "unique_hashes": unique_hashes,
        "unique_bit_patterns": unique_bit_patterns,
        "unique_hash_count": len(unique_hashes),
        "unique_bit_pattern_count": len(unique_bit_patterns),
        "stable_when_recreated": len(unique_hashes) == 1,
        "first_hash": hashes[0],
        "first_marshal_hex": first_bytes.hex(),
    }


def main() -> None:
    """Run all member B tests and save the current platform result JSON."""
    RESULTS_DIR.mkdir(parents=True, exist_ok=True)

    cases = [
        marshal_case(case_name, value, note)
        for case_name, value, note in fixed_cases()
    ]
    recreated_cases = [
        recreated_float_nan_case(),
        recreated_complex_nan_case(),
    ]

    output = {
        "member": "B",
        "topic": "float and complex deep precision marshal tests",
        "environment": environment_info(),
        "repeat_count": REPEAT_COUNT,
        "cases": cases,
        "recreated_nan_cases": recreated_cases,
    }

    result_path = RESULTS_DIR / f"{result_file_stem()}_results.json"
    result_path.write_text(
        json.dumps(output, ensure_ascii=False, indent=2),
        encoding="utf-8",
    )
    print(f"Wrote result JSON: {result_path}")


if __name__ == "__main__":
    main()
