# Member D Marshal Test Summary: `member_d_all_linux_x86_64_py3_13_results.json`

## 1. Environment

| Field | Value |
|---|---|
| Platform | Linux-6.17.0-1015-azure-x86_64-with-glibc2.39 |
| System | Linux |
| Machine | x86_64 |
| Python implementation | CPython |
| Python version | 3.13 |
| Full sys.version | 3.13.13 (main, Apr 30 2026, 14:44:12) [GCC 13.3.0] |
| marshal.version | 4 |
| Recursion limit | 1000 |

## 2. Overall Result Counts

| Metric | Value |
|---|---:|
| Top-level case count | 18 |
| Flattened case count | 31 |
| Stable count | 25 |
| Unstable count | 0 |
| Exception count | 6 |
| Repeat count | 100 |

## 3. Flattened Case Results

| Case ID | Parent | Operation | Requirements | Status | Unique Hash Count | Exception | Roundtrip Correct | Hash |
|---|---|---|---|---|---:|---|---|---|
| TC-D01 | - | dumps | R5.1 | PASS | 1 | - | True | d77105626a6c... |
| TC-D02 | - | dumps | R5.1 | PASS | 1 | - | True | ba5fe04b4870... |
| TC-D03 | - | dumps | R5.1 | PASS | 1 | - | True | 552c90733114... |
| TC-D04-depth-10 | - | dumps | R5.2 | PASS | 1 | - | True | 9a0d806cfa97... |
| TC-D04-depth-100 | - | dumps | R5.2 | PASS | 1 | - | True | 19544ac41bf4... |
| TC-D04-depth-500 | - | dumps | R5.2 | PASS | 1 | - | True | ac450374ff61... |
| TC-D04-depth-900 | - | dumps | R5.2 | PASS | 1 | - | True | 65832f5ae5a6... |
| TC-D04-depth-1000 | - | dumps | R5.2 | PASS | 1 | - | True | 6525e29210e0... |
| TC-D05-depth-10 | - | dumps | R5.2 | PASS | 1 | - | True | 3268a7dc67f7... |
| TC-D05-depth-100 | - | dumps | R5.2 | PASS | 1 | - | True | 7fd38dad3e0f... |
| TC-D05-depth-500 | - | dumps | R5.2 | PASS | 1 | - | True | 8de6f99a65bb... |
| TC-D05-depth-900 | - | dumps | R5.2 | PASS | 1 | - | True | 6eda7495d5cb... |
| TC-D05-depth-1000 | - | dumps | R5.2 | PASS | 1 | - | True | 0c1b6a0bfd86... |
| TC-D06-object_instance | TC-D06 | dumps | R5.3 | EXPECTED_EXCEPTION | 0 | ValueError | - | - |
| TC-D06-custom_class_instance | TC-D06 | dumps | R5.3 | EXPECTED_EXCEPTION | 0 | ValueError | - | - |
| TC-D06-normal_function | TC-D06 | dumps | R5.3 | EXPECTED_EXCEPTION | 0 | ValueError | - | - |
| TC-D06-lambda_function | TC-D06 | dumps | R5.3 | EXPECTED_EXCEPTION | 0 | ValueError | - | - |
| TC-D06-generator_object | TC-D06 | dumps | R5.3 | EXPECTED_EXCEPTION | 0 | ValueError | - | - |
| TC-D06-file_object | TC-D06 | dumps | R5.3 | EXPECTED_EXCEPTION | 0 | ValueError | - | - |
| TC-D07 | - | dumps | R5.4 | PASS | 1 | - | True | 4f2ecf2128e5... |
| TC-D08 | - | dumps | R5.4 | PASS | 1 | - | True | 947a122c9fac... |
| TC-D09-version-0 | TC-D09 | dumps | R5.5 | PASS | 1 | - | True | 39a7383add8e... |
| TC-D09-version-1 | TC-D09 | dumps | R5.5 | PASS | 1 | - | True | 39a7383add8e... |
| TC-D09-version-2 | TC-D09 | dumps | R5.5 | PASS | 1 | - | True | 39a7383add8e... |
| TC-D09-version-3 | TC-D09 | dumps | R5.5 | PASS | 1 | - | True | 1936299e8fdc... |
| TC-D09-version-4 | TC-D09 | dumps | R5.5 | PASS | 1 | - | True | fb42180d5c38... |
| TC-D10-empty-bytes | TC-D10 | loads | R5.6 | PASS | - | - | - | - |
| TC-D10-single-null | TC-D10 | loads | R5.6 | PASS | - | - | - | - |
| TC-D10-random-noise | TC-D10 | loads | R5.6 | PASS | - | - | - | - |
| TC-D10-truncated-valid-data | TC-D10 | loads | R5.6 | PASS | - | - | - | - |
| TC-D10-valid-data-with-extra-bytes | TC-D10 | loads | R5.6 | PASS | - | - | - | - |

## 4. Requirement Coverage

| Requirement ID | Covered By |
|---|---|
| R5.1 | TC-D01, TC-D02, TC-D03 |
| R5.2 | TC-D04-depth-10, TC-D04-depth-100, TC-D04-depth-1000, TC-D04-depth-500, TC-D04-depth-900, TC-D05-depth-10, TC-D05-depth-100, TC-D05-depth-1000, TC-D05-depth-500, TC-D05-depth-900 |
| R5.3 | TC-D06-custom_class_instance, TC-D06-file_object, TC-D06-generator_object, TC-D06-lambda_function, TC-D06-normal_function, TC-D06-object_instance |
| R5.4 | TC-D07, TC-D08 |
| R5.5 | TC-D09-version-0, TC-D09-version-1, TC-D09-version-2, TC-D09-version-3, TC-D09-version-4 |
| R5.6 | TC-D10-empty-bytes, TC-D10-random-noise, TC-D10-single-null, TC-D10-truncated-valid-data, TC-D10-valid-data-with-extra-bytes |

## 5. Exception Details

| Case ID | Exception Type | Exception Message | Interpretation |
|---|---|---|---|
| TC-D06-object_instance | ValueError | unmarshallable object | Expected rejection for unsupported or invalid input; not treated as a stability bug. |
| TC-D06-custom_class_instance | ValueError | unmarshallable object | Expected rejection for unsupported or invalid input; not treated as a stability bug. |
| TC-D06-normal_function | ValueError | unmarshallable object | Expected rejection for unsupported or invalid input; not treated as a stability bug. |
| TC-D06-lambda_function | ValueError | unmarshallable object | Expected rejection for unsupported or invalid input; not treated as a stability bug. |
| TC-D06-generator_object | ValueError | unmarshallable object | Expected rejection for unsupported or invalid input; not treated as a stability bug. |
| TC-D06-file_object | ValueError | unmarshallable object | Expected rejection for unsupported or invalid input; not treated as a stability bug. |

## 6. Preliminary Conclusion

In this environment, 25 flattened cases showed stable behavior and no non-deterministic marshal output was observed. The 6 exception cases were expected rejection or invalid-byte-stream cases and should not be treated as marshal bugs.