# Member D Cross-Platform Marshal Test Summary

## 1. Scope

This summary aggregates member D marshal stability results across GitHub Actions environments. The tested scope includes cyclic references, deep nesting boundaries, unsupported types, shared references, marshal version arguments, and invalid byte-stream deserialization.

## 2. Environment Matrix

| # | Source File | System | Machine | Python | marshal.version | Flat Cases | Stable | Unstable | Exceptions |
|---:|---|---|---|---|---:|---:|---:|---:|---:|
| 1 | `member_d_all_darwin_arm64_py3_10_results.json` | Darwin | arm64 | 3.10 | 4 | 31 | 25 | 0 | 6 |
| 2 | `member_d_all_darwin_arm64_py3_11_results.json` | Darwin | arm64 | 3.11 | 4 | 31 | 25 | 0 | 6 |
| 3 | `member_d_all_darwin_arm64_py3_12_results.json` | Darwin | arm64 | 3.12 | 4 | 31 | 25 | 0 | 6 |
| 4 | `member_d_all_darwin_arm64_py3_13_results.json` | Darwin | arm64 | 3.13 | 4 | 31 | 25 | 0 | 6 |
| 5 | `member_d_all_darwin_arm64_py3_9_results.json` | Darwin | arm64 | 3.9 | 4 | 31 | 25 | 0 | 6 |
| 6 | `member_d_all_linux_x86_64_py3_10_results.json` | Linux | x86_64 | 3.10 | 4 | 31 | 25 | 0 | 6 |
| 7 | `member_d_all_linux_x86_64_py3_11_results.json` | Linux | x86_64 | 3.11 | 4 | 31 | 25 | 0 | 6 |
| 8 | `member_d_all_linux_x86_64_py3_12_results.json` | Linux | x86_64 | 3.12 | 4 | 31 | 25 | 0 | 6 |
| 9 | `member_d_all_linux_x86_64_py3_13_results.json` | Linux | x86_64 | 3.13 | 4 | 31 | 25 | 0 | 6 |
| 10 | `member_d_all_linux_x86_64_py3_9_results.json` | Linux | x86_64 | 3.9 | 4 | 31 | 25 | 0 | 6 |
| 11 | `member_d_all_windows_amd64_py3_10_results.json` | Windows | AMD64 | 3.10 | 4 | 31 | 23 | 0 | 8 |
| 12 | `member_d_all_windows_amd64_py3_11_results.json` | Windows | AMD64 | 3.11 | 4 | 31 | 23 | 0 | 8 |
| 13 | `member_d_all_windows_amd64_py3_12_results.json` | Windows | AMD64 | 3.12 | 4 | 31 | 23 | 0 | 8 |
| 14 | `member_d_all_windows_amd64_py3_13_results.json` | Windows | AMD64 | 3.13 | 4 | 31 | 23 | 0 | 8 |
| 15 | `member_d_all_windows_amd64_py3_9_results.json` | Windows | AMD64 | 3.9 | 4 | 31 | 23 | 0 | 8 |

## 3. Overall Result

| Metric | Value |
|---|---:|
| Environment count | 15 |
| Total flattened executions | 465 |
| Total unstable cases reported | 0 |

No non-deterministic marshal output was observed in the aggregated GitHub Actions results. All unstable counts reported by the per-environment summaries were zero.

## 4. Requirement Coverage

| Requirement ID | Covered Cases |
|---|---|
| R5.1 | TC-D01, TC-D02, TC-D03 |
| R5.2 | TC-D04-depth-10, TC-D04-depth-100, TC-D04-depth-1000, TC-D04-depth-500, TC-D04-depth-900, TC-D05-depth-10, TC-D05-depth-100, TC-D05-depth-1000, TC-D05-depth-500, TC-D05-depth-900 |
| R5.3 | TC-D06-custom_class_instance, TC-D06-file_object, TC-D06-generator_object, TC-D06-lambda_function, TC-D06-normal_function, TC-D06-object_instance |
| R5.4 | TC-D07, TC-D08 |
| R5.5 | TC-D09-version-0, TC-D09-version-1, TC-D09-version-2, TC-D09-version-3, TC-D09-version-4 |
| R5.6 | TC-D10-empty-bytes, TC-D10-random-noise, TC-D10-single-null, TC-D10-truncated-valid-data, TC-D10-valid-data-with-extra-bytes |

## 5. Cross-Environment Case Outcome Matrix

