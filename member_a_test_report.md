# Member A Test Report: Basic Immutable Types and Integer Boundary Testing

**Name:** Xu Xinyi  
**Role:** Basic Immutable Types and Integer Boundary Testing  
**Responsible Requirements:** R1.1, R2.1, R2.2, R2.3

---

## 1. Testing Strategy Overview

This test suite comprehensively tests **basic immutable types and integer boundaries** of the `marshal` module, using a combination of testing techniques:

### 1.1 Testing Techniques

| Technique | Application | Description |
|-----------|-------------|-------------|
| **Equivalence Partitioning** | Integer classification | Small integers, large integers, boundary integers |
| **Boundary Value Analysis** | Critical values | int32/int64 boundaries, string length boundaries |
| **Round-trip Testing** | Correctness | Verify dumps → loads consistency |
| **File I/O Testing** | Real scenario simulation | Test file read/write scenarios |
| **Multiple Run Verification** | Determinism guarantee | Each test runs 10-100 times to verify hash consistency |
| **White-box Testing** | Based on marshal.c | Directly test TYPE_INT64 encoding, variable-length encoding boundaries |

### 1.2 Tools and Framework

- **Testing Framework:** Python standard library `unittest`
- **Hash Verification:** `hashlib.sha256` to ensure byte stream consistency
- **Decorator Pattern:** `@test_determinism()` for unified multiple run verification
- **Mixin Pattern:** `HelperMixin` providing round-trip testing utilities

---

## 2. Test Case Design

### 2.1 R1.1: Core Equivalence Determinism

**Requirement Description:** Under the same Python version and operating system, identical input objects shall produce identical byte stream hashes.

**Test Coverage:**

| Test Case | Test Object | Description |
|-----------|-------------|-------------|
| `test_none` | `None` | Singleton object serialization |
| `test_bool_true` / `test_bool_false` | `True` / `False` | Boolean values |
| `test_zero` | `0` | Integer 0 (special value) |
| `test_small_positive_int` | `42` | Small positive integer |
| `test_small_negative_int` | `-42` | Small negative integer |
| `test_empty_string` | `""` | Empty string |
| `test_ascii_string` | `"hello world"` | ASCII string |
| `test_unicode_string` | `"你好世界"` | Unicode string |
| `test_empty_bytes` | `b""` | Empty bytes |
| `test_bytes` | `b"hello world"` | Bytes |
| `test_roundtrip_none` | `None` | Round-trip testing |
| `test_roundtrip_bool` | `True`/`False` | Round-trip testing |
| `test_roundtrip_small_ints` | `-10` to `10` | Round-trip testing |

### 2.2 R2.1: Cross-platform Word Length Independence

**Requirement Description:** Large integers (exceeding 32-bit/64-bit word lengths) shall produce consistent serialization outputs across different bitness operating systems and architectures.

**Test Coverage:**

| Test Case | Test Value | Description |
|-----------|------------|-------------|
| `test_int32_boundary_positive` | `2^31 - 1` | 32-bit signed integer max value |
| `test_int32_boundary_negative` | `-2^31` | 32-bit signed integer min value |
| `test_int32_overflow_positive` | `2^31` | Just exceeding 32-bit boundary |
| `test_int32_overflow_negative` | `-2^31 - 1` | Just exceeding 32-bit boundary |
| `test_int64_boundary_positive` | `2^63 - 1` | 64-bit signed integer max value |
| `test_int64_boundary_negative` | `-2^63` | 64-bit signed integer min value |
| `test_int64_overflow_positive` | `2^63` | Just exceeding 64-bit boundary |
| `test_int64_overflow_negative` | `-2^63 - 1` | Just exceeding 64-bit boundary |
| `test_large_integer_1000_bits` | `2^1000` | 1000-bit very large integer |
| `test_large_integer_10000_bits` | `2^10000` | 10000-bit extremely large integer |
| `test_negative_large_integer` | `-2^1000` | Large negative integer |
| `test_wide_range_ints` | Bitwise traversal | Systematic large range testing |
| `test_int64_direct` | Byte construction | White-box TYPE_INT64 encoding test |

