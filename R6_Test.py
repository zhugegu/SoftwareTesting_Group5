"""Member E marshal stability tests.

This test suite evaluates the stability, determinism, and format boundaries 
of Python code object serialization using the standard marshal module.

Complies with requirements: R1.2, R6.1, R6.2, R6.3, R6.4, R6.5, R6.6.
Integrated into the standard unittest framework with robust I/O error handling,
dynamic assertions, and safe teardown mechanics for CI/CD integration.
"""
import marshal
import sys
import os
import platform
import hashlib
import math
import unittest
import atexit
from datetime import datetime
from typing import Any, Callable, Set


REPEAT_COMPILE_COUNT = 20
ASYNC_COMPILE_COUNT = 30
STABILITY_CHECK_COUNT = 10
HASH_DISPLAY_LEN = 16

def get_marshal_hash(obj: Any) -> str:
    """Serialize object using marshal and return its SHA-256 hex digest."""
    return hashlib.sha256(marshal.dumps(obj)).hexdigest()

def datetime_str() -> str:
    """Return local execution timestamp."""
    return datetime.now().strftime("%Y-%m-%d %H:%M:%S")

class TestMarshalCodeObjects(unittest.TestCase):
    log_file = None

    @classmethod
    def setUpClass(cls) -> None:
        """Initialize global system parameters and safe logging descriptors."""
        cls.os_name = platform.system()
        cls.py_version = sys.version.split()[0]
        cls.machine = platform.machine()

        cls.log_dir = os.path.dirname(os.path.abspath(__file__))
        # 日志名：系统名_版本号，示例 member_e_stability_Windows_3.9.12.log
        log_filename = f"member_e_stability_{cls.os_name}_{cls.py_version}.log"
        cls.log_path = os.path.join(cls.log_dir, log_filename)

        try:
            os.makedirs(cls.log_dir, exist_ok=True)
            cls.log_file = open(cls.log_path, "a", encoding="utf-8")
            atexit.register(cls._safe_close_log)
        except PermissionError as e:
            raise RuntimeError(f"Permission denied: Cannot create log file at {cls.log_path}") from e
        except OSError as e:
            raise RuntimeError(f"OS error when initializing log directory: {e}") from e

        cls._log_raw("=" * 80)
        cls._log_raw(f"MEMBER E - MARSHAL STABILITY TEST RUN | {datetime_str()}")
        cls._log_raw(f"OS: {cls.os_name} | Arch: {cls.machine} | Python: {cls.py_version}")
        cls._log_raw("=" * 80)


    @classmethod
    def tearDownClass(cls) -> None:
        """Safely release file stream handlers upon suite completion."""
        cls._log_raw(f"\n[ SUITE EXECUTION COMPLETED AT {datetime_str()} ]\n" + "=" * 80)
        cls._safe_close_log()

    @classmethod
    def _safe_close_log(cls) -> None:
        """Fallback cleanup trigger for I/O buffers."""
        if cls.log_file is not None and not cls.log_file.closed:
            cls.log_file.close()

    @classmethod
    def _log_raw(cls, msg: str) -> None:
        """Internal helper to write to both stdout and telemetry log files safely."""
        print(msg)
        if cls.log_file is not None and not cls.log_file.closed:
            try:
                cls.log_file.write(msg + "\n")
                cls.log_file.flush()
            except IOError as e:
                print(f"[Warning] Log write failed: {e}")

    def _assert_determinism(self, obj_provider: Callable[[], object], 
                             case_name: str, runs: int = STABILITY_CHECK_COUNT) -> str:
        """Refactored strict bound verification to eliminate redundant loops."""
        hashes: Set[str] = set()
        for _ in range(runs):
            hashes.add(get_marshal_hash(obj_provider()))

        self.assertEqual(len(hashes), 1, f"Non-deterministic payload generated in {case_name}!")
        stable_hash = list(hashes)[0]
        self._log_raw(f"[{case_name}] Determinism Verified. Hash = {stable_hash[:HASH_DISPLAY_LEN]}...")
        return stable_hash

    def test_r12_basic_cross_platform(self) -> None:
        """R1.2: Determinism check for canonical scalar invariants."""
        self._log_raw("\n[ RUNNING: test_r12_basic_cross_platform ]")
        test_scalars = [
            None, True, False, 123456, -9876543210123456789,
            3.141592653589793, "Hello ZJUT Software Engineering",
            b"Binary Payload Buffer", (1, 2, "mixed", (3, 4))
        ]
        for idx, obj in enumerate(test_scalars):
            self._assert_determinism(lambda o=obj: o, f"Scalar_Type_{type(obj).__name__}_{idx}")

    def test_r61_code_optimize_level(self) -> None:
        """R6.1: Dynamic validation of bytecode optimization payload stripping (-O/-OO)."""
        self._log_raw("\n[ RUNNING: test_r61_code_optimize_level ]")
        src = (
            'def compute_square(x):\n'
            '    """Docstring payload to be evaluated."""\n'
            '    assert x >= 0\n'
            '    return x * x\n'
        )

        hashes = {}
        for level in [0, 1, 2]:
            code_obj = compile(src, "<optimize_test>", "exec", optimize=level)
            hashes[level] = get_marshal_hash(code_obj)
            self._log_raw(f"Optimization Level {level}: Hash = {hashes[level][:HASH_DISPLAY_LEN]}...")

        self.assertNotEqual(hashes[0], hashes[2],
                            "Optimization Level 2 failed to strip docstring payload structures.")
        self._log_raw("Analysis: Optimization levels properly mutated bytecode structures.")

    def test_r62_repeat_compile(self) -> None:
        """R6.2: Ensure reproducibility of repeated compilation and evaluate dynamic filename injections."""
        self._log_raw("\n[ RUNNING: test_r62_repeat_compile ]")
        src = "def process_data(items):\n    return [x**2 for x in items if x % 2 == 0]\n"

        name1 = "<file_name_001>"
        name2 = "<file_name_002>"
        code1 = compile(src, name1, "exec")
        code2 = compile(src, name2, "exec")
        hash1 = get_marshal_hash(code1)
        hash2 = get_marshal_hash(code2)

        self.assertNotEqual(hash1, hash2,
                            "Different filenames produce identical marshal output (unexpected)!")
        self._log_raw("Observed Behavior: Filename parameters are embedded into code object structures.")

        self._assert_determinism(lambda: compile(src, "<fixed_identity>", "exec"),
                                 "Fixed_Filename_Compilation", REPEAT_COMPILE_COUNT)

    def test_r63_cross_version_format(self) -> None:
        """R6.3: Capture runtime interpreter magic tracking layout structures & invalid bytes test."""
        self._log_raw("\n[ RUNNING: test_r63_cross_version_format ]")
        src = "x = [1, 2, 3]"
        code_obj = compile(src, "<version_test>", "exec")
        raw_bytes = marshal.dumps(code_obj)
        self._log_raw(f"Format Bound Descriptor Size: {len(raw_bytes)} bytes | Hex Signature = {raw_bytes[:16].hex()}")

        truncated = raw_bytes[:-5]
        with self.assertRaises((EOFError, ValueError)):
            marshal.loads(truncated)
        self._log_raw("Cross-check: Truncated marshal bytes raise expected exception.")

    def test_r63_marshal_version_matrix(self) -> None:
        """R6.3 Refactored: Evaluate down-version compatibility boundaries handling precise exceptions."""
        self._log_raw("\n[ RUNNING: test_r63_marshal_version_matrix ]")
        src = "def identity(x): return x"
        code_obj = compile(src, "<version_matrix_test>", "exec")
        max_test_version = min(marshal.version, 4)

        for version in range(max_test_version + 1):
            try:
                payload = marshal.dumps(code_obj, version)
                h_val = hashlib.sha256(payload).hexdigest()
                self._log_raw(f"Version Param {version}: Stream Size = {len(payload)} bytes | Hash = {h_val[:HASH_DISPLAY_LEN]}...")
            except (ValueError, DeprecationWarning):
                self._log_raw(f"Version Param {version}: Expected backward incompatibility boundary hit.")
            except Exception as e:
                self.fail(f"Unexpected system crash encountered at version parameter {version}: {e}")

    def test_r64_closure_code_stability(self) -> None:
        """R6.4: Validate multi-tiered cell and free variable graph traversal paths in marshal.c."""
        self._log_raw("\n[ RUNNING: test_r64_closure_code_stability ]")
        src = (
            "def outer(f):\n"
            "    def middle(o):\n"
            "        def inner(v): return v * f + o\n"
            "        return inner\n"
            "    return middle\n"
        )
        self._assert_determinism(lambda: compile(src, "<closure_test>", "exec"), "Multi_Tiered_Closure")

    def test_r65_class_exception_optimize(self) -> None:
        """R6.5: Evaluate serialization persistence over compound AST class declarations and exception blocks under different optimization levels."""
        self._log_raw("\n[ RUNNING: test_r65_class_exception_optimize ]")
        src = (
            "class E(Exception): pass\n"
            "class P:\n"
            "    def run(self, v):\n"
            "        try:\n"
            "            if v < 0: raise E()\n"
            "        except E: return 0\n"
        )

        for opt_level in [0, 1, 2]:
            self._assert_determinism(
                lambda: compile(src, "<class_exception_test>", "exec", optimize=opt_level),
                f"Compound_AST_Opt_Level_{opt_level}"
            )

    def test_r66_async_nan_code(self) -> None:
        """R6.6 Refactored: Robust boundary evaluation for floating-point permutations inside constant tables."""
        self._log_raw("\n[ RUNNING: test_r66_async_nan_code ]")
        async_src = "async def minimal_async_task():\n    await None\n    return True\n"
        self._assert_determinism(lambda: compile(async_src, "<async_code_test>", "exec"),
                                 "Async_Coroutine_Block", ASYNC_COMPILE_COUNT)

        special_src = (
            "def specials():\n"
            "    return (1e300*1e300/1e300*0.0, 1e300*1e300, -1e300*1e300, 0.0, -0.0)\n"
        )
        code_with_specials = compile(special_src, "<special_constants_test>", "exec")

        inner_co = None
        for c in code_with_specials.co_consts:
            if isinstance(c, type(code_with_specials)):
                inner_co = c
                break
        self.assertIsNotNone(inner_co, "Constants buffer structure anomaly: Inner code object missing.")

        consts = [c for c in inner_co.co_consts if isinstance(c, float)]
        has_nan = any(math.isnan(c) for c in consts)
        has_inf = any(math.isinf(c) for c in consts)
        has_neg_zero = any(c == -0.0 and math.copysign(1, c) == -1 for c in consts)

        self._log_raw(f"White-box Constants Table Diagnostics: NaN={has_nan} | Inf={has_inf} | -0.0={has_neg_zero}")
        self._assert_determinism(lambda: code_with_specials, "Special_Floats_Constants_Pool")

    def test_r6_boundary_empty_recursive_code(self) -> None:
        """Extension Boundary: Empty code & recursive function code object stability."""
        self._log_raw("\n[ RUNNING: test_r6_boundary_empty_recursive_code ]")
        # Empty code
        self._assert_determinism(lambda: compile("", "<empty_stub>", "exec"), "Empty_Code_Object")
        # Recursive function
        recursive_src = "def recurse(n):\n    if n <= 1: return 1\n    return n * recurse(n - 1)\n"
        self._assert_determinism(lambda: compile(recursive_src, "<recursive_stub>", "exec"), "Recursive_Code_Object")

if __name__ == "__main__":
    unittest.main(verbosity=2)