| Case ID | Requirements | Operation | Parent | Cross-Env Outcome | Distinct Hashes | Exception Signatures |
|---|---|---|---|---|---:|---:|
| TC-D01 | R5.1 | dumps | - | PASS_ALL | 1 | 0 |
| TC-D02 | R5.1 | dumps | - | PASS_ALL | 1 | 0 |
| TC-D03 | R5.1 | dumps | - | PASS_ALL | 1 | 0 |
| TC-D04-depth-10 | R5.2 | dumps | - | PASS_ALL | 1 | 0 |
| TC-D04-depth-100 | R5.2 | dumps | - | PASS_ALL | 1 | 0 |
| TC-D04-depth-1000 | R5.2 | dumps | - | MIXED_EXPECTED | 1 | 1 |
| TC-D04-depth-500 | R5.2 | dumps | - | PASS_ALL | 1 | 0 |
| TC-D04-depth-900 | R5.2 | dumps | - | PASS_ALL | 1 | 0 |
| TC-D05-depth-10 | R5.2 | dumps | - | PASS_ALL | 1 | 0 |
| TC-D05-depth-100 | R5.2 | dumps | - | PASS_ALL | 1 | 0 |
| TC-D05-depth-1000 | R5.2 | dumps | - | MIXED_EXPECTED | 1 | 1 |
| TC-D05-depth-500 | R5.2 | dumps | - | PASS_ALL | 1 | 0 |
| TC-D05-depth-900 | R5.2 | dumps | - | PASS_ALL | 1 | 0 |
| TC-D06-custom_class_instance | R5.3 | dumps | TC-D06 | EXPECTED_EXCEPTION_ALL | 0 | 1 |
| TC-D06-file_object | R5.3 | dumps | TC-D06 | EXPECTED_EXCEPTION_ALL | 0 | 1 |
| TC-D06-generator_object | R5.3 | dumps | TC-D06 | EXPECTED_EXCEPTION_ALL | 0 | 1 |
| TC-D06-lambda_function | R5.3 | dumps | TC-D06 | EXPECTED_EXCEPTION_ALL | 0 | 1 |
| TC-D06-normal_function | R5.3 | dumps | TC-D06 | EXPECTED_EXCEPTION_ALL | 0 | 1 |
| TC-D06-object_instance | R5.3 | dumps | TC-D06 | EXPECTED_EXCEPTION_ALL | 0 | 1 |
| TC-D07 | R5.4 | dumps | - | PASS_ALL | 1 | 0 |
| TC-D08 | R5.4 | dumps | - | PASS_ALL | 1 | 0 |
| TC-D09-version-0 | R5.5 | dumps | TC-D09 | PASS_ALL | 1 | 0 |
| TC-D09-version-1 | R5.5 | dumps | TC-D09 | PASS_ALL | 1 | 0 |
| TC-D09-version-2 | R5.5 | dumps | TC-D09 | PASS_ALL | 1 | 0 |
| TC-D09-version-3 | R5.5 | dumps | TC-D09 | PASS_ALL | 1 | 0 |
| TC-D09-version-4 | R5.5 | dumps | TC-D09 | PASS_ALL | 1 | 0 |
| TC-D10-empty-bytes | R5.6 | loads | TC-D10 | PASS_ALL | 0 | 0 |
| TC-D10-random-noise | R5.6 | loads | TC-D10 | PASS_ALL | 0 | 0 |
| TC-D10-single-null | R5.6 | loads | TC-D10 | PASS_ALL | 0 | 0 |
| TC-D10-truncated-valid-data | R5.6 | loads | TC-D10 | PASS_ALL | 0 | 0 |
| TC-D10-valid-data-with-extra-bytes | R5.6 | loads | TC-D10 | PASS_ALL | 0 | 0 |

## 6. Expected Exception Summary

| Case ID | Exception Signature | Environment Count |
|---|---|---:|
| TC-D04-depth-1000 | ValueError: object too deeply nested to marshal | 5 |
| TC-D05-depth-1000 | ValueError: object too deeply nested to marshal | 5 |
| TC-D06-custom_class_instance | ValueError: unmarshallable object | 15 |
| TC-D06-file_object | ValueError: unmarshallable object | 15 |
| TC-D06-generator_object | ValueError: unmarshallable object | 15 |
| TC-D06-lambda_function | ValueError: unmarshallable object | 15 |
| TC-D06-normal_function | ValueError: unmarshallable object | 15 |
| TC-D06-object_instance | ValueError: unmarshallable object | 15 |

## 7. Hash Diversity Notes

Distinct hash counts in this cross-platform summary should be interpreted carefully. Different Python versions and marshal format versions are not required to produce identical byte streams. The main stability property tested by member D is same-environment determinism: the same input should produce one unique SHA-256 hash across repeated marshal.dumps() calls, or fail consistently for expected invalid inputs.

| Case ID | Distinct Hash Count | Example Hashes |
|---|---:|---|
| TC-D01 | 1 | d77105626a6c... |
| TC-D02 | 1 | ba5fe04b4870... |
| TC-D03 | 1 | 552c90733114... |
| TC-D04-depth-10 | 1 | 9a0d806cfa97... |
| TC-D04-depth-100 | 1 | 19544ac41bf4... |
| TC-D04-depth-1000 | 1 | 6525e29210e0... |
| TC-D04-depth-500 | 1 | ac450374ff61... |
| TC-D04-depth-900 | 1 | 65832f5ae5a6... |
| TC-D05-depth-10 | 1 | 3268a7dc67f7... |
| TC-D05-depth-100 | 1 | 7fd38dad3e0f... |
| TC-D05-depth-1000 | 1 | 0c1b6a0bfd86... |
| TC-D05-depth-500 | 1 | 8de6f99a65bb... |
| TC-D05-depth-900 | 1 | 6eda7495d5cb... |
| TC-D07 | 1 | 4f2ecf2128e5... |
| TC-D08 | 1 | 947a122c9fac... |
| TC-D09-version-0 | 1 | 39a7383add8e... |
| TC-D09-version-1 | 1 | 39a7383add8e... |
| TC-D09-version-2 | 1 | 39a7383add8e... |
| TC-D09-version-3 | 1 | 1936299e8fdc... |
| TC-D09-version-4 | 1 | fb42180d5c38... |

## 8. Final Aggregated Conclusion

Across the collected member D GitHub Actions results, the test suite did not observe same-process non-determinism. Cyclic structures, deep nested structures below the tested recursion boundary, shared references, marshal version parameter cases, and invalid byte-stream loads all behaved deterministically within each environment. The recorded exceptions were expected boundary or unsupported-input behaviors, such as overly deep nesting and unmarshallable object types.