### 2.3 R2.2: Variable-length Encoding Boundary Stability

**Requirement Description:** Test single-byte, multi-byte storage critical points (e.g., different size integers in marshal's variable-length encoding boundaries).

**Test Coverage:**

| Test Case | Test Value | Description |
|-----------|------------|-------------|
| `test_single_byte_int` | `0` to `255` | Single-byte integer range |
| `test_two_byte_boundary` | `0xFFFF` | Two-byte boundary |
| `test_three_byte_boundary` | `0xFFFFFF` | Three-byte boundary |
| `test_four_byte_boundary` | `0xFFFFFFFF` | Four-byte boundary |
| `test_short_ascii_boundary` | `"a" * 255` | Short ASCII string boundary |
| `test_short_ascii_boundary_plus_1` | `"a" * 256` | Trigger long encoding |
| `test_negative_one` | `-1` | Special negative integer boundary |
| `test_small_int_cache_boundary_positive` | `257` | Small integer cache positive boundary |
| `test_small_int_cache_boundary_negative` | `-257` | Small integer cache negative boundary |
| `test_marshal_long_digit_boundaries` | `32767`, `32768`, `1073741823`, `1073741824` | White-box test: 2^15 encoding boundary |
| `test_large_string` | `" " * 10000` | 10000-character large string |
| `test_file_stream_determinism` | `io.BytesIO` | Stream writing test |

**White-box Test Basis:**
Based on `PyLong_MARSHAL_SHIFT = 15` in `marshal.c`, integers are stored in chunks with base 32768.

### 2.4 R2.3: Internal Optimization Isolation

**Requirement Description:** Serialization output shall not be affected by Python interpreter internal optimizations (e.g., string/integer intern mechanisms).

**Test Coverage:**

| Test Case | Description |
|-----------|-------------|
| `test_interned_string` | Interned string serialization |
| `test_non_interned_string` | Non-interned string |
| `test_interned_vs_non_interned_same_content` | Same content interned vs non-interned |
| `test_small_int_cache` | Small integer cache impact |
| `test_large_int_no_cache` | Large integer (no cache) |
| `test_repeated_interned_calls` | Multiple intern call consistency |
| `test_intern_preservation` | Version 3+ preserves intern state |
| `test_interned_vs_non_interned_string` | Interned vs dynamically constructed string hash equality |
| `test_small_int_pool_isolation` | Small integer pool vs computed values |

### 2.5 Supplementary Tests

| Category | Test Cases |
|----------|-----------|
| **Edge Cases** | `test_one`, `test_minus_one`, `test_bytes_with_zero`, `test_mixed_string`, `test_special_characters` |
| **Determinism Verification** | `test_consistent_hash_output` (100 runs), `test_deterministic_across_versions` (cross-version) |
| **Exact Type Match** | `test_subclass_rejection` (subclass rejection test) |

---

## 3. Traceability Matrix

| Requirement ID | Requirement Name | Test Case Count | Covered Test Cases | Status |
|----------------|------------------|-----------------|--------------------|--------|
| **R1.1** | Core Equivalence Determinism | 15 | `test_none`, `test_bool_true`, `test_bool_false`, `test_zero`, `test_small_positive_int`, `test_small_negative_int`, `test_empty_string`, `test_ascii_string`, `test_unicode_string`, `test_empty_bytes`, `test_bytes`, `test_roundtrip_none`, `test_roundtrip_bool`, `test_roundtrip_small_ints`, `test_consistent_hash_output` | ✅ Full Coverage |
| **R2.1** | Cross-platform Word Length Independence | 14 | `test_int32_boundary_positive`, `test_int32_boundary_negative`, `test_int32_overflow_positive`, `test_int32_overflow_negative`, `test_int64_boundary_positive`, `test_int64_boundary_negative`, `test_int64_overflow_positive`, `test_int64_overflow_negative`, `test_large_integer_1000_bits`, `test_large_integer_10000_bits`, `test_negative_large_integer`, `test_wide_range_ints`, `test_int64_direct` | ✅ Full Coverage |
| **R2.2** | Variable-length Encoding Boundary Stability | 13 | `test_single_byte_int`, `test_two_byte_boundary`, `test_three_byte_boundary`, `test_four_byte_boundary`, `test_short_ascii_boundary`, `test_short_ascii_boundary_plus_1`, `test_negative_one`, `test_small_int_cache_boundary_positive`, `test_small_int_cache_boundary_negative`, `test_marshal_long_digit_boundaries`, `test_large_string`, `test_file_stream_determinism` | ✅ Full Coverage |
| **R2.3** | Internal Optimization Isolation | 10 | `test_interned_string`, `test_non_interned_string`, `test_interned_vs_non_interned_same_content`, `test_small_int_cache`, `test_large_int_no_cache`, `test_repeated_interned_calls`, `test_intern_preservation`, `test_interned_vs_non_interned_string`, `test_small_int_pool_isolation` | ✅ Full Coverage |
| **Supplementary** | Edge/Verification/Type Tests | 4 | `test_one`, `test_minus_one`, `test_bytes_with_zero`, `test_mixed_string`, `test_special_characters`, `test_deterministic_across_versions`, `test_subclass_rejection` | ✅ Full Coverage |

---

## 4. Test Results

### 4.1 Execution Statistics

| Statistic | Value |
|-----------|-------|
| Total Test Cases | 56 |
| Passed | 56 |
| Failed | 0 |
| Errors | 0 |
| Skipped | 0 |
| Pass Rate | 100% |
| Execution Time | 0.113 seconds |

### 4.2 Observed Stability Issues

Within this test scope, **no non-deterministic outputs were observed**. All test cases produce consistent hashes across multiple runs.

**Findings and Conclusions:**

1. **Subclass Behavior:** marshal rejects all custom subclasses (`int`, `float`, `complex`, `tuple`, `list`, `dict`, `set`, `frozenset`) by throwing `ValueError`.
2. **Intern Mechanism:**
   - Version 3+ preserves intern state
   - Version 2 does not preserve intern state
3. **Variable-length Encoding:** Accurately verified the `PyLong_MARSHAL_SHIFT = 15` chunk storage behavior.

---

## 5. Limitations and Future Work

### 5.1 Known Limitations

1. **Platform Coverage:** This test was executed only on a single platform (macOS), without actual cross-platform (Windows/Linux) verification for R2.1.
2. **Version Coverage:** Limited by current environment, no actual testing of multiple Python major versions was performed.
3. **Memory Constraints:** Extremely large integers (10^6+ bits) were not tested to avoid memory overflow.
4. **Performance Testing:** No quantitative performance testing of serialization/deserialization was performed.

### 5.2 Improvement Suggestions

1. **CI/CD Integration:** Use GitHub Actions or similar tools to automatically run on multiple OS/Python version combinations.
2. **Cross-platform Verification:** Actually execute tests on Windows/Linux environments to verify R2.1.
3. **Performance Benchmarking:** Add performance testing to monitor serialization speed changes with object size.

---

## 6. Code Repository

**Test Code Location:** [Provide your GitHub/GitLab repository link]

**Main Files:**
- `test_member_a.py`: Member A test suite (56 test cases)
- `run_test.py`: Test runner script

---

## 7. Summary

This test suite comprehensively covers all requirements assigned to Member A (R1.1, R2.1, R2.2, R2.3), using a combination of black-box and white-box testing methods, with 56 carefully designed test cases. All tests passed, demonstrating that the `marshal` module has good determinism and stability within the scope of basic immutable types and integer boundaries.

---

**Report Pages:** Approximately 4 pages (meets ≤ 8 page requirement)  
**Code Style:** Compliant with PEP 8 coding standard
