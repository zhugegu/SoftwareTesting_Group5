# 成员 B 统一测试跨平台比较

## 环境列表

- `member_b_all_darwin_arm64_py3_10_results.json`: macOS-15.7.7-arm64-arm-64bit; implementation=CPython; marshal_version=4
- `member_b_all_darwin_arm64_py3_11_results.json`: macOS-15.7.7-arm64-arm-64bit; implementation=CPython; marshal_version=4
- `member_b_all_darwin_arm64_py3_12_results.json`: macOS-15.7.7-arm64-arm-64bit; implementation=CPython; marshal_version=4
- `member_b_all_darwin_arm64_py3_13_results.json`: macOS-15.7.7-arm64-arm-64bit-Mach-O; implementation=CPython; marshal_version=4
- `member_b_all_darwin_arm64_py3_9_results.json`: macOS-26.5-arm64-arm-64bit; implementation=CPython; marshal_version=4
- `member_b_all_linux_x86_64_py3_10_results.json`: Linux-6.17.0-1015-azure-x86_64-with-glibc2.39; implementation=CPython; marshal_version=4
- `member_b_all_linux_x86_64_py3_11_results.json`: Linux-6.17.0-1015-azure-x86_64-with-glibc2.39; implementation=CPython; marshal_version=4
- `member_b_all_linux_x86_64_py3_12_results.json`: Linux-6.17.0-1015-azure-x86_64-with-glibc2.39; implementation=CPython; marshal_version=4
- `member_b_all_linux_x86_64_py3_13_results.json`: Linux-6.17.0-1015-azure-x86_64-with-glibc2.39; implementation=CPython; marshal_version=4
- `member_b_all_linux_x86_64_py3_9_results.json`: Linux-6.17.0-1015-azure-x86_64-with-glibc2.39; implementation=CPython; marshal_version=4
- `member_b_all_windows_amd64_py3_10_results.json`: Windows-10-10.0.26100-SP0; implementation=CPython; marshal_version=4
- `member_b_all_windows_amd64_py3_11_results.json`: Windows-10-10.0.26100-SP0; implementation=CPython; marshal_version=4
- `member_b_all_windows_amd64_py3_12_results.json`: Windows-2025Server-10.0.26100-SP0; implementation=CPython; marshal_version=4
- `member_b_all_windows_amd64_py3_13_results.json`: Windows-2025Server-10.0.26100-SP0; implementation=CPython; marshal_version=4
- `member_b_all_windows_amd64_py3_9_results.json`: Windows-10-10.0.26100-SP0; implementation=CPython; marshal_version=4

## 单平台同进程稳定性

| Platform | Case count | Stable supported | Unstable supported | Exception/support boundary |
| --- | ---: | ---: | ---: | ---: |
| member_b_all_darwin_arm64_py3_10_results (Darwin/arm64, Python 3.10.11) | 48 | 45 | 0 | 3 |
| member_b_all_darwin_arm64_py3_11_results (Darwin/arm64, Python 3.11.9) | 48 | 45 | 0 | 3 |
| member_b_all_darwin_arm64_py3_12_results (Darwin/arm64, Python 3.12.10) | 48 | 45 | 0 | 3 |
| member_b_all_darwin_arm64_py3_13_results (Darwin/arm64, Python 3.13.13) | 48 | 45 | 0 | 3 |
| member_b_all_darwin_arm64_py3_9_results (Darwin/arm64, Python 3.9.6) | 48 | 45 | 0 | 3 |
| member_b_all_linux_x86_64_py3_10_results (Linux/x86_64, Python 3.10.20) | 48 | 45 | 0 | 3 |
| member_b_all_linux_x86_64_py3_11_results (Linux/x86_64, Python 3.11.15) | 48 | 45 | 0 | 3 |
| member_b_all_linux_x86_64_py3_12_results (Linux/x86_64, Python 3.12.13) | 48 | 45 | 0 | 3 |
| member_b_all_linux_x86_64_py3_13_results (Linux/x86_64, Python 3.13.13) | 48 | 45 | 0 | 3 |
| member_b_all_linux_x86_64_py3_9_results (Linux/x86_64, Python 3.9.25) | 48 | 45 | 0 | 3 |
| member_b_all_windows_amd64_py3_10_results (Windows/AMD64, Python 3.10.11) | 48 | 45 | 0 | 3 |
| member_b_all_windows_amd64_py3_11_results (Windows/AMD64, Python 3.11.9) | 48 | 45 | 0 | 3 |
| member_b_all_windows_amd64_py3_12_results (Windows/AMD64, Python 3.12.10) | 48 | 45 | 0 | 3 |
| member_b_all_windows_amd64_py3_13_results (Windows/AMD64, Python 3.13.13) | 48 | 45 | 0 | 3 |
| member_b_all_windows_amd64_py3_9_results (Windows/AMD64, Python 3.9.13) | 48 | 45 | 0 | 3 |

## 跨平台比较

### member_b_all_darwin_arm64_py3_10_results (Darwin/arm64, Python 3.10.11) vs member_b_all_darwin_arm64_py3_11_results (Darwin/arm64, Python 3.11.9)

| Case | Category | Same marshal hash | Same exception | Interpretation |
| --- | --- | --- | --- | --- |
| ascii_plain | unicode_string | SAME | SAME | Same input and same marshal hash. |
| bytes_255_a | bytes_payload | SAME | SAME | Same input and same marshal hash. |
| bytes_256_a | bytes_payload | SAME | SAME | Same input and same marshal hash. |
| bytes_65535_a | bytes_payload | SAME | SAME | Same input and same marshal hash. |
| bytes_65536_a | bytes_payload | SAME | SAME | Same input and same marshal hash. |
| bytes_all_byte_values | bytes_payload | SAME | SAME | Same input and same marshal hash. |
| bytes_empty | bytes_payload | SAME | SAME | Same input and same marshal hash. |
| bytes_high_values_with_ascii | bytes_payload | SAME | SAME | Same input and same marshal hash. |
| bytes_single_nul | bytes_payload | SAME | SAME | Same input and same marshal hash. |
| chinese_text | unicode_string | SAME | SAME | Same input and same marshal hash. |
| complex_inf_neg_inf | float_complex | SAME | SAME | Same input and same marshal hash. |
| complex_nan_both | float_complex | SAME | SAME | Same input and same marshal hash. |
| complex_nan_imag | float_complex | SAME | SAME | Same input and same marshal hash. |
| complex_nan_real | float_complex | SAME | SAME | Same input and same marshal hash. |
| complex_payload_nan_imag | float_complex | SAME | SAME | Same input and same marshal hash. |
| complex_payload_nan_real | float_complex | SAME | SAME | Same input and same marshal hash. |
| complex_regular | float_complex | SAME | SAME | Same input and same marshal hash. |
| complex_zero_neg_zero | float_complex | SAME | SAME | Same input and same marshal hash. |
| composed_e_acute | unicode_string | SAME | SAME | Same input and same marshal hash. |
| constant_ellipsis | basic_scalar_constant | SAME | SAME | Same input and same marshal hash. |
| constant_false | basic_scalar_constant | SAME | SAME | Same input and same marshal hash. |
| constant_none | basic_scalar_constant | SAME | SAME | Same input and same marshal hash. |
| constant_true | basic_scalar_constant | SAME | SAME | Same input and same marshal hash. |
| crlf_string | unicode_string | SAME | SAME | Same input and same marshal hash. |
| decomposed_e_acute | unicode_string | SAME | SAME | Same input and same marshal hash. |
| emoji_text | unicode_string | SAME | SAME | Same input and same marshal hash. |
| float_huge_1e300 | float_complex | SAME | SAME | Same input and same marshal hash. |
| float_math_nan | float_complex | SAME | SAME | Same input and same marshal hash. |
| float_nan_constructor | float_complex | SAME | SAME | Same input and same marshal hash. |
| float_nan_payload_0x7ff0000000000001 | float_complex | SAME | SAME | Same input and same marshal hash. |
| float_nan_payload_0x7ff8000000000001 | float_complex | SAME | SAME | Same input and same marshal hash. |
| float_nan_payload_0x7ff8000000000002 | float_complex | SAME | SAME | Same input and same marshal hash. |
| float_neg_inf | float_complex | SAME | SAME | Same input and same marshal hash. |
| float_neg_one | float_complex | SAME | SAME | Same input and same marshal hash. |
| float_neg_zero | float_complex | SAME | SAME | Same input and same marshal hash. |
| float_pos_inf | float_complex | SAME | SAME | Same input and same marshal hash. |
| float_pos_one | float_complex | SAME | SAME | Same input and same marshal hash. |
| float_pos_zero | float_complex | SAME | SAME | Same input and same marshal hash. |
| float_tiny_1e_minus_300 | float_complex | SAME | SAME | Same input and same marshal hash. |
| lone_high_surrogate | unicode_string | SAME | SAME | Same input and same marshal hash. |
| non_bmp_character | unicode_string | SAME | SAME | Same input and same marshal hash. |
| nul_inside_string | unicode_string | SAME | SAME | Same input and same marshal hash. |
| recreated_complex_nan_both | float_complex | SAME | SAME | Same input and same marshal hash. |
| recreated_float_nan | float_complex | SAME | SAME | Same input and same marshal hash. |
| slice_1_10_2 | optional_slice_probe | DIFFERENT | SAME | Same optional support boundary or exception behavior. |
| slice_neg10_none_neg1 | optional_slice_probe | DIFFERENT | SAME | Same optional support boundary or exception behavior. |
| slice_none_none_none | optional_slice_probe | DIFFERENT | SAME | Same optional support boundary or exception behavior. |
| zero_width_joiner_sequence | unicode_string | SAME | SAME | Same input and same marshal hash. |

### member_b_all_darwin_arm64_py3_10_results (Darwin/arm64, Python 3.10.11) vs member_b_all_darwin_arm64_py3_12_results (Darwin/arm64, Python 3.12.10)

| Case | Category | Same marshal hash | Same exception | Interpretation |
| --- | --- | --- | --- | --- |
| ascii_plain | unicode_string | SAME | SAME | Same input and same marshal hash. |
| bytes_255_a | bytes_payload | SAME | SAME | Same input and same marshal hash. |
| bytes_256_a | bytes_payload | SAME | SAME | Same input and same marshal hash. |
| bytes_65535_a | bytes_payload | SAME | SAME | Same input and same marshal hash. |
| bytes_65536_a | bytes_payload | SAME | SAME | Same input and same marshal hash. |
| bytes_all_byte_values | bytes_payload | SAME | SAME | Same input and same marshal hash. |
| bytes_empty | bytes_payload | SAME | SAME | Same input and same marshal hash. |
| bytes_high_values_with_ascii | bytes_payload | SAME | SAME | Same input and same marshal hash. |
| bytes_single_nul | bytes_payload | SAME | SAME | Same input and same marshal hash. |
| chinese_text | unicode_string | SAME | SAME | Same input and same marshal hash. |
| complex_inf_neg_inf | float_complex | SAME | SAME | Same input and same marshal hash. |
| complex_nan_both | float_complex | SAME | SAME | Same input and same marshal hash. |
| complex_nan_imag | float_complex | SAME | SAME | Same input and same marshal hash. |
| complex_nan_real | float_complex | SAME | SAME | Same input and same marshal hash. |
| complex_payload_nan_imag | float_complex | SAME | SAME | Same input and same marshal hash. |
| complex_payload_nan_real | float_complex | SAME | SAME | Same input and same marshal hash. |
| complex_regular | float_complex | SAME | SAME | Same input and same marshal hash. |
| complex_zero_neg_zero | float_complex | SAME | SAME | Same input and same marshal hash. |
| composed_e_acute | unicode_string | DIFFERENT | SAME | Same input representation but Python major/minor differs; likely version-level marshal format difference. |
| constant_ellipsis | basic_scalar_constant | SAME | SAME | Same input and same marshal hash. |
| constant_false | basic_scalar_constant | SAME | SAME | Same input and same marshal hash. |
| constant_none | basic_scalar_constant | SAME | SAME | Same input and same marshal hash. |
| constant_true | basic_scalar_constant | SAME | SAME | Same input and same marshal hash. |
| crlf_string | unicode_string | SAME | SAME | Same input and same marshal hash. |
| decomposed_e_acute | unicode_string | SAME | SAME | Same input and same marshal hash. |
| emoji_text | unicode_string | SAME | SAME | Same input and same marshal hash. |
| float_huge_1e300 | float_complex | SAME | SAME | Same input and same marshal hash. |
| float_math_nan | float_complex | SAME | SAME | Same input and same marshal hash. |
| float_nan_constructor | float_complex | SAME | SAME | Same input and same marshal hash. |
| float_nan_payload_0x7ff0000000000001 | float_complex | SAME | SAME | Same input and same marshal hash. |
| float_nan_payload_0x7ff8000000000001 | float_complex | SAME | SAME | Same input and same marshal hash. |
| float_nan_payload_0x7ff8000000000002 | float_complex | SAME | SAME | Same input and same marshal hash. |
| float_neg_inf | float_complex | SAME | SAME | Same input and same marshal hash. |
| float_neg_one | float_complex | SAME | SAME | Same input and same marshal hash. |
| float_neg_zero | float_complex | SAME | SAME | Same input and same marshal hash. |
| float_pos_inf | float_complex | SAME | SAME | Same input and same marshal hash. |
| float_pos_one | float_complex | SAME | SAME | Same input and same marshal hash. |
| float_pos_zero | float_complex | SAME | SAME | Same input and same marshal hash. |
| float_tiny_1e_minus_300 | float_complex | SAME | SAME | Same input and same marshal hash. |
| lone_high_surrogate | unicode_string | SAME | SAME | Same input and same marshal hash. |
| non_bmp_character | unicode_string | SAME | SAME | Same input and same marshal hash. |
| nul_inside_string | unicode_string | SAME | SAME | Same input and same marshal hash. |
| recreated_complex_nan_both | float_complex | SAME | SAME | Same input and same marshal hash. |
| recreated_float_nan | float_complex | SAME | SAME | Same input and same marshal hash. |
| slice_1_10_2 | optional_slice_probe | DIFFERENT | SAME | Same optional support boundary or exception behavior. |
| slice_neg10_none_neg1 | optional_slice_probe | DIFFERENT | SAME | Same optional support boundary or exception behavior. |
| slice_none_none_none | optional_slice_probe | DIFFERENT | SAME | Same optional support boundary or exception behavior. |
| zero_width_joiner_sequence | unicode_string | SAME | SAME | Same input and same marshal hash. |

### member_b_all_darwin_arm64_py3_10_results (Darwin/arm64, Python 3.10.11) vs member_b_all_darwin_arm64_py3_13_results (Darwin/arm64, Python 3.13.13)

| Case | Category | Same marshal hash | Same exception | Interpretation |
| --- | --- | --- | --- | --- |
| ascii_plain | unicode_string | SAME | SAME | Same input and same marshal hash. |
| bytes_255_a | bytes_payload | SAME | SAME | Same input and same marshal hash. |
| bytes_256_a | bytes_payload | SAME | SAME | Same input and same marshal hash. |
| bytes_65535_a | bytes_payload | SAME | SAME | Same input and same marshal hash. |
| bytes_65536_a | bytes_payload | SAME | SAME | Same input and same marshal hash. |
| bytes_all_byte_values | bytes_payload | SAME | SAME | Same input and same marshal hash. |
| bytes_empty | bytes_payload | SAME | SAME | Same input and same marshal hash. |
| bytes_high_values_with_ascii | bytes_payload | SAME | SAME | Same input and same marshal hash. |
| bytes_single_nul | bytes_payload | SAME | SAME | Same input and same marshal hash. |
| chinese_text | unicode_string | SAME | SAME | Same input and same marshal hash. |
| complex_inf_neg_inf | float_complex | SAME | SAME | Same input and same marshal hash. |
| complex_nan_both | float_complex | SAME | SAME | Same input and same marshal hash. |
| complex_nan_imag | float_complex | SAME | SAME | Same input and same marshal hash. |
| complex_nan_real | float_complex | SAME | SAME | Same input and same marshal hash. |
| complex_payload_nan_imag | float_complex | SAME | SAME | Same input and same marshal hash. |
| complex_payload_nan_real | float_complex | SAME | SAME | Same input and same marshal hash. |
| complex_regular | float_complex | SAME | SAME | Same input and same marshal hash. |
| complex_zero_neg_zero | float_complex | SAME | SAME | Same input and same marshal hash. |
| composed_e_acute | unicode_string | DIFFERENT | SAME | Same input representation but Python major/minor differs; likely version-level marshal format difference. |
| constant_ellipsis | basic_scalar_constant | SAME | SAME | Same input and same marshal hash. |
| constant_false | basic_scalar_constant | SAME | SAME | Same input and same marshal hash. |
| constant_none | basic_scalar_constant | SAME | SAME | Same input and same marshal hash. |
| constant_true | basic_scalar_constant | SAME | SAME | Same input and same marshal hash. |
| crlf_string | unicode_string | SAME | SAME | Same input and same marshal hash. |
| decomposed_e_acute | unicode_string | SAME | SAME | Same input and same marshal hash. |
| emoji_text | unicode_string | SAME | SAME | Same input and same marshal hash. |
| float_huge_1e300 | float_complex | SAME | SAME | Same input and same marshal hash. |
| float_math_nan | float_complex | SAME | SAME | Same input and same marshal hash. |
| float_nan_constructor | float_complex | SAME | SAME | Same input and same marshal hash. |
| float_nan_payload_0x7ff0000000000001 | float_complex | SAME | SAME | Same input and same marshal hash. |
| float_nan_payload_0x7ff8000000000001 | float_complex | SAME | SAME | Same input and same marshal hash. |
| float_nan_payload_0x7ff8000000000002 | float_complex | SAME | SAME | Same input and same marshal hash. |
| float_neg_inf | float_complex | SAME | SAME | Same input and same marshal hash. |
| float_neg_one | float_complex | SAME | SAME | Same input and same marshal hash. |
| float_neg_zero | float_complex | SAME | SAME | Same input and same marshal hash. |
| float_pos_inf | float_complex | SAME | SAME | Same input and same marshal hash. |
| float_pos_one | float_complex | SAME | SAME | Same input and same marshal hash. |
| float_pos_zero | float_complex | SAME | SAME | Same input and same marshal hash. |
| float_tiny_1e_minus_300 | float_complex | SAME | SAME | Same input and same marshal hash. |
| lone_high_surrogate | unicode_string | SAME | SAME | Same input and same marshal hash. |
| non_bmp_character | unicode_string | SAME | SAME | Same input and same marshal hash. |
| nul_inside_string | unicode_string | SAME | SAME | Same input and same marshal hash. |
| recreated_complex_nan_both | float_complex | SAME | SAME | Same input and same marshal hash. |
| recreated_float_nan | float_complex | SAME | SAME | Same input and same marshal hash. |
| slice_1_10_2 | optional_slice_probe | DIFFERENT | SAME | Same optional support boundary or exception behavior. |
| slice_neg10_none_neg1 | optional_slice_probe | DIFFERENT | SAME | Same optional support boundary or exception behavior. |
| slice_none_none_none | optional_slice_probe | DIFFERENT | SAME | Same optional support boundary or exception behavior. |
| zero_width_joiner_sequence | unicode_string | SAME | SAME | Same input and same marshal hash. |

### member_b_all_darwin_arm64_py3_10_results (Darwin/arm64, Python 3.10.11) vs member_b_all_darwin_arm64_py3_9_results (Darwin/arm64, Python 3.9.6)

| Case | Category | Same marshal hash | Same exception | Interpretation |
| --- | --- | --- | --- | --- |
| ascii_plain | unicode_string | SAME | SAME | Same input and same marshal hash. |
| bytes_255_a | bytes_payload | SAME | SAME | Same input and same marshal hash. |
| bytes_256_a | bytes_payload | SAME | SAME | Same input and same marshal hash. |
| bytes_65535_a | bytes_payload | SAME | SAME | Same input and same marshal hash. |
| bytes_65536_a | bytes_payload | SAME | SAME | Same input and same marshal hash. |
| bytes_all_byte_values | bytes_payload | SAME | SAME | Same input and same marshal hash. |
| bytes_empty | bytes_payload | SAME | SAME | Same input and same marshal hash. |
| bytes_high_values_with_ascii | bytes_payload | SAME | SAME | Same input and same marshal hash. |
| bytes_single_nul | bytes_payload | SAME | SAME | Same input and same marshal hash. |
| chinese_text | unicode_string | SAME | SAME | Same input and same marshal hash. |
| complex_inf_neg_inf | float_complex | SAME | SAME | Same input and same marshal hash. |
| complex_nan_both | float_complex | SAME | SAME | Same input and same marshal hash. |
| complex_nan_imag | float_complex | SAME | SAME | Same input and same marshal hash. |
| complex_nan_real | float_complex | SAME | SAME | Same input and same marshal hash. |
| complex_payload_nan_imag | float_complex | SAME | SAME | Same input and same marshal hash. |
| complex_payload_nan_real | float_complex | SAME | SAME | Same input and same marshal hash. |
| complex_regular | float_complex | SAME | SAME | Same input and same marshal hash. |
| complex_zero_neg_zero | float_complex | SAME | SAME | Same input and same marshal hash. |
| composed_e_acute | unicode_string | SAME | SAME | Same input and same marshal hash. |
| constant_ellipsis | basic_scalar_constant | SAME | SAME | Same input and same marshal hash. |
| constant_false | basic_scalar_constant | SAME | SAME | Same input and same marshal hash. |
| constant_none | basic_scalar_constant | SAME | SAME | Same input and same marshal hash. |
| constant_true | basic_scalar_constant | SAME | SAME | Same input and same marshal hash. |
| crlf_string | unicode_string | SAME | SAME | Same input and same marshal hash. |
| decomposed_e_acute | unicode_string | SAME | SAME | Same input and same marshal hash. |
| emoji_text | unicode_string | SAME | SAME | Same input and same marshal hash. |
| float_huge_1e300 | float_complex | SAME | SAME | Same input and same marshal hash. |
| float_math_nan | float_complex | SAME | SAME | Same input and same marshal hash. |
| float_nan_constructor | float_complex | SAME | SAME | Same input and same marshal hash. |
| float_nan_payload_0x7ff0000000000001 | float_complex | SAME | SAME | Same input and same marshal hash. |
| float_nan_payload_0x7ff8000000000001 | float_complex | SAME | SAME | Same input and same marshal hash. |
| float_nan_payload_0x7ff8000000000002 | float_complex | SAME | SAME | Same input and same marshal hash. |
| float_neg_inf | float_complex | SAME | SAME | Same input and same marshal hash. |
| float_neg_one | float_complex | SAME | SAME | Same input and same marshal hash. |
| float_neg_zero | float_complex | SAME | SAME | Same input and same marshal hash. |
| float_pos_inf | float_complex | SAME | SAME | Same input and same marshal hash. |
| float_pos_one | float_complex | SAME | SAME | Same input and same marshal hash. |
| float_pos_zero | float_complex | SAME | SAME | Same input and same marshal hash. |
| float_tiny_1e_minus_300 | float_complex | SAME | SAME | Same input and same marshal hash. |
| lone_high_surrogate | unicode_string | SAME | SAME | Same input and same marshal hash. |
| non_bmp_character | unicode_string | SAME | SAME | Same input and same marshal hash. |
| nul_inside_string | unicode_string | SAME | SAME | Same input and same marshal hash. |
| recreated_complex_nan_both | float_complex | SAME | SAME | Same input and same marshal hash. |
| recreated_float_nan | float_complex | SAME | SAME | Same input and same marshal hash. |
| slice_1_10_2 | optional_slice_probe | DIFFERENT | SAME | Same optional support boundary or exception behavior. |
| slice_neg10_none_neg1 | optional_slice_probe | DIFFERENT | SAME | Same optional support boundary or exception behavior. |
| slice_none_none_none | optional_slice_probe | DIFFERENT | SAME | Same optional support boundary or exception behavior. |
| zero_width_joiner_sequence | unicode_string | SAME | SAME | Same input and same marshal hash. |

### member_b_all_darwin_arm64_py3_10_results (Darwin/arm64, Python 3.10.11) vs member_b_all_linux_x86_64_py3_10_results (Linux/x86_64, Python 3.10.20)

| Case | Category | Same marshal hash | Same exception | Interpretation |
| --- | --- | --- | --- | --- |
| ascii_plain | unicode_string | SAME | SAME | Same input and same marshal hash. |
| bytes_255_a | bytes_payload | SAME | SAME | Same input and same marshal hash. |
| bytes_256_a | bytes_payload | SAME | SAME | Same input and same marshal hash. |
| bytes_65535_a | bytes_payload | SAME | SAME | Same input and same marshal hash. |
| bytes_65536_a | bytes_payload | SAME | SAME | Same input and same marshal hash. |
| bytes_all_byte_values | bytes_payload | SAME | SAME | Same input and same marshal hash. |
| bytes_empty | bytes_payload | SAME | SAME | Same input and same marshal hash. |
| bytes_high_values_with_ascii | bytes_payload | SAME | SAME | Same input and same marshal hash. |
| bytes_single_nul | bytes_payload | SAME | SAME | Same input and same marshal hash. |
| chinese_text | unicode_string | SAME | SAME | Same input and same marshal hash. |
| complex_inf_neg_inf | float_complex | SAME | SAME | Same input and same marshal hash. |
| complex_nan_both | float_complex | SAME | SAME | Same input and same marshal hash. |
| complex_nan_imag | float_complex | SAME | SAME | Same input and same marshal hash. |
| complex_nan_real | float_complex | SAME | SAME | Same input and same marshal hash. |
| complex_payload_nan_imag | float_complex | SAME | SAME | Same input and same marshal hash. |
| complex_payload_nan_real | float_complex | SAME | SAME | Same input and same marshal hash. |
| complex_regular | float_complex | SAME | SAME | Same input and same marshal hash. |
| complex_zero_neg_zero | float_complex | SAME | SAME | Same input and same marshal hash. |
| composed_e_acute | unicode_string | SAME | SAME | Same input and same marshal hash. |
| constant_ellipsis | basic_scalar_constant | SAME | SAME | Same input and same marshal hash. |
| constant_false | basic_scalar_constant | SAME | SAME | Same input and same marshal hash. |
| constant_none | basic_scalar_constant | SAME | SAME | Same input and same marshal hash. |
| constant_true | basic_scalar_constant | SAME | SAME | Same input and same marshal hash. |
| crlf_string | unicode_string | SAME | SAME | Same input and same marshal hash. |
| decomposed_e_acute | unicode_string | SAME | SAME | Same input and same marshal hash. |
| emoji_text | unicode_string | SAME | SAME | Same input and same marshal hash. |
| float_huge_1e300 | float_complex | SAME | SAME | Same input and same marshal hash. |
| float_math_nan | float_complex | SAME | SAME | Same input and same marshal hash. |
| float_nan_constructor | float_complex | SAME | SAME | Same input and same marshal hash. |
| float_nan_payload_0x7ff0000000000001 | float_complex | SAME | SAME | Same input and same marshal hash. |
| float_nan_payload_0x7ff8000000000001 | float_complex | SAME | SAME | Same input and same marshal hash. |
| float_nan_payload_0x7ff8000000000002 | float_complex | SAME | SAME | Same input and same marshal hash. |
| float_neg_inf | float_complex | SAME | SAME | Same input and same marshal hash. |
| float_neg_one | float_complex | SAME | SAME | Same input and same marshal hash. |
| float_neg_zero | float_complex | SAME | SAME | Same input and same marshal hash. |
| float_pos_inf | float_complex | SAME | SAME | Same input and same marshal hash. |
| float_pos_one | float_complex | SAME | SAME | Same input and same marshal hash. |
| float_pos_zero | float_complex | SAME | SAME | Same input and same marshal hash. |
| float_tiny_1e_minus_300 | float_complex | SAME | SAME | Same input and same marshal hash. |
| lone_high_surrogate | unicode_string | SAME | SAME | Same input and same marshal hash. |
| non_bmp_character | unicode_string | SAME | SAME | Same input and same marshal hash. |
| nul_inside_string | unicode_string | SAME | SAME | Same input and same marshal hash. |
| recreated_complex_nan_both | float_complex | SAME | SAME | Same input and same marshal hash. |
| recreated_float_nan | float_complex | SAME | SAME | Same input and same marshal hash. |
| slice_1_10_2 | optional_slice_probe | DIFFERENT | SAME | Same optional support boundary or exception behavior. |
| slice_neg10_none_neg1 | optional_slice_probe | DIFFERENT | SAME | Same optional support boundary or exception behavior. |
| slice_none_none_none | optional_slice_probe | DIFFERENT | SAME | Same optional support boundary or exception behavior. |
| zero_width_joiner_sequence | unicode_string | SAME | SAME | Same input and same marshal hash. |

### member_b_all_darwin_arm64_py3_10_results (Darwin/arm64, Python 3.10.11) vs member_b_all_linux_x86_64_py3_11_results (Linux/x86_64, Python 3.11.15)

| Case | Category | Same marshal hash | Same exception | Interpretation |
| --- | --- | --- | --- | --- |
| ascii_plain | unicode_string | SAME | SAME | Same input and same marshal hash. |
| bytes_255_a | bytes_payload | SAME | SAME | Same input and same marshal hash. |
| bytes_256_a | bytes_payload | SAME | SAME | Same input and same marshal hash. |
| bytes_65535_a | bytes_payload | SAME | SAME | Same input and same marshal hash. |
| bytes_65536_a | bytes_payload | SAME | SAME | Same input and same marshal hash. |
| bytes_all_byte_values | bytes_payload | SAME | SAME | Same input and same marshal hash. |
| bytes_empty | bytes_payload | SAME | SAME | Same input and same marshal hash. |
| bytes_high_values_with_ascii | bytes_payload | SAME | SAME | Same input and same marshal hash. |
| bytes_single_nul | bytes_payload | SAME | SAME | Same input and same marshal hash. |
| chinese_text | unicode_string | SAME | SAME | Same input and same marshal hash. |
| complex_inf_neg_inf | float_complex | SAME | SAME | Same input and same marshal hash. |
| complex_nan_both | float_complex | SAME | SAME | Same input and same marshal hash. |
| complex_nan_imag | float_complex | SAME | SAME | Same input and same marshal hash. |
| complex_nan_real | float_complex | SAME | SAME | Same input and same marshal hash. |
| complex_payload_nan_imag | float_complex | SAME | SAME | Same input and same marshal hash. |
| complex_payload_nan_real | float_complex | SAME | SAME | Same input and same marshal hash. |
| complex_regular | float_complex | SAME | SAME | Same input and same marshal hash. |
| complex_zero_neg_zero | float_complex | SAME | SAME | Same input and same marshal hash. |
| composed_e_acute | unicode_string | SAME | SAME | Same input and same marshal hash. |
| constant_ellipsis | basic_scalar_constant | SAME | SAME | Same input and same marshal hash. |
| constant_false | basic_scalar_constant | SAME | SAME | Same input and same marshal hash. |
| constant_none | basic_scalar_constant | SAME | SAME | Same input and same marshal hash. |
| constant_true | basic_scalar_constant | SAME | SAME | Same input and same marshal hash. |
| crlf_string | unicode_string | SAME | SAME | Same input and same marshal hash. |
| decomposed_e_acute | unicode_string | SAME | SAME | Same input and same marshal hash. |
| emoji_text | unicode_string | SAME | SAME | Same input and same marshal hash. |
| float_huge_1e300 | float_complex | SAME | SAME | Same input and same marshal hash. |
| float_math_nan | float_complex | SAME | SAME | Same input and same marshal hash. |
| float_nan_constructor | float_complex | SAME | SAME | Same input and same marshal hash. |
| float_nan_payload_0x7ff0000000000001 | float_complex | SAME | SAME | Same input and same marshal hash. |
| float_nan_payload_0x7ff8000000000001 | float_complex | SAME | SAME | Same input and same marshal hash. |
| float_nan_payload_0x7ff8000000000002 | float_complex | SAME | SAME | Same input and same marshal hash. |
| float_neg_inf | float_complex | SAME | SAME | Same input and same marshal hash. |
| float_neg_one | float_complex | SAME | SAME | Same input and same marshal hash. |
| float_neg_zero | float_complex | SAME | SAME | Same input and same marshal hash. |
| float_pos_inf | float_complex | SAME | SAME | Same input and same marshal hash. |
| float_pos_one | float_complex | SAME | SAME | Same input and same marshal hash. |
| float_pos_zero | float_complex | SAME | SAME | Same input and same marshal hash. |
| float_tiny_1e_minus_300 | float_complex | SAME | SAME | Same input and same marshal hash. |
| lone_high_surrogate | unicode_string | SAME | SAME | Same input and same marshal hash. |
| non_bmp_character | unicode_string | SAME | SAME | Same input and same marshal hash. |
| nul_inside_string | unicode_string | SAME | SAME | Same input and same marshal hash. |
| recreated_complex_nan_both | float_complex | SAME | SAME | Same input and same marshal hash. |
| recreated_float_nan | float_complex | SAME | SAME | Same input and same marshal hash. |
| slice_1_10_2 | optional_slice_probe | DIFFERENT | SAME | Same optional support boundary or exception behavior. |
| slice_neg10_none_neg1 | optional_slice_probe | DIFFERENT | SAME | Same optional support boundary or exception behavior. |
| slice_none_none_none | optional_slice_probe | DIFFERENT | SAME | Same optional support boundary or exception behavior. |
| zero_width_joiner_sequence | unicode_string | SAME | SAME | Same input and same marshal hash. |

### member_b_all_darwin_arm64_py3_10_results (Darwin/arm64, Python 3.10.11) vs member_b_all_linux_x86_64_py3_12_results (Linux/x86_64, Python 3.12.13)

| Case | Category | Same marshal hash | Same exception | Interpretation |
| --- | --- | --- | --- | --- |
| ascii_plain | unicode_string | SAME | SAME | Same input and same marshal hash. |
| bytes_255_a | bytes_payload | SAME | SAME | Same input and same marshal hash. |
| bytes_256_a | bytes_payload | SAME | SAME | Same input and same marshal hash. |
| bytes_65535_a | bytes_payload | SAME | SAME | Same input and same marshal hash. |
| bytes_65536_a | bytes_payload | SAME | SAME | Same input and same marshal hash. |
| bytes_all_byte_values | bytes_payload | SAME | SAME | Same input and same marshal hash. |
| bytes_empty | bytes_payload | SAME | SAME | Same input and same marshal hash. |
| bytes_high_values_with_ascii | bytes_payload | SAME | SAME | Same input and same marshal hash. |
| bytes_single_nul | bytes_payload | SAME | SAME | Same input and same marshal hash. |
| chinese_text | unicode_string | SAME | SAME | Same input and same marshal hash. |
| complex_inf_neg_inf | float_complex | SAME | SAME | Same input and same marshal hash. |
| complex_nan_both | float_complex | SAME | SAME | Same input and same marshal hash. |
| complex_nan_imag | float_complex | SAME | SAME | Same input and same marshal hash. |
| complex_nan_real | float_complex | SAME | SAME | Same input and same marshal hash. |
| complex_payload_nan_imag | float_complex | SAME | SAME | Same input and same marshal hash. |
| complex_payload_nan_real | float_complex | SAME | SAME | Same input and same marshal hash. |
| complex_regular | float_complex | SAME | SAME | Same input and same marshal hash. |
| complex_zero_neg_zero | float_complex | SAME | SAME | Same input and same marshal hash. |
| composed_e_acute | unicode_string | DIFFERENT | SAME | Same input representation but Python major/minor differs; likely version-level marshal format difference. |
| constant_ellipsis | basic_scalar_constant | SAME | SAME | Same input and same marshal hash. |
| constant_false | basic_scalar_constant | SAME | SAME | Same input and same marshal hash. |
| constant_none | basic_scalar_constant | SAME | SAME | Same input and same marshal hash. |
| constant_true | basic_scalar_constant | SAME | SAME | Same input and same marshal hash. |
| crlf_string | unicode_string | SAME | SAME | Same input and same marshal hash. |
| decomposed_e_acute | unicode_string | SAME | SAME | Same input and same marshal hash. |
| emoji_text | unicode_string | SAME | SAME | Same input and same marshal hash. |
| float_huge_1e300 | float_complex | SAME | SAME | Same input and same marshal hash. |
| float_math_nan | float_complex | SAME | SAME | Same input and same marshal hash. |
| float_nan_constructor | float_complex | SAME | SAME | Same input and same marshal hash. |
| float_nan_payload_0x7ff0000000000001 | float_complex | SAME | SAME | Same input and same marshal hash. |
| float_nan_payload_0x7ff8000000000001 | float_complex | SAME | SAME | Same input and same marshal hash. |
| float_nan_payload_0x7ff8000000000002 | float_complex | SAME | SAME | Same input and same marshal hash. |
| float_neg_inf | float_complex | SAME | SAME | Same input and same marshal hash. |
| float_neg_one | float_complex | SAME | SAME | Same input and same marshal hash. |
| float_neg_zero | float_complex | SAME | SAME | Same input and same marshal hash. |
| float_pos_inf | float_complex | SAME | SAME | Same input and same marshal hash. |
| float_pos_one | float_complex | SAME | SAME | Same input and same marshal hash. |
| float_pos_zero | float_complex | SAME | SAME | Same input and same marshal hash. |
| float_tiny_1e_minus_300 | float_complex | SAME | SAME | Same input and same marshal hash. |
| lone_high_surrogate | unicode_string | SAME | SAME | Same input and same marshal hash. |
| non_bmp_character | unicode_string | SAME | SAME | Same input and same marshal hash. |
| nul_inside_string | unicode_string | SAME | SAME | Same input and same marshal hash. |
| recreated_complex_nan_both | float_complex | SAME | SAME | Same input and same marshal hash. |
| recreated_float_nan | float_complex | SAME | SAME | Same input and same marshal hash. |
| slice_1_10_2 | optional_slice_probe | DIFFERENT | SAME | Same optional support boundary or exception behavior. |
| slice_neg10_none_neg1 | optional_slice_probe | DIFFERENT | SAME | Same optional support boundary or exception behavior. |
| slice_none_none_none | optional_slice_probe | DIFFERENT | SAME | Same optional support boundary or exception behavior. |
| zero_width_joiner_sequence | unicode_string | SAME | SAME | Same input and same marshal hash. |

### member_b_all_darwin_arm64_py3_10_results (Darwin/arm64, Python 3.10.11) vs member_b_all_linux_x86_64_py3_13_results (Linux/x86_64, Python 3.13.13)

| Case | Category | Same marshal hash | Same exception | Interpretation |
| --- | --- | --- | --- | --- |
| ascii_plain | unicode_string | SAME | SAME | Same input and same marshal hash. |
| bytes_255_a | bytes_payload | SAME | SAME | Same input and same marshal hash. |
| bytes_256_a | bytes_payload | SAME | SAME | Same input and same marshal hash. |
| bytes_65535_a | bytes_payload | SAME | SAME | Same input and same marshal hash. |
| bytes_65536_a | bytes_payload | SAME | SAME | Same input and same marshal hash. |
| bytes_all_byte_values | bytes_payload | SAME | SAME | Same input and same marshal hash. |
| bytes_empty | bytes_payload | SAME | SAME | Same input and same marshal hash. |
| bytes_high_values_with_ascii | bytes_payload | SAME | SAME | Same input and same marshal hash. |
| bytes_single_nul | bytes_payload | SAME | SAME | Same input and same marshal hash. |
| chinese_text | unicode_string | SAME | SAME | Same input and same marshal hash. |
| complex_inf_neg_inf | float_complex | SAME | SAME | Same input and same marshal hash. |
| complex_nan_both | float_complex | SAME | SAME | Same input and same marshal hash. |
| complex_nan_imag | float_complex | SAME | SAME | Same input and same marshal hash. |
| complex_nan_real | float_complex | SAME | SAME | Same input and same marshal hash. |
| complex_payload_nan_imag | float_complex | SAME | SAME | Same input and same marshal hash. |
| complex_payload_nan_real | float_complex | SAME | SAME | Same input and same marshal hash. |
| complex_regular | float_complex | SAME | SAME | Same input and same marshal hash. |
| complex_zero_neg_zero | float_complex | SAME | SAME | Same input and same marshal hash. |
| composed_e_acute | unicode_string | DIFFERENT | SAME | Same input representation but Python major/minor differs; likely version-level marshal format difference. |
| constant_ellipsis | basic_scalar_constant | SAME | SAME | Same input and same marshal hash. |
| constant_false | basic_scalar_constant | SAME | SAME | Same input and same marshal hash. |
| constant_none | basic_scalar_constant | SAME | SAME | Same input and same marshal hash. |
| constant_true | basic_scalar_constant | SAME | SAME | Same input and same marshal hash. |
| crlf_string | unicode_string | SAME | SAME | Same input and same marshal hash. |
| decomposed_e_acute | unicode_string | SAME | SAME | Same input and same marshal hash. |
| emoji_text | unicode_string | SAME | SAME | Same input and same marshal hash. |
| float_huge_1e300 | float_complex | SAME | SAME | Same input and same marshal hash. |
| float_math_nan | float_complex | SAME | SAME | Same input and same marshal hash. |
| float_nan_constructor | float_complex | SAME | SAME | Same input and same marshal hash. |
| float_nan_payload_0x7ff0000000000001 | float_complex | SAME | SAME | Same input and same marshal hash. |
| float_nan_payload_0x7ff8000000000001 | float_complex | SAME | SAME | Same input and same marshal hash. |
| float_nan_payload_0x7ff8000000000002 | float_complex | SAME | SAME | Same input and same marshal hash. |
| float_neg_inf | float_complex | SAME | SAME | Same input and same marshal hash. |
| float_neg_one | float_complex | SAME | SAME | Same input and same marshal hash. |
| float_neg_zero | float_complex | SAME | SAME | Same input and same marshal hash. |
| float_pos_inf | float_complex | SAME | SAME | Same input and same marshal hash. |
| float_pos_one | float_complex | SAME | SAME | Same input and same marshal hash. |
| float_pos_zero | float_complex | SAME | SAME | Same input and same marshal hash. |
| float_tiny_1e_minus_300 | float_complex | SAME | SAME | Same input and same marshal hash. |
| lone_high_surrogate | unicode_string | SAME | SAME | Same input and same marshal hash. |
| non_bmp_character | unicode_string | SAME | SAME | Same input and same marshal hash. |
| nul_inside_string | unicode_string | SAME | SAME | Same input and same marshal hash. |
| recreated_complex_nan_both | float_complex | SAME | SAME | Same input and same marshal hash. |
| recreated_float_nan | float_complex | SAME | SAME | Same input and same marshal hash. |
| slice_1_10_2 | optional_slice_probe | DIFFERENT | SAME | Same optional support boundary or exception behavior. |
| slice_neg10_none_neg1 | optional_slice_probe | DIFFERENT | SAME | Same optional support boundary or exception behavior. |
| slice_none_none_none | optional_slice_probe | DIFFERENT | SAME | Same optional support boundary or exception behavior. |
| zero_width_joiner_sequence | unicode_string | SAME | SAME | Same input and same marshal hash. |

### member_b_all_darwin_arm64_py3_10_results (Darwin/arm64, Python 3.10.11) vs member_b_all_linux_x86_64_py3_9_results (Linux/x86_64, Python 3.9.25)

| Case | Category | Same marshal hash | Same exception | Interpretation |
| --- | --- | --- | --- | --- |
| ascii_plain | unicode_string | SAME | SAME | Same input and same marshal hash. |
| bytes_255_a | bytes_payload | SAME | SAME | Same input and same marshal hash. |
| bytes_256_a | bytes_payload | SAME | SAME | Same input and same marshal hash. |
| bytes_65535_a | bytes_payload | SAME | SAME | Same input and same marshal hash. |
| bytes_65536_a | bytes_payload | SAME | SAME | Same input and same marshal hash. |
| bytes_all_byte_values | bytes_payload | SAME | SAME | Same input and same marshal hash. |
| bytes_empty | bytes_payload | SAME | SAME | Same input and same marshal hash. |
| bytes_high_values_with_ascii | bytes_payload | SAME | SAME | Same input and same marshal hash. |
| bytes_single_nul | bytes_payload | SAME | SAME | Same input and same marshal hash. |
| chinese_text | unicode_string | SAME | SAME | Same input and same marshal hash. |
| complex_inf_neg_inf | float_complex | SAME | SAME | Same input and same marshal hash. |
| complex_nan_both | float_complex | SAME | SAME | Same input and same marshal hash. |
| complex_nan_imag | float_complex | SAME | SAME | Same input and same marshal hash. |
| complex_nan_real | float_complex | SAME | SAME | Same input and same marshal hash. |
| complex_payload_nan_imag | float_complex | SAME | SAME | Same input and same marshal hash. |
| complex_payload_nan_real | float_complex | SAME | SAME | Same input and same marshal hash. |
| complex_regular | float_complex | SAME | SAME | Same input and same marshal hash. |
| complex_zero_neg_zero | float_complex | SAME | SAME | Same input and same marshal hash. |
| composed_e_acute | unicode_string | SAME | SAME | Same input and same marshal hash. |
| constant_ellipsis | basic_scalar_constant | SAME | SAME | Same input and same marshal hash. |
| constant_false | basic_scalar_constant | SAME | SAME | Same input and same marshal hash. |
| constant_none | basic_scalar_constant | SAME | SAME | Same input and same marshal hash. |
| constant_true | basic_scalar_constant | SAME | SAME | Same input and same marshal hash. |
| crlf_string | unicode_string | SAME | SAME | Same input and same marshal hash. |
| decomposed_e_acute | unicode_string | SAME | SAME | Same input and same marshal hash. |
| emoji_text | unicode_string | SAME | SAME | Same input and same marshal hash. |
| float_huge_1e300 | float_complex | SAME | SAME | Same input and same marshal hash. |
| float_math_nan | float_complex | SAME | SAME | Same input and same marshal hash. |
| float_nan_constructor | float_complex | SAME | SAME | Same input and same marshal hash. |
| float_nan_payload_0x7ff0000000000001 | float_complex | SAME | SAME | Same input and same marshal hash. |
| float_nan_payload_0x7ff8000000000001 | float_complex | SAME | SAME | Same input and same marshal hash. |
| float_nan_payload_0x7ff8000000000002 | float_complex | SAME | SAME | Same input and same marshal hash. |
| float_neg_inf | float_complex | SAME | SAME | Same input and same marshal hash. |
| float_neg_one | float_complex | SAME | SAME | Same input and same marshal hash. |
| float_neg_zero | float_complex | SAME | SAME | Same input and same marshal hash. |
| float_pos_inf | float_complex | SAME | SAME | Same input and same marshal hash. |
| float_pos_one | float_complex | SAME | SAME | Same input and same marshal hash. |
| float_pos_zero | float_complex | SAME | SAME | Same input and same marshal hash. |
| float_tiny_1e_minus_300 | float_complex | SAME | SAME | Same input and same marshal hash. |
| lone_high_surrogate | unicode_string | SAME | SAME | Same input and same marshal hash. |
| non_bmp_character | unicode_string | SAME | SAME | Same input and same marshal hash. |
| nul_inside_string | unicode_string | SAME | SAME | Same input and same marshal hash. |
| recreated_complex_nan_both | float_complex | SAME | SAME | Same input and same marshal hash. |
| recreated_float_nan | float_complex | SAME | SAME | Same input and same marshal hash. |
| slice_1_10_2 | optional_slice_probe | DIFFERENT | SAME | Same optional support boundary or exception behavior. |
| slice_neg10_none_neg1 | optional_slice_probe | DIFFERENT | SAME | Same optional support boundary or exception behavior. |
| slice_none_none_none | optional_slice_probe | DIFFERENT | SAME | Same optional support boundary or exception behavior. |
| zero_width_joiner_sequence | unicode_string | SAME | SAME | Same input and same marshal hash. |

### member_b_all_darwin_arm64_py3_10_results (Darwin/arm64, Python 3.10.11) vs member_b_all_windows_amd64_py3_10_results (Windows/AMD64, Python 3.10.11)

| Case | Category | Same marshal hash | Same exception | Interpretation |
| --- | --- | --- | --- | --- |
| ascii_plain | unicode_string | SAME | SAME | Same input and same marshal hash. |
| bytes_255_a | bytes_payload | SAME | SAME | Same input and same marshal hash. |
| bytes_256_a | bytes_payload | SAME | SAME | Same input and same marshal hash. |
| bytes_65535_a | bytes_payload | SAME | SAME | Same input and same marshal hash. |
| bytes_65536_a | bytes_payload | SAME | SAME | Same input and same marshal hash. |
| bytes_all_byte_values | bytes_payload | SAME | SAME | Same input and same marshal hash. |
| bytes_empty | bytes_payload | SAME | SAME | Same input and same marshal hash. |
| bytes_high_values_with_ascii | bytes_payload | SAME | SAME | Same input and same marshal hash. |
| bytes_single_nul | bytes_payload | SAME | SAME | Same input and same marshal hash. |
| chinese_text | unicode_string | SAME | SAME | Same input and same marshal hash. |
| complex_inf_neg_inf | float_complex | SAME | SAME | Same input and same marshal hash. |
| complex_nan_both | float_complex | SAME | SAME | Same input and same marshal hash. |
| complex_nan_imag | float_complex | SAME | SAME | Same input and same marshal hash. |
| complex_nan_real | float_complex | SAME | SAME | Same input and same marshal hash. |
| complex_payload_nan_imag | float_complex | SAME | SAME | Same input and same marshal hash. |
| complex_payload_nan_real | float_complex | SAME | SAME | Same input and same marshal hash. |
| complex_regular | float_complex | SAME | SAME | Same input and same marshal hash. |
| complex_zero_neg_zero | float_complex | SAME | SAME | Same input and same marshal hash. |
| composed_e_acute | unicode_string | SAME | SAME | Same input and same marshal hash. |
| constant_ellipsis | basic_scalar_constant | SAME | SAME | Same input and same marshal hash. |
| constant_false | basic_scalar_constant | SAME | SAME | Same input and same marshal hash. |
| constant_none | basic_scalar_constant | SAME | SAME | Same input and same marshal hash. |
| constant_true | basic_scalar_constant | SAME | SAME | Same input and same marshal hash. |
| crlf_string | unicode_string | SAME | SAME | Same input and same marshal hash. |
| decomposed_e_acute | unicode_string | SAME | SAME | Same input and same marshal hash. |
| emoji_text | unicode_string | SAME | SAME | Same input and same marshal hash. |
| float_huge_1e300 | float_complex | SAME | SAME | Same input and same marshal hash. |
| float_math_nan | float_complex | SAME | SAME | Same input and same marshal hash. |
| float_nan_constructor | float_complex | SAME | SAME | Same input and same marshal hash. |
| float_nan_payload_0x7ff0000000000001 | float_complex | SAME | SAME | Same input and same marshal hash. |
| float_nan_payload_0x7ff8000000000001 | float_complex | SAME | SAME | Same input and same marshal hash. |
| float_nan_payload_0x7ff8000000000002 | float_complex | SAME | SAME | Same input and same marshal hash. |
| float_neg_inf | float_complex | SAME | SAME | Same input and same marshal hash. |
| float_neg_one | float_complex | SAME | SAME | Same input and same marshal hash. |
| float_neg_zero | float_complex | SAME | SAME | Same input and same marshal hash. |
| float_pos_inf | float_complex | SAME | SAME | Same input and same marshal hash. |
| float_pos_one | float_complex | SAME | SAME | Same input and same marshal hash. |
| float_pos_zero | float_complex | SAME | SAME | Same input and same marshal hash. |
| float_tiny_1e_minus_300 | float_complex | SAME | SAME | Same input and same marshal hash. |
| lone_high_surrogate | unicode_string | SAME | SAME | Same input and same marshal hash. |
| non_bmp_character | unicode_string | SAME | SAME | Same input and same marshal hash. |
| nul_inside_string | unicode_string | SAME | SAME | Same input and same marshal hash. |
| recreated_complex_nan_both | float_complex | SAME | SAME | Same input and same marshal hash. |
| recreated_float_nan | float_complex | SAME | SAME | Same input and same marshal hash. |
| slice_1_10_2 | optional_slice_probe | DIFFERENT | SAME | Same optional support boundary or exception behavior. |
| slice_neg10_none_neg1 | optional_slice_probe | DIFFERENT | SAME | Same optional support boundary or exception behavior. |
| slice_none_none_none | optional_slice_probe | DIFFERENT | SAME | Same optional support boundary or exception behavior. |
| zero_width_joiner_sequence | unicode_string | SAME | SAME | Same input and same marshal hash. |

### member_b_all_darwin_arm64_py3_10_results (Darwin/arm64, Python 3.10.11) vs member_b_all_windows_amd64_py3_11_results (Windows/AMD64, Python 3.11.9)

| Case | Category | Same marshal hash | Same exception | Interpretation |
| --- | --- | --- | --- | --- |
| ascii_plain | unicode_string | SAME | SAME | Same input and same marshal hash. |
| bytes_255_a | bytes_payload | SAME | SAME | Same input and same marshal hash. |
| bytes_256_a | bytes_payload | SAME | SAME | Same input and same marshal hash. |
| bytes_65535_a | bytes_payload | SAME | SAME | Same input and same marshal hash. |
| bytes_65536_a | bytes_payload | SAME | SAME | Same input and same marshal hash. |
| bytes_all_byte_values | bytes_payload | SAME | SAME | Same input and same marshal hash. |
| bytes_empty | bytes_payload | SAME | SAME | Same input and same marshal hash. |
| bytes_high_values_with_ascii | bytes_payload | SAME | SAME | Same input and same marshal hash. |
| bytes_single_nul | bytes_payload | SAME | SAME | Same input and same marshal hash. |
| chinese_text | unicode_string | SAME | SAME | Same input and same marshal hash. |
| complex_inf_neg_inf | float_complex | SAME | SAME | Same input and same marshal hash. |
| complex_nan_both | float_complex | SAME | SAME | Same input and same marshal hash. |
| complex_nan_imag | float_complex | SAME | SAME | Same input and same marshal hash. |
| complex_nan_real | float_complex | SAME | SAME | Same input and same marshal hash. |
| complex_payload_nan_imag | float_complex | SAME | SAME | Same input and same marshal hash. |
| complex_payload_nan_real | float_complex | SAME | SAME | Same input and same marshal hash. |
| complex_regular | float_complex | SAME | SAME | Same input and same marshal hash. |
| complex_zero_neg_zero | float_complex | SAME | SAME | Same input and same marshal hash. |
| composed_e_acute | unicode_string | SAME | SAME | Same input and same marshal hash. |
| constant_ellipsis | basic_scalar_constant | SAME | SAME | Same input and same marshal hash. |
| constant_false | basic_scalar_constant | SAME | SAME | Same input and same marshal hash. |
| constant_none | basic_scalar_constant | SAME | SAME | Same input and same marshal hash. |
| constant_true | basic_scalar_constant | SAME | SAME | Same input and same marshal hash. |
| crlf_string | unicode_string | SAME | SAME | Same input and same marshal hash. |
| decomposed_e_acute | unicode_string | SAME | SAME | Same input and same marshal hash. |
| emoji_text | unicode_string | SAME | SAME | Same input and same marshal hash. |
| float_huge_1e300 | float_complex | SAME | SAME | Same input and same marshal hash. |
| float_math_nan | float_complex | SAME | SAME | Same input and same marshal hash. |
| float_nan_constructor | float_complex | SAME | SAME | Same input and same marshal hash. |
| float_nan_payload_0x7ff0000000000001 | float_complex | SAME | SAME | Same input and same marshal hash. |
| float_nan_payload_0x7ff8000000000001 | float_complex | SAME | SAME | Same input and same marshal hash. |
| float_nan_payload_0x7ff8000000000002 | float_complex | SAME | SAME | Same input and same marshal hash. |
| float_neg_inf | float_complex | SAME | SAME | Same input and same marshal hash. |
| float_neg_one | float_complex | SAME | SAME | Same input and same marshal hash. |
| float_neg_zero | float_complex | SAME | SAME | Same input and same marshal hash. |
| float_pos_inf | float_complex | SAME | SAME | Same input and same marshal hash. |
| float_pos_one | float_complex | SAME | SAME | Same input and same marshal hash. |
| float_pos_zero | float_complex | SAME | SAME | Same input and same marshal hash. |
| float_tiny_1e_minus_300 | float_complex | SAME | SAME | Same input and same marshal hash. |
| lone_high_surrogate | unicode_string | SAME | SAME | Same input and same marshal hash. |
| non_bmp_character | unicode_string | SAME | SAME | Same input and same marshal hash. |
| nul_inside_string | unicode_string | SAME | SAME | Same input and same marshal hash. |
| recreated_complex_nan_both | float_complex | SAME | SAME | Same input and same marshal hash. |
| recreated_float_nan | float_complex | SAME | SAME | Same input and same marshal hash. |
| slice_1_10_2 | optional_slice_probe | DIFFERENT | SAME | Same optional support boundary or exception behavior. |
| slice_neg10_none_neg1 | optional_slice_probe | DIFFERENT | SAME | Same optional support boundary or exception behavior. |
| slice_none_none_none | optional_slice_probe | DIFFERENT | SAME | Same optional support boundary or exception behavior. |
| zero_width_joiner_sequence | unicode_string | SAME | SAME | Same input and same marshal hash. |

### member_b_all_darwin_arm64_py3_10_results (Darwin/arm64, Python 3.10.11) vs member_b_all_windows_amd64_py3_12_results (Windows/AMD64, Python 3.12.10)

| Case | Category | Same marshal hash | Same exception | Interpretation |
| --- | --- | --- | --- | --- |
| ascii_plain | unicode_string | SAME | SAME | Same input and same marshal hash. |
| bytes_255_a | bytes_payload | SAME | SAME | Same input and same marshal hash. |
| bytes_256_a | bytes_payload | SAME | SAME | Same input and same marshal hash. |
| bytes_65535_a | bytes_payload | SAME | SAME | Same input and same marshal hash. |
| bytes_65536_a | bytes_payload | SAME | SAME | Same input and same marshal hash. |
| bytes_all_byte_values | bytes_payload | SAME | SAME | Same input and same marshal hash. |
| bytes_empty | bytes_payload | SAME | SAME | Same input and same marshal hash. |
| bytes_high_values_with_ascii | bytes_payload | SAME | SAME | Same input and same marshal hash. |
| bytes_single_nul | bytes_payload | SAME | SAME | Same input and same marshal hash. |
| chinese_text | unicode_string | SAME | SAME | Same input and same marshal hash. |
| complex_inf_neg_inf | float_complex | SAME | SAME | Same input and same marshal hash. |
| complex_nan_both | float_complex | SAME | SAME | Same input and same marshal hash. |
| complex_nan_imag | float_complex | SAME | SAME | Same input and same marshal hash. |
| complex_nan_real | float_complex | SAME | SAME | Same input and same marshal hash. |
| complex_payload_nan_imag | float_complex | SAME | SAME | Same input and same marshal hash. |
| complex_payload_nan_real | float_complex | SAME | SAME | Same input and same marshal hash. |
| complex_regular | float_complex | SAME | SAME | Same input and same marshal hash. |
| complex_zero_neg_zero | float_complex | SAME | SAME | Same input and same marshal hash. |
| composed_e_acute | unicode_string | DIFFERENT | SAME | Same input representation but Python major/minor differs; likely version-level marshal format difference. |
| constant_ellipsis | basic_scalar_constant | SAME | SAME | Same input and same marshal hash. |
| constant_false | basic_scalar_constant | SAME | SAME | Same input and same marshal hash. |
| constant_none | basic_scalar_constant | SAME | SAME | Same input and same marshal hash. |
| constant_true | basic_scalar_constant | SAME | SAME | Same input and same marshal hash. |
| crlf_string | unicode_string | SAME | SAME | Same input and same marshal hash. |
| decomposed_e_acute | unicode_string | SAME | SAME | Same input and same marshal hash. |
| emoji_text | unicode_string | SAME | SAME | Same input and same marshal hash. |
| float_huge_1e300 | float_complex | SAME | SAME | Same input and same marshal hash. |
| float_math_nan | float_complex | SAME | SAME | Same input and same marshal hash. |
| float_nan_constructor | float_complex | SAME | SAME | Same input and same marshal hash. |
| float_nan_payload_0x7ff0000000000001 | float_complex | SAME | SAME | Same input and same marshal hash. |
| float_nan_payload_0x7ff8000000000001 | float_complex | SAME | SAME | Same input and same marshal hash. |
| float_nan_payload_0x7ff8000000000002 | float_complex | SAME | SAME | Same input and same marshal hash. |
| float_neg_inf | float_complex | SAME | SAME | Same input and same marshal hash. |
| float_neg_one | float_complex | SAME | SAME | Same input and same marshal hash. |
| float_neg_zero | float_complex | SAME | SAME | Same input and same marshal hash. |
| float_pos_inf | float_complex | SAME | SAME | Same input and same marshal hash. |
| float_pos_one | float_complex | SAME | SAME | Same input and same marshal hash. |
| float_pos_zero | float_complex | SAME | SAME | Same input and same marshal hash. |
| float_tiny_1e_minus_300 | float_complex | SAME | SAME | Same input and same marshal hash. |
| lone_high_surrogate | unicode_string | SAME | SAME | Same input and same marshal hash. |
| non_bmp_character | unicode_string | SAME | SAME | Same input and same marshal hash. |
| nul_inside_string | unicode_string | SAME | SAME | Same input and same marshal hash. |
| recreated_complex_nan_both | float_complex | SAME | SAME | Same input and same marshal hash. |
| recreated_float_nan | float_complex | SAME | SAME | Same input and same marshal hash. |
| slice_1_10_2 | optional_slice_probe | DIFFERENT | SAME | Same optional support boundary or exception behavior. |
| slice_neg10_none_neg1 | optional_slice_probe | DIFFERENT | SAME | Same optional support boundary or exception behavior. |
| slice_none_none_none | optional_slice_probe | DIFFERENT | SAME | Same optional support boundary or exception behavior. |
| zero_width_joiner_sequence | unicode_string | SAME | SAME | Same input and same marshal hash. |

### member_b_all_darwin_arm64_py3_10_results (Darwin/arm64, Python 3.10.11) vs member_b_all_windows_amd64_py3_13_results (Windows/AMD64, Python 3.13.13)

| Case | Category | Same marshal hash | Same exception | Interpretation |
| --- | --- | --- | --- | --- |
| ascii_plain | unicode_string | SAME | SAME | Same input and same marshal hash. |
| bytes_255_a | bytes_payload | SAME | SAME | Same input and same marshal hash. |
| bytes_256_a | bytes_payload | SAME | SAME | Same input and same marshal hash. |
| bytes_65535_a | bytes_payload | SAME | SAME | Same input and same marshal hash. |
| bytes_65536_a | bytes_payload | SAME | SAME | Same input and same marshal hash. |
| bytes_all_byte_values | bytes_payload | SAME | SAME | Same input and same marshal hash. |
| bytes_empty | bytes_payload | SAME | SAME | Same input and same marshal hash. |
| bytes_high_values_with_ascii | bytes_payload | SAME | SAME | Same input and same marshal hash. |
| bytes_single_nul | bytes_payload | SAME | SAME | Same input and same marshal hash. |
| chinese_text | unicode_string | SAME | SAME | Same input and same marshal hash. |
| complex_inf_neg_inf | float_complex | SAME | SAME | Same input and same marshal hash. |
| complex_nan_both | float_complex | SAME | SAME | Same input and same marshal hash. |
| complex_nan_imag | float_complex | SAME | SAME | Same input and same marshal hash. |
| complex_nan_real | float_complex | SAME | SAME | Same input and same marshal hash. |
| complex_payload_nan_imag | float_complex | SAME | SAME | Same input and same marshal hash. |
| complex_payload_nan_real | float_complex | SAME | SAME | Same input and same marshal hash. |
| complex_regular | float_complex | SAME | SAME | Same input and same marshal hash. |
| complex_zero_neg_zero | float_complex | SAME | SAME | Same input and same marshal hash. |
| composed_e_acute | unicode_string | DIFFERENT | SAME | Same input representation but Python major/minor differs; likely version-level marshal format difference. |
| constant_ellipsis | basic_scalar_constant | SAME | SAME | Same input and same marshal hash. |
| constant_false | basic_scalar_constant | SAME | SAME | Same input and same marshal hash. |
| constant_none | basic_scalar_constant | SAME | SAME | Same input and same marshal hash. |
| constant_true | basic_scalar_constant | SAME | SAME | Same input and same marshal hash. |
| crlf_string | unicode_string | SAME | SAME | Same input and same marshal hash. |
| decomposed_e_acute | unicode_string | SAME | SAME | Same input and same marshal hash. |
| emoji_text | unicode_string | SAME | SAME | Same input and same marshal hash. |
| float_huge_1e300 | float_complex | SAME | SAME | Same input and same marshal hash. |
| float_math_nan | float_complex | SAME | SAME | Same input and same marshal hash. |
| float_nan_constructor | float_complex | SAME | SAME | Same input and same marshal hash. |
| float_nan_payload_0x7ff0000000000001 | float_complex | SAME | SAME | Same input and same marshal hash. |
| float_nan_payload_0x7ff8000000000001 | float_complex | SAME | SAME | Same input and same marshal hash. |
| float_nan_payload_0x7ff8000000000002 | float_complex | SAME | SAME | Same input and same marshal hash. |
| float_neg_inf | float_complex | SAME | SAME | Same input and same marshal hash. |
| float_neg_one | float_complex | SAME | SAME | Same input and same marshal hash. |
| float_neg_zero | float_complex | SAME | SAME | Same input and same marshal hash. |
| float_pos_inf | float_complex | SAME | SAME | Same input and same marshal hash. |
| float_pos_one | float_complex | SAME | SAME | Same input and same marshal hash. |
| float_pos_zero | float_complex | SAME | SAME | Same input and same marshal hash. |
| float_tiny_1e_minus_300 | float_complex | SAME | SAME | Same input and same marshal hash. |
| lone_high_surrogate | unicode_string | SAME | SAME | Same input and same marshal hash. |
| non_bmp_character | unicode_string | SAME | SAME | Same input and same marshal hash. |
| nul_inside_string | unicode_string | SAME | SAME | Same input and same marshal hash. |
| recreated_complex_nan_both | float_complex | SAME | SAME | Same input and same marshal hash. |
| recreated_float_nan | float_complex | SAME | SAME | Same input and same marshal hash. |
| slice_1_10_2 | optional_slice_probe | DIFFERENT | SAME | Same optional support boundary or exception behavior. |
| slice_neg10_none_neg1 | optional_slice_probe | DIFFERENT | SAME | Same optional support boundary or exception behavior. |
| slice_none_none_none | optional_slice_probe | DIFFERENT | SAME | Same optional support boundary or exception behavior. |
| zero_width_joiner_sequence | unicode_string | SAME | SAME | Same input and same marshal hash. |

### member_b_all_darwin_arm64_py3_10_results (Darwin/arm64, Python 3.10.11) vs member_b_all_windows_amd64_py3_9_results (Windows/AMD64, Python 3.9.13)

| Case | Category | Same marshal hash | Same exception | Interpretation |
| --- | --- | --- | --- | --- |
| ascii_plain | unicode_string | SAME | SAME | Same input and same marshal hash. |
| bytes_255_a | bytes_payload | SAME | SAME | Same input and same marshal hash. |
| bytes_256_a | bytes_payload | SAME | SAME | Same input and same marshal hash. |
| bytes_65535_a | bytes_payload | SAME | SAME | Same input and same marshal hash. |
| bytes_65536_a | bytes_payload | SAME | SAME | Same input and same marshal hash. |
| bytes_all_byte_values | bytes_payload | SAME | SAME | Same input and same marshal hash. |
| bytes_empty | bytes_payload | SAME | SAME | Same input and same marshal hash. |
| bytes_high_values_with_ascii | bytes_payload | SAME | SAME | Same input and same marshal hash. |
| bytes_single_nul | bytes_payload | SAME | SAME | Same input and same marshal hash. |
| chinese_text | unicode_string | SAME | SAME | Same input and same marshal hash. |
| complex_inf_neg_inf | float_complex | SAME | SAME | Same input and same marshal hash. |
| complex_nan_both | float_complex | SAME | SAME | Same input and same marshal hash. |
| complex_nan_imag | float_complex | SAME | SAME | Same input and same marshal hash. |
| complex_nan_real | float_complex | SAME | SAME | Same input and same marshal hash. |
| complex_payload_nan_imag | float_complex | SAME | SAME | Same input and same marshal hash. |
| complex_payload_nan_real | float_complex | SAME | SAME | Same input and same marshal hash. |
| complex_regular | float_complex | SAME | SAME | Same input and same marshal hash. |
| complex_zero_neg_zero | float_complex | SAME | SAME | Same input and same marshal hash. |
| composed_e_acute | unicode_string | SAME | SAME | Same input and same marshal hash. |
| constant_ellipsis | basic_scalar_constant | SAME | SAME | Same input and same marshal hash. |
| constant_false | basic_scalar_constant | SAME | SAME | Same input and same marshal hash. |
| constant_none | basic_scalar_constant | SAME | SAME | Same input and same marshal hash. |
| constant_true | basic_scalar_constant | SAME | SAME | Same input and same marshal hash. |
| crlf_string | unicode_string | SAME | SAME | Same input and same marshal hash. |
| decomposed_e_acute | unicode_string | SAME | SAME | Same input and same marshal hash. |
| emoji_text | unicode_string | SAME | SAME | Same input and same marshal hash. |
| float_huge_1e300 | float_complex | SAME | SAME | Same input and same marshal hash. |
| float_math_nan | float_complex | SAME | SAME | Same input and same marshal hash. |
| float_nan_constructor | float_complex | SAME | SAME | Same input and same marshal hash. |
| float_nan_payload_0x7ff0000000000001 | float_complex | SAME | SAME | Same input and same marshal hash. |
| float_nan_payload_0x7ff8000000000001 | float_complex | SAME | SAME | Same input and same marshal hash. |
| float_nan_payload_0x7ff8000000000002 | float_complex | SAME | SAME | Same input and same marshal hash. |
| float_neg_inf | float_complex | SAME | SAME | Same input and same marshal hash. |
| float_neg_one | float_complex | SAME | SAME | Same input and same marshal hash. |
| float_neg_zero | float_complex | SAME | SAME | Same input and same marshal hash. |
| float_pos_inf | float_complex | SAME | SAME | Same input and same marshal hash. |
| float_pos_one | float_complex | SAME | SAME | Same input and same marshal hash. |
| float_pos_zero | float_complex | SAME | SAME | Same input and same marshal hash. |
| float_tiny_1e_minus_300 | float_complex | SAME | SAME | Same input and same marshal hash. |
| lone_high_surrogate | unicode_string | SAME | SAME | Same input and same marshal hash. |
| non_bmp_character | unicode_string | SAME | SAME | Same input and same marshal hash. |
| nul_inside_string | unicode_string | SAME | SAME | Same input and same marshal hash. |
| recreated_complex_nan_both | float_complex | SAME | SAME | Same input and same marshal hash. |
| recreated_float_nan | float_complex | SAME | SAME | Same input and same marshal hash. |
| slice_1_10_2 | optional_slice_probe | DIFFERENT | SAME | Same optional support boundary or exception behavior. |
| slice_neg10_none_neg1 | optional_slice_probe | DIFFERENT | SAME | Same optional support boundary or exception behavior. |
| slice_none_none_none | optional_slice_probe | DIFFERENT | SAME | Same optional support boundary or exception behavior. |
| zero_width_joiner_sequence | unicode_string | SAME | SAME | Same input and same marshal hash. |

### member_b_all_darwin_arm64_py3_11_results (Darwin/arm64, Python 3.11.9) vs member_b_all_darwin_arm64_py3_12_results (Darwin/arm64, Python 3.12.10)

| Case | Category | Same marshal hash | Same exception | Interpretation |
| --- | --- | --- | --- | --- |
| ascii_plain | unicode_string | SAME | SAME | Same input and same marshal hash. |
| bytes_255_a | bytes_payload | SAME | SAME | Same input and same marshal hash. |
| bytes_256_a | bytes_payload | SAME | SAME | Same input and same marshal hash. |
| bytes_65535_a | bytes_payload | SAME | SAME | Same input and same marshal hash. |
| bytes_65536_a | bytes_payload | SAME | SAME | Same input and same marshal hash. |
| bytes_all_byte_values | bytes_payload | SAME | SAME | Same input and same marshal hash. |
| bytes_empty | bytes_payload | SAME | SAME | Same input and same marshal hash. |
| bytes_high_values_with_ascii | bytes_payload | SAME | SAME | Same input and same marshal hash. |
| bytes_single_nul | bytes_payload | SAME | SAME | Same input and same marshal hash. |
| chinese_text | unicode_string | SAME | SAME | Same input and same marshal hash. |
| complex_inf_neg_inf | float_complex | SAME | SAME | Same input and same marshal hash. |
| complex_nan_both | float_complex | SAME | SAME | Same input and same marshal hash. |
| complex_nan_imag | float_complex | SAME | SAME | Same input and same marshal hash. |
| complex_nan_real | float_complex | SAME | SAME | Same input and same marshal hash. |
| complex_payload_nan_imag | float_complex | SAME | SAME | Same input and same marshal hash. |
| complex_payload_nan_real | float_complex | SAME | SAME | Same input and same marshal hash. |
| complex_regular | float_complex | SAME | SAME | Same input and same marshal hash. |
| complex_zero_neg_zero | float_complex | SAME | SAME | Same input and same marshal hash. |
| composed_e_acute | unicode_string | DIFFERENT | SAME | Same input representation but Python major/minor differs; likely version-level marshal format difference. |
| constant_ellipsis | basic_scalar_constant | SAME | SAME | Same input and same marshal hash. |
| constant_false | basic_scalar_constant | SAME | SAME | Same input and same marshal hash. |
| constant_none | basic_scalar_constant | SAME | SAME | Same input and same marshal hash. |
| constant_true | basic_scalar_constant | SAME | SAME | Same input and same marshal hash. |
| crlf_string | unicode_string | SAME | SAME | Same input and same marshal hash. |
| decomposed_e_acute | unicode_string | SAME | SAME | Same input and same marshal hash. |
| emoji_text | unicode_string | SAME | SAME | Same input and same marshal hash. |
| float_huge_1e300 | float_complex | SAME | SAME | Same input and same marshal hash. |
| float_math_nan | float_complex | SAME | SAME | Same input and same marshal hash. |
| float_nan_constructor | float_complex | SAME | SAME | Same input and same marshal hash. |
| float_nan_payload_0x7ff0000000000001 | float_complex | SAME | SAME | Same input and same marshal hash. |
| float_nan_payload_0x7ff8000000000001 | float_complex | SAME | SAME | Same input and same marshal hash. |
| float_nan_payload_0x7ff8000000000002 | float_complex | SAME | SAME | Same input and same marshal hash. |
| float_neg_inf | float_complex | SAME | SAME | Same input and same marshal hash. |
| float_neg_one | float_complex | SAME | SAME | Same input and same marshal hash. |
| float_neg_zero | float_complex | SAME | SAME | Same input and same marshal hash. |
| float_pos_inf | float_complex | SAME | SAME | Same input and same marshal hash. |
| float_pos_one | float_complex | SAME | SAME | Same input and same marshal hash. |
| float_pos_zero | float_complex | SAME | SAME | Same input and same marshal hash. |
| float_tiny_1e_minus_300 | float_complex | SAME | SAME | Same input and same marshal hash. |
| lone_high_surrogate | unicode_string | SAME | SAME | Same input and same marshal hash. |
| non_bmp_character | unicode_string | SAME | SAME | Same input and same marshal hash. |
| nul_inside_string | unicode_string | SAME | SAME | Same input and same marshal hash. |
| recreated_complex_nan_both | float_complex | SAME | SAME | Same input and same marshal hash. |
| recreated_float_nan | float_complex | SAME | SAME | Same input and same marshal hash. |
| slice_1_10_2 | optional_slice_probe | DIFFERENT | SAME | Same optional support boundary or exception behavior. |
| slice_neg10_none_neg1 | optional_slice_probe | DIFFERENT | SAME | Same optional support boundary or exception behavior. |
| slice_none_none_none | optional_slice_probe | DIFFERENT | SAME | Same optional support boundary or exception behavior. |
| zero_width_joiner_sequence | unicode_string | SAME | SAME | Same input and same marshal hash. |

### member_b_all_darwin_arm64_py3_11_results (Darwin/arm64, Python 3.11.9) vs member_b_all_darwin_arm64_py3_13_results (Darwin/arm64, Python 3.13.13)

| Case | Category | Same marshal hash | Same exception | Interpretation |
| --- | --- | --- | --- | --- |
| ascii_plain | unicode_string | SAME | SAME | Same input and same marshal hash. |
| bytes_255_a | bytes_payload | SAME | SAME | Same input and same marshal hash. |
| bytes_256_a | bytes_payload | SAME | SAME | Same input and same marshal hash. |
| bytes_65535_a | bytes_payload | SAME | SAME | Same input and same marshal hash. |
| bytes_65536_a | bytes_payload | SAME | SAME | Same input and same marshal hash. |
| bytes_all_byte_values | bytes_payload | SAME | SAME | Same input and same marshal hash. |
| bytes_empty | bytes_payload | SAME | SAME | Same input and same marshal hash. |
| bytes_high_values_with_ascii | bytes_payload | SAME | SAME | Same input and same marshal hash. |
| bytes_single_nul | bytes_payload | SAME | SAME | Same input and same marshal hash. |
| chinese_text | unicode_string | SAME | SAME | Same input and same marshal hash. |
| complex_inf_neg_inf | float_complex | SAME | SAME | Same input and same marshal hash. |
| complex_nan_both | float_complex | SAME | SAME | Same input and same marshal hash. |
| complex_nan_imag | float_complex | SAME | SAME | Same input and same marshal hash. |
| complex_nan_real | float_complex | SAME | SAME | Same input and same marshal hash. |
| complex_payload_nan_imag | float_complex | SAME | SAME | Same input and same marshal hash. |
| complex_payload_nan_real | float_complex | SAME | SAME | Same input and same marshal hash. |
| complex_regular | float_complex | SAME | SAME | Same input and same marshal hash. |
| complex_zero_neg_zero | float_complex | SAME | SAME | Same input and same marshal hash. |
| composed_e_acute | unicode_string | DIFFERENT | SAME | Same input representation but Python major/minor differs; likely version-level marshal format difference. |
| constant_ellipsis | basic_scalar_constant | SAME | SAME | Same input and same marshal hash. |
| constant_false | basic_scalar_constant | SAME | SAME | Same input and same marshal hash. |
| constant_none | basic_scalar_constant | SAME | SAME | Same input and same marshal hash. |
| constant_true | basic_scalar_constant | SAME | SAME | Same input and same marshal hash. |
| crlf_string | unicode_string | SAME | SAME | Same input and same marshal hash. |
| decomposed_e_acute | unicode_string | SAME | SAME | Same input and same marshal hash. |
| emoji_text | unicode_string | SAME | SAME | Same input and same marshal hash. |
| float_huge_1e300 | float_complex | SAME | SAME | Same input and same marshal hash. |
| float_math_nan | float_complex | SAME | SAME | Same input and same marshal hash. |
| float_nan_constructor | float_complex | SAME | SAME | Same input and same marshal hash. |
| float_nan_payload_0x7ff0000000000001 | float_complex | SAME | SAME | Same input and same marshal hash. |
| float_nan_payload_0x7ff8000000000001 | float_complex | SAME | SAME | Same input and same marshal hash. |
| float_nan_payload_0x7ff8000000000002 | float_complex | SAME | SAME | Same input and same marshal hash. |
| float_neg_inf | float_complex | SAME | SAME | Same input and same marshal hash. |
| float_neg_one | float_complex | SAME | SAME | Same input and same marshal hash. |
| float_neg_zero | float_complex | SAME | SAME | Same input and same marshal hash. |
| float_pos_inf | float_complex | SAME | SAME | Same input and same marshal hash. |
| float_pos_one | float_complex | SAME | SAME | Same input and same marshal hash. |
| float_pos_zero | float_complex | SAME | SAME | Same input and same marshal hash. |
| float_tiny_1e_minus_300 | float_complex | SAME | SAME | Same input and same marshal hash. |
| lone_high_surrogate | unicode_string | SAME | SAME | Same input and same marshal hash. |
| non_bmp_character | unicode_string | SAME | SAME | Same input and same marshal hash. |
| nul_inside_string | unicode_string | SAME | SAME | Same input and same marshal hash. |
| recreated_complex_nan_both | float_complex | SAME | SAME | Same input and same marshal hash. |
| recreated_float_nan | float_complex | SAME | SAME | Same input and same marshal hash. |
| slice_1_10_2 | optional_slice_probe | DIFFERENT | SAME | Same optional support boundary or exception behavior. |
| slice_neg10_none_neg1 | optional_slice_probe | DIFFERENT | SAME | Same optional support boundary or exception behavior. |
| slice_none_none_none | optional_slice_probe | DIFFERENT | SAME | Same optional support boundary or exception behavior. |
| zero_width_joiner_sequence | unicode_string | SAME | SAME | Same input and same marshal hash. |

### member_b_all_darwin_arm64_py3_11_results (Darwin/arm64, Python 3.11.9) vs member_b_all_darwin_arm64_py3_9_results (Darwin/arm64, Python 3.9.6)

| Case | Category | Same marshal hash | Same exception | Interpretation |
| --- | --- | --- | --- | --- |
| ascii_plain | unicode_string | SAME | SAME | Same input and same marshal hash. |
| bytes_255_a | bytes_payload | SAME | SAME | Same input and same marshal hash. |
| bytes_256_a | bytes_payload | SAME | SAME | Same input and same marshal hash. |
| bytes_65535_a | bytes_payload | SAME | SAME | Same input and same marshal hash. |
| bytes_65536_a | bytes_payload | SAME | SAME | Same input and same marshal hash. |
| bytes_all_byte_values | bytes_payload | SAME | SAME | Same input and same marshal hash. |
| bytes_empty | bytes_payload | SAME | SAME | Same input and same marshal hash. |
| bytes_high_values_with_ascii | bytes_payload | SAME | SAME | Same input and same marshal hash. |
| bytes_single_nul | bytes_payload | SAME | SAME | Same input and same marshal hash. |
| chinese_text | unicode_string | SAME | SAME | Same input and same marshal hash. |
| complex_inf_neg_inf | float_complex | SAME | SAME | Same input and same marshal hash. |
| complex_nan_both | float_complex | SAME | SAME | Same input and same marshal hash. |
| complex_nan_imag | float_complex | SAME | SAME | Same input and same marshal hash. |
| complex_nan_real | float_complex | SAME | SAME | Same input and same marshal hash. |
| complex_payload_nan_imag | float_complex | SAME | SAME | Same input and same marshal hash. |
| complex_payload_nan_real | float_complex | SAME | SAME | Same input and same marshal hash. |
| complex_regular | float_complex | SAME | SAME | Same input and same marshal hash. |
| complex_zero_neg_zero | float_complex | SAME | SAME | Same input and same marshal hash. |
| composed_e_acute | unicode_string | SAME | SAME | Same input and same marshal hash. |
| constant_ellipsis | basic_scalar_constant | SAME | SAME | Same input and same marshal hash. |
| constant_false | basic_scalar_constant | SAME | SAME | Same input and same marshal hash. |
| constant_none | basic_scalar_constant | SAME | SAME | Same input and same marshal hash. |
| constant_true | basic_scalar_constant | SAME | SAME | Same input and same marshal hash. |
| crlf_string | unicode_string | SAME | SAME | Same input and same marshal hash. |
| decomposed_e_acute | unicode_string | SAME | SAME | Same input and same marshal hash. |
| emoji_text | unicode_string | SAME | SAME | Same input and same marshal hash. |
| float_huge_1e300 | float_complex | SAME | SAME | Same input and same marshal hash. |
| float_math_nan | float_complex | SAME | SAME | Same input and same marshal hash. |
| float_nan_constructor | float_complex | SAME | SAME | Same input and same marshal hash. |
| float_nan_payload_0x7ff0000000000001 | float_complex | SAME | SAME | Same input and same marshal hash. |
| float_nan_payload_0x7ff8000000000001 | float_complex | SAME | SAME | Same input and same marshal hash. |
| float_nan_payload_0x7ff8000000000002 | float_complex | SAME | SAME | Same input and same marshal hash. |
| float_neg_inf | float_complex | SAME | SAME | Same input and same marshal hash. |
| float_neg_one | float_complex | SAME | SAME | Same input and same marshal hash. |
| float_neg_zero | float_complex | SAME | SAME | Same input and same marshal hash. |
| float_pos_inf | float_complex | SAME | SAME | Same input and same marshal hash. |
| float_pos_one | float_complex | SAME | SAME | Same input and same marshal hash. |
| float_pos_zero | float_complex | SAME | SAME | Same input and same marshal hash. |
| float_tiny_1e_minus_300 | float_complex | SAME | SAME | Same input and same marshal hash. |
| lone_high_surrogate | unicode_string | SAME | SAME | Same input and same marshal hash. |
| non_bmp_character | unicode_string | SAME | SAME | Same input and same marshal hash. |
| nul_inside_string | unicode_string | SAME | SAME | Same input and same marshal hash. |
| recreated_complex_nan_both | float_complex | SAME | SAME | Same input and same marshal hash. |
| recreated_float_nan | float_complex | SAME | SAME | Same input and same marshal hash. |
| slice_1_10_2 | optional_slice_probe | DIFFERENT | SAME | Same optional support boundary or exception behavior. |
| slice_neg10_none_neg1 | optional_slice_probe | DIFFERENT | SAME | Same optional support boundary or exception behavior. |
| slice_none_none_none | optional_slice_probe | DIFFERENT | SAME | Same optional support boundary or exception behavior. |
| zero_width_joiner_sequence | unicode_string | SAME | SAME | Same input and same marshal hash. |

### member_b_all_darwin_arm64_py3_11_results (Darwin/arm64, Python 3.11.9) vs member_b_all_linux_x86_64_py3_10_results (Linux/x86_64, Python 3.10.20)

| Case | Category | Same marshal hash | Same exception | Interpretation |
| --- | --- | --- | --- | --- |
| ascii_plain | unicode_string | SAME | SAME | Same input and same marshal hash. |
| bytes_255_a | bytes_payload | SAME | SAME | Same input and same marshal hash. |
| bytes_256_a | bytes_payload | SAME | SAME | Same input and same marshal hash. |
| bytes_65535_a | bytes_payload | SAME | SAME | Same input and same marshal hash. |
| bytes_65536_a | bytes_payload | SAME | SAME | Same input and same marshal hash. |
| bytes_all_byte_values | bytes_payload | SAME | SAME | Same input and same marshal hash. |
| bytes_empty | bytes_payload | SAME | SAME | Same input and same marshal hash. |
| bytes_high_values_with_ascii | bytes_payload | SAME | SAME | Same input and same marshal hash. |
| bytes_single_nul | bytes_payload | SAME | SAME | Same input and same marshal hash. |
| chinese_text | unicode_string | SAME | SAME | Same input and same marshal hash. |
| complex_inf_neg_inf | float_complex | SAME | SAME | Same input and same marshal hash. |
| complex_nan_both | float_complex | SAME | SAME | Same input and same marshal hash. |
| complex_nan_imag | float_complex | SAME | SAME | Same input and same marshal hash. |
| complex_nan_real | float_complex | SAME | SAME | Same input and same marshal hash. |
| complex_payload_nan_imag | float_complex | SAME | SAME | Same input and same marshal hash. |
| complex_payload_nan_real | float_complex | SAME | SAME | Same input and same marshal hash. |
| complex_regular | float_complex | SAME | SAME | Same input and same marshal hash. |
| complex_zero_neg_zero | float_complex | SAME | SAME | Same input and same marshal hash. |
| composed_e_acute | unicode_string | SAME | SAME | Same input and same marshal hash. |
| constant_ellipsis | basic_scalar_constant | SAME | SAME | Same input and same marshal hash. |
| constant_false | basic_scalar_constant | SAME | SAME | Same input and same marshal hash. |
| constant_none | basic_scalar_constant | SAME | SAME | Same input and same marshal hash. |
| constant_true | basic_scalar_constant | SAME | SAME | Same input and same marshal hash. |
| crlf_string | unicode_string | SAME | SAME | Same input and same marshal hash. |
| decomposed_e_acute | unicode_string | SAME | SAME | Same input and same marshal hash. |
| emoji_text | unicode_string | SAME | SAME | Same input and same marshal hash. |
| float_huge_1e300 | float_complex | SAME | SAME | Same input and same marshal hash. |
| float_math_nan | float_complex | SAME | SAME | Same input and same marshal hash. |
| float_nan_constructor | float_complex | SAME | SAME | Same input and same marshal hash. |
| float_nan_payload_0x7ff0000000000001 | float_complex | SAME | SAME | Same input and same marshal hash. |
| float_nan_payload_0x7ff8000000000001 | float_complex | SAME | SAME | Same input and same marshal hash. |
| float_nan_payload_0x7ff8000000000002 | float_complex | SAME | SAME | Same input and same marshal hash. |
| float_neg_inf | float_complex | SAME | SAME | Same input and same marshal hash. |
| float_neg_one | float_complex | SAME | SAME | Same input and same marshal hash. |
| float_neg_zero | float_complex | SAME | SAME | Same input and same marshal hash. |
| float_pos_inf | float_complex | SAME | SAME | Same input and same marshal hash. |
| float_pos_one | float_complex | SAME | SAME | Same input and same marshal hash. |
| float_pos_zero | float_complex | SAME | SAME | Same input and same marshal hash. |
| float_tiny_1e_minus_300 | float_complex | SAME | SAME | Same input and same marshal hash. |
| lone_high_surrogate | unicode_string | SAME | SAME | Same input and same marshal hash. |
| non_bmp_character | unicode_string | SAME | SAME | Same input and same marshal hash. |
| nul_inside_string | unicode_string | SAME | SAME | Same input and same marshal hash. |
| recreated_complex_nan_both | float_complex | SAME | SAME | Same input and same marshal hash. |
| recreated_float_nan | float_complex | SAME | SAME | Same input and same marshal hash. |
| slice_1_10_2 | optional_slice_probe | DIFFERENT | SAME | Same optional support boundary or exception behavior. |
| slice_neg10_none_neg1 | optional_slice_probe | DIFFERENT | SAME | Same optional support boundary or exception behavior. |
| slice_none_none_none | optional_slice_probe | DIFFERENT | SAME | Same optional support boundary or exception behavior. |
| zero_width_joiner_sequence | unicode_string | SAME | SAME | Same input and same marshal hash. |

### member_b_all_darwin_arm64_py3_11_results (Darwin/arm64, Python 3.11.9) vs member_b_all_linux_x86_64_py3_11_results (Linux/x86_64, Python 3.11.15)

| Case | Category | Same marshal hash | Same exception | Interpretation |
| --- | --- | --- | --- | --- |
| ascii_plain | unicode_string | SAME | SAME | Same input and same marshal hash. |
| bytes_255_a | bytes_payload | SAME | SAME | Same input and same marshal hash. |
| bytes_256_a | bytes_payload | SAME | SAME | Same input and same marshal hash. |
| bytes_65535_a | bytes_payload | SAME | SAME | Same input and same marshal hash. |
| bytes_65536_a | bytes_payload | SAME | SAME | Same input and same marshal hash. |
| bytes_all_byte_values | bytes_payload | SAME | SAME | Same input and same marshal hash. |
| bytes_empty | bytes_payload | SAME | SAME | Same input and same marshal hash. |
| bytes_high_values_with_ascii | bytes_payload | SAME | SAME | Same input and same marshal hash. |
| bytes_single_nul | bytes_payload | SAME | SAME | Same input and same marshal hash. |
| chinese_text | unicode_string | SAME | SAME | Same input and same marshal hash. |
| complex_inf_neg_inf | float_complex | SAME | SAME | Same input and same marshal hash. |
| complex_nan_both | float_complex | SAME | SAME | Same input and same marshal hash. |
| complex_nan_imag | float_complex | SAME | SAME | Same input and same marshal hash. |
| complex_nan_real | float_complex | SAME | SAME | Same input and same marshal hash. |
| complex_payload_nan_imag | float_complex | SAME | SAME | Same input and same marshal hash. |
| complex_payload_nan_real | float_complex | SAME | SAME | Same input and same marshal hash. |
| complex_regular | float_complex | SAME | SAME | Same input and same marshal hash. |
| complex_zero_neg_zero | float_complex | SAME | SAME | Same input and same marshal hash. |
| composed_e_acute | unicode_string | SAME | SAME | Same input and same marshal hash. |
| constant_ellipsis | basic_scalar_constant | SAME | SAME | Same input and same marshal hash. |
| constant_false | basic_scalar_constant | SAME | SAME | Same input and same marshal hash. |
| constant_none | basic_scalar_constant | SAME | SAME | Same input and same marshal hash. |
| constant_true | basic_scalar_constant | SAME | SAME | Same input and same marshal hash. |
| crlf_string | unicode_string | SAME | SAME | Same input and same marshal hash. |
| decomposed_e_acute | unicode_string | SAME | SAME | Same input and same marshal hash. |
| emoji_text | unicode_string | SAME | SAME | Same input and same marshal hash. |
| float_huge_1e300 | float_complex | SAME | SAME | Same input and same marshal hash. |
| float_math_nan | float_complex | SAME | SAME | Same input and same marshal hash. |
| float_nan_constructor | float_complex | SAME | SAME | Same input and same marshal hash. |
| float_nan_payload_0x7ff0000000000001 | float_complex | SAME | SAME | Same input and same marshal hash. |
| float_nan_payload_0x7ff8000000000001 | float_complex | SAME | SAME | Same input and same marshal hash. |
| float_nan_payload_0x7ff8000000000002 | float_complex | SAME | SAME | Same input and same marshal hash. |
| float_neg_inf | float_complex | SAME | SAME | Same input and same marshal hash. |
| float_neg_one | float_complex | SAME | SAME | Same input and same marshal hash. |
| float_neg_zero | float_complex | SAME | SAME | Same input and same marshal hash. |
| float_pos_inf | float_complex | SAME | SAME | Same input and same marshal hash. |
| float_pos_one | float_complex | SAME | SAME | Same input and same marshal hash. |
| float_pos_zero | float_complex | SAME | SAME | Same input and same marshal hash. |
| float_tiny_1e_minus_300 | float_complex | SAME | SAME | Same input and same marshal hash. |
| lone_high_surrogate | unicode_string | SAME | SAME | Same input and same marshal hash. |
| non_bmp_character | unicode_string | SAME | SAME | Same input and same marshal hash. |
| nul_inside_string | unicode_string | SAME | SAME | Same input and same marshal hash. |
| recreated_complex_nan_both | float_complex | SAME | SAME | Same input and same marshal hash. |
| recreated_float_nan | float_complex | SAME | SAME | Same input and same marshal hash. |
| slice_1_10_2 | optional_slice_probe | DIFFERENT | SAME | Same optional support boundary or exception behavior. |
| slice_neg10_none_neg1 | optional_slice_probe | DIFFERENT | SAME | Same optional support boundary or exception behavior. |
| slice_none_none_none | optional_slice_probe | DIFFERENT | SAME | Same optional support boundary or exception behavior. |
| zero_width_joiner_sequence | unicode_string | SAME | SAME | Same input and same marshal hash. |

### member_b_all_darwin_arm64_py3_11_results (Darwin/arm64, Python 3.11.9) vs member_b_all_linux_x86_64_py3_12_results (Linux/x86_64, Python 3.12.13)

| Case | Category | Same marshal hash | Same exception | Interpretation |
| --- | --- | --- | --- | --- |
| ascii_plain | unicode_string | SAME | SAME | Same input and same marshal hash. |
| bytes_255_a | bytes_payload | SAME | SAME | Same input and same marshal hash. |
| bytes_256_a | bytes_payload | SAME | SAME | Same input and same marshal hash. |
| bytes_65535_a | bytes_payload | SAME | SAME | Same input and same marshal hash. |
| bytes_65536_a | bytes_payload | SAME | SAME | Same input and same marshal hash. |
| bytes_all_byte_values | bytes_payload | SAME | SAME | Same input and same marshal hash. |
| bytes_empty | bytes_payload | SAME | SAME | Same input and same marshal hash. |
| bytes_high_values_with_ascii | bytes_payload | SAME | SAME | Same input and same marshal hash. |
| bytes_single_nul | bytes_payload | SAME | SAME | Same input and same marshal hash. |
| chinese_text | unicode_string | SAME | SAME | Same input and same marshal hash. |
| complex_inf_neg_inf | float_complex | SAME | SAME | Same input and same marshal hash. |
| complex_nan_both | float_complex | SAME | SAME | Same input and same marshal hash. |
| complex_nan_imag | float_complex | SAME | SAME | Same input and same marshal hash. |
| complex_nan_real | float_complex | SAME | SAME | Same input and same marshal hash. |
| complex_payload_nan_imag | float_complex | SAME | SAME | Same input and same marshal hash. |
| complex_payload_nan_real | float_complex | SAME | SAME | Same input and same marshal hash. |
| complex_regular | float_complex | SAME | SAME | Same input and same marshal hash. |
| complex_zero_neg_zero | float_complex | SAME | SAME | Same input and same marshal hash. |
| composed_e_acute | unicode_string | DIFFERENT | SAME | Same input representation but Python major/minor differs; likely version-level marshal format difference. |
| constant_ellipsis | basic_scalar_constant | SAME | SAME | Same input and same marshal hash. |
| constant_false | basic_scalar_constant | SAME | SAME | Same input and same marshal hash. |
| constant_none | basic_scalar_constant | SAME | SAME | Same input and same marshal hash. |
| constant_true | basic_scalar_constant | SAME | SAME | Same input and same marshal hash. |
| crlf_string | unicode_string | SAME | SAME | Same input and same marshal hash. |
| decomposed_e_acute | unicode_string | SAME | SAME | Same input and same marshal hash. |
| emoji_text | unicode_string | SAME | SAME | Same input and same marshal hash. |
| float_huge_1e300 | float_complex | SAME | SAME | Same input and same marshal hash. |
| float_math_nan | float_complex | SAME | SAME | Same input and same marshal hash. |
| float_nan_constructor | float_complex | SAME | SAME | Same input and same marshal hash. |
| float_nan_payload_0x7ff0000000000001 | float_complex | SAME | SAME | Same input and same marshal hash. |
| float_nan_payload_0x7ff8000000000001 | float_complex | SAME | SAME | Same input and same marshal hash. |
| float_nan_payload_0x7ff8000000000002 | float_complex | SAME | SAME | Same input and same marshal hash. |
| float_neg_inf | float_complex | SAME | SAME | Same input and same marshal hash. |
| float_neg_one | float_complex | SAME | SAME | Same input and same marshal hash. |
| float_neg_zero | float_complex | SAME | SAME | Same input and same marshal hash. |
| float_pos_inf | float_complex | SAME | SAME | Same input and same marshal hash. |
| float_pos_one | float_complex | SAME | SAME | Same input and same marshal hash. |
| float_pos_zero | float_complex | SAME | SAME | Same input and same marshal hash. |
| float_tiny_1e_minus_300 | float_complex | SAME | SAME | Same input and same marshal hash. |
| lone_high_surrogate | unicode_string | SAME | SAME | Same input and same marshal hash. |
| non_bmp_character | unicode_string | SAME | SAME | Same input and same marshal hash. |
| nul_inside_string | unicode_string | SAME | SAME | Same input and same marshal hash. |
| recreated_complex_nan_both | float_complex | SAME | SAME | Same input and same marshal hash. |
| recreated_float_nan | float_complex | SAME | SAME | Same input and same marshal hash. |
| slice_1_10_2 | optional_slice_probe | DIFFERENT | SAME | Same optional support boundary or exception behavior. |
| slice_neg10_none_neg1 | optional_slice_probe | DIFFERENT | SAME | Same optional support boundary or exception behavior. |
| slice_none_none_none | optional_slice_probe | DIFFERENT | SAME | Same optional support boundary or exception behavior. |
| zero_width_joiner_sequence | unicode_string | SAME | SAME | Same input and same marshal hash. |

### member_b_all_darwin_arm64_py3_11_results (Darwin/arm64, Python 3.11.9) vs member_b_all_linux_x86_64_py3_13_results (Linux/x86_64, Python 3.13.13)

| Case | Category | Same marshal hash | Same exception | Interpretation |
| --- | --- | --- | --- | --- |
| ascii_plain | unicode_string | SAME | SAME | Same input and same marshal hash. |
| bytes_255_a | bytes_payload | SAME | SAME | Same input and same marshal hash. |
| bytes_256_a | bytes_payload | SAME | SAME | Same input and same marshal hash. |
| bytes_65535_a | bytes_payload | SAME | SAME | Same input and same marshal hash. |
| bytes_65536_a | bytes_payload | SAME | SAME | Same input and same marshal hash. |
| bytes_all_byte_values | bytes_payload | SAME | SAME | Same input and same marshal hash. |
| bytes_empty | bytes_payload | SAME | SAME | Same input and same marshal hash. |
| bytes_high_values_with_ascii | bytes_payload | SAME | SAME | Same input and same marshal hash. |
| bytes_single_nul | bytes_payload | SAME | SAME | Same input and same marshal hash. |
| chinese_text | unicode_string | SAME | SAME | Same input and same marshal hash. |
| complex_inf_neg_inf | float_complex | SAME | SAME | Same input and same marshal hash. |
| complex_nan_both | float_complex | SAME | SAME | Same input and same marshal hash. |
| complex_nan_imag | float_complex | SAME | SAME | Same input and same marshal hash. |
| complex_nan_real | float_complex | SAME | SAME | Same input and same marshal hash. |
| complex_payload_nan_imag | float_complex | SAME | SAME | Same input and same marshal hash. |
| complex_payload_nan_real | float_complex | SAME | SAME | Same input and same marshal hash. |
| complex_regular | float_complex | SAME | SAME | Same input and same marshal hash. |
| complex_zero_neg_zero | float_complex | SAME | SAME | Same input and same marshal hash. |
| composed_e_acute | unicode_string | DIFFERENT | SAME | Same input representation but Python major/minor differs; likely version-level marshal format difference. |
| constant_ellipsis | basic_scalar_constant | SAME | SAME | Same input and same marshal hash. |
| constant_false | basic_scalar_constant | SAME | SAME | Same input and same marshal hash. |
| constant_none | basic_scalar_constant | SAME | SAME | Same input and same marshal hash. |
| constant_true | basic_scalar_constant | SAME | SAME | Same input and same marshal hash. |
| crlf_string | unicode_string | SAME | SAME | Same input and same marshal hash. |
| decomposed_e_acute | unicode_string | SAME | SAME | Same input and same marshal hash. |
| emoji_text | unicode_string | SAME | SAME | Same input and same marshal hash. |
| float_huge_1e300 | float_complex | SAME | SAME | Same input and same marshal hash. |
| float_math_nan | float_complex | SAME | SAME | Same input and same marshal hash. |
| float_nan_constructor | float_complex | SAME | SAME | Same input and same marshal hash. |
| float_nan_payload_0x7ff0000000000001 | float_complex | SAME | SAME | Same input and same marshal hash. |
| float_nan_payload_0x7ff8000000000001 | float_complex | SAME | SAME | Same input and same marshal hash. |
| float_nan_payload_0x7ff8000000000002 | float_complex | SAME | SAME | Same input and same marshal hash. |
| float_neg_inf | float_complex | SAME | SAME | Same input and same marshal hash. |
| float_neg_one | float_complex | SAME | SAME | Same input and same marshal hash. |
| float_neg_zero | float_complex | SAME | SAME | Same input and same marshal hash. |
| float_pos_inf | float_complex | SAME | SAME | Same input and same marshal hash. |
| float_pos_one | float_complex | SAME | SAME | Same input and same marshal hash. |
| float_pos_zero | float_complex | SAME | SAME | Same input and same marshal hash. |
| float_tiny_1e_minus_300 | float_complex | SAME | SAME | Same input and same marshal hash. |
| lone_high_surrogate | unicode_string | SAME | SAME | Same input and same marshal hash. |
| non_bmp_character | unicode_string | SAME | SAME | Same input and same marshal hash. |
| nul_inside_string | unicode_string | SAME | SAME | Same input and same marshal hash. |
| recreated_complex_nan_both | float_complex | SAME | SAME | Same input and same marshal hash. |
| recreated_float_nan | float_complex | SAME | SAME | Same input and same marshal hash. |
| slice_1_10_2 | optional_slice_probe | DIFFERENT | SAME | Same optional support boundary or exception behavior. |
| slice_neg10_none_neg1 | optional_slice_probe | DIFFERENT | SAME | Same optional support boundary or exception behavior. |
| slice_none_none_none | optional_slice_probe | DIFFERENT | SAME | Same optional support boundary or exception behavior. |
| zero_width_joiner_sequence | unicode_string | SAME | SAME | Same input and same marshal hash. |

### member_b_all_darwin_arm64_py3_11_results (Darwin/arm64, Python 3.11.9) vs member_b_all_linux_x86_64_py3_9_results (Linux/x86_64, Python 3.9.25)

| Case | Category | Same marshal hash | Same exception | Interpretation |
| --- | --- | --- | --- | --- |
| ascii_plain | unicode_string | SAME | SAME | Same input and same marshal hash. |
| bytes_255_a | bytes_payload | SAME | SAME | Same input and same marshal hash. |
| bytes_256_a | bytes_payload | SAME | SAME | Same input and same marshal hash. |
| bytes_65535_a | bytes_payload | SAME | SAME | Same input and same marshal hash. |
| bytes_65536_a | bytes_payload | SAME | SAME | Same input and same marshal hash. |
| bytes_all_byte_values | bytes_payload | SAME | SAME | Same input and same marshal hash. |
| bytes_empty | bytes_payload | SAME | SAME | Same input and same marshal hash. |
| bytes_high_values_with_ascii | bytes_payload | SAME | SAME | Same input and same marshal hash. |
| bytes_single_nul | bytes_payload | SAME | SAME | Same input and same marshal hash. |
| chinese_text | unicode_string | SAME | SAME | Same input and same marshal hash. |
| complex_inf_neg_inf | float_complex | SAME | SAME | Same input and same marshal hash. |
| complex_nan_both | float_complex | SAME | SAME | Same input and same marshal hash. |
| complex_nan_imag | float_complex | SAME | SAME | Same input and same marshal hash. |
| complex_nan_real | float_complex | SAME | SAME | Same input and same marshal hash. |
| complex_payload_nan_imag | float_complex | SAME | SAME | Same input and same marshal hash. |
| complex_payload_nan_real | float_complex | SAME | SAME | Same input and same marshal hash. |
| complex_regular | float_complex | SAME | SAME | Same input and same marshal hash. |
| complex_zero_neg_zero | float_complex | SAME | SAME | Same input and same marshal hash. |
| composed_e_acute | unicode_string | SAME | SAME | Same input and same marshal hash. |
| constant_ellipsis | basic_scalar_constant | SAME | SAME | Same input and same marshal hash. |
| constant_false | basic_scalar_constant | SAME | SAME | Same input and same marshal hash. |
| constant_none | basic_scalar_constant | SAME | SAME | Same input and same marshal hash. |
| constant_true | basic_scalar_constant | SAME | SAME | Same input and same marshal hash. |
| crlf_string | unicode_string | SAME | SAME | Same input and same marshal hash. |
| decomposed_e_acute | unicode_string | SAME | SAME | Same input and same marshal hash. |
| emoji_text | unicode_string | SAME | SAME | Same input and same marshal hash. |
| float_huge_1e300 | float_complex | SAME | SAME | Same input and same marshal hash. |
| float_math_nan | float_complex | SAME | SAME | Same input and same marshal hash. |
| float_nan_constructor | float_complex | SAME | SAME | Same input and same marshal hash. |
| float_nan_payload_0x7ff0000000000001 | float_complex | SAME | SAME | Same input and same marshal hash. |
| float_nan_payload_0x7ff8000000000001 | float_complex | SAME | SAME | Same input and same marshal hash. |
| float_nan_payload_0x7ff8000000000002 | float_complex | SAME | SAME | Same input and same marshal hash. |
| float_neg_inf | float_complex | SAME | SAME | Same input and same marshal hash. |
| float_neg_one | float_complex | SAME | SAME | Same input and same marshal hash. |
| float_neg_zero | float_complex | SAME | SAME | Same input and same marshal hash. |
| float_pos_inf | float_complex | SAME | SAME | Same input and same marshal hash. |
| float_pos_one | float_complex | SAME | SAME | Same input and same marshal hash. |
| float_pos_zero | float_complex | SAME | SAME | Same input and same marshal hash. |
| float_tiny_1e_minus_300 | float_complex | SAME | SAME | Same input and same marshal hash. |
| lone_high_surrogate | unicode_string | SAME | SAME | Same input and same marshal hash. |
| non_bmp_character | unicode_string | SAME | SAME | Same input and same marshal hash. |
| nul_inside_string | unicode_string | SAME | SAME | Same input and same marshal hash. |
| recreated_complex_nan_both | float_complex | SAME | SAME | Same input and same marshal hash. |
| recreated_float_nan | float_complex | SAME | SAME | Same input and same marshal hash. |
| slice_1_10_2 | optional_slice_probe | DIFFERENT | SAME | Same optional support boundary or exception behavior. |
| slice_neg10_none_neg1 | optional_slice_probe | DIFFERENT | SAME | Same optional support boundary or exception behavior. |
| slice_none_none_none | optional_slice_probe | DIFFERENT | SAME | Same optional support boundary or exception behavior. |
| zero_width_joiner_sequence | unicode_string | SAME | SAME | Same input and same marshal hash. |

### member_b_all_darwin_arm64_py3_11_results (Darwin/arm64, Python 3.11.9) vs member_b_all_windows_amd64_py3_10_results (Windows/AMD64, Python 3.10.11)

| Case | Category | Same marshal hash | Same exception | Interpretation |
| --- | --- | --- | --- | --- |
| ascii_plain | unicode_string | SAME | SAME | Same input and same marshal hash. |
| bytes_255_a | bytes_payload | SAME | SAME | Same input and same marshal hash. |
| bytes_256_a | bytes_payload | SAME | SAME | Same input and same marshal hash. |
| bytes_65535_a | bytes_payload | SAME | SAME | Same input and same marshal hash. |
| bytes_65536_a | bytes_payload | SAME | SAME | Same input and same marshal hash. |
| bytes_all_byte_values | bytes_payload | SAME | SAME | Same input and same marshal hash. |
| bytes_empty | bytes_payload | SAME | SAME | Same input and same marshal hash. |
| bytes_high_values_with_ascii | bytes_payload | SAME | SAME | Same input and same marshal hash. |
| bytes_single_nul | bytes_payload | SAME | SAME | Same input and same marshal hash. |
| chinese_text | unicode_string | SAME | SAME | Same input and same marshal hash. |
| complex_inf_neg_inf | float_complex | SAME | SAME | Same input and same marshal hash. |
| complex_nan_both | float_complex | SAME | SAME | Same input and same marshal hash. |
| complex_nan_imag | float_complex | SAME | SAME | Same input and same marshal hash. |
| complex_nan_real | float_complex | SAME | SAME | Same input and same marshal hash. |
| complex_payload_nan_imag | float_complex | SAME | SAME | Same input and same marshal hash. |
| complex_payload_nan_real | float_complex | SAME | SAME | Same input and same marshal hash. |
| complex_regular | float_complex | SAME | SAME | Same input and same marshal hash. |
| complex_zero_neg_zero | float_complex | SAME | SAME | Same input and same marshal hash. |
| composed_e_acute | unicode_string | SAME | SAME | Same input and same marshal hash. |
| constant_ellipsis | basic_scalar_constant | SAME | SAME | Same input and same marshal hash. |
| constant_false | basic_scalar_constant | SAME | SAME | Same input and same marshal hash. |
| constant_none | basic_scalar_constant | SAME | SAME | Same input and same marshal hash. |
| constant_true | basic_scalar_constant | SAME | SAME | Same input and same marshal hash. |
| crlf_string | unicode_string | SAME | SAME | Same input and same marshal hash. |
| decomposed_e_acute | unicode_string | SAME | SAME | Same input and same marshal hash. |
| emoji_text | unicode_string | SAME | SAME | Same input and same marshal hash. |
| float_huge_1e300 | float_complex | SAME | SAME | Same input and same marshal hash. |
| float_math_nan | float_complex | SAME | SAME | Same input and same marshal hash. |
| float_nan_constructor | float_complex | SAME | SAME | Same input and same marshal hash. |
| float_nan_payload_0x7ff0000000000001 | float_complex | SAME | SAME | Same input and same marshal hash. |
| float_nan_payload_0x7ff8000000000001 | float_complex | SAME | SAME | Same input and same marshal hash. |
| float_nan_payload_0x7ff8000000000002 | float_complex | SAME | SAME | Same input and same marshal hash. |
| float_neg_inf | float_complex | SAME | SAME | Same input and same marshal hash. |
| float_neg_one | float_complex | SAME | SAME | Same input and same marshal hash. |
| float_neg_zero | float_complex | SAME | SAME | Same input and same marshal hash. |
| float_pos_inf | float_complex | SAME | SAME | Same input and same marshal hash. |
| float_pos_one | float_complex | SAME | SAME | Same input and same marshal hash. |
| float_pos_zero | float_complex | SAME | SAME | Same input and same marshal hash. |
| float_tiny_1e_minus_300 | float_complex | SAME | SAME | Same input and same marshal hash. |
| lone_high_surrogate | unicode_string | SAME | SAME | Same input and same marshal hash. |
| non_bmp_character | unicode_string | SAME | SAME | Same input and same marshal hash. |
| nul_inside_string | unicode_string | SAME | SAME | Same input and same marshal hash. |
| recreated_complex_nan_both | float_complex | SAME | SAME | Same input and same marshal hash. |
| recreated_float_nan | float_complex | SAME | SAME | Same input and same marshal hash. |
| slice_1_10_2 | optional_slice_probe | DIFFERENT | SAME | Same optional support boundary or exception behavior. |
| slice_neg10_none_neg1 | optional_slice_probe | DIFFERENT | SAME | Same optional support boundary or exception behavior. |
| slice_none_none_none | optional_slice_probe | DIFFERENT | SAME | Same optional support boundary or exception behavior. |
| zero_width_joiner_sequence | unicode_string | SAME | SAME | Same input and same marshal hash. |

### member_b_all_darwin_arm64_py3_11_results (Darwin/arm64, Python 3.11.9) vs member_b_all_windows_amd64_py3_11_results (Windows/AMD64, Python 3.11.9)

| Case | Category | Same marshal hash | Same exception | Interpretation |
| --- | --- | --- | --- | --- |
| ascii_plain | unicode_string | SAME | SAME | Same input and same marshal hash. |
| bytes_255_a | bytes_payload | SAME | SAME | Same input and same marshal hash. |
| bytes_256_a | bytes_payload | SAME | SAME | Same input and same marshal hash. |
| bytes_65535_a | bytes_payload | SAME | SAME | Same input and same marshal hash. |
| bytes_65536_a | bytes_payload | SAME | SAME | Same input and same marshal hash. |
| bytes_all_byte_values | bytes_payload | SAME | SAME | Same input and same marshal hash. |
| bytes_empty | bytes_payload | SAME | SAME | Same input and same marshal hash. |
| bytes_high_values_with_ascii | bytes_payload | SAME | SAME | Same input and same marshal hash. |
| bytes_single_nul | bytes_payload | SAME | SAME | Same input and same marshal hash. |
| chinese_text | unicode_string | SAME | SAME | Same input and same marshal hash. |
| complex_inf_neg_inf | float_complex | SAME | SAME | Same input and same marshal hash. |
| complex_nan_both | float_complex | SAME | SAME | Same input and same marshal hash. |
| complex_nan_imag | float_complex | SAME | SAME | Same input and same marshal hash. |
| complex_nan_real | float_complex | SAME | SAME | Same input and same marshal hash. |
| complex_payload_nan_imag | float_complex | SAME | SAME | Same input and same marshal hash. |
| complex_payload_nan_real | float_complex | SAME | SAME | Same input and same marshal hash. |
| complex_regular | float_complex | SAME | SAME | Same input and same marshal hash. |
| complex_zero_neg_zero | float_complex | SAME | SAME | Same input and same marshal hash. |
| composed_e_acute | unicode_string | SAME | SAME | Same input and same marshal hash. |
| constant_ellipsis | basic_scalar_constant | SAME | SAME | Same input and same marshal hash. |
| constant_false | basic_scalar_constant | SAME | SAME | Same input and same marshal hash. |
| constant_none | basic_scalar_constant | SAME | SAME | Same input and same marshal hash. |
| constant_true | basic_scalar_constant | SAME | SAME | Same input and same marshal hash. |
| crlf_string | unicode_string | SAME | SAME | Same input and same marshal hash. |
| decomposed_e_acute | unicode_string | SAME | SAME | Same input and same marshal hash. |
| emoji_text | unicode_string | SAME | SAME | Same input and same marshal hash. |
| float_huge_1e300 | float_complex | SAME | SAME | Same input and same marshal hash. |
| float_math_nan | float_complex | SAME | SAME | Same input and same marshal hash. |
| float_nan_constructor | float_complex | SAME | SAME | Same input and same marshal hash. |
| float_nan_payload_0x7ff0000000000001 | float_complex | SAME | SAME | Same input and same marshal hash. |
| float_nan_payload_0x7ff8000000000001 | float_complex | SAME | SAME | Same input and same marshal hash. |
| float_nan_payload_0x7ff8000000000002 | float_complex | SAME | SAME | Same input and same marshal hash. |
| float_neg_inf | float_complex | SAME | SAME | Same input and same marshal hash. |
| float_neg_one | float_complex | SAME | SAME | Same input and same marshal hash. |
| float_neg_zero | float_complex | SAME | SAME | Same input and same marshal hash. |
| float_pos_inf | float_complex | SAME | SAME | Same input and same marshal hash. |
| float_pos_one | float_complex | SAME | SAME | Same input and same marshal hash. |
| float_pos_zero | float_complex | SAME | SAME | Same input and same marshal hash. |
| float_tiny_1e_minus_300 | float_complex | SAME | SAME | Same input and same marshal hash. |
| lone_high_surrogate | unicode_string | SAME | SAME | Same input and same marshal hash. |
| non_bmp_character | unicode_string | SAME | SAME | Same input and same marshal hash. |
| nul_inside_string | unicode_string | SAME | SAME | Same input and same marshal hash. |
| recreated_complex_nan_both | float_complex | SAME | SAME | Same input and same marshal hash. |
| recreated_float_nan | float_complex | SAME | SAME | Same input and same marshal hash. |
| slice_1_10_2 | optional_slice_probe | DIFFERENT | SAME | Same optional support boundary or exception behavior. |
| slice_neg10_none_neg1 | optional_slice_probe | DIFFERENT | SAME | Same optional support boundary or exception behavior. |
| slice_none_none_none | optional_slice_probe | DIFFERENT | SAME | Same optional support boundary or exception behavior. |
| zero_width_joiner_sequence | unicode_string | SAME | SAME | Same input and same marshal hash. |

### member_b_all_darwin_arm64_py3_11_results (Darwin/arm64, Python 3.11.9) vs member_b_all_windows_amd64_py3_12_results (Windows/AMD64, Python 3.12.10)

| Case | Category | Same marshal hash | Same exception | Interpretation |
| --- | --- | --- | --- | --- |
| ascii_plain | unicode_string | SAME | SAME | Same input and same marshal hash. |
| bytes_255_a | bytes_payload | SAME | SAME | Same input and same marshal hash. |
| bytes_256_a | bytes_payload | SAME | SAME | Same input and same marshal hash. |
| bytes_65535_a | bytes_payload | SAME | SAME | Same input and same marshal hash. |
| bytes_65536_a | bytes_payload | SAME | SAME | Same input and same marshal hash. |
| bytes_all_byte_values | bytes_payload | SAME | SAME | Same input and same marshal hash. |
| bytes_empty | bytes_payload | SAME | SAME | Same input and same marshal hash. |
| bytes_high_values_with_ascii | bytes_payload | SAME | SAME | Same input and same marshal hash. |
| bytes_single_nul | bytes_payload | SAME | SAME | Same input and same marshal hash. |
| chinese_text | unicode_string | SAME | SAME | Same input and same marshal hash. |
| complex_inf_neg_inf | float_complex | SAME | SAME | Same input and same marshal hash. |
| complex_nan_both | float_complex | SAME | SAME | Same input and same marshal hash. |
| complex_nan_imag | float_complex | SAME | SAME | Same input and same marshal hash. |
| complex_nan_real | float_complex | SAME | SAME | Same input and same marshal hash. |
| complex_payload_nan_imag | float_complex | SAME | SAME | Same input and same marshal hash. |
| complex_payload_nan_real | float_complex | SAME | SAME | Same input and same marshal hash. |
| complex_regular | float_complex | SAME | SAME | Same input and same marshal hash. |
| complex_zero_neg_zero | float_complex | SAME | SAME | Same input and same marshal hash. |
| composed_e_acute | unicode_string | DIFFERENT | SAME | Same input representation but Python major/minor differs; likely version-level marshal format difference. |
| constant_ellipsis | basic_scalar_constant | SAME | SAME | Same input and same marshal hash. |
| constant_false | basic_scalar_constant | SAME | SAME | Same input and same marshal hash. |
| constant_none | basic_scalar_constant | SAME | SAME | Same input and same marshal hash. |
| constant_true | basic_scalar_constant | SAME | SAME | Same input and same marshal hash. |
| crlf_string | unicode_string | SAME | SAME | Same input and same marshal hash. |
| decomposed_e_acute | unicode_string | SAME | SAME | Same input and same marshal hash. |
| emoji_text | unicode_string | SAME | SAME | Same input and same marshal hash. |
| float_huge_1e300 | float_complex | SAME | SAME | Same input and same marshal hash. |
| float_math_nan | float_complex | SAME | SAME | Same input and same marshal hash. |
| float_nan_constructor | float_complex | SAME | SAME | Same input and same marshal hash. |
| float_nan_payload_0x7ff0000000000001 | float_complex | SAME | SAME | Same input and same marshal hash. |
| float_nan_payload_0x7ff8000000000001 | float_complex | SAME | SAME | Same input and same marshal hash. |
| float_nan_payload_0x7ff8000000000002 | float_complex | SAME | SAME | Same input and same marshal hash. |
| float_neg_inf | float_complex | SAME | SAME | Same input and same marshal hash. |
| float_neg_one | float_complex | SAME | SAME | Same input and same marshal hash. |
| float_neg_zero | float_complex | SAME | SAME | Same input and same marshal hash. |
| float_pos_inf | float_complex | SAME | SAME | Same input and same marshal hash. |
| float_pos_one | float_complex | SAME | SAME | Same input and same marshal hash. |
| float_pos_zero | float_complex | SAME | SAME | Same input and same marshal hash. |
| float_tiny_1e_minus_300 | float_complex | SAME | SAME | Same input and same marshal hash. |
| lone_high_surrogate | unicode_string | SAME | SAME | Same input and same marshal hash. |
| non_bmp_character | unicode_string | SAME | SAME | Same input and same marshal hash. |
| nul_inside_string | unicode_string | SAME | SAME | Same input and same marshal hash. |
| recreated_complex_nan_both | float_complex | SAME | SAME | Same input and same marshal hash. |
| recreated_float_nan | float_complex | SAME | SAME | Same input and same marshal hash. |
| slice_1_10_2 | optional_slice_probe | DIFFERENT | SAME | Same optional support boundary or exception behavior. |
| slice_neg10_none_neg1 | optional_slice_probe | DIFFERENT | SAME | Same optional support boundary or exception behavior. |
| slice_none_none_none | optional_slice_probe | DIFFERENT | SAME | Same optional support boundary or exception behavior. |
| zero_width_joiner_sequence | unicode_string | SAME | SAME | Same input and same marshal hash. |

### member_b_all_darwin_arm64_py3_11_results (Darwin/arm64, Python 3.11.9) vs member_b_all_windows_amd64_py3_13_results (Windows/AMD64, Python 3.13.13)

| Case | Category | Same marshal hash | Same exception | Interpretation |
| --- | --- | --- | --- | --- |
| ascii_plain | unicode_string | SAME | SAME | Same input and same marshal hash. |
| bytes_255_a | bytes_payload | SAME | SAME | Same input and same marshal hash. |
| bytes_256_a | bytes_payload | SAME | SAME | Same input and same marshal hash. |
| bytes_65535_a | bytes_payload | SAME | SAME | Same input and same marshal hash. |
| bytes_65536_a | bytes_payload | SAME | SAME | Same input and same marshal hash. |
| bytes_all_byte_values | bytes_payload | SAME | SAME | Same input and same marshal hash. |
| bytes_empty | bytes_payload | SAME | SAME | Same input and same marshal hash. |
| bytes_high_values_with_ascii | bytes_payload | SAME | SAME | Same input and same marshal hash. |
| bytes_single_nul | bytes_payload | SAME | SAME | Same input and same marshal hash. |
| chinese_text | unicode_string | SAME | SAME | Same input and same marshal hash. |
| complex_inf_neg_inf | float_complex | SAME | SAME | Same input and same marshal hash. |
| complex_nan_both | float_complex | SAME | SAME | Same input and same marshal hash. |
| complex_nan_imag | float_complex | SAME | SAME | Same input and same marshal hash. |
| complex_nan_real | float_complex | SAME | SAME | Same input and same marshal hash. |
| complex_payload_nan_imag | float_complex | SAME | SAME | Same input and same marshal hash. |
| complex_payload_nan_real | float_complex | SAME | SAME | Same input and same marshal hash. |
| complex_regular | float_complex | SAME | SAME | Same input and same marshal hash. |
| complex_zero_neg_zero | float_complex | SAME | SAME | Same input and same marshal hash. |
| composed_e_acute | unicode_string | DIFFERENT | SAME | Same input representation but Python major/minor differs; likely version-level marshal format difference. |
| constant_ellipsis | basic_scalar_constant | SAME | SAME | Same input and same marshal hash. |
| constant_false | basic_scalar_constant | SAME | SAME | Same input and same marshal hash. |
| constant_none | basic_scalar_constant | SAME | SAME | Same input and same marshal hash. |
| constant_true | basic_scalar_constant | SAME | SAME | Same input and same marshal hash. |
| crlf_string | unicode_string | SAME | SAME | Same input and same marshal hash. |
| decomposed_e_acute | unicode_string | SAME | SAME | Same input and same marshal hash. |
| emoji_text | unicode_string | SAME | SAME | Same input and same marshal hash. |
| float_huge_1e300 | float_complex | SAME | SAME | Same input and same marshal hash. |
| float_math_nan | float_complex | SAME | SAME | Same input and same marshal hash. |
| float_nan_constructor | float_complex | SAME | SAME | Same input and same marshal hash. |
| float_nan_payload_0x7ff0000000000001 | float_complex | SAME | SAME | Same input and same marshal hash. |
| float_nan_payload_0x7ff8000000000001 | float_complex | SAME | SAME | Same input and same marshal hash. |
| float_nan_payload_0x7ff8000000000002 | float_complex | SAME | SAME | Same input and same marshal hash. |
| float_neg_inf | float_complex | SAME | SAME | Same input and same marshal hash. |
| float_neg_one | float_complex | SAME | SAME | Same input and same marshal hash. |
| float_neg_zero | float_complex | SAME | SAME | Same input and same marshal hash. |
| float_pos_inf | float_complex | SAME | SAME | Same input and same marshal hash. |
| float_pos_one | float_complex | SAME | SAME | Same input and same marshal hash. |
| float_pos_zero | float_complex | SAME | SAME | Same input and same marshal hash. |
| float_tiny_1e_minus_300 | float_complex | SAME | SAME | Same input and same marshal hash. |
| lone_high_surrogate | unicode_string | SAME | SAME | Same input and same marshal hash. |
| non_bmp_character | unicode_string | SAME | SAME | Same input and same marshal hash. |
| nul_inside_string | unicode_string | SAME | SAME | Same input and same marshal hash. |
| recreated_complex_nan_both | float_complex | SAME | SAME | Same input and same marshal hash. |
| recreated_float_nan | float_complex | SAME | SAME | Same input and same marshal hash. |
| slice_1_10_2 | optional_slice_probe | DIFFERENT | SAME | Same optional support boundary or exception behavior. |
| slice_neg10_none_neg1 | optional_slice_probe | DIFFERENT | SAME | Same optional support boundary or exception behavior. |
| slice_none_none_none | optional_slice_probe | DIFFERENT | SAME | Same optional support boundary or exception behavior. |
| zero_width_joiner_sequence | unicode_string | SAME | SAME | Same input and same marshal hash. |

### member_b_all_darwin_arm64_py3_11_results (Darwin/arm64, Python 3.11.9) vs member_b_all_windows_amd64_py3_9_results (Windows/AMD64, Python 3.9.13)

| Case | Category | Same marshal hash | Same exception | Interpretation |
| --- | --- | --- | --- | --- |
| ascii_plain | unicode_string | SAME | SAME | Same input and same marshal hash. |
| bytes_255_a | bytes_payload | SAME | SAME | Same input and same marshal hash. |
| bytes_256_a | bytes_payload | SAME | SAME | Same input and same marshal hash. |
| bytes_65535_a | bytes_payload | SAME | SAME | Same input and same marshal hash. |
| bytes_65536_a | bytes_payload | SAME | SAME | Same input and same marshal hash. |
| bytes_all_byte_values | bytes_payload | SAME | SAME | Same input and same marshal hash. |
| bytes_empty | bytes_payload | SAME | SAME | Same input and same marshal hash. |
| bytes_high_values_with_ascii | bytes_payload | SAME | SAME | Same input and same marshal hash. |
| bytes_single_nul | bytes_payload | SAME | SAME | Same input and same marshal hash. |
| chinese_text | unicode_string | SAME | SAME | Same input and same marshal hash. |
| complex_inf_neg_inf | float_complex | SAME | SAME | Same input and same marshal hash. |
| complex_nan_both | float_complex | SAME | SAME | Same input and same marshal hash. |
| complex_nan_imag | float_complex | SAME | SAME | Same input and same marshal hash. |
| complex_nan_real | float_complex | SAME | SAME | Same input and same marshal hash. |
| complex_payload_nan_imag | float_complex | SAME | SAME | Same input and same marshal hash. |
| complex_payload_nan_real | float_complex | SAME | SAME | Same input and same marshal hash. |
| complex_regular | float_complex | SAME | SAME | Same input and same marshal hash. |
| complex_zero_neg_zero | float_complex | SAME | SAME | Same input and same marshal hash. |
| composed_e_acute | unicode_string | SAME | SAME | Same input and same marshal hash. |
| constant_ellipsis | basic_scalar_constant | SAME | SAME | Same input and same marshal hash. |
| constant_false | basic_scalar_constant | SAME | SAME | Same input and same marshal hash. |
| constant_none | basic_scalar_constant | SAME | SAME | Same input and same marshal hash. |
| constant_true | basic_scalar_constant | SAME | SAME | Same input and same marshal hash. |
| crlf_string | unicode_string | SAME | SAME | Same input and same marshal hash. |
| decomposed_e_acute | unicode_string | SAME | SAME | Same input and same marshal hash. |
| emoji_text | unicode_string | SAME | SAME | Same input and same marshal hash. |
| float_huge_1e300 | float_complex | SAME | SAME | Same input and same marshal hash. |
| float_math_nan | float_complex | SAME | SAME | Same input and same marshal hash. |
| float_nan_constructor | float_complex | SAME | SAME | Same input and same marshal hash. |
| float_nan_payload_0x7ff0000000000001 | float_complex | SAME | SAME | Same input and same marshal hash. |
| float_nan_payload_0x7ff8000000000001 | float_complex | SAME | SAME | Same input and same marshal hash. |
| float_nan_payload_0x7ff8000000000002 | float_complex | SAME | SAME | Same input and same marshal hash. |
| float_neg_inf | float_complex | SAME | SAME | Same input and same marshal hash. |
| float_neg_one | float_complex | SAME | SAME | Same input and same marshal hash. |
| float_neg_zero | float_complex | SAME | SAME | Same input and same marshal hash. |
| float_pos_inf | float_complex | SAME | SAME | Same input and same marshal hash. |
| float_pos_one | float_complex | SAME | SAME | Same input and same marshal hash. |
| float_pos_zero | float_complex | SAME | SAME | Same input and same marshal hash. |
| float_tiny_1e_minus_300 | float_complex | SAME | SAME | Same input and same marshal hash. |
| lone_high_surrogate | unicode_string | SAME | SAME | Same input and same marshal hash. |
| non_bmp_character | unicode_string | SAME | SAME | Same input and same marshal hash. |
| nul_inside_string | unicode_string | SAME | SAME | Same input and same marshal hash. |
| recreated_complex_nan_both | float_complex | SAME | SAME | Same input and same marshal hash. |
| recreated_float_nan | float_complex | SAME | SAME | Same input and same marshal hash. |
| slice_1_10_2 | optional_slice_probe | DIFFERENT | SAME | Same optional support boundary or exception behavior. |
| slice_neg10_none_neg1 | optional_slice_probe | DIFFERENT | SAME | Same optional support boundary or exception behavior. |
| slice_none_none_none | optional_slice_probe | DIFFERENT | SAME | Same optional support boundary or exception behavior. |
| zero_width_joiner_sequence | unicode_string | SAME | SAME | Same input and same marshal hash. |

### member_b_all_darwin_arm64_py3_12_results (Darwin/arm64, Python 3.12.10) vs member_b_all_darwin_arm64_py3_13_results (Darwin/arm64, Python 3.13.13)

| Case | Category | Same marshal hash | Same exception | Interpretation |
| --- | --- | --- | --- | --- |
| ascii_plain | unicode_string | SAME | SAME | Same input and same marshal hash. |
| bytes_255_a | bytes_payload | SAME | SAME | Same input and same marshal hash. |
| bytes_256_a | bytes_payload | SAME | SAME | Same input and same marshal hash. |
| bytes_65535_a | bytes_payload | SAME | SAME | Same input and same marshal hash. |
| bytes_65536_a | bytes_payload | SAME | SAME | Same input and same marshal hash. |
| bytes_all_byte_values | bytes_payload | SAME | SAME | Same input and same marshal hash. |
| bytes_empty | bytes_payload | SAME | SAME | Same input and same marshal hash. |
| bytes_high_values_with_ascii | bytes_payload | SAME | SAME | Same input and same marshal hash. |
| bytes_single_nul | bytes_payload | SAME | SAME | Same input and same marshal hash. |
| chinese_text | unicode_string | SAME | SAME | Same input and same marshal hash. |
| complex_inf_neg_inf | float_complex | SAME | SAME | Same input and same marshal hash. |
| complex_nan_both | float_complex | SAME | SAME | Same input and same marshal hash. |
| complex_nan_imag | float_complex | SAME | SAME | Same input and same marshal hash. |
| complex_nan_real | float_complex | SAME | SAME | Same input and same marshal hash. |
| complex_payload_nan_imag | float_complex | SAME | SAME | Same input and same marshal hash. |
| complex_payload_nan_real | float_complex | SAME | SAME | Same input and same marshal hash. |
| complex_regular | float_complex | SAME | SAME | Same input and same marshal hash. |
| complex_zero_neg_zero | float_complex | SAME | SAME | Same input and same marshal hash. |
| composed_e_acute | unicode_string | SAME | SAME | Same input and same marshal hash. |
| constant_ellipsis | basic_scalar_constant | SAME | SAME | Same input and same marshal hash. |
| constant_false | basic_scalar_constant | SAME | SAME | Same input and same marshal hash. |
| constant_none | basic_scalar_constant | SAME | SAME | Same input and same marshal hash. |
| constant_true | basic_scalar_constant | SAME | SAME | Same input and same marshal hash. |
| crlf_string | unicode_string | SAME | SAME | Same input and same marshal hash. |
| decomposed_e_acute | unicode_string | SAME | SAME | Same input and same marshal hash. |
| emoji_text | unicode_string | SAME | SAME | Same input and same marshal hash. |
| float_huge_1e300 | float_complex | SAME | SAME | Same input and same marshal hash. |
| float_math_nan | float_complex | SAME | SAME | Same input and same marshal hash. |
| float_nan_constructor | float_complex | SAME | SAME | Same input and same marshal hash. |
| float_nan_payload_0x7ff0000000000001 | float_complex | SAME | SAME | Same input and same marshal hash. |
| float_nan_payload_0x7ff8000000000001 | float_complex | SAME | SAME | Same input and same marshal hash. |
| float_nan_payload_0x7ff8000000000002 | float_complex | SAME | SAME | Same input and same marshal hash. |
| float_neg_inf | float_complex | SAME | SAME | Same input and same marshal hash. |
| float_neg_one | float_complex | SAME | SAME | Same input and same marshal hash. |
| float_neg_zero | float_complex | SAME | SAME | Same input and same marshal hash. |
| float_pos_inf | float_complex | SAME | SAME | Same input and same marshal hash. |
| float_pos_one | float_complex | SAME | SAME | Same input and same marshal hash. |
| float_pos_zero | float_complex | SAME | SAME | Same input and same marshal hash. |
| float_tiny_1e_minus_300 | float_complex | SAME | SAME | Same input and same marshal hash. |
| lone_high_surrogate | unicode_string | SAME | SAME | Same input and same marshal hash. |
| non_bmp_character | unicode_string | SAME | SAME | Same input and same marshal hash. |
| nul_inside_string | unicode_string | SAME | SAME | Same input and same marshal hash. |
| recreated_complex_nan_both | float_complex | SAME | SAME | Same input and same marshal hash. |
| recreated_float_nan | float_complex | SAME | SAME | Same input and same marshal hash. |
| slice_1_10_2 | optional_slice_probe | DIFFERENT | SAME | Same optional support boundary or exception behavior. |
| slice_neg10_none_neg1 | optional_slice_probe | DIFFERENT | SAME | Same optional support boundary or exception behavior. |
| slice_none_none_none | optional_slice_probe | DIFFERENT | SAME | Same optional support boundary or exception behavior. |
| zero_width_joiner_sequence | unicode_string | SAME | SAME | Same input and same marshal hash. |

### member_b_all_darwin_arm64_py3_12_results (Darwin/arm64, Python 3.12.10) vs member_b_all_darwin_arm64_py3_9_results (Darwin/arm64, Python 3.9.6)

| Case | Category | Same marshal hash | Same exception | Interpretation |
| --- | --- | --- | --- | --- |
| ascii_plain | unicode_string | SAME | SAME | Same input and same marshal hash. |
| bytes_255_a | bytes_payload | SAME | SAME | Same input and same marshal hash. |
| bytes_256_a | bytes_payload | SAME | SAME | Same input and same marshal hash. |
| bytes_65535_a | bytes_payload | SAME | SAME | Same input and same marshal hash. |
| bytes_65536_a | bytes_payload | SAME | SAME | Same input and same marshal hash. |
| bytes_all_byte_values | bytes_payload | SAME | SAME | Same input and same marshal hash. |
| bytes_empty | bytes_payload | SAME | SAME | Same input and same marshal hash. |
| bytes_high_values_with_ascii | bytes_payload | SAME | SAME | Same input and same marshal hash. |
| bytes_single_nul | bytes_payload | SAME | SAME | Same input and same marshal hash. |
| chinese_text | unicode_string | SAME | SAME | Same input and same marshal hash. |
| complex_inf_neg_inf | float_complex | SAME | SAME | Same input and same marshal hash. |
| complex_nan_both | float_complex | SAME | SAME | Same input and same marshal hash. |
| complex_nan_imag | float_complex | SAME | SAME | Same input and same marshal hash. |
| complex_nan_real | float_complex | SAME | SAME | Same input and same marshal hash. |
| complex_payload_nan_imag | float_complex | SAME | SAME | Same input and same marshal hash. |
| complex_payload_nan_real | float_complex | SAME | SAME | Same input and same marshal hash. |
| complex_regular | float_complex | SAME | SAME | Same input and same marshal hash. |
| complex_zero_neg_zero | float_complex | SAME | SAME | Same input and same marshal hash. |
| composed_e_acute | unicode_string | DIFFERENT | SAME | Same input representation but Python major/minor differs; likely version-level marshal format difference. |
| constant_ellipsis | basic_scalar_constant | SAME | SAME | Same input and same marshal hash. |
| constant_false | basic_scalar_constant | SAME | SAME | Same input and same marshal hash. |
| constant_none | basic_scalar_constant | SAME | SAME | Same input and same marshal hash. |
| constant_true | basic_scalar_constant | SAME | SAME | Same input and same marshal hash. |
| crlf_string | unicode_string | SAME | SAME | Same input and same marshal hash. |
| decomposed_e_acute | unicode_string | SAME | SAME | Same input and same marshal hash. |
| emoji_text | unicode_string | SAME | SAME | Same input and same marshal hash. |
| float_huge_1e300 | float_complex | SAME | SAME | Same input and same marshal hash. |
| float_math_nan | float_complex | SAME | SAME | Same input and same marshal hash. |
| float_nan_constructor | float_complex | SAME | SAME | Same input and same marshal hash. |
| float_nan_payload_0x7ff0000000000001 | float_complex | SAME | SAME | Same input and same marshal hash. |
| float_nan_payload_0x7ff8000000000001 | float_complex | SAME | SAME | Same input and same marshal hash. |
| float_nan_payload_0x7ff8000000000002 | float_complex | SAME | SAME | Same input and same marshal hash. |
| float_neg_inf | float_complex | SAME | SAME | Same input and same marshal hash. |
| float_neg_one | float_complex | SAME | SAME | Same input and same marshal hash. |
| float_neg_zero | float_complex | SAME | SAME | Same input and same marshal hash. |
| float_pos_inf | float_complex | SAME | SAME | Same input and same marshal hash. |
| float_pos_one | float_complex | SAME | SAME | Same input and same marshal hash. |
| float_pos_zero | float_complex | SAME | SAME | Same input and same marshal hash. |
| float_tiny_1e_minus_300 | float_complex | SAME | SAME | Same input and same marshal hash. |
| lone_high_surrogate | unicode_string | SAME | SAME | Same input and same marshal hash. |
| non_bmp_character | unicode_string | SAME | SAME | Same input and same marshal hash. |
| nul_inside_string | unicode_string | SAME | SAME | Same input and same marshal hash. |
| recreated_complex_nan_both | float_complex | SAME | SAME | Same input and same marshal hash. |
| recreated_float_nan | float_complex | SAME | SAME | Same input and same marshal hash. |
| slice_1_10_2 | optional_slice_probe | DIFFERENT | SAME | Same optional support boundary or exception behavior. |
| slice_neg10_none_neg1 | optional_slice_probe | DIFFERENT | SAME | Same optional support boundary or exception behavior. |
| slice_none_none_none | optional_slice_probe | DIFFERENT | SAME | Same optional support boundary or exception behavior. |
| zero_width_joiner_sequence | unicode_string | SAME | SAME | Same input and same marshal hash. |

### member_b_all_darwin_arm64_py3_12_results (Darwin/arm64, Python 3.12.10) vs member_b_all_linux_x86_64_py3_10_results (Linux/x86_64, Python 3.10.20)

| Case | Category | Same marshal hash | Same exception | Interpretation |
| --- | --- | --- | --- | --- |
| ascii_plain | unicode_string | SAME | SAME | Same input and same marshal hash. |
| bytes_255_a | bytes_payload | SAME | SAME | Same input and same marshal hash. |
| bytes_256_a | bytes_payload | SAME | SAME | Same input and same marshal hash. |
| bytes_65535_a | bytes_payload | SAME | SAME | Same input and same marshal hash. |
| bytes_65536_a | bytes_payload | SAME | SAME | Same input and same marshal hash. |
| bytes_all_byte_values | bytes_payload | SAME | SAME | Same input and same marshal hash. |
| bytes_empty | bytes_payload | SAME | SAME | Same input and same marshal hash. |
| bytes_high_values_with_ascii | bytes_payload | SAME | SAME | Same input and same marshal hash. |
| bytes_single_nul | bytes_payload | SAME | SAME | Same input and same marshal hash. |
| chinese_text | unicode_string | SAME | SAME | Same input and same marshal hash. |
| complex_inf_neg_inf | float_complex | SAME | SAME | Same input and same marshal hash. |
| complex_nan_both | float_complex | SAME | SAME | Same input and same marshal hash. |
| complex_nan_imag | float_complex | SAME | SAME | Same input and same marshal hash. |
| complex_nan_real | float_complex | SAME | SAME | Same input and same marshal hash. |
| complex_payload_nan_imag | float_complex | SAME | SAME | Same input and same marshal hash. |
| complex_payload_nan_real | float_complex | SAME | SAME | Same input and same marshal hash. |
| complex_regular | float_complex | SAME | SAME | Same input and same marshal hash. |
| complex_zero_neg_zero | float_complex | SAME | SAME | Same input and same marshal hash. |
| composed_e_acute | unicode_string | DIFFERENT | SAME | Same input representation but Python major/minor differs; likely version-level marshal format difference. |
| constant_ellipsis | basic_scalar_constant | SAME | SAME | Same input and same marshal hash. |
| constant_false | basic_scalar_constant | SAME | SAME | Same input and same marshal hash. |
| constant_none | basic_scalar_constant | SAME | SAME | Same input and same marshal hash. |
| constant_true | basic_scalar_constant | SAME | SAME | Same input and same marshal hash. |
| crlf_string | unicode_string | SAME | SAME | Same input and same marshal hash. |
| decomposed_e_acute | unicode_string | SAME | SAME | Same input and same marshal hash. |
| emoji_text | unicode_string | SAME | SAME | Same input and same marshal hash. |
| float_huge_1e300 | float_complex | SAME | SAME | Same input and same marshal hash. |
| float_math_nan | float_complex | SAME | SAME | Same input and same marshal hash. |
| float_nan_constructor | float_complex | SAME | SAME | Same input and same marshal hash. |
| float_nan_payload_0x7ff0000000000001 | float_complex | SAME | SAME | Same input and same marshal hash. |
| float_nan_payload_0x7ff8000000000001 | float_complex | SAME | SAME | Same input and same marshal hash. |
| float_nan_payload_0x7ff8000000000002 | float_complex | SAME | SAME | Same input and same marshal hash. |
| float_neg_inf | float_complex | SAME | SAME | Same input and same marshal hash. |
| float_neg_one | float_complex | SAME | SAME | Same input and same marshal hash. |
| float_neg_zero | float_complex | SAME | SAME | Same input and same marshal hash. |
| float_pos_inf | float_complex | SAME | SAME | Same input and same marshal hash. |
| float_pos_one | float_complex | SAME | SAME | Same input and same marshal hash. |
| float_pos_zero | float_complex | SAME | SAME | Same input and same marshal hash. |
| float_tiny_1e_minus_300 | float_complex | SAME | SAME | Same input and same marshal hash. |
| lone_high_surrogate | unicode_string | SAME | SAME | Same input and same marshal hash. |
| non_bmp_character | unicode_string | SAME | SAME | Same input and same marshal hash. |
| nul_inside_string | unicode_string | SAME | SAME | Same input and same marshal hash. |
| recreated_complex_nan_both | float_complex | SAME | SAME | Same input and same marshal hash. |
| recreated_float_nan | float_complex | SAME | SAME | Same input and same marshal hash. |
| slice_1_10_2 | optional_slice_probe | DIFFERENT | SAME | Same optional support boundary or exception behavior. |
| slice_neg10_none_neg1 | optional_slice_probe | DIFFERENT | SAME | Same optional support boundary or exception behavior. |
| slice_none_none_none | optional_slice_probe | DIFFERENT | SAME | Same optional support boundary or exception behavior. |
| zero_width_joiner_sequence | unicode_string | SAME | SAME | Same input and same marshal hash. |

### member_b_all_darwin_arm64_py3_12_results (Darwin/arm64, Python 3.12.10) vs member_b_all_linux_x86_64_py3_11_results (Linux/x86_64, Python 3.11.15)

| Case | Category | Same marshal hash | Same exception | Interpretation |
| --- | --- | --- | --- | --- |
| ascii_plain | unicode_string | SAME | SAME | Same input and same marshal hash. |
| bytes_255_a | bytes_payload | SAME | SAME | Same input and same marshal hash. |
| bytes_256_a | bytes_payload | SAME | SAME | Same input and same marshal hash. |
| bytes_65535_a | bytes_payload | SAME | SAME | Same input and same marshal hash. |
| bytes_65536_a | bytes_payload | SAME | SAME | Same input and same marshal hash. |
| bytes_all_byte_values | bytes_payload | SAME | SAME | Same input and same marshal hash. |
| bytes_empty | bytes_payload | SAME | SAME | Same input and same marshal hash. |
| bytes_high_values_with_ascii | bytes_payload | SAME | SAME | Same input and same marshal hash. |
| bytes_single_nul | bytes_payload | SAME | SAME | Same input and same marshal hash. |
| chinese_text | unicode_string | SAME | SAME | Same input and same marshal hash. |
| complex_inf_neg_inf | float_complex | SAME | SAME | Same input and same marshal hash. |
| complex_nan_both | float_complex | SAME | SAME | Same input and same marshal hash. |
| complex_nan_imag | float_complex | SAME | SAME | Same input and same marshal hash. |
| complex_nan_real | float_complex | SAME | SAME | Same input and same marshal hash. |
| complex_payload_nan_imag | float_complex | SAME | SAME | Same input and same marshal hash. |
| complex_payload_nan_real | float_complex | SAME | SAME | Same input and same marshal hash. |
| complex_regular | float_complex | SAME | SAME | Same input and same marshal hash. |
| complex_zero_neg_zero | float_complex | SAME | SAME | Same input and same marshal hash. |
| composed_e_acute | unicode_string | DIFFERENT | SAME | Same input representation but Python major/minor differs; likely version-level marshal format difference. |
| constant_ellipsis | basic_scalar_constant | SAME | SAME | Same input and same marshal hash. |
| constant_false | basic_scalar_constant | SAME | SAME | Same input and same marshal hash. |
| constant_none | basic_scalar_constant | SAME | SAME | Same input and same marshal hash. |
| constant_true | basic_scalar_constant | SAME | SAME | Same input and same marshal hash. |
| crlf_string | unicode_string | SAME | SAME | Same input and same marshal hash. |
| decomposed_e_acute | unicode_string | SAME | SAME | Same input and same marshal hash. |
| emoji_text | unicode_string | SAME | SAME | Same input and same marshal hash. |
| float_huge_1e300 | float_complex | SAME | SAME | Same input and same marshal hash. |
| float_math_nan | float_complex | SAME | SAME | Same input and same marshal hash. |
| float_nan_constructor | float_complex | SAME | SAME | Same input and same marshal hash. |
| float_nan_payload_0x7ff0000000000001 | float_complex | SAME | SAME | Same input and same marshal hash. |
| float_nan_payload_0x7ff8000000000001 | float_complex | SAME | SAME | Same input and same marshal hash. |
| float_nan_payload_0x7ff8000000000002 | float_complex | SAME | SAME | Same input and same marshal hash. |
| float_neg_inf | float_complex | SAME | SAME | Same input and same marshal hash. |
| float_neg_one | float_complex | SAME | SAME | Same input and same marshal hash. |
| float_neg_zero | float_complex | SAME | SAME | Same input and same marshal hash. |
| float_pos_inf | float_complex | SAME | SAME | Same input and same marshal hash. |
| float_pos_one | float_complex | SAME | SAME | Same input and same marshal hash. |
| float_pos_zero | float_complex | SAME | SAME | Same input and same marshal hash. |
| float_tiny_1e_minus_300 | float_complex | SAME | SAME | Same input and same marshal hash. |
| lone_high_surrogate | unicode_string | SAME | SAME | Same input and same marshal hash. |
| non_bmp_character | unicode_string | SAME | SAME | Same input and same marshal hash. |
| nul_inside_string | unicode_string | SAME | SAME | Same input and same marshal hash. |
| recreated_complex_nan_both | float_complex | SAME | SAME | Same input and same marshal hash. |
| recreated_float_nan | float_complex | SAME | SAME | Same input and same marshal hash. |
| slice_1_10_2 | optional_slice_probe | DIFFERENT | SAME | Same optional support boundary or exception behavior. |
| slice_neg10_none_neg1 | optional_slice_probe | DIFFERENT | SAME | Same optional support boundary or exception behavior. |
| slice_none_none_none | optional_slice_probe | DIFFERENT | SAME | Same optional support boundary or exception behavior. |
| zero_width_joiner_sequence | unicode_string | SAME | SAME | Same input and same marshal hash. |

### member_b_all_darwin_arm64_py3_12_results (Darwin/arm64, Python 3.12.10) vs member_b_all_linux_x86_64_py3_12_results (Linux/x86_64, Python 3.12.13)

| Case | Category | Same marshal hash | Same exception | Interpretation |
| --- | --- | --- | --- | --- |
| ascii_plain | unicode_string | SAME | SAME | Same input and same marshal hash. |
| bytes_255_a | bytes_payload | SAME | SAME | Same input and same marshal hash. |
| bytes_256_a | bytes_payload | SAME | SAME | Same input and same marshal hash. |
| bytes_65535_a | bytes_payload | SAME | SAME | Same input and same marshal hash. |
| bytes_65536_a | bytes_payload | SAME | SAME | Same input and same marshal hash. |
| bytes_all_byte_values | bytes_payload | SAME | SAME | Same input and same marshal hash. |
| bytes_empty | bytes_payload | SAME | SAME | Same input and same marshal hash. |
| bytes_high_values_with_ascii | bytes_payload | SAME | SAME | Same input and same marshal hash. |
| bytes_single_nul | bytes_payload | SAME | SAME | Same input and same marshal hash. |
| chinese_text | unicode_string | SAME | SAME | Same input and same marshal hash. |
| complex_inf_neg_inf | float_complex | SAME | SAME | Same input and same marshal hash. |
| complex_nan_both | float_complex | SAME | SAME | Same input and same marshal hash. |
| complex_nan_imag | float_complex | SAME | SAME | Same input and same marshal hash. |
| complex_nan_real | float_complex | SAME | SAME | Same input and same marshal hash. |
| complex_payload_nan_imag | float_complex | SAME | SAME | Same input and same marshal hash. |
| complex_payload_nan_real | float_complex | SAME | SAME | Same input and same marshal hash. |
| complex_regular | float_complex | SAME | SAME | Same input and same marshal hash. |
| complex_zero_neg_zero | float_complex | SAME | SAME | Same input and same marshal hash. |
| composed_e_acute | unicode_string | SAME | SAME | Same input and same marshal hash. |
| constant_ellipsis | basic_scalar_constant | SAME | SAME | Same input and same marshal hash. |
| constant_false | basic_scalar_constant | SAME | SAME | Same input and same marshal hash. |
| constant_none | basic_scalar_constant | SAME | SAME | Same input and same marshal hash. |
| constant_true | basic_scalar_constant | SAME | SAME | Same input and same marshal hash. |
| crlf_string | unicode_string | SAME | SAME | Same input and same marshal hash. |
| decomposed_e_acute | unicode_string | SAME | SAME | Same input and same marshal hash. |
| emoji_text | unicode_string | SAME | SAME | Same input and same marshal hash. |
| float_huge_1e300 | float_complex | SAME | SAME | Same input and same marshal hash. |
| float_math_nan | float_complex | SAME | SAME | Same input and same marshal hash. |
| float_nan_constructor | float_complex | SAME | SAME | Same input and same marshal hash. |
| float_nan_payload_0x7ff0000000000001 | float_complex | SAME | SAME | Same input and same marshal hash. |
| float_nan_payload_0x7ff8000000000001 | float_complex | SAME | SAME | Same input and same marshal hash. |
| float_nan_payload_0x7ff8000000000002 | float_complex | SAME | SAME | Same input and same marshal hash. |
| float_neg_inf | float_complex | SAME | SAME | Same input and same marshal hash. |
| float_neg_one | float_complex | SAME | SAME | Same input and same marshal hash. |
| float_neg_zero | float_complex | SAME | SAME | Same input and same marshal hash. |
| float_pos_inf | float_complex | SAME | SAME | Same input and same marshal hash. |
| float_pos_one | float_complex | SAME | SAME | Same input and same marshal hash. |
| float_pos_zero | float_complex | SAME | SAME | Same input and same marshal hash. |
| float_tiny_1e_minus_300 | float_complex | SAME | SAME | Same input and same marshal hash. |
| lone_high_surrogate | unicode_string | SAME | SAME | Same input and same marshal hash. |
| non_bmp_character | unicode_string | SAME | SAME | Same input and same marshal hash. |
| nul_inside_string | unicode_string | SAME | SAME | Same input and same marshal hash. |
| recreated_complex_nan_both | float_complex | SAME | SAME | Same input and same marshal hash. |
| recreated_float_nan | float_complex | SAME | SAME | Same input and same marshal hash. |
| slice_1_10_2 | optional_slice_probe | DIFFERENT | SAME | Same optional support boundary or exception behavior. |
| slice_neg10_none_neg1 | optional_slice_probe | DIFFERENT | SAME | Same optional support boundary or exception behavior. |
| slice_none_none_none | optional_slice_probe | DIFFERENT | SAME | Same optional support boundary or exception behavior. |
| zero_width_joiner_sequence | unicode_string | SAME | SAME | Same input and same marshal hash. |

### member_b_all_darwin_arm64_py3_12_results (Darwin/arm64, Python 3.12.10) vs member_b_all_linux_x86_64_py3_13_results (Linux/x86_64, Python 3.13.13)

| Case | Category | Same marshal hash | Same exception | Interpretation |
| --- | --- | --- | --- | --- |
| ascii_plain | unicode_string | SAME | SAME | Same input and same marshal hash. |
| bytes_255_a | bytes_payload | SAME | SAME | Same input and same marshal hash. |
| bytes_256_a | bytes_payload | SAME | SAME | Same input and same marshal hash. |
| bytes_65535_a | bytes_payload | SAME | SAME | Same input and same marshal hash. |
| bytes_65536_a | bytes_payload | SAME | SAME | Same input and same marshal hash. |
| bytes_all_byte_values | bytes_payload | SAME | SAME | Same input and same marshal hash. |
| bytes_empty | bytes_payload | SAME | SAME | Same input and same marshal hash. |
| bytes_high_values_with_ascii | bytes_payload | SAME | SAME | Same input and same marshal hash. |
| bytes_single_nul | bytes_payload | SAME | SAME | Same input and same marshal hash. |
| chinese_text | unicode_string | SAME | SAME | Same input and same marshal hash. |
| complex_inf_neg_inf | float_complex | SAME | SAME | Same input and same marshal hash. |
| complex_nan_both | float_complex | SAME | SAME | Same input and same marshal hash. |
| complex_nan_imag | float_complex | SAME | SAME | Same input and same marshal hash. |
| complex_nan_real | float_complex | SAME | SAME | Same input and same marshal hash. |
| complex_payload_nan_imag | float_complex | SAME | SAME | Same input and same marshal hash. |
| complex_payload_nan_real | float_complex | SAME | SAME | Same input and same marshal hash. |
| complex_regular | float_complex | SAME | SAME | Same input and same marshal hash. |
| complex_zero_neg_zero | float_complex | SAME | SAME | Same input and same marshal hash. |
| composed_e_acute | unicode_string | SAME | SAME | Same input and same marshal hash. |
| constant_ellipsis | basic_scalar_constant | SAME | SAME | Same input and same marshal hash. |
| constant_false | basic_scalar_constant | SAME | SAME | Same input and same marshal hash. |
| constant_none | basic_scalar_constant | SAME | SAME | Same input and same marshal hash. |
| constant_true | basic_scalar_constant | SAME | SAME | Same input and same marshal hash. |
| crlf_string | unicode_string | SAME | SAME | Same input and same marshal hash. |
| decomposed_e_acute | unicode_string | SAME | SAME | Same input and same marshal hash. |
| emoji_text | unicode_string | SAME | SAME | Same input and same marshal hash. |
| float_huge_1e300 | float_complex | SAME | SAME | Same input and same marshal hash. |
| float_math_nan | float_complex | SAME | SAME | Same input and same marshal hash. |
| float_nan_constructor | float_complex | SAME | SAME | Same input and same marshal hash. |
| float_nan_payload_0x7ff0000000000001 | float_complex | SAME | SAME | Same input and same marshal hash. |
| float_nan_payload_0x7ff8000000000001 | float_complex | SAME | SAME | Same input and same marshal hash. |
| float_nan_payload_0x7ff8000000000002 | float_complex | SAME | SAME | Same input and same marshal hash. |
| float_neg_inf | float_complex | SAME | SAME | Same input and same marshal hash. |
| float_neg_one | float_complex | SAME | SAME | Same input and same marshal hash. |
| float_neg_zero | float_complex | SAME | SAME | Same input and same marshal hash. |
| float_pos_inf | float_complex | SAME | SAME | Same input and same marshal hash. |
| float_pos_one | float_complex | SAME | SAME | Same input and same marshal hash. |
| float_pos_zero | float_complex | SAME | SAME | Same input and same marshal hash. |
| float_tiny_1e_minus_300 | float_complex | SAME | SAME | Same input and same marshal hash. |
| lone_high_surrogate | unicode_string | SAME | SAME | Same input and same marshal hash. |
| non_bmp_character | unicode_string | SAME | SAME | Same input and same marshal hash. |
| nul_inside_string | unicode_string | SAME | SAME | Same input and same marshal hash. |
| recreated_complex_nan_both | float_complex | SAME | SAME | Same input and same marshal hash. |
| recreated_float_nan | float_complex | SAME | SAME | Same input and same marshal hash. |
| slice_1_10_2 | optional_slice_probe | DIFFERENT | SAME | Same optional support boundary or exception behavior. |
| slice_neg10_none_neg1 | optional_slice_probe | DIFFERENT | SAME | Same optional support boundary or exception behavior. |
| slice_none_none_none | optional_slice_probe | DIFFERENT | SAME | Same optional support boundary or exception behavior. |
| zero_width_joiner_sequence | unicode_string | SAME | SAME | Same input and same marshal hash. |

### member_b_all_darwin_arm64_py3_12_results (Darwin/arm64, Python 3.12.10) vs member_b_all_linux_x86_64_py3_9_results (Linux/x86_64, Python 3.9.25)

| Case | Category | Same marshal hash | Same exception | Interpretation |
| --- | --- | --- | --- | --- |
| ascii_plain | unicode_string | SAME | SAME | Same input and same marshal hash. |
| bytes_255_a | bytes_payload | SAME | SAME | Same input and same marshal hash. |
| bytes_256_a | bytes_payload | SAME | SAME | Same input and same marshal hash. |
| bytes_65535_a | bytes_payload | SAME | SAME | Same input and same marshal hash. |
| bytes_65536_a | bytes_payload | SAME | SAME | Same input and same marshal hash. |
| bytes_all_byte_values | bytes_payload | SAME | SAME | Same input and same marshal hash. |
| bytes_empty | bytes_payload | SAME | SAME | Same input and same marshal hash. |
| bytes_high_values_with_ascii | bytes_payload | SAME | SAME | Same input and same marshal hash. |
| bytes_single_nul | bytes_payload | SAME | SAME | Same input and same marshal hash. |
| chinese_text | unicode_string | SAME | SAME | Same input and same marshal hash. |
| complex_inf_neg_inf | float_complex | SAME | SAME | Same input and same marshal hash. |
| complex_nan_both | float_complex | SAME | SAME | Same input and same marshal hash. |
| complex_nan_imag | float_complex | SAME | SAME | Same input and same marshal hash. |
| complex_nan_real | float_complex | SAME | SAME | Same input and same marshal hash. |
| complex_payload_nan_imag | float_complex | SAME | SAME | Same input and same marshal hash. |
| complex_payload_nan_real | float_complex | SAME | SAME | Same input and same marshal hash. |
| complex_regular | float_complex | SAME | SAME | Same input and same marshal hash. |
| complex_zero_neg_zero | float_complex | SAME | SAME | Same input and same marshal hash. |
| composed_e_acute | unicode_string | DIFFERENT | SAME | Same input representation but Python major/minor differs; likely version-level marshal format difference. |
| constant_ellipsis | basic_scalar_constant | SAME | SAME | Same input and same marshal hash. |
| constant_false | basic_scalar_constant | SAME | SAME | Same input and same marshal hash. |
| constant_none | basic_scalar_constant | SAME | SAME | Same input and same marshal hash. |
| constant_true | basic_scalar_constant | SAME | SAME | Same input and same marshal hash. |
| crlf_string | unicode_string | SAME | SAME | Same input and same marshal hash. |
| decomposed_e_acute | unicode_string | SAME | SAME | Same input and same marshal hash. |
| emoji_text | unicode_string | SAME | SAME | Same input and same marshal hash. |
| float_huge_1e300 | float_complex | SAME | SAME | Same input and same marshal hash. |
| float_math_nan | float_complex | SAME | SAME | Same input and same marshal hash. |
| float_nan_constructor | float_complex | SAME | SAME | Same input and same marshal hash. |
| float_nan_payload_0x7ff0000000000001 | float_complex | SAME | SAME | Same input and same marshal hash. |
| float_nan_payload_0x7ff8000000000001 | float_complex | SAME | SAME | Same input and same marshal hash. |
| float_nan_payload_0x7ff8000000000002 | float_complex | SAME | SAME | Same input and same marshal hash. |
| float_neg_inf | float_complex | SAME | SAME | Same input and same marshal hash. |
| float_neg_one | float_complex | SAME | SAME | Same input and same marshal hash. |
| float_neg_zero | float_complex | SAME | SAME | Same input and same marshal hash. |
| float_pos_inf | float_complex | SAME | SAME | Same input and same marshal hash. |
| float_pos_one | float_complex | SAME | SAME | Same input and same marshal hash. |
| float_pos_zero | float_complex | SAME | SAME | Same input and same marshal hash. |
| float_tiny_1e_minus_300 | float_complex | SAME | SAME | Same input and same marshal hash. |
| lone_high_surrogate | unicode_string | SAME | SAME | Same input and same marshal hash. |
| non_bmp_character | unicode_string | SAME | SAME | Same input and same marshal hash. |
| nul_inside_string | unicode_string | SAME | SAME | Same input and same marshal hash. |
| recreated_complex_nan_both | float_complex | SAME | SAME | Same input and same marshal hash. |
| recreated_float_nan | float_complex | SAME | SAME | Same input and same marshal hash. |
| slice_1_10_2 | optional_slice_probe | DIFFERENT | SAME | Same optional support boundary or exception behavior. |
| slice_neg10_none_neg1 | optional_slice_probe | DIFFERENT | SAME | Same optional support boundary or exception behavior. |
| slice_none_none_none | optional_slice_probe | DIFFERENT | SAME | Same optional support boundary or exception behavior. |
| zero_width_joiner_sequence | unicode_string | SAME | SAME | Same input and same marshal hash. |

### member_b_all_darwin_arm64_py3_12_results (Darwin/arm64, Python 3.12.10) vs member_b_all_windows_amd64_py3_10_results (Windows/AMD64, Python 3.10.11)

| Case | Category | Same marshal hash | Same exception | Interpretation |
| --- | --- | --- | --- | --- |
| ascii_plain | unicode_string | SAME | SAME | Same input and same marshal hash. |
| bytes_255_a | bytes_payload | SAME | SAME | Same input and same marshal hash. |
| bytes_256_a | bytes_payload | SAME | SAME | Same input and same marshal hash. |
| bytes_65535_a | bytes_payload | SAME | SAME | Same input and same marshal hash. |
| bytes_65536_a | bytes_payload | SAME | SAME | Same input and same marshal hash. |
| bytes_all_byte_values | bytes_payload | SAME | SAME | Same input and same marshal hash. |
| bytes_empty | bytes_payload | SAME | SAME | Same input and same marshal hash. |
| bytes_high_values_with_ascii | bytes_payload | SAME | SAME | Same input and same marshal hash. |
| bytes_single_nul | bytes_payload | SAME | SAME | Same input and same marshal hash. |
| chinese_text | unicode_string | SAME | SAME | Same input and same marshal hash. |
| complex_inf_neg_inf | float_complex | SAME | SAME | Same input and same marshal hash. |
| complex_nan_both | float_complex | SAME | SAME | Same input and same marshal hash. |
| complex_nan_imag | float_complex | SAME | SAME | Same input and same marshal hash. |
| complex_nan_real | float_complex | SAME | SAME | Same input and same marshal hash. |
| complex_payload_nan_imag | float_complex | SAME | SAME | Same input and same marshal hash. |
| complex_payload_nan_real | float_complex | SAME | SAME | Same input and same marshal hash. |
| complex_regular | float_complex | SAME | SAME | Same input and same marshal hash. |
| complex_zero_neg_zero | float_complex | SAME | SAME | Same input and same marshal hash. |
| composed_e_acute | unicode_string | DIFFERENT | SAME | Same input representation but Python major/minor differs; likely version-level marshal format difference. |
| constant_ellipsis | basic_scalar_constant | SAME | SAME | Same input and same marshal hash. |
| constant_false | basic_scalar_constant | SAME | SAME | Same input and same marshal hash. |
| constant_none | basic_scalar_constant | SAME | SAME | Same input and same marshal hash. |
| constant_true | basic_scalar_constant | SAME | SAME | Same input and same marshal hash. |
| crlf_string | unicode_string | SAME | SAME | Same input and same marshal hash. |
| decomposed_e_acute | unicode_string | SAME | SAME | Same input and same marshal hash. |
| emoji_text | unicode_string | SAME | SAME | Same input and same marshal hash. |
| float_huge_1e300 | float_complex | SAME | SAME | Same input and same marshal hash. |
| float_math_nan | float_complex | SAME | SAME | Same input and same marshal hash. |
| float_nan_constructor | float_complex | SAME | SAME | Same input and same marshal hash. |
| float_nan_payload_0x7ff0000000000001 | float_complex | SAME | SAME | Same input and same marshal hash. |
| float_nan_payload_0x7ff8000000000001 | float_complex | SAME | SAME | Same input and same marshal hash. |
| float_nan_payload_0x7ff8000000000002 | float_complex | SAME | SAME | Same input and same marshal hash. |
| float_neg_inf | float_complex | SAME | SAME | Same input and same marshal hash. |
| float_neg_one | float_complex | SAME | SAME | Same input and same marshal hash. |
| float_neg_zero | float_complex | SAME | SAME | Same input and same marshal hash. |
| float_pos_inf | float_complex | SAME | SAME | Same input and same marshal hash. |
| float_pos_one | float_complex | SAME | SAME | Same input and same marshal hash. |
| float_pos_zero | float_complex | SAME | SAME | Same input and same marshal hash. |
| float_tiny_1e_minus_300 | float_complex | SAME | SAME | Same input and same marshal hash. |
| lone_high_surrogate | unicode_string | SAME | SAME | Same input and same marshal hash. |
| non_bmp_character | unicode_string | SAME | SAME | Same input and same marshal hash. |
| nul_inside_string | unicode_string | SAME | SAME | Same input and same marshal hash. |
| recreated_complex_nan_both | float_complex | SAME | SAME | Same input and same marshal hash. |
| recreated_float_nan | float_complex | SAME | SAME | Same input and same marshal hash. |
| slice_1_10_2 | optional_slice_probe | DIFFERENT | SAME | Same optional support boundary or exception behavior. |
| slice_neg10_none_neg1 | optional_slice_probe | DIFFERENT | SAME | Same optional support boundary or exception behavior. |
| slice_none_none_none | optional_slice_probe | DIFFERENT | SAME | Same optional support boundary or exception behavior. |
| zero_width_joiner_sequence | unicode_string | SAME | SAME | Same input and same marshal hash. |

### member_b_all_darwin_arm64_py3_12_results (Darwin/arm64, Python 3.12.10) vs member_b_all_windows_amd64_py3_11_results (Windows/AMD64, Python 3.11.9)

| Case | Category | Same marshal hash | Same exception | Interpretation |
| --- | --- | --- | --- | --- |
| ascii_plain | unicode_string | SAME | SAME | Same input and same marshal hash. |
| bytes_255_a | bytes_payload | SAME | SAME | Same input and same marshal hash. |
| bytes_256_a | bytes_payload | SAME | SAME | Same input and same marshal hash. |
| bytes_65535_a | bytes_payload | SAME | SAME | Same input and same marshal hash. |
| bytes_65536_a | bytes_payload | SAME | SAME | Same input and same marshal hash. |
| bytes_all_byte_values | bytes_payload | SAME | SAME | Same input and same marshal hash. |
| bytes_empty | bytes_payload | SAME | SAME | Same input and same marshal hash. |
| bytes_high_values_with_ascii | bytes_payload | SAME | SAME | Same input and same marshal hash. |
| bytes_single_nul | bytes_payload | SAME | SAME | Same input and same marshal hash. |
| chinese_text | unicode_string | SAME | SAME | Same input and same marshal hash. |
| complex_inf_neg_inf | float_complex | SAME | SAME | Same input and same marshal hash. |
| complex_nan_both | float_complex | SAME | SAME | Same input and same marshal hash. |
| complex_nan_imag | float_complex | SAME | SAME | Same input and same marshal hash. |
| complex_nan_real | float_complex | SAME | SAME | Same input and same marshal hash. |
| complex_payload_nan_imag | float_complex | SAME | SAME | Same input and same marshal hash. |
| complex_payload_nan_real | float_complex | SAME | SAME | Same input and same marshal hash. |
| complex_regular | float_complex | SAME | SAME | Same input and same marshal hash. |
| complex_zero_neg_zero | float_complex | SAME | SAME | Same input and same marshal hash. |
| composed_e_acute | unicode_string | DIFFERENT | SAME | Same input representation but Python major/minor differs; likely version-level marshal format difference. |
| constant_ellipsis | basic_scalar_constant | SAME | SAME | Same input and same marshal hash. |
| constant_false | basic_scalar_constant | SAME | SAME | Same input and same marshal hash. |
| constant_none | basic_scalar_constant | SAME | SAME | Same input and same marshal hash. |
| constant_true | basic_scalar_constant | SAME | SAME | Same input and same marshal hash. |
| crlf_string | unicode_string | SAME | SAME | Same input and same marshal hash. |
| decomposed_e_acute | unicode_string | SAME | SAME | Same input and same marshal hash. |
| emoji_text | unicode_string | SAME | SAME | Same input and same marshal hash. |
| float_huge_1e300 | float_complex | SAME | SAME | Same input and same marshal hash. |
| float_math_nan | float_complex | SAME | SAME | Same input and same marshal hash. |
| float_nan_constructor | float_complex | SAME | SAME | Same input and same marshal hash. |
| float_nan_payload_0x7ff0000000000001 | float_complex | SAME | SAME | Same input and same marshal hash. |
| float_nan_payload_0x7ff8000000000001 | float_complex | SAME | SAME | Same input and same marshal hash. |
| float_nan_payload_0x7ff8000000000002 | float_complex | SAME | SAME | Same input and same marshal hash. |
| float_neg_inf | float_complex | SAME | SAME | Same input and same marshal hash. |
| float_neg_one | float_complex | SAME | SAME | Same input and same marshal hash. |
| float_neg_zero | float_complex | SAME | SAME | Same input and same marshal hash. |
| float_pos_inf | float_complex | SAME | SAME | Same input and same marshal hash. |
| float_pos_one | float_complex | SAME | SAME | Same input and same marshal hash. |
| float_pos_zero | float_complex | SAME | SAME | Same input and same marshal hash. |
| float_tiny_1e_minus_300 | float_complex | SAME | SAME | Same input and same marshal hash. |
| lone_high_surrogate | unicode_string | SAME | SAME | Same input and same marshal hash. |
| non_bmp_character | unicode_string | SAME | SAME | Same input and same marshal hash. |
| nul_inside_string | unicode_string | SAME | SAME | Same input and same marshal hash. |
| recreated_complex_nan_both | float_complex | SAME | SAME | Same input and same marshal hash. |
| recreated_float_nan | float_complex | SAME | SAME | Same input and same marshal hash. |
| slice_1_10_2 | optional_slice_probe | DIFFERENT | SAME | Same optional support boundary or exception behavior. |
| slice_neg10_none_neg1 | optional_slice_probe | DIFFERENT | SAME | Same optional support boundary or exception behavior. |
| slice_none_none_none | optional_slice_probe | DIFFERENT | SAME | Same optional support boundary or exception behavior. |
| zero_width_joiner_sequence | unicode_string | SAME | SAME | Same input and same marshal hash. |

### member_b_all_darwin_arm64_py3_12_results (Darwin/arm64, Python 3.12.10) vs member_b_all_windows_amd64_py3_12_results (Windows/AMD64, Python 3.12.10)

| Case | Category | Same marshal hash | Same exception | Interpretation |
| --- | --- | --- | --- | --- |
| ascii_plain | unicode_string | SAME | SAME | Same input and same marshal hash. |
| bytes_255_a | bytes_payload | SAME | SAME | Same input and same marshal hash. |
| bytes_256_a | bytes_payload | SAME | SAME | Same input and same marshal hash. |
| bytes_65535_a | bytes_payload | SAME | SAME | Same input and same marshal hash. |
| bytes_65536_a | bytes_payload | SAME | SAME | Same input and same marshal hash. |
| bytes_all_byte_values | bytes_payload | SAME | SAME | Same input and same marshal hash. |
| bytes_empty | bytes_payload | SAME | SAME | Same input and same marshal hash. |
| bytes_high_values_with_ascii | bytes_payload | SAME | SAME | Same input and same marshal hash. |
| bytes_single_nul | bytes_payload | SAME | SAME | Same input and same marshal hash. |
| chinese_text | unicode_string | SAME | SAME | Same input and same marshal hash. |
| complex_inf_neg_inf | float_complex | SAME | SAME | Same input and same marshal hash. |
| complex_nan_both | float_complex | SAME | SAME | Same input and same marshal hash. |
| complex_nan_imag | float_complex | SAME | SAME | Same input and same marshal hash. |
| complex_nan_real | float_complex | SAME | SAME | Same input and same marshal hash. |
| complex_payload_nan_imag | float_complex | SAME | SAME | Same input and same marshal hash. |
| complex_payload_nan_real | float_complex | SAME | SAME | Same input and same marshal hash. |
| complex_regular | float_complex | SAME | SAME | Same input and same marshal hash. |
| complex_zero_neg_zero | float_complex | SAME | SAME | Same input and same marshal hash. |
| composed_e_acute | unicode_string | SAME | SAME | Same input and same marshal hash. |
| constant_ellipsis | basic_scalar_constant | SAME | SAME | Same input and same marshal hash. |
| constant_false | basic_scalar_constant | SAME | SAME | Same input and same marshal hash. |
| constant_none | basic_scalar_constant | SAME | SAME | Same input and same marshal hash. |
| constant_true | basic_scalar_constant | SAME | SAME | Same input and same marshal hash. |
| crlf_string | unicode_string | SAME | SAME | Same input and same marshal hash. |
| decomposed_e_acute | unicode_string | SAME | SAME | Same input and same marshal hash. |
| emoji_text | unicode_string | SAME | SAME | Same input and same marshal hash. |
| float_huge_1e300 | float_complex | SAME | SAME | Same input and same marshal hash. |
| float_math_nan | float_complex | SAME | SAME | Same input and same marshal hash. |
| float_nan_constructor | float_complex | SAME | SAME | Same input and same marshal hash. |
| float_nan_payload_0x7ff0000000000001 | float_complex | SAME | SAME | Same input and same marshal hash. |
| float_nan_payload_0x7ff8000000000001 | float_complex | SAME | SAME | Same input and same marshal hash. |
| float_nan_payload_0x7ff8000000000002 | float_complex | SAME | SAME | Same input and same marshal hash. |
| float_neg_inf | float_complex | SAME | SAME | Same input and same marshal hash. |
| float_neg_one | float_complex | SAME | SAME | Same input and same marshal hash. |
| float_neg_zero | float_complex | SAME | SAME | Same input and same marshal hash. |
| float_pos_inf | float_complex | SAME | SAME | Same input and same marshal hash. |
| float_pos_one | float_complex | SAME | SAME | Same input and same marshal hash. |
| float_pos_zero | float_complex | SAME | SAME | Same input and same marshal hash. |
| float_tiny_1e_minus_300 | float_complex | SAME | SAME | Same input and same marshal hash. |
| lone_high_surrogate | unicode_string | SAME | SAME | Same input and same marshal hash. |
| non_bmp_character | unicode_string | SAME | SAME | Same input and same marshal hash. |
| nul_inside_string | unicode_string | SAME | SAME | Same input and same marshal hash. |
| recreated_complex_nan_both | float_complex | SAME | SAME | Same input and same marshal hash. |
| recreated_float_nan | float_complex | SAME | SAME | Same input and same marshal hash. |
| slice_1_10_2 | optional_slice_probe | DIFFERENT | SAME | Same optional support boundary or exception behavior. |
| slice_neg10_none_neg1 | optional_slice_probe | DIFFERENT | SAME | Same optional support boundary or exception behavior. |
| slice_none_none_none | optional_slice_probe | DIFFERENT | SAME | Same optional support boundary or exception behavior. |
| zero_width_joiner_sequence | unicode_string | SAME | SAME | Same input and same marshal hash. |

### member_b_all_darwin_arm64_py3_12_results (Darwin/arm64, Python 3.12.10) vs member_b_all_windows_amd64_py3_13_results (Windows/AMD64, Python 3.13.13)

| Case | Category | Same marshal hash | Same exception | Interpretation |
| --- | --- | --- | --- | --- |
| ascii_plain | unicode_string | SAME | SAME | Same input and same marshal hash. |
| bytes_255_a | bytes_payload | SAME | SAME | Same input and same marshal hash. |
| bytes_256_a | bytes_payload | SAME | SAME | Same input and same marshal hash. |
| bytes_65535_a | bytes_payload | SAME | SAME | Same input and same marshal hash. |
| bytes_65536_a | bytes_payload | SAME | SAME | Same input and same marshal hash. |
| bytes_all_byte_values | bytes_payload | SAME | SAME | Same input and same marshal hash. |
| bytes_empty | bytes_payload | SAME | SAME | Same input and same marshal hash. |
| bytes_high_values_with_ascii | bytes_payload | SAME | SAME | Same input and same marshal hash. |
| bytes_single_nul | bytes_payload | SAME | SAME | Same input and same marshal hash. |
| chinese_text | unicode_string | SAME | SAME | Same input and same marshal hash. |
| complex_inf_neg_inf | float_complex | SAME | SAME | Same input and same marshal hash. |
| complex_nan_both | float_complex | SAME | SAME | Same input and same marshal hash. |
| complex_nan_imag | float_complex | SAME | SAME | Same input and same marshal hash. |
| complex_nan_real | float_complex | SAME | SAME | Same input and same marshal hash. |
| complex_payload_nan_imag | float_complex | SAME | SAME | Same input and same marshal hash. |
| complex_payload_nan_real | float_complex | SAME | SAME | Same input and same marshal hash. |
| complex_regular | float_complex | SAME | SAME | Same input and same marshal hash. |
| complex_zero_neg_zero | float_complex | SAME | SAME | Same input and same marshal hash. |
| composed_e_acute | unicode_string | SAME | SAME | Same input and same marshal hash. |
| constant_ellipsis | basic_scalar_constant | SAME | SAME | Same input and same marshal hash. |
| constant_false | basic_scalar_constant | SAME | SAME | Same input and same marshal hash. |
| constant_none | basic_scalar_constant | SAME | SAME | Same input and same marshal hash. |
| constant_true | basic_scalar_constant | SAME | SAME | Same input and same marshal hash. |
| crlf_string | unicode_string | SAME | SAME | Same input and same marshal hash. |
| decomposed_e_acute | unicode_string | SAME | SAME | Same input and same marshal hash. |
| emoji_text | unicode_string | SAME | SAME | Same input and same marshal hash. |
| float_huge_1e300 | float_complex | SAME | SAME | Same input and same marshal hash. |
| float_math_nan | float_complex | SAME | SAME | Same input and same marshal hash. |
| float_nan_constructor | float_complex | SAME | SAME | Same input and same marshal hash. |
| float_nan_payload_0x7ff0000000000001 | float_complex | SAME | SAME | Same input and same marshal hash. |
| float_nan_payload_0x7ff8000000000001 | float_complex | SAME | SAME | Same input and same marshal hash. |
| float_nan_payload_0x7ff8000000000002 | float_complex | SAME | SAME | Same input and same marshal hash. |
| float_neg_inf | float_complex | SAME | SAME | Same input and same marshal hash. |
| float_neg_one | float_complex | SAME | SAME | Same input and same marshal hash. |
| float_neg_zero | float_complex | SAME | SAME | Same input and same marshal hash. |
| float_pos_inf | float_complex | SAME | SAME | Same input and same marshal hash. |
| float_pos_one | float_complex | SAME | SAME | Same input and same marshal hash. |
| float_pos_zero | float_complex | SAME | SAME | Same input and same marshal hash. |
| float_tiny_1e_minus_300 | float_complex | SAME | SAME | Same input and same marshal hash. |
| lone_high_surrogate | unicode_string | SAME | SAME | Same input and same marshal hash. |
| non_bmp_character | unicode_string | SAME | SAME | Same input and same marshal hash. |
| nul_inside_string | unicode_string | SAME | SAME | Same input and same marshal hash. |
| recreated_complex_nan_both | float_complex | SAME | SAME | Same input and same marshal hash. |
| recreated_float_nan | float_complex | SAME | SAME | Same input and same marshal hash. |
| slice_1_10_2 | optional_slice_probe | DIFFERENT | SAME | Same optional support boundary or exception behavior. |
| slice_neg10_none_neg1 | optional_slice_probe | DIFFERENT | SAME | Same optional support boundary or exception behavior. |
| slice_none_none_none | optional_slice_probe | DIFFERENT | SAME | Same optional support boundary or exception behavior. |
| zero_width_joiner_sequence | unicode_string | SAME | SAME | Same input and same marshal hash. |

### member_b_all_darwin_arm64_py3_12_results (Darwin/arm64, Python 3.12.10) vs member_b_all_windows_amd64_py3_9_results (Windows/AMD64, Python 3.9.13)

| Case | Category | Same marshal hash | Same exception | Interpretation |
| --- | --- | --- | --- | --- |
| ascii_plain | unicode_string | SAME | SAME | Same input and same marshal hash. |
| bytes_255_a | bytes_payload | SAME | SAME | Same input and same marshal hash. |
| bytes_256_a | bytes_payload | SAME | SAME | Same input and same marshal hash. |
| bytes_65535_a | bytes_payload | SAME | SAME | Same input and same marshal hash. |
| bytes_65536_a | bytes_payload | SAME | SAME | Same input and same marshal hash. |
| bytes_all_byte_values | bytes_payload | SAME | SAME | Same input and same marshal hash. |
| bytes_empty | bytes_payload | SAME | SAME | Same input and same marshal hash. |
| bytes_high_values_with_ascii | bytes_payload | SAME | SAME | Same input and same marshal hash. |
| bytes_single_nul | bytes_payload | SAME | SAME | Same input and same marshal hash. |
| chinese_text | unicode_string | SAME | SAME | Same input and same marshal hash. |
| complex_inf_neg_inf | float_complex | SAME | SAME | Same input and same marshal hash. |
| complex_nan_both | float_complex | SAME | SAME | Same input and same marshal hash. |
| complex_nan_imag | float_complex | SAME | SAME | Same input and same marshal hash. |
| complex_nan_real | float_complex | SAME | SAME | Same input and same marshal hash. |
| complex_payload_nan_imag | float_complex | SAME | SAME | Same input and same marshal hash. |
| complex_payload_nan_real | float_complex | SAME | SAME | Same input and same marshal hash. |
| complex_regular | float_complex | SAME | SAME | Same input and same marshal hash. |
| complex_zero_neg_zero | float_complex | SAME | SAME | Same input and same marshal hash. |
| composed_e_acute | unicode_string | DIFFERENT | SAME | Same input representation but Python major/minor differs; likely version-level marshal format difference. |
| constant_ellipsis | basic_scalar_constant | SAME | SAME | Same input and same marshal hash. |
| constant_false | basic_scalar_constant | SAME | SAME | Same input and same marshal hash. |
| constant_none | basic_scalar_constant | SAME | SAME | Same input and same marshal hash. |
| constant_true | basic_scalar_constant | SAME | SAME | Same input and same marshal hash. |
| crlf_string | unicode_string | SAME | SAME | Same input and same marshal hash. |
| decomposed_e_acute | unicode_string | SAME | SAME | Same input and same marshal hash. |
| emoji_text | unicode_string | SAME | SAME | Same input and same marshal hash. |
| float_huge_1e300 | float_complex | SAME | SAME | Same input and same marshal hash. |
| float_math_nan | float_complex | SAME | SAME | Same input and same marshal hash. |
| float_nan_constructor | float_complex | SAME | SAME | Same input and same marshal hash. |
| float_nan_payload_0x7ff0000000000001 | float_complex | SAME | SAME | Same input and same marshal hash. |
| float_nan_payload_0x7ff8000000000001 | float_complex | SAME | SAME | Same input and same marshal hash. |
| float_nan_payload_0x7ff8000000000002 | float_complex | SAME | SAME | Same input and same marshal hash. |
| float_neg_inf | float_complex | SAME | SAME | Same input and same marshal hash. |
| float_neg_one | float_complex | SAME | SAME | Same input and same marshal hash. |
| float_neg_zero | float_complex | SAME | SAME | Same input and same marshal hash. |
| float_pos_inf | float_complex | SAME | SAME | Same input and same marshal hash. |
| float_pos_one | float_complex | SAME | SAME | Same input and same marshal hash. |
| float_pos_zero | float_complex | SAME | SAME | Same input and same marshal hash. |
| float_tiny_1e_minus_300 | float_complex | SAME | SAME | Same input and same marshal hash. |
| lone_high_surrogate | unicode_string | SAME | SAME | Same input and same marshal hash. |
| non_bmp_character | unicode_string | SAME | SAME | Same input and same marshal hash. |
| nul_inside_string | unicode_string | SAME | SAME | Same input and same marshal hash. |
| recreated_complex_nan_both | float_complex | SAME | SAME | Same input and same marshal hash. |
| recreated_float_nan | float_complex | SAME | SAME | Same input and same marshal hash. |
| slice_1_10_2 | optional_slice_probe | DIFFERENT | SAME | Same optional support boundary or exception behavior. |
| slice_neg10_none_neg1 | optional_slice_probe | DIFFERENT | SAME | Same optional support boundary or exception behavior. |
| slice_none_none_none | optional_slice_probe | DIFFERENT | SAME | Same optional support boundary or exception behavior. |
| zero_width_joiner_sequence | unicode_string | SAME | SAME | Same input and same marshal hash. |

### member_b_all_darwin_arm64_py3_13_results (Darwin/arm64, Python 3.13.13) vs member_b_all_darwin_arm64_py3_9_results (Darwin/arm64, Python 3.9.6)

| Case | Category | Same marshal hash | Same exception | Interpretation |
| --- | --- | --- | --- | --- |
| ascii_plain | unicode_string | SAME | SAME | Same input and same marshal hash. |
| bytes_255_a | bytes_payload | SAME | SAME | Same input and same marshal hash. |
| bytes_256_a | bytes_payload | SAME | SAME | Same input and same marshal hash. |
| bytes_65535_a | bytes_payload | SAME | SAME | Same input and same marshal hash. |
| bytes_65536_a | bytes_payload | SAME | SAME | Same input and same marshal hash. |
| bytes_all_byte_values | bytes_payload | SAME | SAME | Same input and same marshal hash. |
| bytes_empty | bytes_payload | SAME | SAME | Same input and same marshal hash. |
| bytes_high_values_with_ascii | bytes_payload | SAME | SAME | Same input and same marshal hash. |
| bytes_single_nul | bytes_payload | SAME | SAME | Same input and same marshal hash. |
| chinese_text | unicode_string | SAME | SAME | Same input and same marshal hash. |
| complex_inf_neg_inf | float_complex | SAME | SAME | Same input and same marshal hash. |
| complex_nan_both | float_complex | SAME | SAME | Same input and same marshal hash. |
| complex_nan_imag | float_complex | SAME | SAME | Same input and same marshal hash. |
| complex_nan_real | float_complex | SAME | SAME | Same input and same marshal hash. |
| complex_payload_nan_imag | float_complex | SAME | SAME | Same input and same marshal hash. |
| complex_payload_nan_real | float_complex | SAME | SAME | Same input and same marshal hash. |
| complex_regular | float_complex | SAME | SAME | Same input and same marshal hash. |
| complex_zero_neg_zero | float_complex | SAME | SAME | Same input and same marshal hash. |
| composed_e_acute | unicode_string | DIFFERENT | SAME | Same input representation but Python major/minor differs; likely version-level marshal format difference. |
| constant_ellipsis | basic_scalar_constant | SAME | SAME | Same input and same marshal hash. |
| constant_false | basic_scalar_constant | SAME | SAME | Same input and same marshal hash. |
| constant_none | basic_scalar_constant | SAME | SAME | Same input and same marshal hash. |
| constant_true | basic_scalar_constant | SAME | SAME | Same input and same marshal hash. |
| crlf_string | unicode_string | SAME | SAME | Same input and same marshal hash. |
| decomposed_e_acute | unicode_string | SAME | SAME | Same input and same marshal hash. |
| emoji_text | unicode_string | SAME | SAME | Same input and same marshal hash. |
| float_huge_1e300 | float_complex | SAME | SAME | Same input and same marshal hash. |
| float_math_nan | float_complex | SAME | SAME | Same input and same marshal hash. |
| float_nan_constructor | float_complex | SAME | SAME | Same input and same marshal hash. |
| float_nan_payload_0x7ff0000000000001 | float_complex | SAME | SAME | Same input and same marshal hash. |
| float_nan_payload_0x7ff8000000000001 | float_complex | SAME | SAME | Same input and same marshal hash. |
| float_nan_payload_0x7ff8000000000002 | float_complex | SAME | SAME | Same input and same marshal hash. |
| float_neg_inf | float_complex | SAME | SAME | Same input and same marshal hash. |
| float_neg_one | float_complex | SAME | SAME | Same input and same marshal hash. |
| float_neg_zero | float_complex | SAME | SAME | Same input and same marshal hash. |
| float_pos_inf | float_complex | SAME | SAME | Same input and same marshal hash. |
| float_pos_one | float_complex | SAME | SAME | Same input and same marshal hash. |
| float_pos_zero | float_complex | SAME | SAME | Same input and same marshal hash. |
| float_tiny_1e_minus_300 | float_complex | SAME | SAME | Same input and same marshal hash. |
| lone_high_surrogate | unicode_string | SAME | SAME | Same input and same marshal hash. |
| non_bmp_character | unicode_string | SAME | SAME | Same input and same marshal hash. |
| nul_inside_string | unicode_string | SAME | SAME | Same input and same marshal hash. |
| recreated_complex_nan_both | float_complex | SAME | SAME | Same input and same marshal hash. |
| recreated_float_nan | float_complex | SAME | SAME | Same input and same marshal hash. |
| slice_1_10_2 | optional_slice_probe | DIFFERENT | SAME | Same optional support boundary or exception behavior. |
| slice_neg10_none_neg1 | optional_slice_probe | DIFFERENT | SAME | Same optional support boundary or exception behavior. |
| slice_none_none_none | optional_slice_probe | DIFFERENT | SAME | Same optional support boundary or exception behavior. |
| zero_width_joiner_sequence | unicode_string | SAME | SAME | Same input and same marshal hash. |

### member_b_all_darwin_arm64_py3_13_results (Darwin/arm64, Python 3.13.13) vs member_b_all_linux_x86_64_py3_10_results (Linux/x86_64, Python 3.10.20)

| Case | Category | Same marshal hash | Same exception | Interpretation |
| --- | --- | --- | --- | --- |
| ascii_plain | unicode_string | SAME | SAME | Same input and same marshal hash. |
| bytes_255_a | bytes_payload | SAME | SAME | Same input and same marshal hash. |
| bytes_256_a | bytes_payload | SAME | SAME | Same input and same marshal hash. |
| bytes_65535_a | bytes_payload | SAME | SAME | Same input and same marshal hash. |
| bytes_65536_a | bytes_payload | SAME | SAME | Same input and same marshal hash. |
| bytes_all_byte_values | bytes_payload | SAME | SAME | Same input and same marshal hash. |
| bytes_empty | bytes_payload | SAME | SAME | Same input and same marshal hash. |
| bytes_high_values_with_ascii | bytes_payload | SAME | SAME | Same input and same marshal hash. |
| bytes_single_nul | bytes_payload | SAME | SAME | Same input and same marshal hash. |
| chinese_text | unicode_string | SAME | SAME | Same input and same marshal hash. |
| complex_inf_neg_inf | float_complex | SAME | SAME | Same input and same marshal hash. |
| complex_nan_both | float_complex | SAME | SAME | Same input and same marshal hash. |
| complex_nan_imag | float_complex | SAME | SAME | Same input and same marshal hash. |
| complex_nan_real | float_complex | SAME | SAME | Same input and same marshal hash. |
| complex_payload_nan_imag | float_complex | SAME | SAME | Same input and same marshal hash. |
| complex_payload_nan_real | float_complex | SAME | SAME | Same input and same marshal hash. |
| complex_regular | float_complex | SAME | SAME | Same input and same marshal hash. |
| complex_zero_neg_zero | float_complex | SAME | SAME | Same input and same marshal hash. |
| composed_e_acute | unicode_string | DIFFERENT | SAME | Same input representation but Python major/minor differs; likely version-level marshal format difference. |
| constant_ellipsis | basic_scalar_constant | SAME | SAME | Same input and same marshal hash. |
| constant_false | basic_scalar_constant | SAME | SAME | Same input and same marshal hash. |
| constant_none | basic_scalar_constant | SAME | SAME | Same input and same marshal hash. |
| constant_true | basic_scalar_constant | SAME | SAME | Same input and same marshal hash. |
| crlf_string | unicode_string | SAME | SAME | Same input and same marshal hash. |
| decomposed_e_acute | unicode_string | SAME | SAME | Same input and same marshal hash. |
| emoji_text | unicode_string | SAME | SAME | Same input and same marshal hash. |
| float_huge_1e300 | float_complex | SAME | SAME | Same input and same marshal hash. |
| float_math_nan | float_complex | SAME | SAME | Same input and same marshal hash. |
| float_nan_constructor | float_complex | SAME | SAME | Same input and same marshal hash. |
| float_nan_payload_0x7ff0000000000001 | float_complex | SAME | SAME | Same input and same marshal hash. |
| float_nan_payload_0x7ff8000000000001 | float_complex | SAME | SAME | Same input and same marshal hash. |
| float_nan_payload_0x7ff8000000000002 | float_complex | SAME | SAME | Same input and same marshal hash. |
| float_neg_inf | float_complex | SAME | SAME | Same input and same marshal hash. |
| float_neg_one | float_complex | SAME | SAME | Same input and same marshal hash. |
| float_neg_zero | float_complex | SAME | SAME | Same input and same marshal hash. |
| float_pos_inf | float_complex | SAME | SAME | Same input and same marshal hash. |
| float_pos_one | float_complex | SAME | SAME | Same input and same marshal hash. |
| float_pos_zero | float_complex | SAME | SAME | Same input and same marshal hash. |
| float_tiny_1e_minus_300 | float_complex | SAME | SAME | Same input and same marshal hash. |
| lone_high_surrogate | unicode_string | SAME | SAME | Same input and same marshal hash. |
| non_bmp_character | unicode_string | SAME | SAME | Same input and same marshal hash. |
| nul_inside_string | unicode_string | SAME | SAME | Same input and same marshal hash. |
| recreated_complex_nan_both | float_complex | SAME | SAME | Same input and same marshal hash. |
| recreated_float_nan | float_complex | SAME | SAME | Same input and same marshal hash. |
| slice_1_10_2 | optional_slice_probe | DIFFERENT | SAME | Same optional support boundary or exception behavior. |
| slice_neg10_none_neg1 | optional_slice_probe | DIFFERENT | SAME | Same optional support boundary or exception behavior. |
| slice_none_none_none | optional_slice_probe | DIFFERENT | SAME | Same optional support boundary or exception behavior. |
| zero_width_joiner_sequence | unicode_string | SAME | SAME | Same input and same marshal hash. |

### member_b_all_darwin_arm64_py3_13_results (Darwin/arm64, Python 3.13.13) vs member_b_all_linux_x86_64_py3_11_results (Linux/x86_64, Python 3.11.15)

| Case | Category | Same marshal hash | Same exception | Interpretation |
| --- | --- | --- | --- | --- |
| ascii_plain | unicode_string | SAME | SAME | Same input and same marshal hash. |
| bytes_255_a | bytes_payload | SAME | SAME | Same input and same marshal hash. |
| bytes_256_a | bytes_payload | SAME | SAME | Same input and same marshal hash. |
| bytes_65535_a | bytes_payload | SAME | SAME | Same input and same marshal hash. |
| bytes_65536_a | bytes_payload | SAME | SAME | Same input and same marshal hash. |
| bytes_all_byte_values | bytes_payload | SAME | SAME | Same input and same marshal hash. |
| bytes_empty | bytes_payload | SAME | SAME | Same input and same marshal hash. |
| bytes_high_values_with_ascii | bytes_payload | SAME | SAME | Same input and same marshal hash. |
| bytes_single_nul | bytes_payload | SAME | SAME | Same input and same marshal hash. |
| chinese_text | unicode_string | SAME | SAME | Same input and same marshal hash. |
| complex_inf_neg_inf | float_complex | SAME | SAME | Same input and same marshal hash. |
| complex_nan_both | float_complex | SAME | SAME | Same input and same marshal hash. |
| complex_nan_imag | float_complex | SAME | SAME | Same input and same marshal hash. |
| complex_nan_real | float_complex | SAME | SAME | Same input and same marshal hash. |
| complex_payload_nan_imag | float_complex | SAME | SAME | Same input and same marshal hash. |
| complex_payload_nan_real | float_complex | SAME | SAME | Same input and same marshal hash. |
| complex_regular | float_complex | SAME | SAME | Same input and same marshal hash. |
| complex_zero_neg_zero | float_complex | SAME | SAME | Same input and same marshal hash. |
| composed_e_acute | unicode_string | DIFFERENT | SAME | Same input representation but Python major/minor differs; likely version-level marshal format difference. |
| constant_ellipsis | basic_scalar_constant | SAME | SAME | Same input and same marshal hash. |
| constant_false | basic_scalar_constant | SAME | SAME | Same input and same marshal hash. |
| constant_none | basic_scalar_constant | SAME | SAME | Same input and same marshal hash. |
| constant_true | basic_scalar_constant | SAME | SAME | Same input and same marshal hash. |
| crlf_string | unicode_string | SAME | SAME | Same input and same marshal hash. |
| decomposed_e_acute | unicode_string | SAME | SAME | Same input and same marshal hash. |
| emoji_text | unicode_string | SAME | SAME | Same input and same marshal hash. |
| float_huge_1e300 | float_complex | SAME | SAME | Same input and same marshal hash. |
| float_math_nan | float_complex | SAME | SAME | Same input and same marshal hash. |
| float_nan_constructor | float_complex | SAME | SAME | Same input and same marshal hash. |
| float_nan_payload_0x7ff0000000000001 | float_complex | SAME | SAME | Same input and same marshal hash. |
| float_nan_payload_0x7ff8000000000001 | float_complex | SAME | SAME | Same input and same marshal hash. |
| float_nan_payload_0x7ff8000000000002 | float_complex | SAME | SAME | Same input and same marshal hash. |
| float_neg_inf | float_complex | SAME | SAME | Same input and same marshal hash. |
| float_neg_one | float_complex | SAME | SAME | Same input and same marshal hash. |
| float_neg_zero | float_complex | SAME | SAME | Same input and same marshal hash. |
| float_pos_inf | float_complex | SAME | SAME | Same input and same marshal hash. |
| float_pos_one | float_complex | SAME | SAME | Same input and same marshal hash. |
| float_pos_zero | float_complex | SAME | SAME | Same input and same marshal hash. |
| float_tiny_1e_minus_300 | float_complex | SAME | SAME | Same input and same marshal hash. |
| lone_high_surrogate | unicode_string | SAME | SAME | Same input and same marshal hash. |
| non_bmp_character | unicode_string | SAME | SAME | Same input and same marshal hash. |
| nul_inside_string | unicode_string | SAME | SAME | Same input and same marshal hash. |
| recreated_complex_nan_both | float_complex | SAME | SAME | Same input and same marshal hash. |
| recreated_float_nan | float_complex | SAME | SAME | Same input and same marshal hash. |
| slice_1_10_2 | optional_slice_probe | DIFFERENT | SAME | Same optional support boundary or exception behavior. |
| slice_neg10_none_neg1 | optional_slice_probe | DIFFERENT | SAME | Same optional support boundary or exception behavior. |
| slice_none_none_none | optional_slice_probe | DIFFERENT | SAME | Same optional support boundary or exception behavior. |
| zero_width_joiner_sequence | unicode_string | SAME | SAME | Same input and same marshal hash. |

### member_b_all_darwin_arm64_py3_13_results (Darwin/arm64, Python 3.13.13) vs member_b_all_linux_x86_64_py3_12_results (Linux/x86_64, Python 3.12.13)

| Case | Category | Same marshal hash | Same exception | Interpretation |
| --- | --- | --- | --- | --- |
| ascii_plain | unicode_string | SAME | SAME | Same input and same marshal hash. |
| bytes_255_a | bytes_payload | SAME | SAME | Same input and same marshal hash. |
| bytes_256_a | bytes_payload | SAME | SAME | Same input and same marshal hash. |
| bytes_65535_a | bytes_payload | SAME | SAME | Same input and same marshal hash. |
| bytes_65536_a | bytes_payload | SAME | SAME | Same input and same marshal hash. |
| bytes_all_byte_values | bytes_payload | SAME | SAME | Same input and same marshal hash. |
| bytes_empty | bytes_payload | SAME | SAME | Same input and same marshal hash. |
| bytes_high_values_with_ascii | bytes_payload | SAME | SAME | Same input and same marshal hash. |
| bytes_single_nul | bytes_payload | SAME | SAME | Same input and same marshal hash. |
| chinese_text | unicode_string | SAME | SAME | Same input and same marshal hash. |
| complex_inf_neg_inf | float_complex | SAME | SAME | Same input and same marshal hash. |
| complex_nan_both | float_complex | SAME | SAME | Same input and same marshal hash. |
| complex_nan_imag | float_complex | SAME | SAME | Same input and same marshal hash. |
| complex_nan_real | float_complex | SAME | SAME | Same input and same marshal hash. |
| complex_payload_nan_imag | float_complex | SAME | SAME | Same input and same marshal hash. |
| complex_payload_nan_real | float_complex | SAME | SAME | Same input and same marshal hash. |
| complex_regular | float_complex | SAME | SAME | Same input and same marshal hash. |
| complex_zero_neg_zero | float_complex | SAME | SAME | Same input and same marshal hash. |
| composed_e_acute | unicode_string | SAME | SAME | Same input and same marshal hash. |
| constant_ellipsis | basic_scalar_constant | SAME | SAME | Same input and same marshal hash. |
| constant_false | basic_scalar_constant | SAME | SAME | Same input and same marshal hash. |
| constant_none | basic_scalar_constant | SAME | SAME | Same input and same marshal hash. |
| constant_true | basic_scalar_constant | SAME | SAME | Same input and same marshal hash. |
| crlf_string | unicode_string | SAME | SAME | Same input and same marshal hash. |
| decomposed_e_acute | unicode_string | SAME | SAME | Same input and same marshal hash. |
| emoji_text | unicode_string | SAME | SAME | Same input and same marshal hash. |
| float_huge_1e300 | float_complex | SAME | SAME | Same input and same marshal hash. |
| float_math_nan | float_complex | SAME | SAME | Same input and same marshal hash. |
| float_nan_constructor | float_complex | SAME | SAME | Same input and same marshal hash. |
| float_nan_payload_0x7ff0000000000001 | float_complex | SAME | SAME | Same input and same marshal hash. |
| float_nan_payload_0x7ff8000000000001 | float_complex | SAME | SAME | Same input and same marshal hash. |
| float_nan_payload_0x7ff8000000000002 | float_complex | SAME | SAME | Same input and same marshal hash. |
| float_neg_inf | float_complex | SAME | SAME | Same input and same marshal hash. |
| float_neg_one | float_complex | SAME | SAME | Same input and same marshal hash. |
| float_neg_zero | float_complex | SAME | SAME | Same input and same marshal hash. |
| float_pos_inf | float_complex | SAME | SAME | Same input and same marshal hash. |
| float_pos_one | float_complex | SAME | SAME | Same input and same marshal hash. |
| float_pos_zero | float_complex | SAME | SAME | Same input and same marshal hash. |
| float_tiny_1e_minus_300 | float_complex | SAME | SAME | Same input and same marshal hash. |
| lone_high_surrogate | unicode_string | SAME | SAME | Same input and same marshal hash. |
| non_bmp_character | unicode_string | SAME | SAME | Same input and same marshal hash. |
| nul_inside_string | unicode_string | SAME | SAME | Same input and same marshal hash. |
| recreated_complex_nan_both | float_complex | SAME | SAME | Same input and same marshal hash. |
| recreated_float_nan | float_complex | SAME | SAME | Same input and same marshal hash. |
| slice_1_10_2 | optional_slice_probe | DIFFERENT | SAME | Same optional support boundary or exception behavior. |
| slice_neg10_none_neg1 | optional_slice_probe | DIFFERENT | SAME | Same optional support boundary or exception behavior. |
| slice_none_none_none | optional_slice_probe | DIFFERENT | SAME | Same optional support boundary or exception behavior. |
| zero_width_joiner_sequence | unicode_string | SAME | SAME | Same input and same marshal hash. |

### member_b_all_darwin_arm64_py3_13_results (Darwin/arm64, Python 3.13.13) vs member_b_all_linux_x86_64_py3_13_results (Linux/x86_64, Python 3.13.13)

| Case | Category | Same marshal hash | Same exception | Interpretation |
| --- | --- | --- | --- | --- |
| ascii_plain | unicode_string | SAME | SAME | Same input and same marshal hash. |
| bytes_255_a | bytes_payload | SAME | SAME | Same input and same marshal hash. |
| bytes_256_a | bytes_payload | SAME | SAME | Same input and same marshal hash. |
| bytes_65535_a | bytes_payload | SAME | SAME | Same input and same marshal hash. |
| bytes_65536_a | bytes_payload | SAME | SAME | Same input and same marshal hash. |
| bytes_all_byte_values | bytes_payload | SAME | SAME | Same input and same marshal hash. |
| bytes_empty | bytes_payload | SAME | SAME | Same input and same marshal hash. |
| bytes_high_values_with_ascii | bytes_payload | SAME | SAME | Same input and same marshal hash. |
| bytes_single_nul | bytes_payload | SAME | SAME | Same input and same marshal hash. |
| chinese_text | unicode_string | SAME | SAME | Same input and same marshal hash. |
| complex_inf_neg_inf | float_complex | SAME | SAME | Same input and same marshal hash. |
| complex_nan_both | float_complex | SAME | SAME | Same input and same marshal hash. |
| complex_nan_imag | float_complex | SAME | SAME | Same input and same marshal hash. |
| complex_nan_real | float_complex | SAME | SAME | Same input and same marshal hash. |
| complex_payload_nan_imag | float_complex | SAME | SAME | Same input and same marshal hash. |
| complex_payload_nan_real | float_complex | SAME | SAME | Same input and same marshal hash. |
| complex_regular | float_complex | SAME | SAME | Same input and same marshal hash. |
| complex_zero_neg_zero | float_complex | SAME | SAME | Same input and same marshal hash. |
| composed_e_acute | unicode_string | SAME | SAME | Same input and same marshal hash. |
| constant_ellipsis | basic_scalar_constant | SAME | SAME | Same input and same marshal hash. |
| constant_false | basic_scalar_constant | SAME | SAME | Same input and same marshal hash. |
| constant_none | basic_scalar_constant | SAME | SAME | Same input and same marshal hash. |
| constant_true | basic_scalar_constant | SAME | SAME | Same input and same marshal hash. |
| crlf_string | unicode_string | SAME | SAME | Same input and same marshal hash. |
| decomposed_e_acute | unicode_string | SAME | SAME | Same input and same marshal hash. |
| emoji_text | unicode_string | SAME | SAME | Same input and same marshal hash. |
| float_huge_1e300 | float_complex | SAME | SAME | Same input and same marshal hash. |
| float_math_nan | float_complex | SAME | SAME | Same input and same marshal hash. |
| float_nan_constructor | float_complex | SAME | SAME | Same input and same marshal hash. |
| float_nan_payload_0x7ff0000000000001 | float_complex | SAME | SAME | Same input and same marshal hash. |
| float_nan_payload_0x7ff8000000000001 | float_complex | SAME | SAME | Same input and same marshal hash. |
| float_nan_payload_0x7ff8000000000002 | float_complex | SAME | SAME | Same input and same marshal hash. |
| float_neg_inf | float_complex | SAME | SAME | Same input and same marshal hash. |
| float_neg_one | float_complex | SAME | SAME | Same input and same marshal hash. |
| float_neg_zero | float_complex | SAME | SAME | Same input and same marshal hash. |
| float_pos_inf | float_complex | SAME | SAME | Same input and same marshal hash. |
| float_pos_one | float_complex | SAME | SAME | Same input and same marshal hash. |
| float_pos_zero | float_complex | SAME | SAME | Same input and same marshal hash. |
| float_tiny_1e_minus_300 | float_complex | SAME | SAME | Same input and same marshal hash. |
| lone_high_surrogate | unicode_string | SAME | SAME | Same input and same marshal hash. |
| non_bmp_character | unicode_string | SAME | SAME | Same input and same marshal hash. |
| nul_inside_string | unicode_string | SAME | SAME | Same input and same marshal hash. |
| recreated_complex_nan_both | float_complex | SAME | SAME | Same input and same marshal hash. |
| recreated_float_nan | float_complex | SAME | SAME | Same input and same marshal hash. |
| slice_1_10_2 | optional_slice_probe | DIFFERENT | SAME | Same optional support boundary or exception behavior. |
| slice_neg10_none_neg1 | optional_slice_probe | DIFFERENT | SAME | Same optional support boundary or exception behavior. |
| slice_none_none_none | optional_slice_probe | DIFFERENT | SAME | Same optional support boundary or exception behavior. |
| zero_width_joiner_sequence | unicode_string | SAME | SAME | Same input and same marshal hash. |

### member_b_all_darwin_arm64_py3_13_results (Darwin/arm64, Python 3.13.13) vs member_b_all_linux_x86_64_py3_9_results (Linux/x86_64, Python 3.9.25)

| Case | Category | Same marshal hash | Same exception | Interpretation |
| --- | --- | --- | --- | --- |
| ascii_plain | unicode_string | SAME | SAME | Same input and same marshal hash. |
| bytes_255_a | bytes_payload | SAME | SAME | Same input and same marshal hash. |
| bytes_256_a | bytes_payload | SAME | SAME | Same input and same marshal hash. |
| bytes_65535_a | bytes_payload | SAME | SAME | Same input and same marshal hash. |
| bytes_65536_a | bytes_payload | SAME | SAME | Same input and same marshal hash. |
| bytes_all_byte_values | bytes_payload | SAME | SAME | Same input and same marshal hash. |
| bytes_empty | bytes_payload | SAME | SAME | Same input and same marshal hash. |
| bytes_high_values_with_ascii | bytes_payload | SAME | SAME | Same input and same marshal hash. |
| bytes_single_nul | bytes_payload | SAME | SAME | Same input and same marshal hash. |
| chinese_text | unicode_string | SAME | SAME | Same input and same marshal hash. |
| complex_inf_neg_inf | float_complex | SAME | SAME | Same input and same marshal hash. |
| complex_nan_both | float_complex | SAME | SAME | Same input and same marshal hash. |
| complex_nan_imag | float_complex | SAME | SAME | Same input and same marshal hash. |
| complex_nan_real | float_complex | SAME | SAME | Same input and same marshal hash. |
| complex_payload_nan_imag | float_complex | SAME | SAME | Same input and same marshal hash. |
| complex_payload_nan_real | float_complex | SAME | SAME | Same input and same marshal hash. |
| complex_regular | float_complex | SAME | SAME | Same input and same marshal hash. |
| complex_zero_neg_zero | float_complex | SAME | SAME | Same input and same marshal hash. |
| composed_e_acute | unicode_string | DIFFERENT | SAME | Same input representation but Python major/minor differs; likely version-level marshal format difference. |
| constant_ellipsis | basic_scalar_constant | SAME | SAME | Same input and same marshal hash. |
| constant_false | basic_scalar_constant | SAME | SAME | Same input and same marshal hash. |
| constant_none | basic_scalar_constant | SAME | SAME | Same input and same marshal hash. |
| constant_true | basic_scalar_constant | SAME | SAME | Same input and same marshal hash. |
| crlf_string | unicode_string | SAME | SAME | Same input and same marshal hash. |
| decomposed_e_acute | unicode_string | SAME | SAME | Same input and same marshal hash. |
| emoji_text | unicode_string | SAME | SAME | Same input and same marshal hash. |
| float_huge_1e300 | float_complex | SAME | SAME | Same input and same marshal hash. |
| float_math_nan | float_complex | SAME | SAME | Same input and same marshal hash. |
| float_nan_constructor | float_complex | SAME | SAME | Same input and same marshal hash. |
| float_nan_payload_0x7ff0000000000001 | float_complex | SAME | SAME | Same input and same marshal hash. |
| float_nan_payload_0x7ff8000000000001 | float_complex | SAME | SAME | Same input and same marshal hash. |
| float_nan_payload_0x7ff8000000000002 | float_complex | SAME | SAME | Same input and same marshal hash. |
| float_neg_inf | float_complex | SAME | SAME | Same input and same marshal hash. |
| float_neg_one | float_complex | SAME | SAME | Same input and same marshal hash. |
| float_neg_zero | float_complex | SAME | SAME | Same input and same marshal hash. |
| float_pos_inf | float_complex | SAME | SAME | Same input and same marshal hash. |
| float_pos_one | float_complex | SAME | SAME | Same input and same marshal hash. |
| float_pos_zero | float_complex | SAME | SAME | Same input and same marshal hash. |
| float_tiny_1e_minus_300 | float_complex | SAME | SAME | Same input and same marshal hash. |
| lone_high_surrogate | unicode_string | SAME | SAME | Same input and same marshal hash. |
| non_bmp_character | unicode_string | SAME | SAME | Same input and same marshal hash. |
| nul_inside_string | unicode_string | SAME | SAME | Same input and same marshal hash. |
| recreated_complex_nan_both | float_complex | SAME | SAME | Same input and same marshal hash. |
| recreated_float_nan | float_complex | SAME | SAME | Same input and same marshal hash. |
| slice_1_10_2 | optional_slice_probe | DIFFERENT | SAME | Same optional support boundary or exception behavior. |
| slice_neg10_none_neg1 | optional_slice_probe | DIFFERENT | SAME | Same optional support boundary or exception behavior. |
| slice_none_none_none | optional_slice_probe | DIFFERENT | SAME | Same optional support boundary or exception behavior. |
| zero_width_joiner_sequence | unicode_string | SAME | SAME | Same input and same marshal hash. |

### member_b_all_darwin_arm64_py3_13_results (Darwin/arm64, Python 3.13.13) vs member_b_all_windows_amd64_py3_10_results (Windows/AMD64, Python 3.10.11)

| Case | Category | Same marshal hash | Same exception | Interpretation |
| --- | --- | --- | --- | --- |
| ascii_plain | unicode_string | SAME | SAME | Same input and same marshal hash. |
| bytes_255_a | bytes_payload | SAME | SAME | Same input and same marshal hash. |
| bytes_256_a | bytes_payload | SAME | SAME | Same input and same marshal hash. |
| bytes_65535_a | bytes_payload | SAME | SAME | Same input and same marshal hash. |
| bytes_65536_a | bytes_payload | SAME | SAME | Same input and same marshal hash. |
| bytes_all_byte_values | bytes_payload | SAME | SAME | Same input and same marshal hash. |
| bytes_empty | bytes_payload | SAME | SAME | Same input and same marshal hash. |
| bytes_high_values_with_ascii | bytes_payload | SAME | SAME | Same input and same marshal hash. |
| bytes_single_nul | bytes_payload | SAME | SAME | Same input and same marshal hash. |
| chinese_text | unicode_string | SAME | SAME | Same input and same marshal hash. |
| complex_inf_neg_inf | float_complex | SAME | SAME | Same input and same marshal hash. |
| complex_nan_both | float_complex | SAME | SAME | Same input and same marshal hash. |
| complex_nan_imag | float_complex | SAME | SAME | Same input and same marshal hash. |
| complex_nan_real | float_complex | SAME | SAME | Same input and same marshal hash. |
| complex_payload_nan_imag | float_complex | SAME | SAME | Same input and same marshal hash. |
| complex_payload_nan_real | float_complex | SAME | SAME | Same input and same marshal hash. |
| complex_regular | float_complex | SAME | SAME | Same input and same marshal hash. |
| complex_zero_neg_zero | float_complex | SAME | SAME | Same input and same marshal hash. |
| composed_e_acute | unicode_string | DIFFERENT | SAME | Same input representation but Python major/minor differs; likely version-level marshal format difference. |
| constant_ellipsis | basic_scalar_constant | SAME | SAME | Same input and same marshal hash. |
| constant_false | basic_scalar_constant | SAME | SAME | Same input and same marshal hash. |
| constant_none | basic_scalar_constant | SAME | SAME | Same input and same marshal hash. |
| constant_true | basic_scalar_constant | SAME | SAME | Same input and same marshal hash. |
| crlf_string | unicode_string | SAME | SAME | Same input and same marshal hash. |
| decomposed_e_acute | unicode_string | SAME | SAME | Same input and same marshal hash. |
| emoji_text | unicode_string | SAME | SAME | Same input and same marshal hash. |
| float_huge_1e300 | float_complex | SAME | SAME | Same input and same marshal hash. |
| float_math_nan | float_complex | SAME | SAME | Same input and same marshal hash. |
| float_nan_constructor | float_complex | SAME | SAME | Same input and same marshal hash. |
| float_nan_payload_0x7ff0000000000001 | float_complex | SAME | SAME | Same input and same marshal hash. |
| float_nan_payload_0x7ff8000000000001 | float_complex | SAME | SAME | Same input and same marshal hash. |
| float_nan_payload_0x7ff8000000000002 | float_complex | SAME | SAME | Same input and same marshal hash. |
| float_neg_inf | float_complex | SAME | SAME | Same input and same marshal hash. |
| float_neg_one | float_complex | SAME | SAME | Same input and same marshal hash. |
| float_neg_zero | float_complex | SAME | SAME | Same input and same marshal hash. |
| float_pos_inf | float_complex | SAME | SAME | Same input and same marshal hash. |
| float_pos_one | float_complex | SAME | SAME | Same input and same marshal hash. |
| float_pos_zero | float_complex | SAME | SAME | Same input and same marshal hash. |
| float_tiny_1e_minus_300 | float_complex | SAME | SAME | Same input and same marshal hash. |
| lone_high_surrogate | unicode_string | SAME | SAME | Same input and same marshal hash. |
| non_bmp_character | unicode_string | SAME | SAME | Same input and same marshal hash. |
| nul_inside_string | unicode_string | SAME | SAME | Same input and same marshal hash. |
| recreated_complex_nan_both | float_complex | SAME | SAME | Same input and same marshal hash. |
| recreated_float_nan | float_complex | SAME | SAME | Same input and same marshal hash. |
| slice_1_10_2 | optional_slice_probe | DIFFERENT | SAME | Same optional support boundary or exception behavior. |
| slice_neg10_none_neg1 | optional_slice_probe | DIFFERENT | SAME | Same optional support boundary or exception behavior. |
| slice_none_none_none | optional_slice_probe | DIFFERENT | SAME | Same optional support boundary or exception behavior. |
| zero_width_joiner_sequence | unicode_string | SAME | SAME | Same input and same marshal hash. |

### member_b_all_darwin_arm64_py3_13_results (Darwin/arm64, Python 3.13.13) vs member_b_all_windows_amd64_py3_11_results (Windows/AMD64, Python 3.11.9)

| Case | Category | Same marshal hash | Same exception | Interpretation |
| --- | --- | --- | --- | --- |
| ascii_plain | unicode_string | SAME | SAME | Same input and same marshal hash. |
| bytes_255_a | bytes_payload | SAME | SAME | Same input and same marshal hash. |
| bytes_256_a | bytes_payload | SAME | SAME | Same input and same marshal hash. |
| bytes_65535_a | bytes_payload | SAME | SAME | Same input and same marshal hash. |
| bytes_65536_a | bytes_payload | SAME | SAME | Same input and same marshal hash. |
| bytes_all_byte_values | bytes_payload | SAME | SAME | Same input and same marshal hash. |
| bytes_empty | bytes_payload | SAME | SAME | Same input and same marshal hash. |
| bytes_high_values_with_ascii | bytes_payload | SAME | SAME | Same input and same marshal hash. |
| bytes_single_nul | bytes_payload | SAME | SAME | Same input and same marshal hash. |
| chinese_text | unicode_string | SAME | SAME | Same input and same marshal hash. |
| complex_inf_neg_inf | float_complex | SAME | SAME | Same input and same marshal hash. |
| complex_nan_both | float_complex | SAME | SAME | Same input and same marshal hash. |
| complex_nan_imag | float_complex | SAME | SAME | Same input and same marshal hash. |
| complex_nan_real | float_complex | SAME | SAME | Same input and same marshal hash. |
| complex_payload_nan_imag | float_complex | SAME | SAME | Same input and same marshal hash. |
| complex_payload_nan_real | float_complex | SAME | SAME | Same input and same marshal hash. |
| complex_regular | float_complex | SAME | SAME | Same input and same marshal hash. |
| complex_zero_neg_zero | float_complex | SAME | SAME | Same input and same marshal hash. |
| composed_e_acute | unicode_string | DIFFERENT | SAME | Same input representation but Python major/minor differs; likely version-level marshal format difference. |
| constant_ellipsis | basic_scalar_constant | SAME | SAME | Same input and same marshal hash. |
| constant_false | basic_scalar_constant | SAME | SAME | Same input and same marshal hash. |
| constant_none | basic_scalar_constant | SAME | SAME | Same input and same marshal hash. |
| constant_true | basic_scalar_constant | SAME | SAME | Same input and same marshal hash. |
| crlf_string | unicode_string | SAME | SAME | Same input and same marshal hash. |
| decomposed_e_acute | unicode_string | SAME | SAME | Same input and same marshal hash. |
| emoji_text | unicode_string | SAME | SAME | Same input and same marshal hash. |
| float_huge_1e300 | float_complex | SAME | SAME | Same input and same marshal hash. |
| float_math_nan | float_complex | SAME | SAME | Same input and same marshal hash. |
| float_nan_constructor | float_complex | SAME | SAME | Same input and same marshal hash. |
| float_nan_payload_0x7ff0000000000001 | float_complex | SAME | SAME | Same input and same marshal hash. |
| float_nan_payload_0x7ff8000000000001 | float_complex | SAME | SAME | Same input and same marshal hash. |
| float_nan_payload_0x7ff8000000000002 | float_complex | SAME | SAME | Same input and same marshal hash. |
| float_neg_inf | float_complex | SAME | SAME | Same input and same marshal hash. |
| float_neg_one | float_complex | SAME | SAME | Same input and same marshal hash. |
| float_neg_zero | float_complex | SAME | SAME | Same input and same marshal hash. |
| float_pos_inf | float_complex | SAME | SAME | Same input and same marshal hash. |
| float_pos_one | float_complex | SAME | SAME | Same input and same marshal hash. |
| float_pos_zero | float_complex | SAME | SAME | Same input and same marshal hash. |
| float_tiny_1e_minus_300 | float_complex | SAME | SAME | Same input and same marshal hash. |
| lone_high_surrogate | unicode_string | SAME | SAME | Same input and same marshal hash. |
| non_bmp_character | unicode_string | SAME | SAME | Same input and same marshal hash. |
| nul_inside_string | unicode_string | SAME | SAME | Same input and same marshal hash. |
| recreated_complex_nan_both | float_complex | SAME | SAME | Same input and same marshal hash. |
| recreated_float_nan | float_complex | SAME | SAME | Same input and same marshal hash. |
| slice_1_10_2 | optional_slice_probe | DIFFERENT | SAME | Same optional support boundary or exception behavior. |
| slice_neg10_none_neg1 | optional_slice_probe | DIFFERENT | SAME | Same optional support boundary or exception behavior. |
| slice_none_none_none | optional_slice_probe | DIFFERENT | SAME | Same optional support boundary or exception behavior. |
| zero_width_joiner_sequence | unicode_string | SAME | SAME | Same input and same marshal hash. |

### member_b_all_darwin_arm64_py3_13_results (Darwin/arm64, Python 3.13.13) vs member_b_all_windows_amd64_py3_12_results (Windows/AMD64, Python 3.12.10)

| Case | Category | Same marshal hash | Same exception | Interpretation |
| --- | --- | --- | --- | --- |
| ascii_plain | unicode_string | SAME | SAME | Same input and same marshal hash. |
| bytes_255_a | bytes_payload | SAME | SAME | Same input and same marshal hash. |
| bytes_256_a | bytes_payload | SAME | SAME | Same input and same marshal hash. |
| bytes_65535_a | bytes_payload | SAME | SAME | Same input and same marshal hash. |
| bytes_65536_a | bytes_payload | SAME | SAME | Same input and same marshal hash. |
| bytes_all_byte_values | bytes_payload | SAME | SAME | Same input and same marshal hash. |
| bytes_empty | bytes_payload | SAME | SAME | Same input and same marshal hash. |
| bytes_high_values_with_ascii | bytes_payload | SAME | SAME | Same input and same marshal hash. |
| bytes_single_nul | bytes_payload | SAME | SAME | Same input and same marshal hash. |
| chinese_text | unicode_string | SAME | SAME | Same input and same marshal hash. |
| complex_inf_neg_inf | float_complex | SAME | SAME | Same input and same marshal hash. |
| complex_nan_both | float_complex | SAME | SAME | Same input and same marshal hash. |
| complex_nan_imag | float_complex | SAME | SAME | Same input and same marshal hash. |
| complex_nan_real | float_complex | SAME | SAME | Same input and same marshal hash. |
| complex_payload_nan_imag | float_complex | SAME | SAME | Same input and same marshal hash. |
| complex_payload_nan_real | float_complex | SAME | SAME | Same input and same marshal hash. |
| complex_regular | float_complex | SAME | SAME | Same input and same marshal hash. |
| complex_zero_neg_zero | float_complex | SAME | SAME | Same input and same marshal hash. |
| composed_e_acute | unicode_string | SAME | SAME | Same input and same marshal hash. |
| constant_ellipsis | basic_scalar_constant | SAME | SAME | Same input and same marshal hash. |
| constant_false | basic_scalar_constant | SAME | SAME | Same input and same marshal hash. |
| constant_none | basic_scalar_constant | SAME | SAME | Same input and same marshal hash. |
| constant_true | basic_scalar_constant | SAME | SAME | Same input and same marshal hash. |
| crlf_string | unicode_string | SAME | SAME | Same input and same marshal hash. |
| decomposed_e_acute | unicode_string | SAME | SAME | Same input and same marshal hash. |
| emoji_text | unicode_string | SAME | SAME | Same input and same marshal hash. |
| float_huge_1e300 | float_complex | SAME | SAME | Same input and same marshal hash. |
| float_math_nan | float_complex | SAME | SAME | Same input and same marshal hash. |
| float_nan_constructor | float_complex | SAME | SAME | Same input and same marshal hash. |
| float_nan_payload_0x7ff0000000000001 | float_complex | SAME | SAME | Same input and same marshal hash. |
| float_nan_payload_0x7ff8000000000001 | float_complex | SAME | SAME | Same input and same marshal hash. |
| float_nan_payload_0x7ff8000000000002 | float_complex | SAME | SAME | Same input and same marshal hash. |
| float_neg_inf | float_complex | SAME | SAME | Same input and same marshal hash. |
| float_neg_one | float_complex | SAME | SAME | Same input and same marshal hash. |
| float_neg_zero | float_complex | SAME | SAME | Same input and same marshal hash. |
| float_pos_inf | float_complex | SAME | SAME | Same input and same marshal hash. |
| float_pos_one | float_complex | SAME | SAME | Same input and same marshal hash. |
| float_pos_zero | float_complex | SAME | SAME | Same input and same marshal hash. |
| float_tiny_1e_minus_300 | float_complex | SAME | SAME | Same input and same marshal hash. |
| lone_high_surrogate | unicode_string | SAME | SAME | Same input and same marshal hash. |
| non_bmp_character | unicode_string | SAME | SAME | Same input and same marshal hash. |
| nul_inside_string | unicode_string | SAME | SAME | Same input and same marshal hash. |
| recreated_complex_nan_both | float_complex | SAME | SAME | Same input and same marshal hash. |
| recreated_float_nan | float_complex | SAME | SAME | Same input and same marshal hash. |
| slice_1_10_2 | optional_slice_probe | DIFFERENT | SAME | Same optional support boundary or exception behavior. |
| slice_neg10_none_neg1 | optional_slice_probe | DIFFERENT | SAME | Same optional support boundary or exception behavior. |
| slice_none_none_none | optional_slice_probe | DIFFERENT | SAME | Same optional support boundary or exception behavior. |
| zero_width_joiner_sequence | unicode_string | SAME | SAME | Same input and same marshal hash. |

### member_b_all_darwin_arm64_py3_13_results (Darwin/arm64, Python 3.13.13) vs member_b_all_windows_amd64_py3_13_results (Windows/AMD64, Python 3.13.13)

| Case | Category | Same marshal hash | Same exception | Interpretation |
| --- | --- | --- | --- | --- |
| ascii_plain | unicode_string | SAME | SAME | Same input and same marshal hash. |
| bytes_255_a | bytes_payload | SAME | SAME | Same input and same marshal hash. |
| bytes_256_a | bytes_payload | SAME | SAME | Same input and same marshal hash. |
| bytes_65535_a | bytes_payload | SAME | SAME | Same input and same marshal hash. |
| bytes_65536_a | bytes_payload | SAME | SAME | Same input and same marshal hash. |
| bytes_all_byte_values | bytes_payload | SAME | SAME | Same input and same marshal hash. |
| bytes_empty | bytes_payload | SAME | SAME | Same input and same marshal hash. |
| bytes_high_values_with_ascii | bytes_payload | SAME | SAME | Same input and same marshal hash. |
| bytes_single_nul | bytes_payload | SAME | SAME | Same input and same marshal hash. |
| chinese_text | unicode_string | SAME | SAME | Same input and same marshal hash. |
| complex_inf_neg_inf | float_complex | SAME | SAME | Same input and same marshal hash. |
| complex_nan_both | float_complex | SAME | SAME | Same input and same marshal hash. |
| complex_nan_imag | float_complex | SAME | SAME | Same input and same marshal hash. |
| complex_nan_real | float_complex | SAME | SAME | Same input and same marshal hash. |
| complex_payload_nan_imag | float_complex | SAME | SAME | Same input and same marshal hash. |
| complex_payload_nan_real | float_complex | SAME | SAME | Same input and same marshal hash. |
| complex_regular | float_complex | SAME | SAME | Same input and same marshal hash. |
| complex_zero_neg_zero | float_complex | SAME | SAME | Same input and same marshal hash. |
| composed_e_acute | unicode_string | SAME | SAME | Same input and same marshal hash. |
| constant_ellipsis | basic_scalar_constant | SAME | SAME | Same input and same marshal hash. |
| constant_false | basic_scalar_constant | SAME | SAME | Same input and same marshal hash. |
| constant_none | basic_scalar_constant | SAME | SAME | Same input and same marshal hash. |
| constant_true | basic_scalar_constant | SAME | SAME | Same input and same marshal hash. |
| crlf_string | unicode_string | SAME | SAME | Same input and same marshal hash. |
| decomposed_e_acute | unicode_string | SAME | SAME | Same input and same marshal hash. |
| emoji_text | unicode_string | SAME | SAME | Same input and same marshal hash. |
| float_huge_1e300 | float_complex | SAME | SAME | Same input and same marshal hash. |
| float_math_nan | float_complex | SAME | SAME | Same input and same marshal hash. |
| float_nan_constructor | float_complex | SAME | SAME | Same input and same marshal hash. |
| float_nan_payload_0x7ff0000000000001 | float_complex | SAME | SAME | Same input and same marshal hash. |
| float_nan_payload_0x7ff8000000000001 | float_complex | SAME | SAME | Same input and same marshal hash. |
| float_nan_payload_0x7ff8000000000002 | float_complex | SAME | SAME | Same input and same marshal hash. |
| float_neg_inf | float_complex | SAME | SAME | Same input and same marshal hash. |
| float_neg_one | float_complex | SAME | SAME | Same input and same marshal hash. |
| float_neg_zero | float_complex | SAME | SAME | Same input and same marshal hash. |
| float_pos_inf | float_complex | SAME | SAME | Same input and same marshal hash. |
| float_pos_one | float_complex | SAME | SAME | Same input and same marshal hash. |
| float_pos_zero | float_complex | SAME | SAME | Same input and same marshal hash. |
| float_tiny_1e_minus_300 | float_complex | SAME | SAME | Same input and same marshal hash. |
| lone_high_surrogate | unicode_string | SAME | SAME | Same input and same marshal hash. |
| non_bmp_character | unicode_string | SAME | SAME | Same input and same marshal hash. |
| nul_inside_string | unicode_string | SAME | SAME | Same input and same marshal hash. |
| recreated_complex_nan_both | float_complex | SAME | SAME | Same input and same marshal hash. |
| recreated_float_nan | float_complex | SAME | SAME | Same input and same marshal hash. |
| slice_1_10_2 | optional_slice_probe | DIFFERENT | SAME | Same optional support boundary or exception behavior. |
| slice_neg10_none_neg1 | optional_slice_probe | DIFFERENT | SAME | Same optional support boundary or exception behavior. |
| slice_none_none_none | optional_slice_probe | DIFFERENT | SAME | Same optional support boundary or exception behavior. |
| zero_width_joiner_sequence | unicode_string | SAME | SAME | Same input and same marshal hash. |

### member_b_all_darwin_arm64_py3_13_results (Darwin/arm64, Python 3.13.13) vs member_b_all_windows_amd64_py3_9_results (Windows/AMD64, Python 3.9.13)

| Case | Category | Same marshal hash | Same exception | Interpretation |
| --- | --- | --- | --- | --- |
| ascii_plain | unicode_string | SAME | SAME | Same input and same marshal hash. |
| bytes_255_a | bytes_payload | SAME | SAME | Same input and same marshal hash. |
| bytes_256_a | bytes_payload | SAME | SAME | Same input and same marshal hash. |
| bytes_65535_a | bytes_payload | SAME | SAME | Same input and same marshal hash. |
| bytes_65536_a | bytes_payload | SAME | SAME | Same input and same marshal hash. |
| bytes_all_byte_values | bytes_payload | SAME | SAME | Same input and same marshal hash. |
| bytes_empty | bytes_payload | SAME | SAME | Same input and same marshal hash. |
| bytes_high_values_with_ascii | bytes_payload | SAME | SAME | Same input and same marshal hash. |
| bytes_single_nul | bytes_payload | SAME | SAME | Same input and same marshal hash. |
| chinese_text | unicode_string | SAME | SAME | Same input and same marshal hash. |
| complex_inf_neg_inf | float_complex | SAME | SAME | Same input and same marshal hash. |
| complex_nan_both | float_complex | SAME | SAME | Same input and same marshal hash. |
| complex_nan_imag | float_complex | SAME | SAME | Same input and same marshal hash. |
| complex_nan_real | float_complex | SAME | SAME | Same input and same marshal hash. |
| complex_payload_nan_imag | float_complex | SAME | SAME | Same input and same marshal hash. |
| complex_payload_nan_real | float_complex | SAME | SAME | Same input and same marshal hash. |
| complex_regular | float_complex | SAME | SAME | Same input and same marshal hash. |
| complex_zero_neg_zero | float_complex | SAME | SAME | Same input and same marshal hash. |
| composed_e_acute | unicode_string | DIFFERENT | SAME | Same input representation but Python major/minor differs; likely version-level marshal format difference. |
| constant_ellipsis | basic_scalar_constant | SAME | SAME | Same input and same marshal hash. |
| constant_false | basic_scalar_constant | SAME | SAME | Same input and same marshal hash. |
| constant_none | basic_scalar_constant | SAME | SAME | Same input and same marshal hash. |
| constant_true | basic_scalar_constant | SAME | SAME | Same input and same marshal hash. |
| crlf_string | unicode_string | SAME | SAME | Same input and same marshal hash. |
| decomposed_e_acute | unicode_string | SAME | SAME | Same input and same marshal hash. |
| emoji_text | unicode_string | SAME | SAME | Same input and same marshal hash. |
| float_huge_1e300 | float_complex | SAME | SAME | Same input and same marshal hash. |
| float_math_nan | float_complex | SAME | SAME | Same input and same marshal hash. |
| float_nan_constructor | float_complex | SAME | SAME | Same input and same marshal hash. |
| float_nan_payload_0x7ff0000000000001 | float_complex | SAME | SAME | Same input and same marshal hash. |
| float_nan_payload_0x7ff8000000000001 | float_complex | SAME | SAME | Same input and same marshal hash. |
| float_nan_payload_0x7ff8000000000002 | float_complex | SAME | SAME | Same input and same marshal hash. |
| float_neg_inf | float_complex | SAME | SAME | Same input and same marshal hash. |
| float_neg_one | float_complex | SAME | SAME | Same input and same marshal hash. |
| float_neg_zero | float_complex | SAME | SAME | Same input and same marshal hash. |
| float_pos_inf | float_complex | SAME | SAME | Same input and same marshal hash. |
| float_pos_one | float_complex | SAME | SAME | Same input and same marshal hash. |
| float_pos_zero | float_complex | SAME | SAME | Same input and same marshal hash. |
| float_tiny_1e_minus_300 | float_complex | SAME | SAME | Same input and same marshal hash. |
| lone_high_surrogate | unicode_string | SAME | SAME | Same input and same marshal hash. |
| non_bmp_character | unicode_string | SAME | SAME | Same input and same marshal hash. |
| nul_inside_string | unicode_string | SAME | SAME | Same input and same marshal hash. |
| recreated_complex_nan_both | float_complex | SAME | SAME | Same input and same marshal hash. |
| recreated_float_nan | float_complex | SAME | SAME | Same input and same marshal hash. |
| slice_1_10_2 | optional_slice_probe | DIFFERENT | SAME | Same optional support boundary or exception behavior. |
| slice_neg10_none_neg1 | optional_slice_probe | DIFFERENT | SAME | Same optional support boundary or exception behavior. |
| slice_none_none_none | optional_slice_probe | DIFFERENT | SAME | Same optional support boundary or exception behavior. |
| zero_width_joiner_sequence | unicode_string | SAME | SAME | Same input and same marshal hash. |

### member_b_all_darwin_arm64_py3_9_results (Darwin/arm64, Python 3.9.6) vs member_b_all_linux_x86_64_py3_10_results (Linux/x86_64, Python 3.10.20)

| Case | Category | Same marshal hash | Same exception | Interpretation |
| --- | --- | --- | --- | --- |
| ascii_plain | unicode_string | SAME | SAME | Same input and same marshal hash. |
| bytes_255_a | bytes_payload | SAME | SAME | Same input and same marshal hash. |
| bytes_256_a | bytes_payload | SAME | SAME | Same input and same marshal hash. |
| bytes_65535_a | bytes_payload | SAME | SAME | Same input and same marshal hash. |
| bytes_65536_a | bytes_payload | SAME | SAME | Same input and same marshal hash. |
| bytes_all_byte_values | bytes_payload | SAME | SAME | Same input and same marshal hash. |
| bytes_empty | bytes_payload | SAME | SAME | Same input and same marshal hash. |
| bytes_high_values_with_ascii | bytes_payload | SAME | SAME | Same input and same marshal hash. |
| bytes_single_nul | bytes_payload | SAME | SAME | Same input and same marshal hash. |
| chinese_text | unicode_string | SAME | SAME | Same input and same marshal hash. |
| complex_inf_neg_inf | float_complex | SAME | SAME | Same input and same marshal hash. |
| complex_nan_both | float_complex | SAME | SAME | Same input and same marshal hash. |
| complex_nan_imag | float_complex | SAME | SAME | Same input and same marshal hash. |
| complex_nan_real | float_complex | SAME | SAME | Same input and same marshal hash. |
| complex_payload_nan_imag | float_complex | SAME | SAME | Same input and same marshal hash. |
| complex_payload_nan_real | float_complex | SAME | SAME | Same input and same marshal hash. |
| complex_regular | float_complex | SAME | SAME | Same input and same marshal hash. |
| complex_zero_neg_zero | float_complex | SAME | SAME | Same input and same marshal hash. |
| composed_e_acute | unicode_string | SAME | SAME | Same input and same marshal hash. |
| constant_ellipsis | basic_scalar_constant | SAME | SAME | Same input and same marshal hash. |
| constant_false | basic_scalar_constant | SAME | SAME | Same input and same marshal hash. |
| constant_none | basic_scalar_constant | SAME | SAME | Same input and same marshal hash. |
| constant_true | basic_scalar_constant | SAME | SAME | Same input and same marshal hash. |
| crlf_string | unicode_string | SAME | SAME | Same input and same marshal hash. |
| decomposed_e_acute | unicode_string | SAME | SAME | Same input and same marshal hash. |
| emoji_text | unicode_string | SAME | SAME | Same input and same marshal hash. |
| float_huge_1e300 | float_complex | SAME | SAME | Same input and same marshal hash. |
| float_math_nan | float_complex | SAME | SAME | Same input and same marshal hash. |
| float_nan_constructor | float_complex | SAME | SAME | Same input and same marshal hash. |
| float_nan_payload_0x7ff0000000000001 | float_complex | SAME | SAME | Same input and same marshal hash. |
| float_nan_payload_0x7ff8000000000001 | float_complex | SAME | SAME | Same input and same marshal hash. |
| float_nan_payload_0x7ff8000000000002 | float_complex | SAME | SAME | Same input and same marshal hash. |
| float_neg_inf | float_complex | SAME | SAME | Same input and same marshal hash. |
| float_neg_one | float_complex | SAME | SAME | Same input and same marshal hash. |
| float_neg_zero | float_complex | SAME | SAME | Same input and same marshal hash. |
| float_pos_inf | float_complex | SAME | SAME | Same input and same marshal hash. |
| float_pos_one | float_complex | SAME | SAME | Same input and same marshal hash. |
| float_pos_zero | float_complex | SAME | SAME | Same input and same marshal hash. |
| float_tiny_1e_minus_300 | float_complex | SAME | SAME | Same input and same marshal hash. |
| lone_high_surrogate | unicode_string | SAME | SAME | Same input and same marshal hash. |
| non_bmp_character | unicode_string | SAME | SAME | Same input and same marshal hash. |
| nul_inside_string | unicode_string | SAME | SAME | Same input and same marshal hash. |
| recreated_complex_nan_both | float_complex | SAME | SAME | Same input and same marshal hash. |
| recreated_float_nan | float_complex | SAME | SAME | Same input and same marshal hash. |
| slice_1_10_2 | optional_slice_probe | DIFFERENT | SAME | Same optional support boundary or exception behavior. |
| slice_neg10_none_neg1 | optional_slice_probe | DIFFERENT | SAME | Same optional support boundary or exception behavior. |
| slice_none_none_none | optional_slice_probe | DIFFERENT | SAME | Same optional support boundary or exception behavior. |
| zero_width_joiner_sequence | unicode_string | SAME | SAME | Same input and same marshal hash. |

### member_b_all_darwin_arm64_py3_9_results (Darwin/arm64, Python 3.9.6) vs member_b_all_linux_x86_64_py3_11_results (Linux/x86_64, Python 3.11.15)

| Case | Category | Same marshal hash | Same exception | Interpretation |
| --- | --- | --- | --- | --- |
| ascii_plain | unicode_string | SAME | SAME | Same input and same marshal hash. |
| bytes_255_a | bytes_payload | SAME | SAME | Same input and same marshal hash. |
| bytes_256_a | bytes_payload | SAME | SAME | Same input and same marshal hash. |
| bytes_65535_a | bytes_payload | SAME | SAME | Same input and same marshal hash. |
| bytes_65536_a | bytes_payload | SAME | SAME | Same input and same marshal hash. |
| bytes_all_byte_values | bytes_payload | SAME | SAME | Same input and same marshal hash. |
| bytes_empty | bytes_payload | SAME | SAME | Same input and same marshal hash. |
| bytes_high_values_with_ascii | bytes_payload | SAME | SAME | Same input and same marshal hash. |
| bytes_single_nul | bytes_payload | SAME | SAME | Same input and same marshal hash. |
| chinese_text | unicode_string | SAME | SAME | Same input and same marshal hash. |
| complex_inf_neg_inf | float_complex | SAME | SAME | Same input and same marshal hash. |
| complex_nan_both | float_complex | SAME | SAME | Same input and same marshal hash. |
| complex_nan_imag | float_complex | SAME | SAME | Same input and same marshal hash. |
| complex_nan_real | float_complex | SAME | SAME | Same input and same marshal hash. |
| complex_payload_nan_imag | float_complex | SAME | SAME | Same input and same marshal hash. |
| complex_payload_nan_real | float_complex | SAME | SAME | Same input and same marshal hash. |
| complex_regular | float_complex | SAME | SAME | Same input and same marshal hash. |
| complex_zero_neg_zero | float_complex | SAME | SAME | Same input and same marshal hash. |
| composed_e_acute | unicode_string | SAME | SAME | Same input and same marshal hash. |
| constant_ellipsis | basic_scalar_constant | SAME | SAME | Same input and same marshal hash. |
| constant_false | basic_scalar_constant | SAME | SAME | Same input and same marshal hash. |
| constant_none | basic_scalar_constant | SAME | SAME | Same input and same marshal hash. |
| constant_true | basic_scalar_constant | SAME | SAME | Same input and same marshal hash. |
| crlf_string | unicode_string | SAME | SAME | Same input and same marshal hash. |
| decomposed_e_acute | unicode_string | SAME | SAME | Same input and same marshal hash. |
| emoji_text | unicode_string | SAME | SAME | Same input and same marshal hash. |
| float_huge_1e300 | float_complex | SAME | SAME | Same input and same marshal hash. |
| float_math_nan | float_complex | SAME | SAME | Same input and same marshal hash. |
| float_nan_constructor | float_complex | SAME | SAME | Same input and same marshal hash. |
| float_nan_payload_0x7ff0000000000001 | float_complex | SAME | SAME | Same input and same marshal hash. |
| float_nan_payload_0x7ff8000000000001 | float_complex | SAME | SAME | Same input and same marshal hash. |
| float_nan_payload_0x7ff8000000000002 | float_complex | SAME | SAME | Same input and same marshal hash. |
| float_neg_inf | float_complex | SAME | SAME | Same input and same marshal hash. |
| float_neg_one | float_complex | SAME | SAME | Same input and same marshal hash. |
| float_neg_zero | float_complex | SAME | SAME | Same input and same marshal hash. |
| float_pos_inf | float_complex | SAME | SAME | Same input and same marshal hash. |
| float_pos_one | float_complex | SAME | SAME | Same input and same marshal hash. |
| float_pos_zero | float_complex | SAME | SAME | Same input and same marshal hash. |
| float_tiny_1e_minus_300 | float_complex | SAME | SAME | Same input and same marshal hash. |
| lone_high_surrogate | unicode_string | SAME | SAME | Same input and same marshal hash. |
| non_bmp_character | unicode_string | SAME | SAME | Same input and same marshal hash. |
| nul_inside_string | unicode_string | SAME | SAME | Same input and same marshal hash. |
| recreated_complex_nan_both | float_complex | SAME | SAME | Same input and same marshal hash. |
| recreated_float_nan | float_complex | SAME | SAME | Same input and same marshal hash. |
| slice_1_10_2 | optional_slice_probe | DIFFERENT | SAME | Same optional support boundary or exception behavior. |
| slice_neg10_none_neg1 | optional_slice_probe | DIFFERENT | SAME | Same optional support boundary or exception behavior. |
| slice_none_none_none | optional_slice_probe | DIFFERENT | SAME | Same optional support boundary or exception behavior. |
| zero_width_joiner_sequence | unicode_string | SAME | SAME | Same input and same marshal hash. |

### member_b_all_darwin_arm64_py3_9_results (Darwin/arm64, Python 3.9.6) vs member_b_all_linux_x86_64_py3_12_results (Linux/x86_64, Python 3.12.13)

| Case | Category | Same marshal hash | Same exception | Interpretation |
| --- | --- | --- | --- | --- |
| ascii_plain | unicode_string | SAME | SAME | Same input and same marshal hash. |
| bytes_255_a | bytes_payload | SAME | SAME | Same input and same marshal hash. |
| bytes_256_a | bytes_payload | SAME | SAME | Same input and same marshal hash. |
| bytes_65535_a | bytes_payload | SAME | SAME | Same input and same marshal hash. |
| bytes_65536_a | bytes_payload | SAME | SAME | Same input and same marshal hash. |
| bytes_all_byte_values | bytes_payload | SAME | SAME | Same input and same marshal hash. |
| bytes_empty | bytes_payload | SAME | SAME | Same input and same marshal hash. |
| bytes_high_values_with_ascii | bytes_payload | SAME | SAME | Same input and same marshal hash. |
| bytes_single_nul | bytes_payload | SAME | SAME | Same input and same marshal hash. |
| chinese_text | unicode_string | SAME | SAME | Same input and same marshal hash. |
| complex_inf_neg_inf | float_complex | SAME | SAME | Same input and same marshal hash. |
| complex_nan_both | float_complex | SAME | SAME | Same input and same marshal hash. |
| complex_nan_imag | float_complex | SAME | SAME | Same input and same marshal hash. |
| complex_nan_real | float_complex | SAME | SAME | Same input and same marshal hash. |
| complex_payload_nan_imag | float_complex | SAME | SAME | Same input and same marshal hash. |
| complex_payload_nan_real | float_complex | SAME | SAME | Same input and same marshal hash. |
| complex_regular | float_complex | SAME | SAME | Same input and same marshal hash. |
| complex_zero_neg_zero | float_complex | SAME | SAME | Same input and same marshal hash. |
| composed_e_acute | unicode_string | DIFFERENT | SAME | Same input representation but Python major/minor differs; likely version-level marshal format difference. |
| constant_ellipsis | basic_scalar_constant | SAME | SAME | Same input and same marshal hash. |
| constant_false | basic_scalar_constant | SAME | SAME | Same input and same marshal hash. |
| constant_none | basic_scalar_constant | SAME | SAME | Same input and same marshal hash. |
| constant_true | basic_scalar_constant | SAME | SAME | Same input and same marshal hash. |
| crlf_string | unicode_string | SAME | SAME | Same input and same marshal hash. |
| decomposed_e_acute | unicode_string | SAME | SAME | Same input and same marshal hash. |
| emoji_text | unicode_string | SAME | SAME | Same input and same marshal hash. |
| float_huge_1e300 | float_complex | SAME | SAME | Same input and same marshal hash. |
| float_math_nan | float_complex | SAME | SAME | Same input and same marshal hash. |
| float_nan_constructor | float_complex | SAME | SAME | Same input and same marshal hash. |
| float_nan_payload_0x7ff0000000000001 | float_complex | SAME | SAME | Same input and same marshal hash. |
| float_nan_payload_0x7ff8000000000001 | float_complex | SAME | SAME | Same input and same marshal hash. |
| float_nan_payload_0x7ff8000000000002 | float_complex | SAME | SAME | Same input and same marshal hash. |
| float_neg_inf | float_complex | SAME | SAME | Same input and same marshal hash. |
| float_neg_one | float_complex | SAME | SAME | Same input and same marshal hash. |
| float_neg_zero | float_complex | SAME | SAME | Same input and same marshal hash. |
| float_pos_inf | float_complex | SAME | SAME | Same input and same marshal hash. |
| float_pos_one | float_complex | SAME | SAME | Same input and same marshal hash. |
| float_pos_zero | float_complex | SAME | SAME | Same input and same marshal hash. |
| float_tiny_1e_minus_300 | float_complex | SAME | SAME | Same input and same marshal hash. |
| lone_high_surrogate | unicode_string | SAME | SAME | Same input and same marshal hash. |
| non_bmp_character | unicode_string | SAME | SAME | Same input and same marshal hash. |
| nul_inside_string | unicode_string | SAME | SAME | Same input and same marshal hash. |
| recreated_complex_nan_both | float_complex | SAME | SAME | Same input and same marshal hash. |
| recreated_float_nan | float_complex | SAME | SAME | Same input and same marshal hash. |
| slice_1_10_2 | optional_slice_probe | DIFFERENT | SAME | Same optional support boundary or exception behavior. |
| slice_neg10_none_neg1 | optional_slice_probe | DIFFERENT | SAME | Same optional support boundary or exception behavior. |
| slice_none_none_none | optional_slice_probe | DIFFERENT | SAME | Same optional support boundary or exception behavior. |
| zero_width_joiner_sequence | unicode_string | SAME | SAME | Same input and same marshal hash. |

### member_b_all_darwin_arm64_py3_9_results (Darwin/arm64, Python 3.9.6) vs member_b_all_linux_x86_64_py3_13_results (Linux/x86_64, Python 3.13.13)

| Case | Category | Same marshal hash | Same exception | Interpretation |
| --- | --- | --- | --- | --- |
| ascii_plain | unicode_string | SAME | SAME | Same input and same marshal hash. |
| bytes_255_a | bytes_payload | SAME | SAME | Same input and same marshal hash. |
| bytes_256_a | bytes_payload | SAME | SAME | Same input and same marshal hash. |
| bytes_65535_a | bytes_payload | SAME | SAME | Same input and same marshal hash. |
| bytes_65536_a | bytes_payload | SAME | SAME | Same input and same marshal hash. |
| bytes_all_byte_values | bytes_payload | SAME | SAME | Same input and same marshal hash. |
| bytes_empty | bytes_payload | SAME | SAME | Same input and same marshal hash. |
| bytes_high_values_with_ascii | bytes_payload | SAME | SAME | Same input and same marshal hash. |
| bytes_single_nul | bytes_payload | SAME | SAME | Same input and same marshal hash. |
| chinese_text | unicode_string | SAME | SAME | Same input and same marshal hash. |
| complex_inf_neg_inf | float_complex | SAME | SAME | Same input and same marshal hash. |
| complex_nan_both | float_complex | SAME | SAME | Same input and same marshal hash. |
| complex_nan_imag | float_complex | SAME | SAME | Same input and same marshal hash. |
| complex_nan_real | float_complex | SAME | SAME | Same input and same marshal hash. |
| complex_payload_nan_imag | float_complex | SAME | SAME | Same input and same marshal hash. |
| complex_payload_nan_real | float_complex | SAME | SAME | Same input and same marshal hash. |
| complex_regular | float_complex | SAME | SAME | Same input and same marshal hash. |
| complex_zero_neg_zero | float_complex | SAME | SAME | Same input and same marshal hash. |
| composed_e_acute | unicode_string | DIFFERENT | SAME | Same input representation but Python major/minor differs; likely version-level marshal format difference. |
| constant_ellipsis | basic_scalar_constant | SAME | SAME | Same input and same marshal hash. |
| constant_false | basic_scalar_constant | SAME | SAME | Same input and same marshal hash. |
| constant_none | basic_scalar_constant | SAME | SAME | Same input and same marshal hash. |
| constant_true | basic_scalar_constant | SAME | SAME | Same input and same marshal hash. |
| crlf_string | unicode_string | SAME | SAME | Same input and same marshal hash. |
| decomposed_e_acute | unicode_string | SAME | SAME | Same input and same marshal hash. |
| emoji_text | unicode_string | SAME | SAME | Same input and same marshal hash. |
| float_huge_1e300 | float_complex | SAME | SAME | Same input and same marshal hash. |
| float_math_nan | float_complex | SAME | SAME | Same input and same marshal hash. |
| float_nan_constructor | float_complex | SAME | SAME | Same input and same marshal hash. |
| float_nan_payload_0x7ff0000000000001 | float_complex | SAME | SAME | Same input and same marshal hash. |
| float_nan_payload_0x7ff8000000000001 | float_complex | SAME | SAME | Same input and same marshal hash. |
| float_nan_payload_0x7ff8000000000002 | float_complex | SAME | SAME | Same input and same marshal hash. |
| float_neg_inf | float_complex | SAME | SAME | Same input and same marshal hash. |
| float_neg_one | float_complex | SAME | SAME | Same input and same marshal hash. |
| float_neg_zero | float_complex | SAME | SAME | Same input and same marshal hash. |
| float_pos_inf | float_complex | SAME | SAME | Same input and same marshal hash. |
| float_pos_one | float_complex | SAME | SAME | Same input and same marshal hash. |
| float_pos_zero | float_complex | SAME | SAME | Same input and same marshal hash. |
| float_tiny_1e_minus_300 | float_complex | SAME | SAME | Same input and same marshal hash. |
| lone_high_surrogate | unicode_string | SAME | SAME | Same input and same marshal hash. |
| non_bmp_character | unicode_string | SAME | SAME | Same input and same marshal hash. |
| nul_inside_string | unicode_string | SAME | SAME | Same input and same marshal hash. |
| recreated_complex_nan_both | float_complex | SAME | SAME | Same input and same marshal hash. |
| recreated_float_nan | float_complex | SAME | SAME | Same input and same marshal hash. |
| slice_1_10_2 | optional_slice_probe | DIFFERENT | SAME | Same optional support boundary or exception behavior. |
| slice_neg10_none_neg1 | optional_slice_probe | DIFFERENT | SAME | Same optional support boundary or exception behavior. |
| slice_none_none_none | optional_slice_probe | DIFFERENT | SAME | Same optional support boundary or exception behavior. |
| zero_width_joiner_sequence | unicode_string | SAME | SAME | Same input and same marshal hash. |

### member_b_all_darwin_arm64_py3_9_results (Darwin/arm64, Python 3.9.6) vs member_b_all_linux_x86_64_py3_9_results (Linux/x86_64, Python 3.9.25)

| Case | Category | Same marshal hash | Same exception | Interpretation |
| --- | --- | --- | --- | --- |
| ascii_plain | unicode_string | SAME | SAME | Same input and same marshal hash. |
| bytes_255_a | bytes_payload | SAME | SAME | Same input and same marshal hash. |
| bytes_256_a | bytes_payload | SAME | SAME | Same input and same marshal hash. |
| bytes_65535_a | bytes_payload | SAME | SAME | Same input and same marshal hash. |
| bytes_65536_a | bytes_payload | SAME | SAME | Same input and same marshal hash. |
| bytes_all_byte_values | bytes_payload | SAME | SAME | Same input and same marshal hash. |
| bytes_empty | bytes_payload | SAME | SAME | Same input and same marshal hash. |
| bytes_high_values_with_ascii | bytes_payload | SAME | SAME | Same input and same marshal hash. |
| bytes_single_nul | bytes_payload | SAME | SAME | Same input and same marshal hash. |
| chinese_text | unicode_string | SAME | SAME | Same input and same marshal hash. |
| complex_inf_neg_inf | float_complex | SAME | SAME | Same input and same marshal hash. |
| complex_nan_both | float_complex | SAME | SAME | Same input and same marshal hash. |
| complex_nan_imag | float_complex | SAME | SAME | Same input and same marshal hash. |
| complex_nan_real | float_complex | SAME | SAME | Same input and same marshal hash. |
| complex_payload_nan_imag | float_complex | SAME | SAME | Same input and same marshal hash. |
| complex_payload_nan_real | float_complex | SAME | SAME | Same input and same marshal hash. |
| complex_regular | float_complex | SAME | SAME | Same input and same marshal hash. |
| complex_zero_neg_zero | float_complex | SAME | SAME | Same input and same marshal hash. |
| composed_e_acute | unicode_string | SAME | SAME | Same input and same marshal hash. |
| constant_ellipsis | basic_scalar_constant | SAME | SAME | Same input and same marshal hash. |
| constant_false | basic_scalar_constant | SAME | SAME | Same input and same marshal hash. |
| constant_none | basic_scalar_constant | SAME | SAME | Same input and same marshal hash. |
| constant_true | basic_scalar_constant | SAME | SAME | Same input and same marshal hash. |
| crlf_string | unicode_string | SAME | SAME | Same input and same marshal hash. |
| decomposed_e_acute | unicode_string | SAME | SAME | Same input and same marshal hash. |
| emoji_text | unicode_string | SAME | SAME | Same input and same marshal hash. |
| float_huge_1e300 | float_complex | SAME | SAME | Same input and same marshal hash. |
| float_math_nan | float_complex | SAME | SAME | Same input and same marshal hash. |
| float_nan_constructor | float_complex | SAME | SAME | Same input and same marshal hash. |
| float_nan_payload_0x7ff0000000000001 | float_complex | SAME | SAME | Same input and same marshal hash. |
| float_nan_payload_0x7ff8000000000001 | float_complex | SAME | SAME | Same input and same marshal hash. |
| float_nan_payload_0x7ff8000000000002 | float_complex | SAME | SAME | Same input and same marshal hash. |
| float_neg_inf | float_complex | SAME | SAME | Same input and same marshal hash. |
| float_neg_one | float_complex | SAME | SAME | Same input and same marshal hash. |
| float_neg_zero | float_complex | SAME | SAME | Same input and same marshal hash. |
| float_pos_inf | float_complex | SAME | SAME | Same input and same marshal hash. |
| float_pos_one | float_complex | SAME | SAME | Same input and same marshal hash. |
| float_pos_zero | float_complex | SAME | SAME | Same input and same marshal hash. |
| float_tiny_1e_minus_300 | float_complex | SAME | SAME | Same input and same marshal hash. |
| lone_high_surrogate | unicode_string | SAME | SAME | Same input and same marshal hash. |
| non_bmp_character | unicode_string | SAME | SAME | Same input and same marshal hash. |
| nul_inside_string | unicode_string | SAME | SAME | Same input and same marshal hash. |
| recreated_complex_nan_both | float_complex | SAME | SAME | Same input and same marshal hash. |
| recreated_float_nan | float_complex | SAME | SAME | Same input and same marshal hash. |
| slice_1_10_2 | optional_slice_probe | DIFFERENT | SAME | Same optional support boundary or exception behavior. |
| slice_neg10_none_neg1 | optional_slice_probe | DIFFERENT | SAME | Same optional support boundary or exception behavior. |
| slice_none_none_none | optional_slice_probe | DIFFERENT | SAME | Same optional support boundary or exception behavior. |
| zero_width_joiner_sequence | unicode_string | SAME | SAME | Same input and same marshal hash. |

### member_b_all_darwin_arm64_py3_9_results (Darwin/arm64, Python 3.9.6) vs member_b_all_windows_amd64_py3_10_results (Windows/AMD64, Python 3.10.11)

| Case | Category | Same marshal hash | Same exception | Interpretation |
| --- | --- | --- | --- | --- |
| ascii_plain | unicode_string | SAME | SAME | Same input and same marshal hash. |
| bytes_255_a | bytes_payload | SAME | SAME | Same input and same marshal hash. |
| bytes_256_a | bytes_payload | SAME | SAME | Same input and same marshal hash. |
| bytes_65535_a | bytes_payload | SAME | SAME | Same input and same marshal hash. |
| bytes_65536_a | bytes_payload | SAME | SAME | Same input and same marshal hash. |
| bytes_all_byte_values | bytes_payload | SAME | SAME | Same input and same marshal hash. |
| bytes_empty | bytes_payload | SAME | SAME | Same input and same marshal hash. |
| bytes_high_values_with_ascii | bytes_payload | SAME | SAME | Same input and same marshal hash. |
| bytes_single_nul | bytes_payload | SAME | SAME | Same input and same marshal hash. |
| chinese_text | unicode_string | SAME | SAME | Same input and same marshal hash. |
| complex_inf_neg_inf | float_complex | SAME | SAME | Same input and same marshal hash. |
| complex_nan_both | float_complex | SAME | SAME | Same input and same marshal hash. |
| complex_nan_imag | float_complex | SAME | SAME | Same input and same marshal hash. |
| complex_nan_real | float_complex | SAME | SAME | Same input and same marshal hash. |
| complex_payload_nan_imag | float_complex | SAME | SAME | Same input and same marshal hash. |
| complex_payload_nan_real | float_complex | SAME | SAME | Same input and same marshal hash. |
| complex_regular | float_complex | SAME | SAME | Same input and same marshal hash. |
| complex_zero_neg_zero | float_complex | SAME | SAME | Same input and same marshal hash. |
| composed_e_acute | unicode_string | SAME | SAME | Same input and same marshal hash. |
| constant_ellipsis | basic_scalar_constant | SAME | SAME | Same input and same marshal hash. |
| constant_false | basic_scalar_constant | SAME | SAME | Same input and same marshal hash. |
| constant_none | basic_scalar_constant | SAME | SAME | Same input and same marshal hash. |
| constant_true | basic_scalar_constant | SAME | SAME | Same input and same marshal hash. |
| crlf_string | unicode_string | SAME | SAME | Same input and same marshal hash. |
| decomposed_e_acute | unicode_string | SAME | SAME | Same input and same marshal hash. |
| emoji_text | unicode_string | SAME | SAME | Same input and same marshal hash. |
| float_huge_1e300 | float_complex | SAME | SAME | Same input and same marshal hash. |
| float_math_nan | float_complex | SAME | SAME | Same input and same marshal hash. |
| float_nan_constructor | float_complex | SAME | SAME | Same input and same marshal hash. |
| float_nan_payload_0x7ff0000000000001 | float_complex | SAME | SAME | Same input and same marshal hash. |
| float_nan_payload_0x7ff8000000000001 | float_complex | SAME | SAME | Same input and same marshal hash. |
| float_nan_payload_0x7ff8000000000002 | float_complex | SAME | SAME | Same input and same marshal hash. |
| float_neg_inf | float_complex | SAME | SAME | Same input and same marshal hash. |
| float_neg_one | float_complex | SAME | SAME | Same input and same marshal hash. |
| float_neg_zero | float_complex | SAME | SAME | Same input and same marshal hash. |
| float_pos_inf | float_complex | SAME | SAME | Same input and same marshal hash. |
| float_pos_one | float_complex | SAME | SAME | Same input and same marshal hash. |
| float_pos_zero | float_complex | SAME | SAME | Same input and same marshal hash. |
| float_tiny_1e_minus_300 | float_complex | SAME | SAME | Same input and same marshal hash. |
| lone_high_surrogate | unicode_string | SAME | SAME | Same input and same marshal hash. |
| non_bmp_character | unicode_string | SAME | SAME | Same input and same marshal hash. |
| nul_inside_string | unicode_string | SAME | SAME | Same input and same marshal hash. |
| recreated_complex_nan_both | float_complex | SAME | SAME | Same input and same marshal hash. |
| recreated_float_nan | float_complex | SAME | SAME | Same input and same marshal hash. |
| slice_1_10_2 | optional_slice_probe | DIFFERENT | SAME | Same optional support boundary or exception behavior. |
| slice_neg10_none_neg1 | optional_slice_probe | DIFFERENT | SAME | Same optional support boundary or exception behavior. |
| slice_none_none_none | optional_slice_probe | DIFFERENT | SAME | Same optional support boundary or exception behavior. |
| zero_width_joiner_sequence | unicode_string | SAME | SAME | Same input and same marshal hash. |

### member_b_all_darwin_arm64_py3_9_results (Darwin/arm64, Python 3.9.6) vs member_b_all_windows_amd64_py3_11_results (Windows/AMD64, Python 3.11.9)

| Case | Category | Same marshal hash | Same exception | Interpretation |
| --- | --- | --- | --- | --- |
| ascii_plain | unicode_string | SAME | SAME | Same input and same marshal hash. |
| bytes_255_a | bytes_payload | SAME | SAME | Same input and same marshal hash. |
| bytes_256_a | bytes_payload | SAME | SAME | Same input and same marshal hash. |
| bytes_65535_a | bytes_payload | SAME | SAME | Same input and same marshal hash. |
| bytes_65536_a | bytes_payload | SAME | SAME | Same input and same marshal hash. |
| bytes_all_byte_values | bytes_payload | SAME | SAME | Same input and same marshal hash. |
| bytes_empty | bytes_payload | SAME | SAME | Same input and same marshal hash. |
| bytes_high_values_with_ascii | bytes_payload | SAME | SAME | Same input and same marshal hash. |
| bytes_single_nul | bytes_payload | SAME | SAME | Same input and same marshal hash. |
| chinese_text | unicode_string | SAME | SAME | Same input and same marshal hash. |
| complex_inf_neg_inf | float_complex | SAME | SAME | Same input and same marshal hash. |
| complex_nan_both | float_complex | SAME | SAME | Same input and same marshal hash. |
| complex_nan_imag | float_complex | SAME | SAME | Same input and same marshal hash. |
| complex_nan_real | float_complex | SAME | SAME | Same input and same marshal hash. |
| complex_payload_nan_imag | float_complex | SAME | SAME | Same input and same marshal hash. |
| complex_payload_nan_real | float_complex | SAME | SAME | Same input and same marshal hash. |
| complex_regular | float_complex | SAME | SAME | Same input and same marshal hash. |
| complex_zero_neg_zero | float_complex | SAME | SAME | Same input and same marshal hash. |
| composed_e_acute | unicode_string | SAME | SAME | Same input and same marshal hash. |
| constant_ellipsis | basic_scalar_constant | SAME | SAME | Same input and same marshal hash. |
| constant_false | basic_scalar_constant | SAME | SAME | Same input and same marshal hash. |
| constant_none | basic_scalar_constant | SAME | SAME | Same input and same marshal hash. |
| constant_true | basic_scalar_constant | SAME | SAME | Same input and same marshal hash. |
| crlf_string | unicode_string | SAME | SAME | Same input and same marshal hash. |
| decomposed_e_acute | unicode_string | SAME | SAME | Same input and same marshal hash. |
| emoji_text | unicode_string | SAME | SAME | Same input and same marshal hash. |
| float_huge_1e300 | float_complex | SAME | SAME | Same input and same marshal hash. |
| float_math_nan | float_complex | SAME | SAME | Same input and same marshal hash. |
| float_nan_constructor | float_complex | SAME | SAME | Same input and same marshal hash. |
| float_nan_payload_0x7ff0000000000001 | float_complex | SAME | SAME | Same input and same marshal hash. |
| float_nan_payload_0x7ff8000000000001 | float_complex | SAME | SAME | Same input and same marshal hash. |
| float_nan_payload_0x7ff8000000000002 | float_complex | SAME | SAME | Same input and same marshal hash. |
| float_neg_inf | float_complex | SAME | SAME | Same input and same marshal hash. |
| float_neg_one | float_complex | SAME | SAME | Same input and same marshal hash. |
| float_neg_zero | float_complex | SAME | SAME | Same input and same marshal hash. |
| float_pos_inf | float_complex | SAME | SAME | Same input and same marshal hash. |
| float_pos_one | float_complex | SAME | SAME | Same input and same marshal hash. |
| float_pos_zero | float_complex | SAME | SAME | Same input and same marshal hash. |
| float_tiny_1e_minus_300 | float_complex | SAME | SAME | Same input and same marshal hash. |
| lone_high_surrogate | unicode_string | SAME | SAME | Same input and same marshal hash. |
| non_bmp_character | unicode_string | SAME | SAME | Same input and same marshal hash. |
| nul_inside_string | unicode_string | SAME | SAME | Same input and same marshal hash. |
| recreated_complex_nan_both | float_complex | SAME | SAME | Same input and same marshal hash. |
| recreated_float_nan | float_complex | SAME | SAME | Same input and same marshal hash. |
| slice_1_10_2 | optional_slice_probe | DIFFERENT | SAME | Same optional support boundary or exception behavior. |
| slice_neg10_none_neg1 | optional_slice_probe | DIFFERENT | SAME | Same optional support boundary or exception behavior. |
| slice_none_none_none | optional_slice_probe | DIFFERENT | SAME | Same optional support boundary or exception behavior. |
| zero_width_joiner_sequence | unicode_string | SAME | SAME | Same input and same marshal hash. |

### member_b_all_darwin_arm64_py3_9_results (Darwin/arm64, Python 3.9.6) vs member_b_all_windows_amd64_py3_12_results (Windows/AMD64, Python 3.12.10)

| Case | Category | Same marshal hash | Same exception | Interpretation |
| --- | --- | --- | --- | --- |
| ascii_plain | unicode_string | SAME | SAME | Same input and same marshal hash. |
| bytes_255_a | bytes_payload | SAME | SAME | Same input and same marshal hash. |
| bytes_256_a | bytes_payload | SAME | SAME | Same input and same marshal hash. |
| bytes_65535_a | bytes_payload | SAME | SAME | Same input and same marshal hash. |
| bytes_65536_a | bytes_payload | SAME | SAME | Same input and same marshal hash. |
| bytes_all_byte_values | bytes_payload | SAME | SAME | Same input and same marshal hash. |
| bytes_empty | bytes_payload | SAME | SAME | Same input and same marshal hash. |
| bytes_high_values_with_ascii | bytes_payload | SAME | SAME | Same input and same marshal hash. |
| bytes_single_nul | bytes_payload | SAME | SAME | Same input and same marshal hash. |
| chinese_text | unicode_string | SAME | SAME | Same input and same marshal hash. |
| complex_inf_neg_inf | float_complex | SAME | SAME | Same input and same marshal hash. |
| complex_nan_both | float_complex | SAME | SAME | Same input and same marshal hash. |
| complex_nan_imag | float_complex | SAME | SAME | Same input and same marshal hash. |
| complex_nan_real | float_complex | SAME | SAME | Same input and same marshal hash. |
| complex_payload_nan_imag | float_complex | SAME | SAME | Same input and same marshal hash. |
| complex_payload_nan_real | float_complex | SAME | SAME | Same input and same marshal hash. |
| complex_regular | float_complex | SAME | SAME | Same input and same marshal hash. |
| complex_zero_neg_zero | float_complex | SAME | SAME | Same input and same marshal hash. |
| composed_e_acute | unicode_string | DIFFERENT | SAME | Same input representation but Python major/minor differs; likely version-level marshal format difference. |
| constant_ellipsis | basic_scalar_constant | SAME | SAME | Same input and same marshal hash. |
| constant_false | basic_scalar_constant | SAME | SAME | Same input and same marshal hash. |
| constant_none | basic_scalar_constant | SAME | SAME | Same input and same marshal hash. |
| constant_true | basic_scalar_constant | SAME | SAME | Same input and same marshal hash. |
| crlf_string | unicode_string | SAME | SAME | Same input and same marshal hash. |
| decomposed_e_acute | unicode_string | SAME | SAME | Same input and same marshal hash. |
| emoji_text | unicode_string | SAME | SAME | Same input and same marshal hash. |
| float_huge_1e300 | float_complex | SAME | SAME | Same input and same marshal hash. |
| float_math_nan | float_complex | SAME | SAME | Same input and same marshal hash. |
| float_nan_constructor | float_complex | SAME | SAME | Same input and same marshal hash. |
| float_nan_payload_0x7ff0000000000001 | float_complex | SAME | SAME | Same input and same marshal hash. |
| float_nan_payload_0x7ff8000000000001 | float_complex | SAME | SAME | Same input and same marshal hash. |
| float_nan_payload_0x7ff8000000000002 | float_complex | SAME | SAME | Same input and same marshal hash. |
| float_neg_inf | float_complex | SAME | SAME | Same input and same marshal hash. |
| float_neg_one | float_complex | SAME | SAME | Same input and same marshal hash. |
| float_neg_zero | float_complex | SAME | SAME | Same input and same marshal hash. |
| float_pos_inf | float_complex | SAME | SAME | Same input and same marshal hash. |
| float_pos_one | float_complex | SAME | SAME | Same input and same marshal hash. |
| float_pos_zero | float_complex | SAME | SAME | Same input and same marshal hash. |
| float_tiny_1e_minus_300 | float_complex | SAME | SAME | Same input and same marshal hash. |
| lone_high_surrogate | unicode_string | SAME | SAME | Same input and same marshal hash. |
| non_bmp_character | unicode_string | SAME | SAME | Same input and same marshal hash. |
| nul_inside_string | unicode_string | SAME | SAME | Same input and same marshal hash. |
| recreated_complex_nan_both | float_complex | SAME | SAME | Same input and same marshal hash. |
| recreated_float_nan | float_complex | SAME | SAME | Same input and same marshal hash. |
| slice_1_10_2 | optional_slice_probe | DIFFERENT | SAME | Same optional support boundary or exception behavior. |
| slice_neg10_none_neg1 | optional_slice_probe | DIFFERENT | SAME | Same optional support boundary or exception behavior. |
| slice_none_none_none | optional_slice_probe | DIFFERENT | SAME | Same optional support boundary or exception behavior. |
| zero_width_joiner_sequence | unicode_string | SAME | SAME | Same input and same marshal hash. |

### member_b_all_darwin_arm64_py3_9_results (Darwin/arm64, Python 3.9.6) vs member_b_all_windows_amd64_py3_13_results (Windows/AMD64, Python 3.13.13)

| Case | Category | Same marshal hash | Same exception | Interpretation |
| --- | --- | --- | --- | --- |
| ascii_plain | unicode_string | SAME | SAME | Same input and same marshal hash. |
| bytes_255_a | bytes_payload | SAME | SAME | Same input and same marshal hash. |
| bytes_256_a | bytes_payload | SAME | SAME | Same input and same marshal hash. |
| bytes_65535_a | bytes_payload | SAME | SAME | Same input and same marshal hash. |
| bytes_65536_a | bytes_payload | SAME | SAME | Same input and same marshal hash. |
| bytes_all_byte_values | bytes_payload | SAME | SAME | Same input and same marshal hash. |
| bytes_empty | bytes_payload | SAME | SAME | Same input and same marshal hash. |
| bytes_high_values_with_ascii | bytes_payload | SAME | SAME | Same input and same marshal hash. |
| bytes_single_nul | bytes_payload | SAME | SAME | Same input and same marshal hash. |
| chinese_text | unicode_string | SAME | SAME | Same input and same marshal hash. |
| complex_inf_neg_inf | float_complex | SAME | SAME | Same input and same marshal hash. |
| complex_nan_both | float_complex | SAME | SAME | Same input and same marshal hash. |
| complex_nan_imag | float_complex | SAME | SAME | Same input and same marshal hash. |
| complex_nan_real | float_complex | SAME | SAME | Same input and same marshal hash. |
| complex_payload_nan_imag | float_complex | SAME | SAME | Same input and same marshal hash. |
| complex_payload_nan_real | float_complex | SAME | SAME | Same input and same marshal hash. |
| complex_regular | float_complex | SAME | SAME | Same input and same marshal hash. |
| complex_zero_neg_zero | float_complex | SAME | SAME | Same input and same marshal hash. |
| composed_e_acute | unicode_string | DIFFERENT | SAME | Same input representation but Python major/minor differs; likely version-level marshal format difference. |
| constant_ellipsis | basic_scalar_constant | SAME | SAME | Same input and same marshal hash. |
| constant_false | basic_scalar_constant | SAME | SAME | Same input and same marshal hash. |
| constant_none | basic_scalar_constant | SAME | SAME | Same input and same marshal hash. |
| constant_true | basic_scalar_constant | SAME | SAME | Same input and same marshal hash. |
| crlf_string | unicode_string | SAME | SAME | Same input and same marshal hash. |
| decomposed_e_acute | unicode_string | SAME | SAME | Same input and same marshal hash. |
| emoji_text | unicode_string | SAME | SAME | Same input and same marshal hash. |
| float_huge_1e300 | float_complex | SAME | SAME | Same input and same marshal hash. |
| float_math_nan | float_complex | SAME | SAME | Same input and same marshal hash. |
| float_nan_constructor | float_complex | SAME | SAME | Same input and same marshal hash. |
| float_nan_payload_0x7ff0000000000001 | float_complex | SAME | SAME | Same input and same marshal hash. |
| float_nan_payload_0x7ff8000000000001 | float_complex | SAME | SAME | Same input and same marshal hash. |
| float_nan_payload_0x7ff8000000000002 | float_complex | SAME | SAME | Same input and same marshal hash. |
| float_neg_inf | float_complex | SAME | SAME | Same input and same marshal hash. |
| float_neg_one | float_complex | SAME | SAME | Same input and same marshal hash. |
| float_neg_zero | float_complex | SAME | SAME | Same input and same marshal hash. |
| float_pos_inf | float_complex | SAME | SAME | Same input and same marshal hash. |
| float_pos_one | float_complex | SAME | SAME | Same input and same marshal hash. |
| float_pos_zero | float_complex | SAME | SAME | Same input and same marshal hash. |
| float_tiny_1e_minus_300 | float_complex | SAME | SAME | Same input and same marshal hash. |
| lone_high_surrogate | unicode_string | SAME | SAME | Same input and same marshal hash. |
| non_bmp_character | unicode_string | SAME | SAME | Same input and same marshal hash. |
| nul_inside_string | unicode_string | SAME | SAME | Same input and same marshal hash. |
| recreated_complex_nan_both | float_complex | SAME | SAME | Same input and same marshal hash. |
| recreated_float_nan | float_complex | SAME | SAME | Same input and same marshal hash. |
| slice_1_10_2 | optional_slice_probe | DIFFERENT | SAME | Same optional support boundary or exception behavior. |
| slice_neg10_none_neg1 | optional_slice_probe | DIFFERENT | SAME | Same optional support boundary or exception behavior. |
| slice_none_none_none | optional_slice_probe | DIFFERENT | SAME | Same optional support boundary or exception behavior. |
| zero_width_joiner_sequence | unicode_string | SAME | SAME | Same input and same marshal hash. |

### member_b_all_darwin_arm64_py3_9_results (Darwin/arm64, Python 3.9.6) vs member_b_all_windows_amd64_py3_9_results (Windows/AMD64, Python 3.9.13)

| Case | Category | Same marshal hash | Same exception | Interpretation |
| --- | --- | --- | --- | --- |
| ascii_plain | unicode_string | SAME | SAME | Same input and same marshal hash. |
| bytes_255_a | bytes_payload | SAME | SAME | Same input and same marshal hash. |
| bytes_256_a | bytes_payload | SAME | SAME | Same input and same marshal hash. |
| bytes_65535_a | bytes_payload | SAME | SAME | Same input and same marshal hash. |
| bytes_65536_a | bytes_payload | SAME | SAME | Same input and same marshal hash. |
| bytes_all_byte_values | bytes_payload | SAME | SAME | Same input and same marshal hash. |
| bytes_empty | bytes_payload | SAME | SAME | Same input and same marshal hash. |
| bytes_high_values_with_ascii | bytes_payload | SAME | SAME | Same input and same marshal hash. |
| bytes_single_nul | bytes_payload | SAME | SAME | Same input and same marshal hash. |
| chinese_text | unicode_string | SAME | SAME | Same input and same marshal hash. |
| complex_inf_neg_inf | float_complex | SAME | SAME | Same input and same marshal hash. |
| complex_nan_both | float_complex | SAME | SAME | Same input and same marshal hash. |
| complex_nan_imag | float_complex | SAME | SAME | Same input and same marshal hash. |
| complex_nan_real | float_complex | SAME | SAME | Same input and same marshal hash. |
| complex_payload_nan_imag | float_complex | SAME | SAME | Same input and same marshal hash. |
| complex_payload_nan_real | float_complex | SAME | SAME | Same input and same marshal hash. |
| complex_regular | float_complex | SAME | SAME | Same input and same marshal hash. |
| complex_zero_neg_zero | float_complex | SAME | SAME | Same input and same marshal hash. |
| composed_e_acute | unicode_string | SAME | SAME | Same input and same marshal hash. |
| constant_ellipsis | basic_scalar_constant | SAME | SAME | Same input and same marshal hash. |
| constant_false | basic_scalar_constant | SAME | SAME | Same input and same marshal hash. |
| constant_none | basic_scalar_constant | SAME | SAME | Same input and same marshal hash. |
| constant_true | basic_scalar_constant | SAME | SAME | Same input and same marshal hash. |
| crlf_string | unicode_string | SAME | SAME | Same input and same marshal hash. |
| decomposed_e_acute | unicode_string | SAME | SAME | Same input and same marshal hash. |
| emoji_text | unicode_string | SAME | SAME | Same input and same marshal hash. |
| float_huge_1e300 | float_complex | SAME | SAME | Same input and same marshal hash. |
| float_math_nan | float_complex | SAME | SAME | Same input and same marshal hash. |
| float_nan_constructor | float_complex | SAME | SAME | Same input and same marshal hash. |
| float_nan_payload_0x7ff0000000000001 | float_complex | SAME | SAME | Same input and same marshal hash. |
| float_nan_payload_0x7ff8000000000001 | float_complex | SAME | SAME | Same input and same marshal hash. |
| float_nan_payload_0x7ff8000000000002 | float_complex | SAME | SAME | Same input and same marshal hash. |
| float_neg_inf | float_complex | SAME | SAME | Same input and same marshal hash. |
| float_neg_one | float_complex | SAME | SAME | Same input and same marshal hash. |
| float_neg_zero | float_complex | SAME | SAME | Same input and same marshal hash. |
| float_pos_inf | float_complex | SAME | SAME | Same input and same marshal hash. |
| float_pos_one | float_complex | SAME | SAME | Same input and same marshal hash. |
| float_pos_zero | float_complex | SAME | SAME | Same input and same marshal hash. |
| float_tiny_1e_minus_300 | float_complex | SAME | SAME | Same input and same marshal hash. |
| lone_high_surrogate | unicode_string | SAME | SAME | Same input and same marshal hash. |
| non_bmp_character | unicode_string | SAME | SAME | Same input and same marshal hash. |
| nul_inside_string | unicode_string | SAME | SAME | Same input and same marshal hash. |
| recreated_complex_nan_both | float_complex | SAME | SAME | Same input and same marshal hash. |
| recreated_float_nan | float_complex | SAME | SAME | Same input and same marshal hash. |
| slice_1_10_2 | optional_slice_probe | DIFFERENT | SAME | Same optional support boundary or exception behavior. |
| slice_neg10_none_neg1 | optional_slice_probe | DIFFERENT | SAME | Same optional support boundary or exception behavior. |
| slice_none_none_none | optional_slice_probe | DIFFERENT | SAME | Same optional support boundary or exception behavior. |
| zero_width_joiner_sequence | unicode_string | SAME | SAME | Same input and same marshal hash. |

### member_b_all_linux_x86_64_py3_10_results (Linux/x86_64, Python 3.10.20) vs member_b_all_linux_x86_64_py3_11_results (Linux/x86_64, Python 3.11.15)

| Case | Category | Same marshal hash | Same exception | Interpretation |
| --- | --- | --- | --- | --- |
| ascii_plain | unicode_string | SAME | SAME | Same input and same marshal hash. |
| bytes_255_a | bytes_payload | SAME | SAME | Same input and same marshal hash. |
| bytes_256_a | bytes_payload | SAME | SAME | Same input and same marshal hash. |
| bytes_65535_a | bytes_payload | SAME | SAME | Same input and same marshal hash. |
| bytes_65536_a | bytes_payload | SAME | SAME | Same input and same marshal hash. |
| bytes_all_byte_values | bytes_payload | SAME | SAME | Same input and same marshal hash. |
| bytes_empty | bytes_payload | SAME | SAME | Same input and same marshal hash. |
| bytes_high_values_with_ascii | bytes_payload | SAME | SAME | Same input and same marshal hash. |
| bytes_single_nul | bytes_payload | SAME | SAME | Same input and same marshal hash. |
| chinese_text | unicode_string | SAME | SAME | Same input and same marshal hash. |
| complex_inf_neg_inf | float_complex | SAME | SAME | Same input and same marshal hash. |
| complex_nan_both | float_complex | SAME | SAME | Same input and same marshal hash. |
| complex_nan_imag | float_complex | SAME | SAME | Same input and same marshal hash. |
| complex_nan_real | float_complex | SAME | SAME | Same input and same marshal hash. |
| complex_payload_nan_imag | float_complex | SAME | SAME | Same input and same marshal hash. |
| complex_payload_nan_real | float_complex | SAME | SAME | Same input and same marshal hash. |
| complex_regular | float_complex | SAME | SAME | Same input and same marshal hash. |
| complex_zero_neg_zero | float_complex | SAME | SAME | Same input and same marshal hash. |
| composed_e_acute | unicode_string | SAME | SAME | Same input and same marshal hash. |
| constant_ellipsis | basic_scalar_constant | SAME | SAME | Same input and same marshal hash. |
| constant_false | basic_scalar_constant | SAME | SAME | Same input and same marshal hash. |
| constant_none | basic_scalar_constant | SAME | SAME | Same input and same marshal hash. |
| constant_true | basic_scalar_constant | SAME | SAME | Same input and same marshal hash. |
| crlf_string | unicode_string | SAME | SAME | Same input and same marshal hash. |
| decomposed_e_acute | unicode_string | SAME | SAME | Same input and same marshal hash. |
| emoji_text | unicode_string | SAME | SAME | Same input and same marshal hash. |
| float_huge_1e300 | float_complex | SAME | SAME | Same input and same marshal hash. |
| float_math_nan | float_complex | SAME | SAME | Same input and same marshal hash. |
| float_nan_constructor | float_complex | SAME | SAME | Same input and same marshal hash. |
| float_nan_payload_0x7ff0000000000001 | float_complex | SAME | SAME | Same input and same marshal hash. |
| float_nan_payload_0x7ff8000000000001 | float_complex | SAME | SAME | Same input and same marshal hash. |
| float_nan_payload_0x7ff8000000000002 | float_complex | SAME | SAME | Same input and same marshal hash. |
| float_neg_inf | float_complex | SAME | SAME | Same input and same marshal hash. |
| float_neg_one | float_complex | SAME | SAME | Same input and same marshal hash. |
| float_neg_zero | float_complex | SAME | SAME | Same input and same marshal hash. |
| float_pos_inf | float_complex | SAME | SAME | Same input and same marshal hash. |
| float_pos_one | float_complex | SAME | SAME | Same input and same marshal hash. |
| float_pos_zero | float_complex | SAME | SAME | Same input and same marshal hash. |
| float_tiny_1e_minus_300 | float_complex | SAME | SAME | Same input and same marshal hash. |
| lone_high_surrogate | unicode_string | SAME | SAME | Same input and same marshal hash. |
| non_bmp_character | unicode_string | SAME | SAME | Same input and same marshal hash. |
| nul_inside_string | unicode_string | SAME | SAME | Same input and same marshal hash. |
| recreated_complex_nan_both | float_complex | SAME | SAME | Same input and same marshal hash. |
| recreated_float_nan | float_complex | SAME | SAME | Same input and same marshal hash. |
| slice_1_10_2 | optional_slice_probe | DIFFERENT | SAME | Same optional support boundary or exception behavior. |
| slice_neg10_none_neg1 | optional_slice_probe | DIFFERENT | SAME | Same optional support boundary or exception behavior. |
| slice_none_none_none | optional_slice_probe | DIFFERENT | SAME | Same optional support boundary or exception behavior. |
| zero_width_joiner_sequence | unicode_string | SAME | SAME | Same input and same marshal hash. |

### member_b_all_linux_x86_64_py3_10_results (Linux/x86_64, Python 3.10.20) vs member_b_all_linux_x86_64_py3_12_results (Linux/x86_64, Python 3.12.13)

| Case | Category | Same marshal hash | Same exception | Interpretation |
| --- | --- | --- | --- | --- |
| ascii_plain | unicode_string | SAME | SAME | Same input and same marshal hash. |
| bytes_255_a | bytes_payload | SAME | SAME | Same input and same marshal hash. |
| bytes_256_a | bytes_payload | SAME | SAME | Same input and same marshal hash. |
| bytes_65535_a | bytes_payload | SAME | SAME | Same input and same marshal hash. |
| bytes_65536_a | bytes_payload | SAME | SAME | Same input and same marshal hash. |
| bytes_all_byte_values | bytes_payload | SAME | SAME | Same input and same marshal hash. |
| bytes_empty | bytes_payload | SAME | SAME | Same input and same marshal hash. |
| bytes_high_values_with_ascii | bytes_payload | SAME | SAME | Same input and same marshal hash. |
| bytes_single_nul | bytes_payload | SAME | SAME | Same input and same marshal hash. |
| chinese_text | unicode_string | SAME | SAME | Same input and same marshal hash. |
| complex_inf_neg_inf | float_complex | SAME | SAME | Same input and same marshal hash. |
| complex_nan_both | float_complex | SAME | SAME | Same input and same marshal hash. |
| complex_nan_imag | float_complex | SAME | SAME | Same input and same marshal hash. |
| complex_nan_real | float_complex | SAME | SAME | Same input and same marshal hash. |
| complex_payload_nan_imag | float_complex | SAME | SAME | Same input and same marshal hash. |
| complex_payload_nan_real | float_complex | SAME | SAME | Same input and same marshal hash. |
| complex_regular | float_complex | SAME | SAME | Same input and same marshal hash. |
| complex_zero_neg_zero | float_complex | SAME | SAME | Same input and same marshal hash. |
| composed_e_acute | unicode_string | DIFFERENT | SAME | Same input representation but Python major/minor differs; likely version-level marshal format difference. |
| constant_ellipsis | basic_scalar_constant | SAME | SAME | Same input and same marshal hash. |
| constant_false | basic_scalar_constant | SAME | SAME | Same input and same marshal hash. |
| constant_none | basic_scalar_constant | SAME | SAME | Same input and same marshal hash. |
| constant_true | basic_scalar_constant | SAME | SAME | Same input and same marshal hash. |
| crlf_string | unicode_string | SAME | SAME | Same input and same marshal hash. |
| decomposed_e_acute | unicode_string | SAME | SAME | Same input and same marshal hash. |
| emoji_text | unicode_string | SAME | SAME | Same input and same marshal hash. |
| float_huge_1e300 | float_complex | SAME | SAME | Same input and same marshal hash. |
| float_math_nan | float_complex | SAME | SAME | Same input and same marshal hash. |
| float_nan_constructor | float_complex | SAME | SAME | Same input and same marshal hash. |
| float_nan_payload_0x7ff0000000000001 | float_complex | SAME | SAME | Same input and same marshal hash. |
| float_nan_payload_0x7ff8000000000001 | float_complex | SAME | SAME | Same input and same marshal hash. |
| float_nan_payload_0x7ff8000000000002 | float_complex | SAME | SAME | Same input and same marshal hash. |
| float_neg_inf | float_complex | SAME | SAME | Same input and same marshal hash. |
| float_neg_one | float_complex | SAME | SAME | Same input and same marshal hash. |
| float_neg_zero | float_complex | SAME | SAME | Same input and same marshal hash. |
| float_pos_inf | float_complex | SAME | SAME | Same input and same marshal hash. |
| float_pos_one | float_complex | SAME | SAME | Same input and same marshal hash. |
| float_pos_zero | float_complex | SAME | SAME | Same input and same marshal hash. |
| float_tiny_1e_minus_300 | float_complex | SAME | SAME | Same input and same marshal hash. |
| lone_high_surrogate | unicode_string | SAME | SAME | Same input and same marshal hash. |
| non_bmp_character | unicode_string | SAME | SAME | Same input and same marshal hash. |
| nul_inside_string | unicode_string | SAME | SAME | Same input and same marshal hash. |
| recreated_complex_nan_both | float_complex | SAME | SAME | Same input and same marshal hash. |
| recreated_float_nan | float_complex | SAME | SAME | Same input and same marshal hash. |
| slice_1_10_2 | optional_slice_probe | DIFFERENT | SAME | Same optional support boundary or exception behavior. |
| slice_neg10_none_neg1 | optional_slice_probe | DIFFERENT | SAME | Same optional support boundary or exception behavior. |
| slice_none_none_none | optional_slice_probe | DIFFERENT | SAME | Same optional support boundary or exception behavior. |
| zero_width_joiner_sequence | unicode_string | SAME | SAME | Same input and same marshal hash. |

### member_b_all_linux_x86_64_py3_10_results (Linux/x86_64, Python 3.10.20) vs member_b_all_linux_x86_64_py3_13_results (Linux/x86_64, Python 3.13.13)

| Case | Category | Same marshal hash | Same exception | Interpretation |
| --- | --- | --- | --- | --- |
| ascii_plain | unicode_string | SAME | SAME | Same input and same marshal hash. |
| bytes_255_a | bytes_payload | SAME | SAME | Same input and same marshal hash. |
| bytes_256_a | bytes_payload | SAME | SAME | Same input and same marshal hash. |
| bytes_65535_a | bytes_payload | SAME | SAME | Same input and same marshal hash. |
| bytes_65536_a | bytes_payload | SAME | SAME | Same input and same marshal hash. |
| bytes_all_byte_values | bytes_payload | SAME | SAME | Same input and same marshal hash. |
| bytes_empty | bytes_payload | SAME | SAME | Same input and same marshal hash. |
| bytes_high_values_with_ascii | bytes_payload | SAME | SAME | Same input and same marshal hash. |
| bytes_single_nul | bytes_payload | SAME | SAME | Same input and same marshal hash. |
| chinese_text | unicode_string | SAME | SAME | Same input and same marshal hash. |
| complex_inf_neg_inf | float_complex | SAME | SAME | Same input and same marshal hash. |
| complex_nan_both | float_complex | SAME | SAME | Same input and same marshal hash. |
| complex_nan_imag | float_complex | SAME | SAME | Same input and same marshal hash. |
| complex_nan_real | float_complex | SAME | SAME | Same input and same marshal hash. |
| complex_payload_nan_imag | float_complex | SAME | SAME | Same input and same marshal hash. |
| complex_payload_nan_real | float_complex | SAME | SAME | Same input and same marshal hash. |
| complex_regular | float_complex | SAME | SAME | Same input and same marshal hash. |
| complex_zero_neg_zero | float_complex | SAME | SAME | Same input and same marshal hash. |
| composed_e_acute | unicode_string | DIFFERENT | SAME | Same input representation but Python major/minor differs; likely version-level marshal format difference. |
| constant_ellipsis | basic_scalar_constant | SAME | SAME | Same input and same marshal hash. |
| constant_false | basic_scalar_constant | SAME | SAME | Same input and same marshal hash. |
| constant_none | basic_scalar_constant | SAME | SAME | Same input and same marshal hash. |
| constant_true | basic_scalar_constant | SAME | SAME | Same input and same marshal hash. |
| crlf_string | unicode_string | SAME | SAME | Same input and same marshal hash. |
| decomposed_e_acute | unicode_string | SAME | SAME | Same input and same marshal hash. |
| emoji_text | unicode_string | SAME | SAME | Same input and same marshal hash. |
| float_huge_1e300 | float_complex | SAME | SAME | Same input and same marshal hash. |
| float_math_nan | float_complex | SAME | SAME | Same input and same marshal hash. |
| float_nan_constructor | float_complex | SAME | SAME | Same input and same marshal hash. |
| float_nan_payload_0x7ff0000000000001 | float_complex | SAME | SAME | Same input and same marshal hash. |
| float_nan_payload_0x7ff8000000000001 | float_complex | SAME | SAME | Same input and same marshal hash. |
| float_nan_payload_0x7ff8000000000002 | float_complex | SAME | SAME | Same input and same marshal hash. |
| float_neg_inf | float_complex | SAME | SAME | Same input and same marshal hash. |
| float_neg_one | float_complex | SAME | SAME | Same input and same marshal hash. |
| float_neg_zero | float_complex | SAME | SAME | Same input and same marshal hash. |
| float_pos_inf | float_complex | SAME | SAME | Same input and same marshal hash. |
| float_pos_one | float_complex | SAME | SAME | Same input and same marshal hash. |
| float_pos_zero | float_complex | SAME | SAME | Same input and same marshal hash. |
| float_tiny_1e_minus_300 | float_complex | SAME | SAME | Same input and same marshal hash. |
| lone_high_surrogate | unicode_string | SAME | SAME | Same input and same marshal hash. |
| non_bmp_character | unicode_string | SAME | SAME | Same input and same marshal hash. |
| nul_inside_string | unicode_string | SAME | SAME | Same input and same marshal hash. |
| recreated_complex_nan_both | float_complex | SAME | SAME | Same input and same marshal hash. |
| recreated_float_nan | float_complex | SAME | SAME | Same input and same marshal hash. |
| slice_1_10_2 | optional_slice_probe | DIFFERENT | SAME | Same optional support boundary or exception behavior. |
| slice_neg10_none_neg1 | optional_slice_probe | DIFFERENT | SAME | Same optional support boundary or exception behavior. |
| slice_none_none_none | optional_slice_probe | DIFFERENT | SAME | Same optional support boundary or exception behavior. |
| zero_width_joiner_sequence | unicode_string | SAME | SAME | Same input and same marshal hash. |

### member_b_all_linux_x86_64_py3_10_results (Linux/x86_64, Python 3.10.20) vs member_b_all_linux_x86_64_py3_9_results (Linux/x86_64, Python 3.9.25)

| Case | Category | Same marshal hash | Same exception | Interpretation |
| --- | --- | --- | --- | --- |
| ascii_plain | unicode_string | SAME | SAME | Same input and same marshal hash. |
| bytes_255_a | bytes_payload | SAME | SAME | Same input and same marshal hash. |
| bytes_256_a | bytes_payload | SAME | SAME | Same input and same marshal hash. |
| bytes_65535_a | bytes_payload | SAME | SAME | Same input and same marshal hash. |
| bytes_65536_a | bytes_payload | SAME | SAME | Same input and same marshal hash. |
| bytes_all_byte_values | bytes_payload | SAME | SAME | Same input and same marshal hash. |
| bytes_empty | bytes_payload | SAME | SAME | Same input and same marshal hash. |
| bytes_high_values_with_ascii | bytes_payload | SAME | SAME | Same input and same marshal hash. |
| bytes_single_nul | bytes_payload | SAME | SAME | Same input and same marshal hash. |
| chinese_text | unicode_string | SAME | SAME | Same input and same marshal hash. |
| complex_inf_neg_inf | float_complex | SAME | SAME | Same input and same marshal hash. |
| complex_nan_both | float_complex | SAME | SAME | Same input and same marshal hash. |
| complex_nan_imag | float_complex | SAME | SAME | Same input and same marshal hash. |
| complex_nan_real | float_complex | SAME | SAME | Same input and same marshal hash. |
| complex_payload_nan_imag | float_complex | SAME | SAME | Same input and same marshal hash. |
| complex_payload_nan_real | float_complex | SAME | SAME | Same input and same marshal hash. |
| complex_regular | float_complex | SAME | SAME | Same input and same marshal hash. |
| complex_zero_neg_zero | float_complex | SAME | SAME | Same input and same marshal hash. |
| composed_e_acute | unicode_string | SAME | SAME | Same input and same marshal hash. |
| constant_ellipsis | basic_scalar_constant | SAME | SAME | Same input and same marshal hash. |
| constant_false | basic_scalar_constant | SAME | SAME | Same input and same marshal hash. |
| constant_none | basic_scalar_constant | SAME | SAME | Same input and same marshal hash. |
| constant_true | basic_scalar_constant | SAME | SAME | Same input and same marshal hash. |
| crlf_string | unicode_string | SAME | SAME | Same input and same marshal hash. |
| decomposed_e_acute | unicode_string | SAME | SAME | Same input and same marshal hash. |
| emoji_text | unicode_string | SAME | SAME | Same input and same marshal hash. |
| float_huge_1e300 | float_complex | SAME | SAME | Same input and same marshal hash. |
| float_math_nan | float_complex | SAME | SAME | Same input and same marshal hash. |
| float_nan_constructor | float_complex | SAME | SAME | Same input and same marshal hash. |
| float_nan_payload_0x7ff0000000000001 | float_complex | SAME | SAME | Same input and same marshal hash. |
| float_nan_payload_0x7ff8000000000001 | float_complex | SAME | SAME | Same input and same marshal hash. |
| float_nan_payload_0x7ff8000000000002 | float_complex | SAME | SAME | Same input and same marshal hash. |
| float_neg_inf | float_complex | SAME | SAME | Same input and same marshal hash. |
| float_neg_one | float_complex | SAME | SAME | Same input and same marshal hash. |
| float_neg_zero | float_complex | SAME | SAME | Same input and same marshal hash. |
| float_pos_inf | float_complex | SAME | SAME | Same input and same marshal hash. |
| float_pos_one | float_complex | SAME | SAME | Same input and same marshal hash. |
| float_pos_zero | float_complex | SAME | SAME | Same input and same marshal hash. |
| float_tiny_1e_minus_300 | float_complex | SAME | SAME | Same input and same marshal hash. |
| lone_high_surrogate | unicode_string | SAME | SAME | Same input and same marshal hash. |
| non_bmp_character | unicode_string | SAME | SAME | Same input and same marshal hash. |
| nul_inside_string | unicode_string | SAME | SAME | Same input and same marshal hash. |
| recreated_complex_nan_both | float_complex | SAME | SAME | Same input and same marshal hash. |
| recreated_float_nan | float_complex | SAME | SAME | Same input and same marshal hash. |
| slice_1_10_2 | optional_slice_probe | DIFFERENT | SAME | Same optional support boundary or exception behavior. |
| slice_neg10_none_neg1 | optional_slice_probe | DIFFERENT | SAME | Same optional support boundary or exception behavior. |
| slice_none_none_none | optional_slice_probe | DIFFERENT | SAME | Same optional support boundary or exception behavior. |
| zero_width_joiner_sequence | unicode_string | SAME | SAME | Same input and same marshal hash. |

### member_b_all_linux_x86_64_py3_10_results (Linux/x86_64, Python 3.10.20) vs member_b_all_windows_amd64_py3_10_results (Windows/AMD64, Python 3.10.11)

| Case | Category | Same marshal hash | Same exception | Interpretation |
| --- | --- | --- | --- | --- |
| ascii_plain | unicode_string | SAME | SAME | Same input and same marshal hash. |
| bytes_255_a | bytes_payload | SAME | SAME | Same input and same marshal hash. |
| bytes_256_a | bytes_payload | SAME | SAME | Same input and same marshal hash. |
| bytes_65535_a | bytes_payload | SAME | SAME | Same input and same marshal hash. |
| bytes_65536_a | bytes_payload | SAME | SAME | Same input and same marshal hash. |
| bytes_all_byte_values | bytes_payload | SAME | SAME | Same input and same marshal hash. |
| bytes_empty | bytes_payload | SAME | SAME | Same input and same marshal hash. |
| bytes_high_values_with_ascii | bytes_payload | SAME | SAME | Same input and same marshal hash. |
| bytes_single_nul | bytes_payload | SAME | SAME | Same input and same marshal hash. |
| chinese_text | unicode_string | SAME | SAME | Same input and same marshal hash. |
| complex_inf_neg_inf | float_complex | SAME | SAME | Same input and same marshal hash. |
| complex_nan_both | float_complex | SAME | SAME | Same input and same marshal hash. |
| complex_nan_imag | float_complex | SAME | SAME | Same input and same marshal hash. |
| complex_nan_real | float_complex | SAME | SAME | Same input and same marshal hash. |
| complex_payload_nan_imag | float_complex | SAME | SAME | Same input and same marshal hash. |
| complex_payload_nan_real | float_complex | SAME | SAME | Same input and same marshal hash. |
| complex_regular | float_complex | SAME | SAME | Same input and same marshal hash. |
| complex_zero_neg_zero | float_complex | SAME | SAME | Same input and same marshal hash. |
| composed_e_acute | unicode_string | SAME | SAME | Same input and same marshal hash. |
| constant_ellipsis | basic_scalar_constant | SAME | SAME | Same input and same marshal hash. |
| constant_false | basic_scalar_constant | SAME | SAME | Same input and same marshal hash. |
| constant_none | basic_scalar_constant | SAME | SAME | Same input and same marshal hash. |
| constant_true | basic_scalar_constant | SAME | SAME | Same input and same marshal hash. |
| crlf_string | unicode_string | SAME | SAME | Same input and same marshal hash. |
| decomposed_e_acute | unicode_string | SAME | SAME | Same input and same marshal hash. |
| emoji_text | unicode_string | SAME | SAME | Same input and same marshal hash. |
| float_huge_1e300 | float_complex | SAME | SAME | Same input and same marshal hash. |
| float_math_nan | float_complex | SAME | SAME | Same input and same marshal hash. |
| float_nan_constructor | float_complex | SAME | SAME | Same input and same marshal hash. |
| float_nan_payload_0x7ff0000000000001 | float_complex | SAME | SAME | Same input and same marshal hash. |
| float_nan_payload_0x7ff8000000000001 | float_complex | SAME | SAME | Same input and same marshal hash. |
| float_nan_payload_0x7ff8000000000002 | float_complex | SAME | SAME | Same input and same marshal hash. |
| float_neg_inf | float_complex | SAME | SAME | Same input and same marshal hash. |
| float_neg_one | float_complex | SAME | SAME | Same input and same marshal hash. |
| float_neg_zero | float_complex | SAME | SAME | Same input and same marshal hash. |
| float_pos_inf | float_complex | SAME | SAME | Same input and same marshal hash. |
| float_pos_one | float_complex | SAME | SAME | Same input and same marshal hash. |
| float_pos_zero | float_complex | SAME | SAME | Same input and same marshal hash. |
| float_tiny_1e_minus_300 | float_complex | SAME | SAME | Same input and same marshal hash. |
| lone_high_surrogate | unicode_string | SAME | SAME | Same input and same marshal hash. |
| non_bmp_character | unicode_string | SAME | SAME | Same input and same marshal hash. |
| nul_inside_string | unicode_string | SAME | SAME | Same input and same marshal hash. |
| recreated_complex_nan_both | float_complex | SAME | SAME | Same input and same marshal hash. |
| recreated_float_nan | float_complex | SAME | SAME | Same input and same marshal hash. |
| slice_1_10_2 | optional_slice_probe | DIFFERENT | SAME | Same optional support boundary or exception behavior. |
| slice_neg10_none_neg1 | optional_slice_probe | DIFFERENT | SAME | Same optional support boundary or exception behavior. |
| slice_none_none_none | optional_slice_probe | DIFFERENT | SAME | Same optional support boundary or exception behavior. |
| zero_width_joiner_sequence | unicode_string | SAME | SAME | Same input and same marshal hash. |

### member_b_all_linux_x86_64_py3_10_results (Linux/x86_64, Python 3.10.20) vs member_b_all_windows_amd64_py3_11_results (Windows/AMD64, Python 3.11.9)

| Case | Category | Same marshal hash | Same exception | Interpretation |
| --- | --- | --- | --- | --- |
| ascii_plain | unicode_string | SAME | SAME | Same input and same marshal hash. |
| bytes_255_a | bytes_payload | SAME | SAME | Same input and same marshal hash. |
| bytes_256_a | bytes_payload | SAME | SAME | Same input and same marshal hash. |
| bytes_65535_a | bytes_payload | SAME | SAME | Same input and same marshal hash. |
| bytes_65536_a | bytes_payload | SAME | SAME | Same input and same marshal hash. |
| bytes_all_byte_values | bytes_payload | SAME | SAME | Same input and same marshal hash. |
| bytes_empty | bytes_payload | SAME | SAME | Same input and same marshal hash. |
| bytes_high_values_with_ascii | bytes_payload | SAME | SAME | Same input and same marshal hash. |
| bytes_single_nul | bytes_payload | SAME | SAME | Same input and same marshal hash. |
| chinese_text | unicode_string | SAME | SAME | Same input and same marshal hash. |
| complex_inf_neg_inf | float_complex | SAME | SAME | Same input and same marshal hash. |
| complex_nan_both | float_complex | SAME | SAME | Same input and same marshal hash. |
| complex_nan_imag | float_complex | SAME | SAME | Same input and same marshal hash. |
| complex_nan_real | float_complex | SAME | SAME | Same input and same marshal hash. |
| complex_payload_nan_imag | float_complex | SAME | SAME | Same input and same marshal hash. |
| complex_payload_nan_real | float_complex | SAME | SAME | Same input and same marshal hash. |
| complex_regular | float_complex | SAME | SAME | Same input and same marshal hash. |
| complex_zero_neg_zero | float_complex | SAME | SAME | Same input and same marshal hash. |
| composed_e_acute | unicode_string | SAME | SAME | Same input and same marshal hash. |
| constant_ellipsis | basic_scalar_constant | SAME | SAME | Same input and same marshal hash. |
| constant_false | basic_scalar_constant | SAME | SAME | Same input and same marshal hash. |
| constant_none | basic_scalar_constant | SAME | SAME | Same input and same marshal hash. |
| constant_true | basic_scalar_constant | SAME | SAME | Same input and same marshal hash. |
| crlf_string | unicode_string | SAME | SAME | Same input and same marshal hash. |
| decomposed_e_acute | unicode_string | SAME | SAME | Same input and same marshal hash. |
| emoji_text | unicode_string | SAME | SAME | Same input and same marshal hash. |
| float_huge_1e300 | float_complex | SAME | SAME | Same input and same marshal hash. |
| float_math_nan | float_complex | SAME | SAME | Same input and same marshal hash. |
| float_nan_constructor | float_complex | SAME | SAME | Same input and same marshal hash. |
| float_nan_payload_0x7ff0000000000001 | float_complex | SAME | SAME | Same input and same marshal hash. |
| float_nan_payload_0x7ff8000000000001 | float_complex | SAME | SAME | Same input and same marshal hash. |
| float_nan_payload_0x7ff8000000000002 | float_complex | SAME | SAME | Same input and same marshal hash. |
| float_neg_inf | float_complex | SAME | SAME | Same input and same marshal hash. |
| float_neg_one | float_complex | SAME | SAME | Same input and same marshal hash. |
| float_neg_zero | float_complex | SAME | SAME | Same input and same marshal hash. |
| float_pos_inf | float_complex | SAME | SAME | Same input and same marshal hash. |
| float_pos_one | float_complex | SAME | SAME | Same input and same marshal hash. |
| float_pos_zero | float_complex | SAME | SAME | Same input and same marshal hash. |
| float_tiny_1e_minus_300 | float_complex | SAME | SAME | Same input and same marshal hash. |
| lone_high_surrogate | unicode_string | SAME | SAME | Same input and same marshal hash. |
| non_bmp_character | unicode_string | SAME | SAME | Same input and same marshal hash. |
| nul_inside_string | unicode_string | SAME | SAME | Same input and same marshal hash. |
| recreated_complex_nan_both | float_complex | SAME | SAME | Same input and same marshal hash. |
| recreated_float_nan | float_complex | SAME | SAME | Same input and same marshal hash. |
| slice_1_10_2 | optional_slice_probe | DIFFERENT | SAME | Same optional support boundary or exception behavior. |
| slice_neg10_none_neg1 | optional_slice_probe | DIFFERENT | SAME | Same optional support boundary or exception behavior. |
| slice_none_none_none | optional_slice_probe | DIFFERENT | SAME | Same optional support boundary or exception behavior. |
| zero_width_joiner_sequence | unicode_string | SAME | SAME | Same input and same marshal hash. |

### member_b_all_linux_x86_64_py3_10_results (Linux/x86_64, Python 3.10.20) vs member_b_all_windows_amd64_py3_12_results (Windows/AMD64, Python 3.12.10)

| Case | Category | Same marshal hash | Same exception | Interpretation |
| --- | --- | --- | --- | --- |
| ascii_plain | unicode_string | SAME | SAME | Same input and same marshal hash. |
| bytes_255_a | bytes_payload | SAME | SAME | Same input and same marshal hash. |
| bytes_256_a | bytes_payload | SAME | SAME | Same input and same marshal hash. |
| bytes_65535_a | bytes_payload | SAME | SAME | Same input and same marshal hash. |
| bytes_65536_a | bytes_payload | SAME | SAME | Same input and same marshal hash. |
| bytes_all_byte_values | bytes_payload | SAME | SAME | Same input and same marshal hash. |
| bytes_empty | bytes_payload | SAME | SAME | Same input and same marshal hash. |
| bytes_high_values_with_ascii | bytes_payload | SAME | SAME | Same input and same marshal hash. |
| bytes_single_nul | bytes_payload | SAME | SAME | Same input and same marshal hash. |
| chinese_text | unicode_string | SAME | SAME | Same input and same marshal hash. |
| complex_inf_neg_inf | float_complex | SAME | SAME | Same input and same marshal hash. |
| complex_nan_both | float_complex | SAME | SAME | Same input and same marshal hash. |
| complex_nan_imag | float_complex | SAME | SAME | Same input and same marshal hash. |
| complex_nan_real | float_complex | SAME | SAME | Same input and same marshal hash. |
| complex_payload_nan_imag | float_complex | SAME | SAME | Same input and same marshal hash. |
| complex_payload_nan_real | float_complex | SAME | SAME | Same input and same marshal hash. |
| complex_regular | float_complex | SAME | SAME | Same input and same marshal hash. |
| complex_zero_neg_zero | float_complex | SAME | SAME | Same input and same marshal hash. |
| composed_e_acute | unicode_string | DIFFERENT | SAME | Same input representation but Python major/minor differs; likely version-level marshal format difference. |
| constant_ellipsis | basic_scalar_constant | SAME | SAME | Same input and same marshal hash. |
| constant_false | basic_scalar_constant | SAME | SAME | Same input and same marshal hash. |
| constant_none | basic_scalar_constant | SAME | SAME | Same input and same marshal hash. |
| constant_true | basic_scalar_constant | SAME | SAME | Same input and same marshal hash. |
| crlf_string | unicode_string | SAME | SAME | Same input and same marshal hash. |
| decomposed_e_acute | unicode_string | SAME | SAME | Same input and same marshal hash. |
| emoji_text | unicode_string | SAME | SAME | Same input and same marshal hash. |
| float_huge_1e300 | float_complex | SAME | SAME | Same input and same marshal hash. |
| float_math_nan | float_complex | SAME | SAME | Same input and same marshal hash. |
| float_nan_constructor | float_complex | SAME | SAME | Same input and same marshal hash. |
| float_nan_payload_0x7ff0000000000001 | float_complex | SAME | SAME | Same input and same marshal hash. |
| float_nan_payload_0x7ff8000000000001 | float_complex | SAME | SAME | Same input and same marshal hash. |
| float_nan_payload_0x7ff8000000000002 | float_complex | SAME | SAME | Same input and same marshal hash. |
| float_neg_inf | float_complex | SAME | SAME | Same input and same marshal hash. |
| float_neg_one | float_complex | SAME | SAME | Same input and same marshal hash. |
| float_neg_zero | float_complex | SAME | SAME | Same input and same marshal hash. |
| float_pos_inf | float_complex | SAME | SAME | Same input and same marshal hash. |
| float_pos_one | float_complex | SAME | SAME | Same input and same marshal hash. |
| float_pos_zero | float_complex | SAME | SAME | Same input and same marshal hash. |
| float_tiny_1e_minus_300 | float_complex | SAME | SAME | Same input and same marshal hash. |
| lone_high_surrogate | unicode_string | SAME | SAME | Same input and same marshal hash. |
| non_bmp_character | unicode_string | SAME | SAME | Same input and same marshal hash. |
| nul_inside_string | unicode_string | SAME | SAME | Same input and same marshal hash. |
| recreated_complex_nan_both | float_complex | SAME | SAME | Same input and same marshal hash. |
| recreated_float_nan | float_complex | SAME | SAME | Same input and same marshal hash. |
| slice_1_10_2 | optional_slice_probe | DIFFERENT | SAME | Same optional support boundary or exception behavior. |
| slice_neg10_none_neg1 | optional_slice_probe | DIFFERENT | SAME | Same optional support boundary or exception behavior. |
| slice_none_none_none | optional_slice_probe | DIFFERENT | SAME | Same optional support boundary or exception behavior. |
| zero_width_joiner_sequence | unicode_string | SAME | SAME | Same input and same marshal hash. |

### member_b_all_linux_x86_64_py3_10_results (Linux/x86_64, Python 3.10.20) vs member_b_all_windows_amd64_py3_13_results (Windows/AMD64, Python 3.13.13)

| Case | Category | Same marshal hash | Same exception | Interpretation |
| --- | --- | --- | --- | --- |
| ascii_plain | unicode_string | SAME | SAME | Same input and same marshal hash. |
| bytes_255_a | bytes_payload | SAME | SAME | Same input and same marshal hash. |
| bytes_256_a | bytes_payload | SAME | SAME | Same input and same marshal hash. |
| bytes_65535_a | bytes_payload | SAME | SAME | Same input and same marshal hash. |
| bytes_65536_a | bytes_payload | SAME | SAME | Same input and same marshal hash. |
| bytes_all_byte_values | bytes_payload | SAME | SAME | Same input and same marshal hash. |
| bytes_empty | bytes_payload | SAME | SAME | Same input and same marshal hash. |
| bytes_high_values_with_ascii | bytes_payload | SAME | SAME | Same input and same marshal hash. |
| bytes_single_nul | bytes_payload | SAME | SAME | Same input and same marshal hash. |
| chinese_text | unicode_string | SAME | SAME | Same input and same marshal hash. |
| complex_inf_neg_inf | float_complex | SAME | SAME | Same input and same marshal hash. |
| complex_nan_both | float_complex | SAME | SAME | Same input and same marshal hash. |
| complex_nan_imag | float_complex | SAME | SAME | Same input and same marshal hash. |
| complex_nan_real | float_complex | SAME | SAME | Same input and same marshal hash. |
| complex_payload_nan_imag | float_complex | SAME | SAME | Same input and same marshal hash. |
| complex_payload_nan_real | float_complex | SAME | SAME | Same input and same marshal hash. |
| complex_regular | float_complex | SAME | SAME | Same input and same marshal hash. |
| complex_zero_neg_zero | float_complex | SAME | SAME | Same input and same marshal hash. |
| composed_e_acute | unicode_string | DIFFERENT | SAME | Same input representation but Python major/minor differs; likely version-level marshal format difference. |
| constant_ellipsis | basic_scalar_constant | SAME | SAME | Same input and same marshal hash. |
| constant_false | basic_scalar_constant | SAME | SAME | Same input and same marshal hash. |
| constant_none | basic_scalar_constant | SAME | SAME | Same input and same marshal hash. |
| constant_true | basic_scalar_constant | SAME | SAME | Same input and same marshal hash. |
| crlf_string | unicode_string | SAME | SAME | Same input and same marshal hash. |
| decomposed_e_acute | unicode_string | SAME | SAME | Same input and same marshal hash. |
| emoji_text | unicode_string | SAME | SAME | Same input and same marshal hash. |
| float_huge_1e300 | float_complex | SAME | SAME | Same input and same marshal hash. |
| float_math_nan | float_complex | SAME | SAME | Same input and same marshal hash. |
| float_nan_constructor | float_complex | SAME | SAME | Same input and same marshal hash. |
| float_nan_payload_0x7ff0000000000001 | float_complex | SAME | SAME | Same input and same marshal hash. |
| float_nan_payload_0x7ff8000000000001 | float_complex | SAME | SAME | Same input and same marshal hash. |
| float_nan_payload_0x7ff8000000000002 | float_complex | SAME | SAME | Same input and same marshal hash. |
| float_neg_inf | float_complex | SAME | SAME | Same input and same marshal hash. |
| float_neg_one | float_complex | SAME | SAME | Same input and same marshal hash. |
| float_neg_zero | float_complex | SAME | SAME | Same input and same marshal hash. |
| float_pos_inf | float_complex | SAME | SAME | Same input and same marshal hash. |
| float_pos_one | float_complex | SAME | SAME | Same input and same marshal hash. |
| float_pos_zero | float_complex | SAME | SAME | Same input and same marshal hash. |
| float_tiny_1e_minus_300 | float_complex | SAME | SAME | Same input and same marshal hash. |
| lone_high_surrogate | unicode_string | SAME | SAME | Same input and same marshal hash. |
| non_bmp_character | unicode_string | SAME | SAME | Same input and same marshal hash. |
| nul_inside_string | unicode_string | SAME | SAME | Same input and same marshal hash. |
| recreated_complex_nan_both | float_complex | SAME | SAME | Same input and same marshal hash. |
| recreated_float_nan | float_complex | SAME | SAME | Same input and same marshal hash. |
| slice_1_10_2 | optional_slice_probe | DIFFERENT | SAME | Same optional support boundary or exception behavior. |
| slice_neg10_none_neg1 | optional_slice_probe | DIFFERENT | SAME | Same optional support boundary or exception behavior. |
| slice_none_none_none | optional_slice_probe | DIFFERENT | SAME | Same optional support boundary or exception behavior. |
| zero_width_joiner_sequence | unicode_string | SAME | SAME | Same input and same marshal hash. |

### member_b_all_linux_x86_64_py3_10_results (Linux/x86_64, Python 3.10.20) vs member_b_all_windows_amd64_py3_9_results (Windows/AMD64, Python 3.9.13)

| Case | Category | Same marshal hash | Same exception | Interpretation |
| --- | --- | --- | --- | --- |
| ascii_plain | unicode_string | SAME | SAME | Same input and same marshal hash. |
| bytes_255_a | bytes_payload | SAME | SAME | Same input and same marshal hash. |
| bytes_256_a | bytes_payload | SAME | SAME | Same input and same marshal hash. |
| bytes_65535_a | bytes_payload | SAME | SAME | Same input and same marshal hash. |
| bytes_65536_a | bytes_payload | SAME | SAME | Same input and same marshal hash. |
| bytes_all_byte_values | bytes_payload | SAME | SAME | Same input and same marshal hash. |
| bytes_empty | bytes_payload | SAME | SAME | Same input and same marshal hash. |
| bytes_high_values_with_ascii | bytes_payload | SAME | SAME | Same input and same marshal hash. |
| bytes_single_nul | bytes_payload | SAME | SAME | Same input and same marshal hash. |
| chinese_text | unicode_string | SAME | SAME | Same input and same marshal hash. |
| complex_inf_neg_inf | float_complex | SAME | SAME | Same input and same marshal hash. |
| complex_nan_both | float_complex | SAME | SAME | Same input and same marshal hash. |
| complex_nan_imag | float_complex | SAME | SAME | Same input and same marshal hash. |
| complex_nan_real | float_complex | SAME | SAME | Same input and same marshal hash. |
| complex_payload_nan_imag | float_complex | SAME | SAME | Same input and same marshal hash. |
| complex_payload_nan_real | float_complex | SAME | SAME | Same input and same marshal hash. |
| complex_regular | float_complex | SAME | SAME | Same input and same marshal hash. |
| complex_zero_neg_zero | float_complex | SAME | SAME | Same input and same marshal hash. |
| composed_e_acute | unicode_string | SAME | SAME | Same input and same marshal hash. |
| constant_ellipsis | basic_scalar_constant | SAME | SAME | Same input and same marshal hash. |
| constant_false | basic_scalar_constant | SAME | SAME | Same input and same marshal hash. |
| constant_none | basic_scalar_constant | SAME | SAME | Same input and same marshal hash. |
| constant_true | basic_scalar_constant | SAME | SAME | Same input and same marshal hash. |
| crlf_string | unicode_string | SAME | SAME | Same input and same marshal hash. |
| decomposed_e_acute | unicode_string | SAME | SAME | Same input and same marshal hash. |
| emoji_text | unicode_string | SAME | SAME | Same input and same marshal hash. |
| float_huge_1e300 | float_complex | SAME | SAME | Same input and same marshal hash. |
| float_math_nan | float_complex | SAME | SAME | Same input and same marshal hash. |
| float_nan_constructor | float_complex | SAME | SAME | Same input and same marshal hash. |
| float_nan_payload_0x7ff0000000000001 | float_complex | SAME | SAME | Same input and same marshal hash. |
| float_nan_payload_0x7ff8000000000001 | float_complex | SAME | SAME | Same input and same marshal hash. |
| float_nan_payload_0x7ff8000000000002 | float_complex | SAME | SAME | Same input and same marshal hash. |
| float_neg_inf | float_complex | SAME | SAME | Same input and same marshal hash. |
| float_neg_one | float_complex | SAME | SAME | Same input and same marshal hash. |
| float_neg_zero | float_complex | SAME | SAME | Same input and same marshal hash. |
| float_pos_inf | float_complex | SAME | SAME | Same input and same marshal hash. |
| float_pos_one | float_complex | SAME | SAME | Same input and same marshal hash. |
| float_pos_zero | float_complex | SAME | SAME | Same input and same marshal hash. |
| float_tiny_1e_minus_300 | float_complex | SAME | SAME | Same input and same marshal hash. |
| lone_high_surrogate | unicode_string | SAME | SAME | Same input and same marshal hash. |
| non_bmp_character | unicode_string | SAME | SAME | Same input and same marshal hash. |
| nul_inside_string | unicode_string | SAME | SAME | Same input and same marshal hash. |
| recreated_complex_nan_both | float_complex | SAME | SAME | Same input and same marshal hash. |
| recreated_float_nan | float_complex | SAME | SAME | Same input and same marshal hash. |
| slice_1_10_2 | optional_slice_probe | DIFFERENT | SAME | Same optional support boundary or exception behavior. |
| slice_neg10_none_neg1 | optional_slice_probe | DIFFERENT | SAME | Same optional support boundary or exception behavior. |
| slice_none_none_none | optional_slice_probe | DIFFERENT | SAME | Same optional support boundary or exception behavior. |
| zero_width_joiner_sequence | unicode_string | SAME | SAME | Same input and same marshal hash. |

### member_b_all_linux_x86_64_py3_11_results (Linux/x86_64, Python 3.11.15) vs member_b_all_linux_x86_64_py3_12_results (Linux/x86_64, Python 3.12.13)

| Case | Category | Same marshal hash | Same exception | Interpretation |
| --- | --- | --- | --- | --- |
| ascii_plain | unicode_string | SAME | SAME | Same input and same marshal hash. |
| bytes_255_a | bytes_payload | SAME | SAME | Same input and same marshal hash. |
| bytes_256_a | bytes_payload | SAME | SAME | Same input and same marshal hash. |
| bytes_65535_a | bytes_payload | SAME | SAME | Same input and same marshal hash. |
| bytes_65536_a | bytes_payload | SAME | SAME | Same input and same marshal hash. |
| bytes_all_byte_values | bytes_payload | SAME | SAME | Same input and same marshal hash. |
| bytes_empty | bytes_payload | SAME | SAME | Same input and same marshal hash. |
| bytes_high_values_with_ascii | bytes_payload | SAME | SAME | Same input and same marshal hash. |
| bytes_single_nul | bytes_payload | SAME | SAME | Same input and same marshal hash. |
| chinese_text | unicode_string | SAME | SAME | Same input and same marshal hash. |
| complex_inf_neg_inf | float_complex | SAME | SAME | Same input and same marshal hash. |
| complex_nan_both | float_complex | SAME | SAME | Same input and same marshal hash. |
| complex_nan_imag | float_complex | SAME | SAME | Same input and same marshal hash. |
| complex_nan_real | float_complex | SAME | SAME | Same input and same marshal hash. |
| complex_payload_nan_imag | float_complex | SAME | SAME | Same input and same marshal hash. |
| complex_payload_nan_real | float_complex | SAME | SAME | Same input and same marshal hash. |
| complex_regular | float_complex | SAME | SAME | Same input and same marshal hash. |
| complex_zero_neg_zero | float_complex | SAME | SAME | Same input and same marshal hash. |
| composed_e_acute | unicode_string | DIFFERENT | SAME | Same input representation but Python major/minor differs; likely version-level marshal format difference. |
| constant_ellipsis | basic_scalar_constant | SAME | SAME | Same input and same marshal hash. |
| constant_false | basic_scalar_constant | SAME | SAME | Same input and same marshal hash. |
| constant_none | basic_scalar_constant | SAME | SAME | Same input and same marshal hash. |
| constant_true | basic_scalar_constant | SAME | SAME | Same input and same marshal hash. |
| crlf_string | unicode_string | SAME | SAME | Same input and same marshal hash. |
| decomposed_e_acute | unicode_string | SAME | SAME | Same input and same marshal hash. |
| emoji_text | unicode_string | SAME | SAME | Same input and same marshal hash. |
| float_huge_1e300 | float_complex | SAME | SAME | Same input and same marshal hash. |
| float_math_nan | float_complex | SAME | SAME | Same input and same marshal hash. |
| float_nan_constructor | float_complex | SAME | SAME | Same input and same marshal hash. |
| float_nan_payload_0x7ff0000000000001 | float_complex | SAME | SAME | Same input and same marshal hash. |
| float_nan_payload_0x7ff8000000000001 | float_complex | SAME | SAME | Same input and same marshal hash. |
| float_nan_payload_0x7ff8000000000002 | float_complex | SAME | SAME | Same input and same marshal hash. |
| float_neg_inf | float_complex | SAME | SAME | Same input and same marshal hash. |
| float_neg_one | float_complex | SAME | SAME | Same input and same marshal hash. |
| float_neg_zero | float_complex | SAME | SAME | Same input and same marshal hash. |
| float_pos_inf | float_complex | SAME | SAME | Same input and same marshal hash. |
| float_pos_one | float_complex | SAME | SAME | Same input and same marshal hash. |
| float_pos_zero | float_complex | SAME | SAME | Same input and same marshal hash. |
| float_tiny_1e_minus_300 | float_complex | SAME | SAME | Same input and same marshal hash. |
| lone_high_surrogate | unicode_string | SAME | SAME | Same input and same marshal hash. |
| non_bmp_character | unicode_string | SAME | SAME | Same input and same marshal hash. |
| nul_inside_string | unicode_string | SAME | SAME | Same input and same marshal hash. |
| recreated_complex_nan_both | float_complex | SAME | SAME | Same input and same marshal hash. |
| recreated_float_nan | float_complex | SAME | SAME | Same input and same marshal hash. |
| slice_1_10_2 | optional_slice_probe | DIFFERENT | SAME | Same optional support boundary or exception behavior. |
| slice_neg10_none_neg1 | optional_slice_probe | DIFFERENT | SAME | Same optional support boundary or exception behavior. |
| slice_none_none_none | optional_slice_probe | DIFFERENT | SAME | Same optional support boundary or exception behavior. |
| zero_width_joiner_sequence | unicode_string | SAME | SAME | Same input and same marshal hash. |

### member_b_all_linux_x86_64_py3_11_results (Linux/x86_64, Python 3.11.15) vs member_b_all_linux_x86_64_py3_13_results (Linux/x86_64, Python 3.13.13)

| Case | Category | Same marshal hash | Same exception | Interpretation |
| --- | --- | --- | --- | --- |
| ascii_plain | unicode_string | SAME | SAME | Same input and same marshal hash. |
| bytes_255_a | bytes_payload | SAME | SAME | Same input and same marshal hash. |
| bytes_256_a | bytes_payload | SAME | SAME | Same input and same marshal hash. |
| bytes_65535_a | bytes_payload | SAME | SAME | Same input and same marshal hash. |
| bytes_65536_a | bytes_payload | SAME | SAME | Same input and same marshal hash. |
| bytes_all_byte_values | bytes_payload | SAME | SAME | Same input and same marshal hash. |
| bytes_empty | bytes_payload | SAME | SAME | Same input and same marshal hash. |
| bytes_high_values_with_ascii | bytes_payload | SAME | SAME | Same input and same marshal hash. |
| bytes_single_nul | bytes_payload | SAME | SAME | Same input and same marshal hash. |
| chinese_text | unicode_string | SAME | SAME | Same input and same marshal hash. |
| complex_inf_neg_inf | float_complex | SAME | SAME | Same input and same marshal hash. |
| complex_nan_both | float_complex | SAME | SAME | Same input and same marshal hash. |
| complex_nan_imag | float_complex | SAME | SAME | Same input and same marshal hash. |
| complex_nan_real | float_complex | SAME | SAME | Same input and same marshal hash. |
| complex_payload_nan_imag | float_complex | SAME | SAME | Same input and same marshal hash. |
| complex_payload_nan_real | float_complex | SAME | SAME | Same input and same marshal hash. |
| complex_regular | float_complex | SAME | SAME | Same input and same marshal hash. |
| complex_zero_neg_zero | float_complex | SAME | SAME | Same input and same marshal hash. |
| composed_e_acute | unicode_string | DIFFERENT | SAME | Same input representation but Python major/minor differs; likely version-level marshal format difference. |
| constant_ellipsis | basic_scalar_constant | SAME | SAME | Same input and same marshal hash. |
| constant_false | basic_scalar_constant | SAME | SAME | Same input and same marshal hash. |
| constant_none | basic_scalar_constant | SAME | SAME | Same input and same marshal hash. |
| constant_true | basic_scalar_constant | SAME | SAME | Same input and same marshal hash. |
| crlf_string | unicode_string | SAME | SAME | Same input and same marshal hash. |
| decomposed_e_acute | unicode_string | SAME | SAME | Same input and same marshal hash. |
| emoji_text | unicode_string | SAME | SAME | Same input and same marshal hash. |
| float_huge_1e300 | float_complex | SAME | SAME | Same input and same marshal hash. |
| float_math_nan | float_complex | SAME | SAME | Same input and same marshal hash. |
| float_nan_constructor | float_complex | SAME | SAME | Same input and same marshal hash. |
| float_nan_payload_0x7ff0000000000001 | float_complex | SAME | SAME | Same input and same marshal hash. |
| float_nan_payload_0x7ff8000000000001 | float_complex | SAME | SAME | Same input and same marshal hash. |
| float_nan_payload_0x7ff8000000000002 | float_complex | SAME | SAME | Same input and same marshal hash. |
| float_neg_inf | float_complex | SAME | SAME | Same input and same marshal hash. |
| float_neg_one | float_complex | SAME | SAME | Same input and same marshal hash. |
| float_neg_zero | float_complex | SAME | SAME | Same input and same marshal hash. |
| float_pos_inf | float_complex | SAME | SAME | Same input and same marshal hash. |
| float_pos_one | float_complex | SAME | SAME | Same input and same marshal hash. |
| float_pos_zero | float_complex | SAME | SAME | Same input and same marshal hash. |
| float_tiny_1e_minus_300 | float_complex | SAME | SAME | Same input and same marshal hash. |
| lone_high_surrogate | unicode_string | SAME | SAME | Same input and same marshal hash. |
| non_bmp_character | unicode_string | SAME | SAME | Same input and same marshal hash. |
| nul_inside_string | unicode_string | SAME | SAME | Same input and same marshal hash. |
| recreated_complex_nan_both | float_complex | SAME | SAME | Same input and same marshal hash. |
| recreated_float_nan | float_complex | SAME | SAME | Same input and same marshal hash. |
| slice_1_10_2 | optional_slice_probe | DIFFERENT | SAME | Same optional support boundary or exception behavior. |
| slice_neg10_none_neg1 | optional_slice_probe | DIFFERENT | SAME | Same optional support boundary or exception behavior. |
| slice_none_none_none | optional_slice_probe | DIFFERENT | SAME | Same optional support boundary or exception behavior. |
| zero_width_joiner_sequence | unicode_string | SAME | SAME | Same input and same marshal hash. |

### member_b_all_linux_x86_64_py3_11_results (Linux/x86_64, Python 3.11.15) vs member_b_all_linux_x86_64_py3_9_results (Linux/x86_64, Python 3.9.25)

| Case | Category | Same marshal hash | Same exception | Interpretation |
| --- | --- | --- | --- | --- |
| ascii_plain | unicode_string | SAME | SAME | Same input and same marshal hash. |
| bytes_255_a | bytes_payload | SAME | SAME | Same input and same marshal hash. |
| bytes_256_a | bytes_payload | SAME | SAME | Same input and same marshal hash. |
| bytes_65535_a | bytes_payload | SAME | SAME | Same input and same marshal hash. |
| bytes_65536_a | bytes_payload | SAME | SAME | Same input and same marshal hash. |
| bytes_all_byte_values | bytes_payload | SAME | SAME | Same input and same marshal hash. |
| bytes_empty | bytes_payload | SAME | SAME | Same input and same marshal hash. |
| bytes_high_values_with_ascii | bytes_payload | SAME | SAME | Same input and same marshal hash. |
| bytes_single_nul | bytes_payload | SAME | SAME | Same input and same marshal hash. |
| chinese_text | unicode_string | SAME | SAME | Same input and same marshal hash. |
| complex_inf_neg_inf | float_complex | SAME | SAME | Same input and same marshal hash. |
| complex_nan_both | float_complex | SAME | SAME | Same input and same marshal hash. |
| complex_nan_imag | float_complex | SAME | SAME | Same input and same marshal hash. |
| complex_nan_real | float_complex | SAME | SAME | Same input and same marshal hash. |
| complex_payload_nan_imag | float_complex | SAME | SAME | Same input and same marshal hash. |
| complex_payload_nan_real | float_complex | SAME | SAME | Same input and same marshal hash. |
| complex_regular | float_complex | SAME | SAME | Same input and same marshal hash. |
| complex_zero_neg_zero | float_complex | SAME | SAME | Same input and same marshal hash. |
| composed_e_acute | unicode_string | SAME | SAME | Same input and same marshal hash. |
| constant_ellipsis | basic_scalar_constant | SAME | SAME | Same input and same marshal hash. |
| constant_false | basic_scalar_constant | SAME | SAME | Same input and same marshal hash. |
| constant_none | basic_scalar_constant | SAME | SAME | Same input and same marshal hash. |
| constant_true | basic_scalar_constant | SAME | SAME | Same input and same marshal hash. |
| crlf_string | unicode_string | SAME | SAME | Same input and same marshal hash. |
| decomposed_e_acute | unicode_string | SAME | SAME | Same input and same marshal hash. |
| emoji_text | unicode_string | SAME | SAME | Same input and same marshal hash. |
| float_huge_1e300 | float_complex | SAME | SAME | Same input and same marshal hash. |
| float_math_nan | float_complex | SAME | SAME | Same input and same marshal hash. |
| float_nan_constructor | float_complex | SAME | SAME | Same input and same marshal hash. |
| float_nan_payload_0x7ff0000000000001 | float_complex | SAME | SAME | Same input and same marshal hash. |
| float_nan_payload_0x7ff8000000000001 | float_complex | SAME | SAME | Same input and same marshal hash. |
| float_nan_payload_0x7ff8000000000002 | float_complex | SAME | SAME | Same input and same marshal hash. |
| float_neg_inf | float_complex | SAME | SAME | Same input and same marshal hash. |
| float_neg_one | float_complex | SAME | SAME | Same input and same marshal hash. |
| float_neg_zero | float_complex | SAME | SAME | Same input and same marshal hash. |
| float_pos_inf | float_complex | SAME | SAME | Same input and same marshal hash. |
| float_pos_one | float_complex | SAME | SAME | Same input and same marshal hash. |
| float_pos_zero | float_complex | SAME | SAME | Same input and same marshal hash. |
| float_tiny_1e_minus_300 | float_complex | SAME | SAME | Same input and same marshal hash. |
| lone_high_surrogate | unicode_string | SAME | SAME | Same input and same marshal hash. |
| non_bmp_character | unicode_string | SAME | SAME | Same input and same marshal hash. |
| nul_inside_string | unicode_string | SAME | SAME | Same input and same marshal hash. |
| recreated_complex_nan_both | float_complex | SAME | SAME | Same input and same marshal hash. |
| recreated_float_nan | float_complex | SAME | SAME | Same input and same marshal hash. |
| slice_1_10_2 | optional_slice_probe | DIFFERENT | SAME | Same optional support boundary or exception behavior. |
| slice_neg10_none_neg1 | optional_slice_probe | DIFFERENT | SAME | Same optional support boundary or exception behavior. |
| slice_none_none_none | optional_slice_probe | DIFFERENT | SAME | Same optional support boundary or exception behavior. |
| zero_width_joiner_sequence | unicode_string | SAME | SAME | Same input and same marshal hash. |

### member_b_all_linux_x86_64_py3_11_results (Linux/x86_64, Python 3.11.15) vs member_b_all_windows_amd64_py3_10_results (Windows/AMD64, Python 3.10.11)

| Case | Category | Same marshal hash | Same exception | Interpretation |
| --- | --- | --- | --- | --- |
| ascii_plain | unicode_string | SAME | SAME | Same input and same marshal hash. |
| bytes_255_a | bytes_payload | SAME | SAME | Same input and same marshal hash. |
| bytes_256_a | bytes_payload | SAME | SAME | Same input and same marshal hash. |
| bytes_65535_a | bytes_payload | SAME | SAME | Same input and same marshal hash. |
| bytes_65536_a | bytes_payload | SAME | SAME | Same input and same marshal hash. |
| bytes_all_byte_values | bytes_payload | SAME | SAME | Same input and same marshal hash. |
| bytes_empty | bytes_payload | SAME | SAME | Same input and same marshal hash. |
| bytes_high_values_with_ascii | bytes_payload | SAME | SAME | Same input and same marshal hash. |
| bytes_single_nul | bytes_payload | SAME | SAME | Same input and same marshal hash. |
| chinese_text | unicode_string | SAME | SAME | Same input and same marshal hash. |
| complex_inf_neg_inf | float_complex | SAME | SAME | Same input and same marshal hash. |
| complex_nan_both | float_complex | SAME | SAME | Same input and same marshal hash. |
| complex_nan_imag | float_complex | SAME | SAME | Same input and same marshal hash. |
| complex_nan_real | float_complex | SAME | SAME | Same input and same marshal hash. |
| complex_payload_nan_imag | float_complex | SAME | SAME | Same input and same marshal hash. |
| complex_payload_nan_real | float_complex | SAME | SAME | Same input and same marshal hash. |
| complex_regular | float_complex | SAME | SAME | Same input and same marshal hash. |
| complex_zero_neg_zero | float_complex | SAME | SAME | Same input and same marshal hash. |
| composed_e_acute | unicode_string | SAME | SAME | Same input and same marshal hash. |
| constant_ellipsis | basic_scalar_constant | SAME | SAME | Same input and same marshal hash. |
| constant_false | basic_scalar_constant | SAME | SAME | Same input and same marshal hash. |
| constant_none | basic_scalar_constant | SAME | SAME | Same input and same marshal hash. |
| constant_true | basic_scalar_constant | SAME | SAME | Same input and same marshal hash. |
| crlf_string | unicode_string | SAME | SAME | Same input and same marshal hash. |
| decomposed_e_acute | unicode_string | SAME | SAME | Same input and same marshal hash. |
| emoji_text | unicode_string | SAME | SAME | Same input and same marshal hash. |
| float_huge_1e300 | float_complex | SAME | SAME | Same input and same marshal hash. |
| float_math_nan | float_complex | SAME | SAME | Same input and same marshal hash. |
| float_nan_constructor | float_complex | SAME | SAME | Same input and same marshal hash. |
| float_nan_payload_0x7ff0000000000001 | float_complex | SAME | SAME | Same input and same marshal hash. |
| float_nan_payload_0x7ff8000000000001 | float_complex | SAME | SAME | Same input and same marshal hash. |
| float_nan_payload_0x7ff8000000000002 | float_complex | SAME | SAME | Same input and same marshal hash. |
| float_neg_inf | float_complex | SAME | SAME | Same input and same marshal hash. |
| float_neg_one | float_complex | SAME | SAME | Same input and same marshal hash. |
| float_neg_zero | float_complex | SAME | SAME | Same input and same marshal hash. |
| float_pos_inf | float_complex | SAME | SAME | Same input and same marshal hash. |
| float_pos_one | float_complex | SAME | SAME | Same input and same marshal hash. |
| float_pos_zero | float_complex | SAME | SAME | Same input and same marshal hash. |
| float_tiny_1e_minus_300 | float_complex | SAME | SAME | Same input and same marshal hash. |
| lone_high_surrogate | unicode_string | SAME | SAME | Same input and same marshal hash. |
| non_bmp_character | unicode_string | SAME | SAME | Same input and same marshal hash. |
| nul_inside_string | unicode_string | SAME | SAME | Same input and same marshal hash. |
| recreated_complex_nan_both | float_complex | SAME | SAME | Same input and same marshal hash. |
| recreated_float_nan | float_complex | SAME | SAME | Same input and same marshal hash. |
| slice_1_10_2 | optional_slice_probe | DIFFERENT | SAME | Same optional support boundary or exception behavior. |
| slice_neg10_none_neg1 | optional_slice_probe | DIFFERENT | SAME | Same optional support boundary or exception behavior. |
| slice_none_none_none | optional_slice_probe | DIFFERENT | SAME | Same optional support boundary or exception behavior. |
| zero_width_joiner_sequence | unicode_string | SAME | SAME | Same input and same marshal hash. |

### member_b_all_linux_x86_64_py3_11_results (Linux/x86_64, Python 3.11.15) vs member_b_all_windows_amd64_py3_11_results (Windows/AMD64, Python 3.11.9)

| Case | Category | Same marshal hash | Same exception | Interpretation |
| --- | --- | --- | --- | --- |
| ascii_plain | unicode_string | SAME | SAME | Same input and same marshal hash. |
| bytes_255_a | bytes_payload | SAME | SAME | Same input and same marshal hash. |
| bytes_256_a | bytes_payload | SAME | SAME | Same input and same marshal hash. |
| bytes_65535_a | bytes_payload | SAME | SAME | Same input and same marshal hash. |
| bytes_65536_a | bytes_payload | SAME | SAME | Same input and same marshal hash. |
| bytes_all_byte_values | bytes_payload | SAME | SAME | Same input and same marshal hash. |
| bytes_empty | bytes_payload | SAME | SAME | Same input and same marshal hash. |
| bytes_high_values_with_ascii | bytes_payload | SAME | SAME | Same input and same marshal hash. |
| bytes_single_nul | bytes_payload | SAME | SAME | Same input and same marshal hash. |
| chinese_text | unicode_string | SAME | SAME | Same input and same marshal hash. |
| complex_inf_neg_inf | float_complex | SAME | SAME | Same input and same marshal hash. |
| complex_nan_both | float_complex | SAME | SAME | Same input and same marshal hash. |
| complex_nan_imag | float_complex | SAME | SAME | Same input and same marshal hash. |
| complex_nan_real | float_complex | SAME | SAME | Same input and same marshal hash. |
| complex_payload_nan_imag | float_complex | SAME | SAME | Same input and same marshal hash. |
| complex_payload_nan_real | float_complex | SAME | SAME | Same input and same marshal hash. |
| complex_regular | float_complex | SAME | SAME | Same input and same marshal hash. |
| complex_zero_neg_zero | float_complex | SAME | SAME | Same input and same marshal hash. |
| composed_e_acute | unicode_string | SAME | SAME | Same input and same marshal hash. |
| constant_ellipsis | basic_scalar_constant | SAME | SAME | Same input and same marshal hash. |
| constant_false | basic_scalar_constant | SAME | SAME | Same input and same marshal hash. |
| constant_none | basic_scalar_constant | SAME | SAME | Same input and same marshal hash. |
| constant_true | basic_scalar_constant | SAME | SAME | Same input and same marshal hash. |
| crlf_string | unicode_string | SAME | SAME | Same input and same marshal hash. |
| decomposed_e_acute | unicode_string | SAME | SAME | Same input and same marshal hash. |
| emoji_text | unicode_string | SAME | SAME | Same input and same marshal hash. |
| float_huge_1e300 | float_complex | SAME | SAME | Same input and same marshal hash. |
| float_math_nan | float_complex | SAME | SAME | Same input and same marshal hash. |
| float_nan_constructor | float_complex | SAME | SAME | Same input and same marshal hash. |
| float_nan_payload_0x7ff0000000000001 | float_complex | SAME | SAME | Same input and same marshal hash. |
| float_nan_payload_0x7ff8000000000001 | float_complex | SAME | SAME | Same input and same marshal hash. |
| float_nan_payload_0x7ff8000000000002 | float_complex | SAME | SAME | Same input and same marshal hash. |
| float_neg_inf | float_complex | SAME | SAME | Same input and same marshal hash. |
| float_neg_one | float_complex | SAME | SAME | Same input and same marshal hash. |
| float_neg_zero | float_complex | SAME | SAME | Same input and same marshal hash. |
| float_pos_inf | float_complex | SAME | SAME | Same input and same marshal hash. |
| float_pos_one | float_complex | SAME | SAME | Same input and same marshal hash. |
| float_pos_zero | float_complex | SAME | SAME | Same input and same marshal hash. |
| float_tiny_1e_minus_300 | float_complex | SAME | SAME | Same input and same marshal hash. |
| lone_high_surrogate | unicode_string | SAME | SAME | Same input and same marshal hash. |
| non_bmp_character | unicode_string | SAME | SAME | Same input and same marshal hash. |
| nul_inside_string | unicode_string | SAME | SAME | Same input and same marshal hash. |
| recreated_complex_nan_both | float_complex | SAME | SAME | Same input and same marshal hash. |
| recreated_float_nan | float_complex | SAME | SAME | Same input and same marshal hash. |
| slice_1_10_2 | optional_slice_probe | DIFFERENT | SAME | Same optional support boundary or exception behavior. |
| slice_neg10_none_neg1 | optional_slice_probe | DIFFERENT | SAME | Same optional support boundary or exception behavior. |
| slice_none_none_none | optional_slice_probe | DIFFERENT | SAME | Same optional support boundary or exception behavior. |
| zero_width_joiner_sequence | unicode_string | SAME | SAME | Same input and same marshal hash. |

### member_b_all_linux_x86_64_py3_11_results (Linux/x86_64, Python 3.11.15) vs member_b_all_windows_amd64_py3_12_results (Windows/AMD64, Python 3.12.10)

| Case | Category | Same marshal hash | Same exception | Interpretation |
| --- | --- | --- | --- | --- |
| ascii_plain | unicode_string | SAME | SAME | Same input and same marshal hash. |
| bytes_255_a | bytes_payload | SAME | SAME | Same input and same marshal hash. |
| bytes_256_a | bytes_payload | SAME | SAME | Same input and same marshal hash. |
| bytes_65535_a | bytes_payload | SAME | SAME | Same input and same marshal hash. |
| bytes_65536_a | bytes_payload | SAME | SAME | Same input and same marshal hash. |
| bytes_all_byte_values | bytes_payload | SAME | SAME | Same input and same marshal hash. |
| bytes_empty | bytes_payload | SAME | SAME | Same input and same marshal hash. |
| bytes_high_values_with_ascii | bytes_payload | SAME | SAME | Same input and same marshal hash. |
| bytes_single_nul | bytes_payload | SAME | SAME | Same input and same marshal hash. |
| chinese_text | unicode_string | SAME | SAME | Same input and same marshal hash. |
| complex_inf_neg_inf | float_complex | SAME | SAME | Same input and same marshal hash. |
| complex_nan_both | float_complex | SAME | SAME | Same input and same marshal hash. |
| complex_nan_imag | float_complex | SAME | SAME | Same input and same marshal hash. |
| complex_nan_real | float_complex | SAME | SAME | Same input and same marshal hash. |
| complex_payload_nan_imag | float_complex | SAME | SAME | Same input and same marshal hash. |
| complex_payload_nan_real | float_complex | SAME | SAME | Same input and same marshal hash. |
| complex_regular | float_complex | SAME | SAME | Same input and same marshal hash. |
| complex_zero_neg_zero | float_complex | SAME | SAME | Same input and same marshal hash. |
| composed_e_acute | unicode_string | DIFFERENT | SAME | Same input representation but Python major/minor differs; likely version-level marshal format difference. |
| constant_ellipsis | basic_scalar_constant | SAME | SAME | Same input and same marshal hash. |
| constant_false | basic_scalar_constant | SAME | SAME | Same input and same marshal hash. |
| constant_none | basic_scalar_constant | SAME | SAME | Same input and same marshal hash. |
| constant_true | basic_scalar_constant | SAME | SAME | Same input and same marshal hash. |
| crlf_string | unicode_string | SAME | SAME | Same input and same marshal hash. |
| decomposed_e_acute | unicode_string | SAME | SAME | Same input and same marshal hash. |
| emoji_text | unicode_string | SAME | SAME | Same input and same marshal hash. |
| float_huge_1e300 | float_complex | SAME | SAME | Same input and same marshal hash. |
| float_math_nan | float_complex | SAME | SAME | Same input and same marshal hash. |
| float_nan_constructor | float_complex | SAME | SAME | Same input and same marshal hash. |
| float_nan_payload_0x7ff0000000000001 | float_complex | SAME | SAME | Same input and same marshal hash. |
| float_nan_payload_0x7ff8000000000001 | float_complex | SAME | SAME | Same input and same marshal hash. |
| float_nan_payload_0x7ff8000000000002 | float_complex | SAME | SAME | Same input and same marshal hash. |
| float_neg_inf | float_complex | SAME | SAME | Same input and same marshal hash. |
| float_neg_one | float_complex | SAME | SAME | Same input and same marshal hash. |
| float_neg_zero | float_complex | SAME | SAME | Same input and same marshal hash. |
| float_pos_inf | float_complex | SAME | SAME | Same input and same marshal hash. |
| float_pos_one | float_complex | SAME | SAME | Same input and same marshal hash. |
| float_pos_zero | float_complex | SAME | SAME | Same input and same marshal hash. |
| float_tiny_1e_minus_300 | float_complex | SAME | SAME | Same input and same marshal hash. |
| lone_high_surrogate | unicode_string | SAME | SAME | Same input and same marshal hash. |
| non_bmp_character | unicode_string | SAME | SAME | Same input and same marshal hash. |
| nul_inside_string | unicode_string | SAME | SAME | Same input and same marshal hash. |
| recreated_complex_nan_both | float_complex | SAME | SAME | Same input and same marshal hash. |
| recreated_float_nan | float_complex | SAME | SAME | Same input and same marshal hash. |
| slice_1_10_2 | optional_slice_probe | DIFFERENT | SAME | Same optional support boundary or exception behavior. |
| slice_neg10_none_neg1 | optional_slice_probe | DIFFERENT | SAME | Same optional support boundary or exception behavior. |
| slice_none_none_none | optional_slice_probe | DIFFERENT | SAME | Same optional support boundary or exception behavior. |
| zero_width_joiner_sequence | unicode_string | SAME | SAME | Same input and same marshal hash. |

### member_b_all_linux_x86_64_py3_11_results (Linux/x86_64, Python 3.11.15) vs member_b_all_windows_amd64_py3_13_results (Windows/AMD64, Python 3.13.13)

| Case | Category | Same marshal hash | Same exception | Interpretation |
| --- | --- | --- | --- | --- |
| ascii_plain | unicode_string | SAME | SAME | Same input and same marshal hash. |
| bytes_255_a | bytes_payload | SAME | SAME | Same input and same marshal hash. |
| bytes_256_a | bytes_payload | SAME | SAME | Same input and same marshal hash. |
| bytes_65535_a | bytes_payload | SAME | SAME | Same input and same marshal hash. |
| bytes_65536_a | bytes_payload | SAME | SAME | Same input and same marshal hash. |
| bytes_all_byte_values | bytes_payload | SAME | SAME | Same input and same marshal hash. |
| bytes_empty | bytes_payload | SAME | SAME | Same input and same marshal hash. |
| bytes_high_values_with_ascii | bytes_payload | SAME | SAME | Same input and same marshal hash. |
| bytes_single_nul | bytes_payload | SAME | SAME | Same input and same marshal hash. |
| chinese_text | unicode_string | SAME | SAME | Same input and same marshal hash. |
| complex_inf_neg_inf | float_complex | SAME | SAME | Same input and same marshal hash. |
| complex_nan_both | float_complex | SAME | SAME | Same input and same marshal hash. |
| complex_nan_imag | float_complex | SAME | SAME | Same input and same marshal hash. |
| complex_nan_real | float_complex | SAME | SAME | Same input and same marshal hash. |
| complex_payload_nan_imag | float_complex | SAME | SAME | Same input and same marshal hash. |
| complex_payload_nan_real | float_complex | SAME | SAME | Same input and same marshal hash. |
| complex_regular | float_complex | SAME | SAME | Same input and same marshal hash. |
| complex_zero_neg_zero | float_complex | SAME | SAME | Same input and same marshal hash. |
| composed_e_acute | unicode_string | DIFFERENT | SAME | Same input representation but Python major/minor differs; likely version-level marshal format difference. |
| constant_ellipsis | basic_scalar_constant | SAME | SAME | Same input and same marshal hash. |
| constant_false | basic_scalar_constant | SAME | SAME | Same input and same marshal hash. |
| constant_none | basic_scalar_constant | SAME | SAME | Same input and same marshal hash. |
| constant_true | basic_scalar_constant | SAME | SAME | Same input and same marshal hash. |
| crlf_string | unicode_string | SAME | SAME | Same input and same marshal hash. |
| decomposed_e_acute | unicode_string | SAME | SAME | Same input and same marshal hash. |
| emoji_text | unicode_string | SAME | SAME | Same input and same marshal hash. |
| float_huge_1e300 | float_complex | SAME | SAME | Same input and same marshal hash. |
| float_math_nan | float_complex | SAME | SAME | Same input and same marshal hash. |
| float_nan_constructor | float_complex | SAME | SAME | Same input and same marshal hash. |
| float_nan_payload_0x7ff0000000000001 | float_complex | SAME | SAME | Same input and same marshal hash. |
| float_nan_payload_0x7ff8000000000001 | float_complex | SAME | SAME | Same input and same marshal hash. |
| float_nan_payload_0x7ff8000000000002 | float_complex | SAME | SAME | Same input and same marshal hash. |
| float_neg_inf | float_complex | SAME | SAME | Same input and same marshal hash. |
| float_neg_one | float_complex | SAME | SAME | Same input and same marshal hash. |
| float_neg_zero | float_complex | SAME | SAME | Same input and same marshal hash. |
| float_pos_inf | float_complex | SAME | SAME | Same input and same marshal hash. |
| float_pos_one | float_complex | SAME | SAME | Same input and same marshal hash. |
| float_pos_zero | float_complex | SAME | SAME | Same input and same marshal hash. |
| float_tiny_1e_minus_300 | float_complex | SAME | SAME | Same input and same marshal hash. |
| lone_high_surrogate | unicode_string | SAME | SAME | Same input and same marshal hash. |
| non_bmp_character | unicode_string | SAME | SAME | Same input and same marshal hash. |
| nul_inside_string | unicode_string | SAME | SAME | Same input and same marshal hash. |
| recreated_complex_nan_both | float_complex | SAME | SAME | Same input and same marshal hash. |
| recreated_float_nan | float_complex | SAME | SAME | Same input and same marshal hash. |
| slice_1_10_2 | optional_slice_probe | DIFFERENT | SAME | Same optional support boundary or exception behavior. |
| slice_neg10_none_neg1 | optional_slice_probe | DIFFERENT | SAME | Same optional support boundary or exception behavior. |
| slice_none_none_none | optional_slice_probe | DIFFERENT | SAME | Same optional support boundary or exception behavior. |
| zero_width_joiner_sequence | unicode_string | SAME | SAME | Same input and same marshal hash. |

### member_b_all_linux_x86_64_py3_11_results (Linux/x86_64, Python 3.11.15) vs member_b_all_windows_amd64_py3_9_results (Windows/AMD64, Python 3.9.13)

| Case | Category | Same marshal hash | Same exception | Interpretation |
| --- | --- | --- | --- | --- |
| ascii_plain | unicode_string | SAME | SAME | Same input and same marshal hash. |
| bytes_255_a | bytes_payload | SAME | SAME | Same input and same marshal hash. |
| bytes_256_a | bytes_payload | SAME | SAME | Same input and same marshal hash. |
| bytes_65535_a | bytes_payload | SAME | SAME | Same input and same marshal hash. |
| bytes_65536_a | bytes_payload | SAME | SAME | Same input and same marshal hash. |
| bytes_all_byte_values | bytes_payload | SAME | SAME | Same input and same marshal hash. |
| bytes_empty | bytes_payload | SAME | SAME | Same input and same marshal hash. |
| bytes_high_values_with_ascii | bytes_payload | SAME | SAME | Same input and same marshal hash. |
| bytes_single_nul | bytes_payload | SAME | SAME | Same input and same marshal hash. |
| chinese_text | unicode_string | SAME | SAME | Same input and same marshal hash. |
| complex_inf_neg_inf | float_complex | SAME | SAME | Same input and same marshal hash. |
| complex_nan_both | float_complex | SAME | SAME | Same input and same marshal hash. |
| complex_nan_imag | float_complex | SAME | SAME | Same input and same marshal hash. |
| complex_nan_real | float_complex | SAME | SAME | Same input and same marshal hash. |
| complex_payload_nan_imag | float_complex | SAME | SAME | Same input and same marshal hash. |
| complex_payload_nan_real | float_complex | SAME | SAME | Same input and same marshal hash. |
| complex_regular | float_complex | SAME | SAME | Same input and same marshal hash. |
| complex_zero_neg_zero | float_complex | SAME | SAME | Same input and same marshal hash. |
| composed_e_acute | unicode_string | SAME | SAME | Same input and same marshal hash. |
| constant_ellipsis | basic_scalar_constant | SAME | SAME | Same input and same marshal hash. |
| constant_false | basic_scalar_constant | SAME | SAME | Same input and same marshal hash. |
| constant_none | basic_scalar_constant | SAME | SAME | Same input and same marshal hash. |
| constant_true | basic_scalar_constant | SAME | SAME | Same input and same marshal hash. |
| crlf_string | unicode_string | SAME | SAME | Same input and same marshal hash. |
| decomposed_e_acute | unicode_string | SAME | SAME | Same input and same marshal hash. |
| emoji_text | unicode_string | SAME | SAME | Same input and same marshal hash. |
| float_huge_1e300 | float_complex | SAME | SAME | Same input and same marshal hash. |
| float_math_nan | float_complex | SAME | SAME | Same input and same marshal hash. |
| float_nan_constructor | float_complex | SAME | SAME | Same input and same marshal hash. |
| float_nan_payload_0x7ff0000000000001 | float_complex | SAME | SAME | Same input and same marshal hash. |
| float_nan_payload_0x7ff8000000000001 | float_complex | SAME | SAME | Same input and same marshal hash. |
| float_nan_payload_0x7ff8000000000002 | float_complex | SAME | SAME | Same input and same marshal hash. |
| float_neg_inf | float_complex | SAME | SAME | Same input and same marshal hash. |
| float_neg_one | float_complex | SAME | SAME | Same input and same marshal hash. |
| float_neg_zero | float_complex | SAME | SAME | Same input and same marshal hash. |
| float_pos_inf | float_complex | SAME | SAME | Same input and same marshal hash. |
| float_pos_one | float_complex | SAME | SAME | Same input and same marshal hash. |
| float_pos_zero | float_complex | SAME | SAME | Same input and same marshal hash. |
| float_tiny_1e_minus_300 | float_complex | SAME | SAME | Same input and same marshal hash. |
| lone_high_surrogate | unicode_string | SAME | SAME | Same input and same marshal hash. |
| non_bmp_character | unicode_string | SAME | SAME | Same input and same marshal hash. |
| nul_inside_string | unicode_string | SAME | SAME | Same input and same marshal hash. |
| recreated_complex_nan_both | float_complex | SAME | SAME | Same input and same marshal hash. |
| recreated_float_nan | float_complex | SAME | SAME | Same input and same marshal hash. |
| slice_1_10_2 | optional_slice_probe | DIFFERENT | SAME | Same optional support boundary or exception behavior. |
| slice_neg10_none_neg1 | optional_slice_probe | DIFFERENT | SAME | Same optional support boundary or exception behavior. |
| slice_none_none_none | optional_slice_probe | DIFFERENT | SAME | Same optional support boundary or exception behavior. |
| zero_width_joiner_sequence | unicode_string | SAME | SAME | Same input and same marshal hash. |

### member_b_all_linux_x86_64_py3_12_results (Linux/x86_64, Python 3.12.13) vs member_b_all_linux_x86_64_py3_13_results (Linux/x86_64, Python 3.13.13)

| Case | Category | Same marshal hash | Same exception | Interpretation |
| --- | --- | --- | --- | --- |
| ascii_plain | unicode_string | SAME | SAME | Same input and same marshal hash. |
| bytes_255_a | bytes_payload | SAME | SAME | Same input and same marshal hash. |
| bytes_256_a | bytes_payload | SAME | SAME | Same input and same marshal hash. |
| bytes_65535_a | bytes_payload | SAME | SAME | Same input and same marshal hash. |
| bytes_65536_a | bytes_payload | SAME | SAME | Same input and same marshal hash. |
| bytes_all_byte_values | bytes_payload | SAME | SAME | Same input and same marshal hash. |
| bytes_empty | bytes_payload | SAME | SAME | Same input and same marshal hash. |
| bytes_high_values_with_ascii | bytes_payload | SAME | SAME | Same input and same marshal hash. |
| bytes_single_nul | bytes_payload | SAME | SAME | Same input and same marshal hash. |
| chinese_text | unicode_string | SAME | SAME | Same input and same marshal hash. |
| complex_inf_neg_inf | float_complex | SAME | SAME | Same input and same marshal hash. |
| complex_nan_both | float_complex | SAME | SAME | Same input and same marshal hash. |
| complex_nan_imag | float_complex | SAME | SAME | Same input and same marshal hash. |
| complex_nan_real | float_complex | SAME | SAME | Same input and same marshal hash. |
| complex_payload_nan_imag | float_complex | SAME | SAME | Same input and same marshal hash. |
| complex_payload_nan_real | float_complex | SAME | SAME | Same input and same marshal hash. |
| complex_regular | float_complex | SAME | SAME | Same input and same marshal hash. |
| complex_zero_neg_zero | float_complex | SAME | SAME | Same input and same marshal hash. |
| composed_e_acute | unicode_string | SAME | SAME | Same input and same marshal hash. |
| constant_ellipsis | basic_scalar_constant | SAME | SAME | Same input and same marshal hash. |
| constant_false | basic_scalar_constant | SAME | SAME | Same input and same marshal hash. |
| constant_none | basic_scalar_constant | SAME | SAME | Same input and same marshal hash. |
| constant_true | basic_scalar_constant | SAME | SAME | Same input and same marshal hash. |
| crlf_string | unicode_string | SAME | SAME | Same input and same marshal hash. |
| decomposed_e_acute | unicode_string | SAME | SAME | Same input and same marshal hash. |
| emoji_text | unicode_string | SAME | SAME | Same input and same marshal hash. |
| float_huge_1e300 | float_complex | SAME | SAME | Same input and same marshal hash. |
| float_math_nan | float_complex | SAME | SAME | Same input and same marshal hash. |
| float_nan_constructor | float_complex | SAME | SAME | Same input and same marshal hash. |
| float_nan_payload_0x7ff0000000000001 | float_complex | SAME | SAME | Same input and same marshal hash. |
| float_nan_payload_0x7ff8000000000001 | float_complex | SAME | SAME | Same input and same marshal hash. |
| float_nan_payload_0x7ff8000000000002 | float_complex | SAME | SAME | Same input and same marshal hash. |
| float_neg_inf | float_complex | SAME | SAME | Same input and same marshal hash. |
| float_neg_one | float_complex | SAME | SAME | Same input and same marshal hash. |
| float_neg_zero | float_complex | SAME | SAME | Same input and same marshal hash. |
| float_pos_inf | float_complex | SAME | SAME | Same input and same marshal hash. |
| float_pos_one | float_complex | SAME | SAME | Same input and same marshal hash. |
| float_pos_zero | float_complex | SAME | SAME | Same input and same marshal hash. |
| float_tiny_1e_minus_300 | float_complex | SAME | SAME | Same input and same marshal hash. |
| lone_high_surrogate | unicode_string | SAME | SAME | Same input and same marshal hash. |
| non_bmp_character | unicode_string | SAME | SAME | Same input and same marshal hash. |
| nul_inside_string | unicode_string | SAME | SAME | Same input and same marshal hash. |
| recreated_complex_nan_both | float_complex | SAME | SAME | Same input and same marshal hash. |
| recreated_float_nan | float_complex | SAME | SAME | Same input and same marshal hash. |
| slice_1_10_2 | optional_slice_probe | DIFFERENT | SAME | Same optional support boundary or exception behavior. |
| slice_neg10_none_neg1 | optional_slice_probe | DIFFERENT | SAME | Same optional support boundary or exception behavior. |
| slice_none_none_none | optional_slice_probe | DIFFERENT | SAME | Same optional support boundary or exception behavior. |
| zero_width_joiner_sequence | unicode_string | SAME | SAME | Same input and same marshal hash. |

### member_b_all_linux_x86_64_py3_12_results (Linux/x86_64, Python 3.12.13) vs member_b_all_linux_x86_64_py3_9_results (Linux/x86_64, Python 3.9.25)

| Case | Category | Same marshal hash | Same exception | Interpretation |
| --- | --- | --- | --- | --- |
| ascii_plain | unicode_string | SAME | SAME | Same input and same marshal hash. |
| bytes_255_a | bytes_payload | SAME | SAME | Same input and same marshal hash. |
| bytes_256_a | bytes_payload | SAME | SAME | Same input and same marshal hash. |
| bytes_65535_a | bytes_payload | SAME | SAME | Same input and same marshal hash. |
| bytes_65536_a | bytes_payload | SAME | SAME | Same input and same marshal hash. |
| bytes_all_byte_values | bytes_payload | SAME | SAME | Same input and same marshal hash. |
| bytes_empty | bytes_payload | SAME | SAME | Same input and same marshal hash. |
| bytes_high_values_with_ascii | bytes_payload | SAME | SAME | Same input and same marshal hash. |
| bytes_single_nul | bytes_payload | SAME | SAME | Same input and same marshal hash. |
| chinese_text | unicode_string | SAME | SAME | Same input and same marshal hash. |
| complex_inf_neg_inf | float_complex | SAME | SAME | Same input and same marshal hash. |
| complex_nan_both | float_complex | SAME | SAME | Same input and same marshal hash. |
| complex_nan_imag | float_complex | SAME | SAME | Same input and same marshal hash. |
| complex_nan_real | float_complex | SAME | SAME | Same input and same marshal hash. |
| complex_payload_nan_imag | float_complex | SAME | SAME | Same input and same marshal hash. |
| complex_payload_nan_real | float_complex | SAME | SAME | Same input and same marshal hash. |
| complex_regular | float_complex | SAME | SAME | Same input and same marshal hash. |
| complex_zero_neg_zero | float_complex | SAME | SAME | Same input and same marshal hash. |
| composed_e_acute | unicode_string | DIFFERENT | SAME | Same input representation but Python major/minor differs; likely version-level marshal format difference. |
| constant_ellipsis | basic_scalar_constant | SAME | SAME | Same input and same marshal hash. |
| constant_false | basic_scalar_constant | SAME | SAME | Same input and same marshal hash. |
| constant_none | basic_scalar_constant | SAME | SAME | Same input and same marshal hash. |
| constant_true | basic_scalar_constant | SAME | SAME | Same input and same marshal hash. |
| crlf_string | unicode_string | SAME | SAME | Same input and same marshal hash. |
| decomposed_e_acute | unicode_string | SAME | SAME | Same input and same marshal hash. |
| emoji_text | unicode_string | SAME | SAME | Same input and same marshal hash. |
| float_huge_1e300 | float_complex | SAME | SAME | Same input and same marshal hash. |
| float_math_nan | float_complex | SAME | SAME | Same input and same marshal hash. |
| float_nan_constructor | float_complex | SAME | SAME | Same input and same marshal hash. |
| float_nan_payload_0x7ff0000000000001 | float_complex | SAME | SAME | Same input and same marshal hash. |
| float_nan_payload_0x7ff8000000000001 | float_complex | SAME | SAME | Same input and same marshal hash. |
| float_nan_payload_0x7ff8000000000002 | float_complex | SAME | SAME | Same input and same marshal hash. |
| float_neg_inf | float_complex | SAME | SAME | Same input and same marshal hash. |
| float_neg_one | float_complex | SAME | SAME | Same input and same marshal hash. |
| float_neg_zero | float_complex | SAME | SAME | Same input and same marshal hash. |
| float_pos_inf | float_complex | SAME | SAME | Same input and same marshal hash. |
| float_pos_one | float_complex | SAME | SAME | Same input and same marshal hash. |
| float_pos_zero | float_complex | SAME | SAME | Same input and same marshal hash. |
| float_tiny_1e_minus_300 | float_complex | SAME | SAME | Same input and same marshal hash. |
| lone_high_surrogate | unicode_string | SAME | SAME | Same input and same marshal hash. |
| non_bmp_character | unicode_string | SAME | SAME | Same input and same marshal hash. |
| nul_inside_string | unicode_string | SAME | SAME | Same input and same marshal hash. |
| recreated_complex_nan_both | float_complex | SAME | SAME | Same input and same marshal hash. |
| recreated_float_nan | float_complex | SAME | SAME | Same input and same marshal hash. |
| slice_1_10_2 | optional_slice_probe | DIFFERENT | SAME | Same optional support boundary or exception behavior. |
| slice_neg10_none_neg1 | optional_slice_probe | DIFFERENT | SAME | Same optional support boundary or exception behavior. |
| slice_none_none_none | optional_slice_probe | DIFFERENT | SAME | Same optional support boundary or exception behavior. |
| zero_width_joiner_sequence | unicode_string | SAME | SAME | Same input and same marshal hash. |

### member_b_all_linux_x86_64_py3_12_results (Linux/x86_64, Python 3.12.13) vs member_b_all_windows_amd64_py3_10_results (Windows/AMD64, Python 3.10.11)

| Case | Category | Same marshal hash | Same exception | Interpretation |
| --- | --- | --- | --- | --- |
| ascii_plain | unicode_string | SAME | SAME | Same input and same marshal hash. |
| bytes_255_a | bytes_payload | SAME | SAME | Same input and same marshal hash. |
| bytes_256_a | bytes_payload | SAME | SAME | Same input and same marshal hash. |
| bytes_65535_a | bytes_payload | SAME | SAME | Same input and same marshal hash. |
| bytes_65536_a | bytes_payload | SAME | SAME | Same input and same marshal hash. |
| bytes_all_byte_values | bytes_payload | SAME | SAME | Same input and same marshal hash. |
| bytes_empty | bytes_payload | SAME | SAME | Same input and same marshal hash. |
| bytes_high_values_with_ascii | bytes_payload | SAME | SAME | Same input and same marshal hash. |
| bytes_single_nul | bytes_payload | SAME | SAME | Same input and same marshal hash. |
| chinese_text | unicode_string | SAME | SAME | Same input and same marshal hash. |
| complex_inf_neg_inf | float_complex | SAME | SAME | Same input and same marshal hash. |
| complex_nan_both | float_complex | SAME | SAME | Same input and same marshal hash. |
| complex_nan_imag | float_complex | SAME | SAME | Same input and same marshal hash. |
| complex_nan_real | float_complex | SAME | SAME | Same input and same marshal hash. |
| complex_payload_nan_imag | float_complex | SAME | SAME | Same input and same marshal hash. |
| complex_payload_nan_real | float_complex | SAME | SAME | Same input and same marshal hash. |
| complex_regular | float_complex | SAME | SAME | Same input and same marshal hash. |
| complex_zero_neg_zero | float_complex | SAME | SAME | Same input and same marshal hash. |
| composed_e_acute | unicode_string | DIFFERENT | SAME | Same input representation but Python major/minor differs; likely version-level marshal format difference. |
| constant_ellipsis | basic_scalar_constant | SAME | SAME | Same input and same marshal hash. |
| constant_false | basic_scalar_constant | SAME | SAME | Same input and same marshal hash. |
| constant_none | basic_scalar_constant | SAME | SAME | Same input and same marshal hash. |
| constant_true | basic_scalar_constant | SAME | SAME | Same input and same marshal hash. |
| crlf_string | unicode_string | SAME | SAME | Same input and same marshal hash. |
| decomposed_e_acute | unicode_string | SAME | SAME | Same input and same marshal hash. |
| emoji_text | unicode_string | SAME | SAME | Same input and same marshal hash. |
| float_huge_1e300 | float_complex | SAME | SAME | Same input and same marshal hash. |
| float_math_nan | float_complex | SAME | SAME | Same input and same marshal hash. |
| float_nan_constructor | float_complex | SAME | SAME | Same input and same marshal hash. |
| float_nan_payload_0x7ff0000000000001 | float_complex | SAME | SAME | Same input and same marshal hash. |
| float_nan_payload_0x7ff8000000000001 | float_complex | SAME | SAME | Same input and same marshal hash. |
| float_nan_payload_0x7ff8000000000002 | float_complex | SAME | SAME | Same input and same marshal hash. |
| float_neg_inf | float_complex | SAME | SAME | Same input and same marshal hash. |
| float_neg_one | float_complex | SAME | SAME | Same input and same marshal hash. |
| float_neg_zero | float_complex | SAME | SAME | Same input and same marshal hash. |
| float_pos_inf | float_complex | SAME | SAME | Same input and same marshal hash. |
| float_pos_one | float_complex | SAME | SAME | Same input and same marshal hash. |
| float_pos_zero | float_complex | SAME | SAME | Same input and same marshal hash. |
| float_tiny_1e_minus_300 | float_complex | SAME | SAME | Same input and same marshal hash. |
| lone_high_surrogate | unicode_string | SAME | SAME | Same input and same marshal hash. |
| non_bmp_character | unicode_string | SAME | SAME | Same input and same marshal hash. |
| nul_inside_string | unicode_string | SAME | SAME | Same input and same marshal hash. |
| recreated_complex_nan_both | float_complex | SAME | SAME | Same input and same marshal hash. |
| recreated_float_nan | float_complex | SAME | SAME | Same input and same marshal hash. |
| slice_1_10_2 | optional_slice_probe | DIFFERENT | SAME | Same optional support boundary or exception behavior. |
| slice_neg10_none_neg1 | optional_slice_probe | DIFFERENT | SAME | Same optional support boundary or exception behavior. |
| slice_none_none_none | optional_slice_probe | DIFFERENT | SAME | Same optional support boundary or exception behavior. |
| zero_width_joiner_sequence | unicode_string | SAME | SAME | Same input and same marshal hash. |

### member_b_all_linux_x86_64_py3_12_results (Linux/x86_64, Python 3.12.13) vs member_b_all_windows_amd64_py3_11_results (Windows/AMD64, Python 3.11.9)

| Case | Category | Same marshal hash | Same exception | Interpretation |
| --- | --- | --- | --- | --- |
| ascii_plain | unicode_string | SAME | SAME | Same input and same marshal hash. |
| bytes_255_a | bytes_payload | SAME | SAME | Same input and same marshal hash. |
| bytes_256_a | bytes_payload | SAME | SAME | Same input and same marshal hash. |
| bytes_65535_a | bytes_payload | SAME | SAME | Same input and same marshal hash. |
| bytes_65536_a | bytes_payload | SAME | SAME | Same input and same marshal hash. |
| bytes_all_byte_values | bytes_payload | SAME | SAME | Same input and same marshal hash. |
| bytes_empty | bytes_payload | SAME | SAME | Same input and same marshal hash. |
| bytes_high_values_with_ascii | bytes_payload | SAME | SAME | Same input and same marshal hash. |
| bytes_single_nul | bytes_payload | SAME | SAME | Same input and same marshal hash. |
| chinese_text | unicode_string | SAME | SAME | Same input and same marshal hash. |
| complex_inf_neg_inf | float_complex | SAME | SAME | Same input and same marshal hash. |
| complex_nan_both | float_complex | SAME | SAME | Same input and same marshal hash. |
| complex_nan_imag | float_complex | SAME | SAME | Same input and same marshal hash. |
| complex_nan_real | float_complex | SAME | SAME | Same input and same marshal hash. |
| complex_payload_nan_imag | float_complex | SAME | SAME | Same input and same marshal hash. |
| complex_payload_nan_real | float_complex | SAME | SAME | Same input and same marshal hash. |
| complex_regular | float_complex | SAME | SAME | Same input and same marshal hash. |
| complex_zero_neg_zero | float_complex | SAME | SAME | Same input and same marshal hash. |
| composed_e_acute | unicode_string | DIFFERENT | SAME | Same input representation but Python major/minor differs; likely version-level marshal format difference. |
| constant_ellipsis | basic_scalar_constant | SAME | SAME | Same input and same marshal hash. |
| constant_false | basic_scalar_constant | SAME | SAME | Same input and same marshal hash. |
| constant_none | basic_scalar_constant | SAME | SAME | Same input and same marshal hash. |
| constant_true | basic_scalar_constant | SAME | SAME | Same input and same marshal hash. |
| crlf_string | unicode_string | SAME | SAME | Same input and same marshal hash. |
| decomposed_e_acute | unicode_string | SAME | SAME | Same input and same marshal hash. |
| emoji_text | unicode_string | SAME | SAME | Same input and same marshal hash. |
| float_huge_1e300 | float_complex | SAME | SAME | Same input and same marshal hash. |
| float_math_nan | float_complex | SAME | SAME | Same input and same marshal hash. |
| float_nan_constructor | float_complex | SAME | SAME | Same input and same marshal hash. |
| float_nan_payload_0x7ff0000000000001 | float_complex | SAME | SAME | Same input and same marshal hash. |
| float_nan_payload_0x7ff8000000000001 | float_complex | SAME | SAME | Same input and same marshal hash. |
| float_nan_payload_0x7ff8000000000002 | float_complex | SAME | SAME | Same input and same marshal hash. |
| float_neg_inf | float_complex | SAME | SAME | Same input and same marshal hash. |
| float_neg_one | float_complex | SAME | SAME | Same input and same marshal hash. |
| float_neg_zero | float_complex | SAME | SAME | Same input and same marshal hash. |
| float_pos_inf | float_complex | SAME | SAME | Same input and same marshal hash. |
| float_pos_one | float_complex | SAME | SAME | Same input and same marshal hash. |
| float_pos_zero | float_complex | SAME | SAME | Same input and same marshal hash. |
| float_tiny_1e_minus_300 | float_complex | SAME | SAME | Same input and same marshal hash. |
| lone_high_surrogate | unicode_string | SAME | SAME | Same input and same marshal hash. |
| non_bmp_character | unicode_string | SAME | SAME | Same input and same marshal hash. |
| nul_inside_string | unicode_string | SAME | SAME | Same input and same marshal hash. |
| recreated_complex_nan_both | float_complex | SAME | SAME | Same input and same marshal hash. |
| recreated_float_nan | float_complex | SAME | SAME | Same input and same marshal hash. |
| slice_1_10_2 | optional_slice_probe | DIFFERENT | SAME | Same optional support boundary or exception behavior. |
| slice_neg10_none_neg1 | optional_slice_probe | DIFFERENT | SAME | Same optional support boundary or exception behavior. |
| slice_none_none_none | optional_slice_probe | DIFFERENT | SAME | Same optional support boundary or exception behavior. |
| zero_width_joiner_sequence | unicode_string | SAME | SAME | Same input and same marshal hash. |

### member_b_all_linux_x86_64_py3_12_results (Linux/x86_64, Python 3.12.13) vs member_b_all_windows_amd64_py3_12_results (Windows/AMD64, Python 3.12.10)

| Case | Category | Same marshal hash | Same exception | Interpretation |
| --- | --- | --- | --- | --- |
| ascii_plain | unicode_string | SAME | SAME | Same input and same marshal hash. |
| bytes_255_a | bytes_payload | SAME | SAME | Same input and same marshal hash. |
| bytes_256_a | bytes_payload | SAME | SAME | Same input and same marshal hash. |
| bytes_65535_a | bytes_payload | SAME | SAME | Same input and same marshal hash. |
| bytes_65536_a | bytes_payload | SAME | SAME | Same input and same marshal hash. |
| bytes_all_byte_values | bytes_payload | SAME | SAME | Same input and same marshal hash. |
| bytes_empty | bytes_payload | SAME | SAME | Same input and same marshal hash. |
| bytes_high_values_with_ascii | bytes_payload | SAME | SAME | Same input and same marshal hash. |
| bytes_single_nul | bytes_payload | SAME | SAME | Same input and same marshal hash. |
| chinese_text | unicode_string | SAME | SAME | Same input and same marshal hash. |
| complex_inf_neg_inf | float_complex | SAME | SAME | Same input and same marshal hash. |
| complex_nan_both | float_complex | SAME | SAME | Same input and same marshal hash. |
| complex_nan_imag | float_complex | SAME | SAME | Same input and same marshal hash. |
| complex_nan_real | float_complex | SAME | SAME | Same input and same marshal hash. |
| complex_payload_nan_imag | float_complex | SAME | SAME | Same input and same marshal hash. |
| complex_payload_nan_real | float_complex | SAME | SAME | Same input and same marshal hash. |
| complex_regular | float_complex | SAME | SAME | Same input and same marshal hash. |
| complex_zero_neg_zero | float_complex | SAME | SAME | Same input and same marshal hash. |
| composed_e_acute | unicode_string | SAME | SAME | Same input and same marshal hash. |
| constant_ellipsis | basic_scalar_constant | SAME | SAME | Same input and same marshal hash. |
| constant_false | basic_scalar_constant | SAME | SAME | Same input and same marshal hash. |
| constant_none | basic_scalar_constant | SAME | SAME | Same input and same marshal hash. |
| constant_true | basic_scalar_constant | SAME | SAME | Same input and same marshal hash. |
| crlf_string | unicode_string | SAME | SAME | Same input and same marshal hash. |
| decomposed_e_acute | unicode_string | SAME | SAME | Same input and same marshal hash. |
| emoji_text | unicode_string | SAME | SAME | Same input and same marshal hash. |
| float_huge_1e300 | float_complex | SAME | SAME | Same input and same marshal hash. |
| float_math_nan | float_complex | SAME | SAME | Same input and same marshal hash. |
| float_nan_constructor | float_complex | SAME | SAME | Same input and same marshal hash. |
| float_nan_payload_0x7ff0000000000001 | float_complex | SAME | SAME | Same input and same marshal hash. |
| float_nan_payload_0x7ff8000000000001 | float_complex | SAME | SAME | Same input and same marshal hash. |
| float_nan_payload_0x7ff8000000000002 | float_complex | SAME | SAME | Same input and same marshal hash. |
| float_neg_inf | float_complex | SAME | SAME | Same input and same marshal hash. |
| float_neg_one | float_complex | SAME | SAME | Same input and same marshal hash. |
| float_neg_zero | float_complex | SAME | SAME | Same input and same marshal hash. |
| float_pos_inf | float_complex | SAME | SAME | Same input and same marshal hash. |
| float_pos_one | float_complex | SAME | SAME | Same input and same marshal hash. |
| float_pos_zero | float_complex | SAME | SAME | Same input and same marshal hash. |
| float_tiny_1e_minus_300 | float_complex | SAME | SAME | Same input and same marshal hash. |
| lone_high_surrogate | unicode_string | SAME | SAME | Same input and same marshal hash. |
| non_bmp_character | unicode_string | SAME | SAME | Same input and same marshal hash. |
| nul_inside_string | unicode_string | SAME | SAME | Same input and same marshal hash. |
| recreated_complex_nan_both | float_complex | SAME | SAME | Same input and same marshal hash. |
| recreated_float_nan | float_complex | SAME | SAME | Same input and same marshal hash. |
| slice_1_10_2 | optional_slice_probe | DIFFERENT | SAME | Same optional support boundary or exception behavior. |
| slice_neg10_none_neg1 | optional_slice_probe | DIFFERENT | SAME | Same optional support boundary or exception behavior. |
| slice_none_none_none | optional_slice_probe | DIFFERENT | SAME | Same optional support boundary or exception behavior. |
| zero_width_joiner_sequence | unicode_string | SAME | SAME | Same input and same marshal hash. |

### member_b_all_linux_x86_64_py3_12_results (Linux/x86_64, Python 3.12.13) vs member_b_all_windows_amd64_py3_13_results (Windows/AMD64, Python 3.13.13)

| Case | Category | Same marshal hash | Same exception | Interpretation |
| --- | --- | --- | --- | --- |
| ascii_plain | unicode_string | SAME | SAME | Same input and same marshal hash. |
| bytes_255_a | bytes_payload | SAME | SAME | Same input and same marshal hash. |
| bytes_256_a | bytes_payload | SAME | SAME | Same input and same marshal hash. |
| bytes_65535_a | bytes_payload | SAME | SAME | Same input and same marshal hash. |
| bytes_65536_a | bytes_payload | SAME | SAME | Same input and same marshal hash. |
| bytes_all_byte_values | bytes_payload | SAME | SAME | Same input and same marshal hash. |
| bytes_empty | bytes_payload | SAME | SAME | Same input and same marshal hash. |
| bytes_high_values_with_ascii | bytes_payload | SAME | SAME | Same input and same marshal hash. |
| bytes_single_nul | bytes_payload | SAME | SAME | Same input and same marshal hash. |
| chinese_text | unicode_string | SAME | SAME | Same input and same marshal hash. |
| complex_inf_neg_inf | float_complex | SAME | SAME | Same input and same marshal hash. |
| complex_nan_both | float_complex | SAME | SAME | Same input and same marshal hash. |
| complex_nan_imag | float_complex | SAME | SAME | Same input and same marshal hash. |
| complex_nan_real | float_complex | SAME | SAME | Same input and same marshal hash. |
| complex_payload_nan_imag | float_complex | SAME | SAME | Same input and same marshal hash. |
| complex_payload_nan_real | float_complex | SAME | SAME | Same input and same marshal hash. |
| complex_regular | float_complex | SAME | SAME | Same input and same marshal hash. |
| complex_zero_neg_zero | float_complex | SAME | SAME | Same input and same marshal hash. |
| composed_e_acute | unicode_string | SAME | SAME | Same input and same marshal hash. |
| constant_ellipsis | basic_scalar_constant | SAME | SAME | Same input and same marshal hash. |
| constant_false | basic_scalar_constant | SAME | SAME | Same input and same marshal hash. |
| constant_none | basic_scalar_constant | SAME | SAME | Same input and same marshal hash. |
| constant_true | basic_scalar_constant | SAME | SAME | Same input and same marshal hash. |
| crlf_string | unicode_string | SAME | SAME | Same input and same marshal hash. |
| decomposed_e_acute | unicode_string | SAME | SAME | Same input and same marshal hash. |
| emoji_text | unicode_string | SAME | SAME | Same input and same marshal hash. |
| float_huge_1e300 | float_complex | SAME | SAME | Same input and same marshal hash. |
| float_math_nan | float_complex | SAME | SAME | Same input and same marshal hash. |
| float_nan_constructor | float_complex | SAME | SAME | Same input and same marshal hash. |
| float_nan_payload_0x7ff0000000000001 | float_complex | SAME | SAME | Same input and same marshal hash. |
| float_nan_payload_0x7ff8000000000001 | float_complex | SAME | SAME | Same input and same marshal hash. |
| float_nan_payload_0x7ff8000000000002 | float_complex | SAME | SAME | Same input and same marshal hash. |
| float_neg_inf | float_complex | SAME | SAME | Same input and same marshal hash. |
| float_neg_one | float_complex | SAME | SAME | Same input and same marshal hash. |
| float_neg_zero | float_complex | SAME | SAME | Same input and same marshal hash. |
| float_pos_inf | float_complex | SAME | SAME | Same input and same marshal hash. |
| float_pos_one | float_complex | SAME | SAME | Same input and same marshal hash. |
| float_pos_zero | float_complex | SAME | SAME | Same input and same marshal hash. |
| float_tiny_1e_minus_300 | float_complex | SAME | SAME | Same input and same marshal hash. |
| lone_high_surrogate | unicode_string | SAME | SAME | Same input and same marshal hash. |
| non_bmp_character | unicode_string | SAME | SAME | Same input and same marshal hash. |
| nul_inside_string | unicode_string | SAME | SAME | Same input and same marshal hash. |
| recreated_complex_nan_both | float_complex | SAME | SAME | Same input and same marshal hash. |
| recreated_float_nan | float_complex | SAME | SAME | Same input and same marshal hash. |
| slice_1_10_2 | optional_slice_probe | DIFFERENT | SAME | Same optional support boundary or exception behavior. |
| slice_neg10_none_neg1 | optional_slice_probe | DIFFERENT | SAME | Same optional support boundary or exception behavior. |
| slice_none_none_none | optional_slice_probe | DIFFERENT | SAME | Same optional support boundary or exception behavior. |
| zero_width_joiner_sequence | unicode_string | SAME | SAME | Same input and same marshal hash. |

### member_b_all_linux_x86_64_py3_12_results (Linux/x86_64, Python 3.12.13) vs member_b_all_windows_amd64_py3_9_results (Windows/AMD64, Python 3.9.13)

| Case | Category | Same marshal hash | Same exception | Interpretation |
| --- | --- | --- | --- | --- |
| ascii_plain | unicode_string | SAME | SAME | Same input and same marshal hash. |
| bytes_255_a | bytes_payload | SAME | SAME | Same input and same marshal hash. |
| bytes_256_a | bytes_payload | SAME | SAME | Same input and same marshal hash. |
| bytes_65535_a | bytes_payload | SAME | SAME | Same input and same marshal hash. |
| bytes_65536_a | bytes_payload | SAME | SAME | Same input and same marshal hash. |
| bytes_all_byte_values | bytes_payload | SAME | SAME | Same input and same marshal hash. |
| bytes_empty | bytes_payload | SAME | SAME | Same input and same marshal hash. |
| bytes_high_values_with_ascii | bytes_payload | SAME | SAME | Same input and same marshal hash. |
| bytes_single_nul | bytes_payload | SAME | SAME | Same input and same marshal hash. |
| chinese_text | unicode_string | SAME | SAME | Same input and same marshal hash. |
| complex_inf_neg_inf | float_complex | SAME | SAME | Same input and same marshal hash. |
| complex_nan_both | float_complex | SAME | SAME | Same input and same marshal hash. |
| complex_nan_imag | float_complex | SAME | SAME | Same input and same marshal hash. |
| complex_nan_real | float_complex | SAME | SAME | Same input and same marshal hash. |
| complex_payload_nan_imag | float_complex | SAME | SAME | Same input and same marshal hash. |
| complex_payload_nan_real | float_complex | SAME | SAME | Same input and same marshal hash. |
| complex_regular | float_complex | SAME | SAME | Same input and same marshal hash. |
| complex_zero_neg_zero | float_complex | SAME | SAME | Same input and same marshal hash. |
| composed_e_acute | unicode_string | DIFFERENT | SAME | Same input representation but Python major/minor differs; likely version-level marshal format difference. |
| constant_ellipsis | basic_scalar_constant | SAME | SAME | Same input and same marshal hash. |
| constant_false | basic_scalar_constant | SAME | SAME | Same input and same marshal hash. |
| constant_none | basic_scalar_constant | SAME | SAME | Same input and same marshal hash. |
| constant_true | basic_scalar_constant | SAME | SAME | Same input and same marshal hash. |
| crlf_string | unicode_string | SAME | SAME | Same input and same marshal hash. |
| decomposed_e_acute | unicode_string | SAME | SAME | Same input and same marshal hash. |
| emoji_text | unicode_string | SAME | SAME | Same input and same marshal hash. |
| float_huge_1e300 | float_complex | SAME | SAME | Same input and same marshal hash. |
| float_math_nan | float_complex | SAME | SAME | Same input and same marshal hash. |
| float_nan_constructor | float_complex | SAME | SAME | Same input and same marshal hash. |
| float_nan_payload_0x7ff0000000000001 | float_complex | SAME | SAME | Same input and same marshal hash. |
| float_nan_payload_0x7ff8000000000001 | float_complex | SAME | SAME | Same input and same marshal hash. |
| float_nan_payload_0x7ff8000000000002 | float_complex | SAME | SAME | Same input and same marshal hash. |
| float_neg_inf | float_complex | SAME | SAME | Same input and same marshal hash. |
| float_neg_one | float_complex | SAME | SAME | Same input and same marshal hash. |
| float_neg_zero | float_complex | SAME | SAME | Same input and same marshal hash. |
| float_pos_inf | float_complex | SAME | SAME | Same input and same marshal hash. |
| float_pos_one | float_complex | SAME | SAME | Same input and same marshal hash. |
| float_pos_zero | float_complex | SAME | SAME | Same input and same marshal hash. |
| float_tiny_1e_minus_300 | float_complex | SAME | SAME | Same input and same marshal hash. |
| lone_high_surrogate | unicode_string | SAME | SAME | Same input and same marshal hash. |
| non_bmp_character | unicode_string | SAME | SAME | Same input and same marshal hash. |
| nul_inside_string | unicode_string | SAME | SAME | Same input and same marshal hash. |
| recreated_complex_nan_both | float_complex | SAME | SAME | Same input and same marshal hash. |
| recreated_float_nan | float_complex | SAME | SAME | Same input and same marshal hash. |
| slice_1_10_2 | optional_slice_probe | DIFFERENT | SAME | Same optional support boundary or exception behavior. |
| slice_neg10_none_neg1 | optional_slice_probe | DIFFERENT | SAME | Same optional support boundary or exception behavior. |
| slice_none_none_none | optional_slice_probe | DIFFERENT | SAME | Same optional support boundary or exception behavior. |
| zero_width_joiner_sequence | unicode_string | SAME | SAME | Same input and same marshal hash. |

### member_b_all_linux_x86_64_py3_13_results (Linux/x86_64, Python 3.13.13) vs member_b_all_linux_x86_64_py3_9_results (Linux/x86_64, Python 3.9.25)

| Case | Category | Same marshal hash | Same exception | Interpretation |
| --- | --- | --- | --- | --- |
| ascii_plain | unicode_string | SAME | SAME | Same input and same marshal hash. |
| bytes_255_a | bytes_payload | SAME | SAME | Same input and same marshal hash. |
| bytes_256_a | bytes_payload | SAME | SAME | Same input and same marshal hash. |
| bytes_65535_a | bytes_payload | SAME | SAME | Same input and same marshal hash. |
| bytes_65536_a | bytes_payload | SAME | SAME | Same input and same marshal hash. |
| bytes_all_byte_values | bytes_payload | SAME | SAME | Same input and same marshal hash. |
| bytes_empty | bytes_payload | SAME | SAME | Same input and same marshal hash. |
| bytes_high_values_with_ascii | bytes_payload | SAME | SAME | Same input and same marshal hash. |
| bytes_single_nul | bytes_payload | SAME | SAME | Same input and same marshal hash. |
| chinese_text | unicode_string | SAME | SAME | Same input and same marshal hash. |
| complex_inf_neg_inf | float_complex | SAME | SAME | Same input and same marshal hash. |
| complex_nan_both | float_complex | SAME | SAME | Same input and same marshal hash. |
| complex_nan_imag | float_complex | SAME | SAME | Same input and same marshal hash. |
| complex_nan_real | float_complex | SAME | SAME | Same input and same marshal hash. |
| complex_payload_nan_imag | float_complex | SAME | SAME | Same input and same marshal hash. |
| complex_payload_nan_real | float_complex | SAME | SAME | Same input and same marshal hash. |
| complex_regular | float_complex | SAME | SAME | Same input and same marshal hash. |
| complex_zero_neg_zero | float_complex | SAME | SAME | Same input and same marshal hash. |
| composed_e_acute | unicode_string | DIFFERENT | SAME | Same input representation but Python major/minor differs; likely version-level marshal format difference. |
| constant_ellipsis | basic_scalar_constant | SAME | SAME | Same input and same marshal hash. |
| constant_false | basic_scalar_constant | SAME | SAME | Same input and same marshal hash. |
| constant_none | basic_scalar_constant | SAME | SAME | Same input and same marshal hash. |
| constant_true | basic_scalar_constant | SAME | SAME | Same input and same marshal hash. |
| crlf_string | unicode_string | SAME | SAME | Same input and same marshal hash. |
| decomposed_e_acute | unicode_string | SAME | SAME | Same input and same marshal hash. |
| emoji_text | unicode_string | SAME | SAME | Same input and same marshal hash. |
| float_huge_1e300 | float_complex | SAME | SAME | Same input and same marshal hash. |
| float_math_nan | float_complex | SAME | SAME | Same input and same marshal hash. |
| float_nan_constructor | float_complex | SAME | SAME | Same input and same marshal hash. |
| float_nan_payload_0x7ff0000000000001 | float_complex | SAME | SAME | Same input and same marshal hash. |
| float_nan_payload_0x7ff8000000000001 | float_complex | SAME | SAME | Same input and same marshal hash. |
| float_nan_payload_0x7ff8000000000002 | float_complex | SAME | SAME | Same input and same marshal hash. |
| float_neg_inf | float_complex | SAME | SAME | Same input and same marshal hash. |
| float_neg_one | float_complex | SAME | SAME | Same input and same marshal hash. |
| float_neg_zero | float_complex | SAME | SAME | Same input and same marshal hash. |
| float_pos_inf | float_complex | SAME | SAME | Same input and same marshal hash. |
| float_pos_one | float_complex | SAME | SAME | Same input and same marshal hash. |
| float_pos_zero | float_complex | SAME | SAME | Same input and same marshal hash. |
| float_tiny_1e_minus_300 | float_complex | SAME | SAME | Same input and same marshal hash. |
| lone_high_surrogate | unicode_string | SAME | SAME | Same input and same marshal hash. |
| non_bmp_character | unicode_string | SAME | SAME | Same input and same marshal hash. |
| nul_inside_string | unicode_string | SAME | SAME | Same input and same marshal hash. |
| recreated_complex_nan_both | float_complex | SAME | SAME | Same input and same marshal hash. |
| recreated_float_nan | float_complex | SAME | SAME | Same input and same marshal hash. |
| slice_1_10_2 | optional_slice_probe | DIFFERENT | SAME | Same optional support boundary or exception behavior. |
| slice_neg10_none_neg1 | optional_slice_probe | DIFFERENT | SAME | Same optional support boundary or exception behavior. |
| slice_none_none_none | optional_slice_probe | DIFFERENT | SAME | Same optional support boundary or exception behavior. |
| zero_width_joiner_sequence | unicode_string | SAME | SAME | Same input and same marshal hash. |

### member_b_all_linux_x86_64_py3_13_results (Linux/x86_64, Python 3.13.13) vs member_b_all_windows_amd64_py3_10_results (Windows/AMD64, Python 3.10.11)

| Case | Category | Same marshal hash | Same exception | Interpretation |
| --- | --- | --- | --- | --- |
| ascii_plain | unicode_string | SAME | SAME | Same input and same marshal hash. |
| bytes_255_a | bytes_payload | SAME | SAME | Same input and same marshal hash. |
| bytes_256_a | bytes_payload | SAME | SAME | Same input and same marshal hash. |
| bytes_65535_a | bytes_payload | SAME | SAME | Same input and same marshal hash. |
| bytes_65536_a | bytes_payload | SAME | SAME | Same input and same marshal hash. |
| bytes_all_byte_values | bytes_payload | SAME | SAME | Same input and same marshal hash. |
| bytes_empty | bytes_payload | SAME | SAME | Same input and same marshal hash. |
| bytes_high_values_with_ascii | bytes_payload | SAME | SAME | Same input and same marshal hash. |
| bytes_single_nul | bytes_payload | SAME | SAME | Same input and same marshal hash. |
| chinese_text | unicode_string | SAME | SAME | Same input and same marshal hash. |
| complex_inf_neg_inf | float_complex | SAME | SAME | Same input and same marshal hash. |
| complex_nan_both | float_complex | SAME | SAME | Same input and same marshal hash. |
| complex_nan_imag | float_complex | SAME | SAME | Same input and same marshal hash. |
| complex_nan_real | float_complex | SAME | SAME | Same input and same marshal hash. |
| complex_payload_nan_imag | float_complex | SAME | SAME | Same input and same marshal hash. |
| complex_payload_nan_real | float_complex | SAME | SAME | Same input and same marshal hash. |
| complex_regular | float_complex | SAME | SAME | Same input and same marshal hash. |
| complex_zero_neg_zero | float_complex | SAME | SAME | Same input and same marshal hash. |
| composed_e_acute | unicode_string | DIFFERENT | SAME | Same input representation but Python major/minor differs; likely version-level marshal format difference. |
| constant_ellipsis | basic_scalar_constant | SAME | SAME | Same input and same marshal hash. |
| constant_false | basic_scalar_constant | SAME | SAME | Same input and same marshal hash. |
| constant_none | basic_scalar_constant | SAME | SAME | Same input and same marshal hash. |
| constant_true | basic_scalar_constant | SAME | SAME | Same input and same marshal hash. |
| crlf_string | unicode_string | SAME | SAME | Same input and same marshal hash. |
| decomposed_e_acute | unicode_string | SAME | SAME | Same input and same marshal hash. |
| emoji_text | unicode_string | SAME | SAME | Same input and same marshal hash. |
| float_huge_1e300 | float_complex | SAME | SAME | Same input and same marshal hash. |
| float_math_nan | float_complex | SAME | SAME | Same input and same marshal hash. |
| float_nan_constructor | float_complex | SAME | SAME | Same input and same marshal hash. |
| float_nan_payload_0x7ff0000000000001 | float_complex | SAME | SAME | Same input and same marshal hash. |
| float_nan_payload_0x7ff8000000000001 | float_complex | SAME | SAME | Same input and same marshal hash. |
| float_nan_payload_0x7ff8000000000002 | float_complex | SAME | SAME | Same input and same marshal hash. |
| float_neg_inf | float_complex | SAME | SAME | Same input and same marshal hash. |
| float_neg_one | float_complex | SAME | SAME | Same input and same marshal hash. |
| float_neg_zero | float_complex | SAME | SAME | Same input and same marshal hash. |
| float_pos_inf | float_complex | SAME | SAME | Same input and same marshal hash. |
| float_pos_one | float_complex | SAME | SAME | Same input and same marshal hash. |
| float_pos_zero | float_complex | SAME | SAME | Same input and same marshal hash. |
| float_tiny_1e_minus_300 | float_complex | SAME | SAME | Same input and same marshal hash. |
| lone_high_surrogate | unicode_string | SAME | SAME | Same input and same marshal hash. |
| non_bmp_character | unicode_string | SAME | SAME | Same input and same marshal hash. |
| nul_inside_string | unicode_string | SAME | SAME | Same input and same marshal hash. |
| recreated_complex_nan_both | float_complex | SAME | SAME | Same input and same marshal hash. |
| recreated_float_nan | float_complex | SAME | SAME | Same input and same marshal hash. |
| slice_1_10_2 | optional_slice_probe | DIFFERENT | SAME | Same optional support boundary or exception behavior. |
| slice_neg10_none_neg1 | optional_slice_probe | DIFFERENT | SAME | Same optional support boundary or exception behavior. |
| slice_none_none_none | optional_slice_probe | DIFFERENT | SAME | Same optional support boundary or exception behavior. |
| zero_width_joiner_sequence | unicode_string | SAME | SAME | Same input and same marshal hash. |

### member_b_all_linux_x86_64_py3_13_results (Linux/x86_64, Python 3.13.13) vs member_b_all_windows_amd64_py3_11_results (Windows/AMD64, Python 3.11.9)

| Case | Category | Same marshal hash | Same exception | Interpretation |
| --- | --- | --- | --- | --- |
| ascii_plain | unicode_string | SAME | SAME | Same input and same marshal hash. |
| bytes_255_a | bytes_payload | SAME | SAME | Same input and same marshal hash. |
| bytes_256_a | bytes_payload | SAME | SAME | Same input and same marshal hash. |
| bytes_65535_a | bytes_payload | SAME | SAME | Same input and same marshal hash. |
| bytes_65536_a | bytes_payload | SAME | SAME | Same input and same marshal hash. |
| bytes_all_byte_values | bytes_payload | SAME | SAME | Same input and same marshal hash. |
| bytes_empty | bytes_payload | SAME | SAME | Same input and same marshal hash. |
| bytes_high_values_with_ascii | bytes_payload | SAME | SAME | Same input and same marshal hash. |
| bytes_single_nul | bytes_payload | SAME | SAME | Same input and same marshal hash. |
| chinese_text | unicode_string | SAME | SAME | Same input and same marshal hash. |
| complex_inf_neg_inf | float_complex | SAME | SAME | Same input and same marshal hash. |
| complex_nan_both | float_complex | SAME | SAME | Same input and same marshal hash. |
| complex_nan_imag | float_complex | SAME | SAME | Same input and same marshal hash. |
| complex_nan_real | float_complex | SAME | SAME | Same input and same marshal hash. |
| complex_payload_nan_imag | float_complex | SAME | SAME | Same input and same marshal hash. |
| complex_payload_nan_real | float_complex | SAME | SAME | Same input and same marshal hash. |
| complex_regular | float_complex | SAME | SAME | Same input and same marshal hash. |
| complex_zero_neg_zero | float_complex | SAME | SAME | Same input and same marshal hash. |
| composed_e_acute | unicode_string | DIFFERENT | SAME | Same input representation but Python major/minor differs; likely version-level marshal format difference. |
| constant_ellipsis | basic_scalar_constant | SAME | SAME | Same input and same marshal hash. |
| constant_false | basic_scalar_constant | SAME | SAME | Same input and same marshal hash. |
| constant_none | basic_scalar_constant | SAME | SAME | Same input and same marshal hash. |
| constant_true | basic_scalar_constant | SAME | SAME | Same input and same marshal hash. |
| crlf_string | unicode_string | SAME | SAME | Same input and same marshal hash. |
| decomposed_e_acute | unicode_string | SAME | SAME | Same input and same marshal hash. |
| emoji_text | unicode_string | SAME | SAME | Same input and same marshal hash. |
| float_huge_1e300 | float_complex | SAME | SAME | Same input and same marshal hash. |
| float_math_nan | float_complex | SAME | SAME | Same input and same marshal hash. |
| float_nan_constructor | float_complex | SAME | SAME | Same input and same marshal hash. |
| float_nan_payload_0x7ff0000000000001 | float_complex | SAME | SAME | Same input and same marshal hash. |
| float_nan_payload_0x7ff8000000000001 | float_complex | SAME | SAME | Same input and same marshal hash. |
| float_nan_payload_0x7ff8000000000002 | float_complex | SAME | SAME | Same input and same marshal hash. |
| float_neg_inf | float_complex | SAME | SAME | Same input and same marshal hash. |
| float_neg_one | float_complex | SAME | SAME | Same input and same marshal hash. |
| float_neg_zero | float_complex | SAME | SAME | Same input and same marshal hash. |
| float_pos_inf | float_complex | SAME | SAME | Same input and same marshal hash. |
| float_pos_one | float_complex | SAME | SAME | Same input and same marshal hash. |
| float_pos_zero | float_complex | SAME | SAME | Same input and same marshal hash. |
| float_tiny_1e_minus_300 | float_complex | SAME | SAME | Same input and same marshal hash. |
| lone_high_surrogate | unicode_string | SAME | SAME | Same input and same marshal hash. |
| non_bmp_character | unicode_string | SAME | SAME | Same input and same marshal hash. |
| nul_inside_string | unicode_string | SAME | SAME | Same input and same marshal hash. |
| recreated_complex_nan_both | float_complex | SAME | SAME | Same input and same marshal hash. |
| recreated_float_nan | float_complex | SAME | SAME | Same input and same marshal hash. |
| slice_1_10_2 | optional_slice_probe | DIFFERENT | SAME | Same optional support boundary or exception behavior. |
| slice_neg10_none_neg1 | optional_slice_probe | DIFFERENT | SAME | Same optional support boundary or exception behavior. |
| slice_none_none_none | optional_slice_probe | DIFFERENT | SAME | Same optional support boundary or exception behavior. |
| zero_width_joiner_sequence | unicode_string | SAME | SAME | Same input and same marshal hash. |

### member_b_all_linux_x86_64_py3_13_results (Linux/x86_64, Python 3.13.13) vs member_b_all_windows_amd64_py3_12_results (Windows/AMD64, Python 3.12.10)

| Case | Category | Same marshal hash | Same exception | Interpretation |
| --- | --- | --- | --- | --- |
| ascii_plain | unicode_string | SAME | SAME | Same input and same marshal hash. |
| bytes_255_a | bytes_payload | SAME | SAME | Same input and same marshal hash. |
| bytes_256_a | bytes_payload | SAME | SAME | Same input and same marshal hash. |
| bytes_65535_a | bytes_payload | SAME | SAME | Same input and same marshal hash. |
| bytes_65536_a | bytes_payload | SAME | SAME | Same input and same marshal hash. |
| bytes_all_byte_values | bytes_payload | SAME | SAME | Same input and same marshal hash. |
| bytes_empty | bytes_payload | SAME | SAME | Same input and same marshal hash. |
| bytes_high_values_with_ascii | bytes_payload | SAME | SAME | Same input and same marshal hash. |
| bytes_single_nul | bytes_payload | SAME | SAME | Same input and same marshal hash. |
| chinese_text | unicode_string | SAME | SAME | Same input and same marshal hash. |
| complex_inf_neg_inf | float_complex | SAME | SAME | Same input and same marshal hash. |
| complex_nan_both | float_complex | SAME | SAME | Same input and same marshal hash. |
| complex_nan_imag | float_complex | SAME | SAME | Same input and same marshal hash. |
| complex_nan_real | float_complex | SAME | SAME | Same input and same marshal hash. |
| complex_payload_nan_imag | float_complex | SAME | SAME | Same input and same marshal hash. |
| complex_payload_nan_real | float_complex | SAME | SAME | Same input and same marshal hash. |
| complex_regular | float_complex | SAME | SAME | Same input and same marshal hash. |
| complex_zero_neg_zero | float_complex | SAME | SAME | Same input and same marshal hash. |
| composed_e_acute | unicode_string | SAME | SAME | Same input and same marshal hash. |
| constant_ellipsis | basic_scalar_constant | SAME | SAME | Same input and same marshal hash. |
| constant_false | basic_scalar_constant | SAME | SAME | Same input and same marshal hash. |
| constant_none | basic_scalar_constant | SAME | SAME | Same input and same marshal hash. |
| constant_true | basic_scalar_constant | SAME | SAME | Same input and same marshal hash. |
| crlf_string | unicode_string | SAME | SAME | Same input and same marshal hash. |
| decomposed_e_acute | unicode_string | SAME | SAME | Same input and same marshal hash. |
| emoji_text | unicode_string | SAME | SAME | Same input and same marshal hash. |
| float_huge_1e300 | float_complex | SAME | SAME | Same input and same marshal hash. |
| float_math_nan | float_complex | SAME | SAME | Same input and same marshal hash. |
| float_nan_constructor | float_complex | SAME | SAME | Same input and same marshal hash. |
| float_nan_payload_0x7ff0000000000001 | float_complex | SAME | SAME | Same input and same marshal hash. |
| float_nan_payload_0x7ff8000000000001 | float_complex | SAME | SAME | Same input and same marshal hash. |
| float_nan_payload_0x7ff8000000000002 | float_complex | SAME | SAME | Same input and same marshal hash. |
| float_neg_inf | float_complex | SAME | SAME | Same input and same marshal hash. |
| float_neg_one | float_complex | SAME | SAME | Same input and same marshal hash. |
| float_neg_zero | float_complex | SAME | SAME | Same input and same marshal hash. |
| float_pos_inf | float_complex | SAME | SAME | Same input and same marshal hash. |
| float_pos_one | float_complex | SAME | SAME | Same input and same marshal hash. |
| float_pos_zero | float_complex | SAME | SAME | Same input and same marshal hash. |
| float_tiny_1e_minus_300 | float_complex | SAME | SAME | Same input and same marshal hash. |
| lone_high_surrogate | unicode_string | SAME | SAME | Same input and same marshal hash. |
| non_bmp_character | unicode_string | SAME | SAME | Same input and same marshal hash. |
| nul_inside_string | unicode_string | SAME | SAME | Same input and same marshal hash. |
| recreated_complex_nan_both | float_complex | SAME | SAME | Same input and same marshal hash. |
| recreated_float_nan | float_complex | SAME | SAME | Same input and same marshal hash. |
| slice_1_10_2 | optional_slice_probe | DIFFERENT | SAME | Same optional support boundary or exception behavior. |
| slice_neg10_none_neg1 | optional_slice_probe | DIFFERENT | SAME | Same optional support boundary or exception behavior. |
| slice_none_none_none | optional_slice_probe | DIFFERENT | SAME | Same optional support boundary or exception behavior. |
| zero_width_joiner_sequence | unicode_string | SAME | SAME | Same input and same marshal hash. |

### member_b_all_linux_x86_64_py3_13_results (Linux/x86_64, Python 3.13.13) vs member_b_all_windows_amd64_py3_13_results (Windows/AMD64, Python 3.13.13)

| Case | Category | Same marshal hash | Same exception | Interpretation |
| --- | --- | --- | --- | --- |
| ascii_plain | unicode_string | SAME | SAME | Same input and same marshal hash. |
| bytes_255_a | bytes_payload | SAME | SAME | Same input and same marshal hash. |
| bytes_256_a | bytes_payload | SAME | SAME | Same input and same marshal hash. |
| bytes_65535_a | bytes_payload | SAME | SAME | Same input and same marshal hash. |
| bytes_65536_a | bytes_payload | SAME | SAME | Same input and same marshal hash. |
| bytes_all_byte_values | bytes_payload | SAME | SAME | Same input and same marshal hash. |
| bytes_empty | bytes_payload | SAME | SAME | Same input and same marshal hash. |
| bytes_high_values_with_ascii | bytes_payload | SAME | SAME | Same input and same marshal hash. |
| bytes_single_nul | bytes_payload | SAME | SAME | Same input and same marshal hash. |
| chinese_text | unicode_string | SAME | SAME | Same input and same marshal hash. |
| complex_inf_neg_inf | float_complex | SAME | SAME | Same input and same marshal hash. |
| complex_nan_both | float_complex | SAME | SAME | Same input and same marshal hash. |
| complex_nan_imag | float_complex | SAME | SAME | Same input and same marshal hash. |
| complex_nan_real | float_complex | SAME | SAME | Same input and same marshal hash. |
| complex_payload_nan_imag | float_complex | SAME | SAME | Same input and same marshal hash. |
| complex_payload_nan_real | float_complex | SAME | SAME | Same input and same marshal hash. |
| complex_regular | float_complex | SAME | SAME | Same input and same marshal hash. |
| complex_zero_neg_zero | float_complex | SAME | SAME | Same input and same marshal hash. |
| composed_e_acute | unicode_string | SAME | SAME | Same input and same marshal hash. |
| constant_ellipsis | basic_scalar_constant | SAME | SAME | Same input and same marshal hash. |
| constant_false | basic_scalar_constant | SAME | SAME | Same input and same marshal hash. |
| constant_none | basic_scalar_constant | SAME | SAME | Same input and same marshal hash. |
| constant_true | basic_scalar_constant | SAME | SAME | Same input and same marshal hash. |
| crlf_string | unicode_string | SAME | SAME | Same input and same marshal hash. |
| decomposed_e_acute | unicode_string | SAME | SAME | Same input and same marshal hash. |
| emoji_text | unicode_string | SAME | SAME | Same input and same marshal hash. |
| float_huge_1e300 | float_complex | SAME | SAME | Same input and same marshal hash. |
| float_math_nan | float_complex | SAME | SAME | Same input and same marshal hash. |
| float_nan_constructor | float_complex | SAME | SAME | Same input and same marshal hash. |
| float_nan_payload_0x7ff0000000000001 | float_complex | SAME | SAME | Same input and same marshal hash. |
| float_nan_payload_0x7ff8000000000001 | float_complex | SAME | SAME | Same input and same marshal hash. |
| float_nan_payload_0x7ff8000000000002 | float_complex | SAME | SAME | Same input and same marshal hash. |
| float_neg_inf | float_complex | SAME | SAME | Same input and same marshal hash. |
| float_neg_one | float_complex | SAME | SAME | Same input and same marshal hash. |
| float_neg_zero | float_complex | SAME | SAME | Same input and same marshal hash. |
| float_pos_inf | float_complex | SAME | SAME | Same input and same marshal hash. |
| float_pos_one | float_complex | SAME | SAME | Same input and same marshal hash. |
| float_pos_zero | float_complex | SAME | SAME | Same input and same marshal hash. |
| float_tiny_1e_minus_300 | float_complex | SAME | SAME | Same input and same marshal hash. |
| lone_high_surrogate | unicode_string | SAME | SAME | Same input and same marshal hash. |
| non_bmp_character | unicode_string | SAME | SAME | Same input and same marshal hash. |
| nul_inside_string | unicode_string | SAME | SAME | Same input and same marshal hash. |
| recreated_complex_nan_both | float_complex | SAME | SAME | Same input and same marshal hash. |
| recreated_float_nan | float_complex | SAME | SAME | Same input and same marshal hash. |
| slice_1_10_2 | optional_slice_probe | DIFFERENT | SAME | Same optional support boundary or exception behavior. |
| slice_neg10_none_neg1 | optional_slice_probe | DIFFERENT | SAME | Same optional support boundary or exception behavior. |
| slice_none_none_none | optional_slice_probe | DIFFERENT | SAME | Same optional support boundary or exception behavior. |
| zero_width_joiner_sequence | unicode_string | SAME | SAME | Same input and same marshal hash. |

### member_b_all_linux_x86_64_py3_13_results (Linux/x86_64, Python 3.13.13) vs member_b_all_windows_amd64_py3_9_results (Windows/AMD64, Python 3.9.13)

| Case | Category | Same marshal hash | Same exception | Interpretation |
| --- | --- | --- | --- | --- |
| ascii_plain | unicode_string | SAME | SAME | Same input and same marshal hash. |
| bytes_255_a | bytes_payload | SAME | SAME | Same input and same marshal hash. |
| bytes_256_a | bytes_payload | SAME | SAME | Same input and same marshal hash. |
| bytes_65535_a | bytes_payload | SAME | SAME | Same input and same marshal hash. |
| bytes_65536_a | bytes_payload | SAME | SAME | Same input and same marshal hash. |
| bytes_all_byte_values | bytes_payload | SAME | SAME | Same input and same marshal hash. |
| bytes_empty | bytes_payload | SAME | SAME | Same input and same marshal hash. |
| bytes_high_values_with_ascii | bytes_payload | SAME | SAME | Same input and same marshal hash. |
| bytes_single_nul | bytes_payload | SAME | SAME | Same input and same marshal hash. |
| chinese_text | unicode_string | SAME | SAME | Same input and same marshal hash. |
| complex_inf_neg_inf | float_complex | SAME | SAME | Same input and same marshal hash. |
| complex_nan_both | float_complex | SAME | SAME | Same input and same marshal hash. |
| complex_nan_imag | float_complex | SAME | SAME | Same input and same marshal hash. |
| complex_nan_real | float_complex | SAME | SAME | Same input and same marshal hash. |
| complex_payload_nan_imag | float_complex | SAME | SAME | Same input and same marshal hash. |
| complex_payload_nan_real | float_complex | SAME | SAME | Same input and same marshal hash. |
| complex_regular | float_complex | SAME | SAME | Same input and same marshal hash. |
| complex_zero_neg_zero | float_complex | SAME | SAME | Same input and same marshal hash. |
| composed_e_acute | unicode_string | DIFFERENT | SAME | Same input representation but Python major/minor differs; likely version-level marshal format difference. |
| constant_ellipsis | basic_scalar_constant | SAME | SAME | Same input and same marshal hash. |
| constant_false | basic_scalar_constant | SAME | SAME | Same input and same marshal hash. |
| constant_none | basic_scalar_constant | SAME | SAME | Same input and same marshal hash. |
| constant_true | basic_scalar_constant | SAME | SAME | Same input and same marshal hash. |
| crlf_string | unicode_string | SAME | SAME | Same input and same marshal hash. |
| decomposed_e_acute | unicode_string | SAME | SAME | Same input and same marshal hash. |
| emoji_text | unicode_string | SAME | SAME | Same input and same marshal hash. |
| float_huge_1e300 | float_complex | SAME | SAME | Same input and same marshal hash. |
| float_math_nan | float_complex | SAME | SAME | Same input and same marshal hash. |
| float_nan_constructor | float_complex | SAME | SAME | Same input and same marshal hash. |
| float_nan_payload_0x7ff0000000000001 | float_complex | SAME | SAME | Same input and same marshal hash. |
| float_nan_payload_0x7ff8000000000001 | float_complex | SAME | SAME | Same input and same marshal hash. |
| float_nan_payload_0x7ff8000000000002 | float_complex | SAME | SAME | Same input and same marshal hash. |
| float_neg_inf | float_complex | SAME | SAME | Same input and same marshal hash. |
| float_neg_one | float_complex | SAME | SAME | Same input and same marshal hash. |
| float_neg_zero | float_complex | SAME | SAME | Same input and same marshal hash. |
| float_pos_inf | float_complex | SAME | SAME | Same input and same marshal hash. |
| float_pos_one | float_complex | SAME | SAME | Same input and same marshal hash. |
| float_pos_zero | float_complex | SAME | SAME | Same input and same marshal hash. |
| float_tiny_1e_minus_300 | float_complex | SAME | SAME | Same input and same marshal hash. |
| lone_high_surrogate | unicode_string | SAME | SAME | Same input and same marshal hash. |
| non_bmp_character | unicode_string | SAME | SAME | Same input and same marshal hash. |
| nul_inside_string | unicode_string | SAME | SAME | Same input and same marshal hash. |
| recreated_complex_nan_both | float_complex | SAME | SAME | Same input and same marshal hash. |
| recreated_float_nan | float_complex | SAME | SAME | Same input and same marshal hash. |
| slice_1_10_2 | optional_slice_probe | DIFFERENT | SAME | Same optional support boundary or exception behavior. |
| slice_neg10_none_neg1 | optional_slice_probe | DIFFERENT | SAME | Same optional support boundary or exception behavior. |
| slice_none_none_none | optional_slice_probe | DIFFERENT | SAME | Same optional support boundary or exception behavior. |
| zero_width_joiner_sequence | unicode_string | SAME | SAME | Same input and same marshal hash. |

### member_b_all_linux_x86_64_py3_9_results (Linux/x86_64, Python 3.9.25) vs member_b_all_windows_amd64_py3_10_results (Windows/AMD64, Python 3.10.11)

| Case | Category | Same marshal hash | Same exception | Interpretation |
| --- | --- | --- | --- | --- |
| ascii_plain | unicode_string | SAME | SAME | Same input and same marshal hash. |
| bytes_255_a | bytes_payload | SAME | SAME | Same input and same marshal hash. |
| bytes_256_a | bytes_payload | SAME | SAME | Same input and same marshal hash. |
| bytes_65535_a | bytes_payload | SAME | SAME | Same input and same marshal hash. |
| bytes_65536_a | bytes_payload | SAME | SAME | Same input and same marshal hash. |
| bytes_all_byte_values | bytes_payload | SAME | SAME | Same input and same marshal hash. |
| bytes_empty | bytes_payload | SAME | SAME | Same input and same marshal hash. |
| bytes_high_values_with_ascii | bytes_payload | SAME | SAME | Same input and same marshal hash. |
| bytes_single_nul | bytes_payload | SAME | SAME | Same input and same marshal hash. |
| chinese_text | unicode_string | SAME | SAME | Same input and same marshal hash. |
| complex_inf_neg_inf | float_complex | SAME | SAME | Same input and same marshal hash. |
| complex_nan_both | float_complex | SAME | SAME | Same input and same marshal hash. |
| complex_nan_imag | float_complex | SAME | SAME | Same input and same marshal hash. |
| complex_nan_real | float_complex | SAME | SAME | Same input and same marshal hash. |
| complex_payload_nan_imag | float_complex | SAME | SAME | Same input and same marshal hash. |
| complex_payload_nan_real | float_complex | SAME | SAME | Same input and same marshal hash. |
| complex_regular | float_complex | SAME | SAME | Same input and same marshal hash. |
| complex_zero_neg_zero | float_complex | SAME | SAME | Same input and same marshal hash. |
| composed_e_acute | unicode_string | SAME | SAME | Same input and same marshal hash. |
| constant_ellipsis | basic_scalar_constant | SAME | SAME | Same input and same marshal hash. |
| constant_false | basic_scalar_constant | SAME | SAME | Same input and same marshal hash. |
| constant_none | basic_scalar_constant | SAME | SAME | Same input and same marshal hash. |
| constant_true | basic_scalar_constant | SAME | SAME | Same input and same marshal hash. |
| crlf_string | unicode_string | SAME | SAME | Same input and same marshal hash. |
| decomposed_e_acute | unicode_string | SAME | SAME | Same input and same marshal hash. |
| emoji_text | unicode_string | SAME | SAME | Same input and same marshal hash. |
| float_huge_1e300 | float_complex | SAME | SAME | Same input and same marshal hash. |
| float_math_nan | float_complex | SAME | SAME | Same input and same marshal hash. |
| float_nan_constructor | float_complex | SAME | SAME | Same input and same marshal hash. |
| float_nan_payload_0x7ff0000000000001 | float_complex | SAME | SAME | Same input and same marshal hash. |
| float_nan_payload_0x7ff8000000000001 | float_complex | SAME | SAME | Same input and same marshal hash. |
| float_nan_payload_0x7ff8000000000002 | float_complex | SAME | SAME | Same input and same marshal hash. |
| float_neg_inf | float_complex | SAME | SAME | Same input and same marshal hash. |
| float_neg_one | float_complex | SAME | SAME | Same input and same marshal hash. |
| float_neg_zero | float_complex | SAME | SAME | Same input and same marshal hash. |
| float_pos_inf | float_complex | SAME | SAME | Same input and same marshal hash. |
| float_pos_one | float_complex | SAME | SAME | Same input and same marshal hash. |
| float_pos_zero | float_complex | SAME | SAME | Same input and same marshal hash. |
| float_tiny_1e_minus_300 | float_complex | SAME | SAME | Same input and same marshal hash. |
| lone_high_surrogate | unicode_string | SAME | SAME | Same input and same marshal hash. |
| non_bmp_character | unicode_string | SAME | SAME | Same input and same marshal hash. |
| nul_inside_string | unicode_string | SAME | SAME | Same input and same marshal hash. |
| recreated_complex_nan_both | float_complex | SAME | SAME | Same input and same marshal hash. |
| recreated_float_nan | float_complex | SAME | SAME | Same input and same marshal hash. |
| slice_1_10_2 | optional_slice_probe | DIFFERENT | SAME | Same optional support boundary or exception behavior. |
| slice_neg10_none_neg1 | optional_slice_probe | DIFFERENT | SAME | Same optional support boundary or exception behavior. |
| slice_none_none_none | optional_slice_probe | DIFFERENT | SAME | Same optional support boundary or exception behavior. |
| zero_width_joiner_sequence | unicode_string | SAME | SAME | Same input and same marshal hash. |

### member_b_all_linux_x86_64_py3_9_results (Linux/x86_64, Python 3.9.25) vs member_b_all_windows_amd64_py3_11_results (Windows/AMD64, Python 3.11.9)

| Case | Category | Same marshal hash | Same exception | Interpretation |
| --- | --- | --- | --- | --- |
| ascii_plain | unicode_string | SAME | SAME | Same input and same marshal hash. |
| bytes_255_a | bytes_payload | SAME | SAME | Same input and same marshal hash. |
| bytes_256_a | bytes_payload | SAME | SAME | Same input and same marshal hash. |
| bytes_65535_a | bytes_payload | SAME | SAME | Same input and same marshal hash. |
| bytes_65536_a | bytes_payload | SAME | SAME | Same input and same marshal hash. |
| bytes_all_byte_values | bytes_payload | SAME | SAME | Same input and same marshal hash. |
| bytes_empty | bytes_payload | SAME | SAME | Same input and same marshal hash. |
| bytes_high_values_with_ascii | bytes_payload | SAME | SAME | Same input and same marshal hash. |
| bytes_single_nul | bytes_payload | SAME | SAME | Same input and same marshal hash. |
| chinese_text | unicode_string | SAME | SAME | Same input and same marshal hash. |
| complex_inf_neg_inf | float_complex | SAME | SAME | Same input and same marshal hash. |
| complex_nan_both | float_complex | SAME | SAME | Same input and same marshal hash. |
| complex_nan_imag | float_complex | SAME | SAME | Same input and same marshal hash. |
| complex_nan_real | float_complex | SAME | SAME | Same input and same marshal hash. |
| complex_payload_nan_imag | float_complex | SAME | SAME | Same input and same marshal hash. |
| complex_payload_nan_real | float_complex | SAME | SAME | Same input and same marshal hash. |
| complex_regular | float_complex | SAME | SAME | Same input and same marshal hash. |
| complex_zero_neg_zero | float_complex | SAME | SAME | Same input and same marshal hash. |
| composed_e_acute | unicode_string | SAME | SAME | Same input and same marshal hash. |
| constant_ellipsis | basic_scalar_constant | SAME | SAME | Same input and same marshal hash. |
| constant_false | basic_scalar_constant | SAME | SAME | Same input and same marshal hash. |
| constant_none | basic_scalar_constant | SAME | SAME | Same input and same marshal hash. |
| constant_true | basic_scalar_constant | SAME | SAME | Same input and same marshal hash. |
| crlf_string | unicode_string | SAME | SAME | Same input and same marshal hash. |
| decomposed_e_acute | unicode_string | SAME | SAME | Same input and same marshal hash. |
| emoji_text | unicode_string | SAME | SAME | Same input and same marshal hash. |
| float_huge_1e300 | float_complex | SAME | SAME | Same input and same marshal hash. |
| float_math_nan | float_complex | SAME | SAME | Same input and same marshal hash. |
| float_nan_constructor | float_complex | SAME | SAME | Same input and same marshal hash. |
| float_nan_payload_0x7ff0000000000001 | float_complex | SAME | SAME | Same input and same marshal hash. |
| float_nan_payload_0x7ff8000000000001 | float_complex | SAME | SAME | Same input and same marshal hash. |
| float_nan_payload_0x7ff8000000000002 | float_complex | SAME | SAME | Same input and same marshal hash. |
| float_neg_inf | float_complex | SAME | SAME | Same input and same marshal hash. |
| float_neg_one | float_complex | SAME | SAME | Same input and same marshal hash. |
| float_neg_zero | float_complex | SAME | SAME | Same input and same marshal hash. |
| float_pos_inf | float_complex | SAME | SAME | Same input and same marshal hash. |
| float_pos_one | float_complex | SAME | SAME | Same input and same marshal hash. |
| float_pos_zero | float_complex | SAME | SAME | Same input and same marshal hash. |
| float_tiny_1e_minus_300 | float_complex | SAME | SAME | Same input and same marshal hash. |
| lone_high_surrogate | unicode_string | SAME | SAME | Same input and same marshal hash. |
| non_bmp_character | unicode_string | SAME | SAME | Same input and same marshal hash. |
| nul_inside_string | unicode_string | SAME | SAME | Same input and same marshal hash. |
| recreated_complex_nan_both | float_complex | SAME | SAME | Same input and same marshal hash. |
| recreated_float_nan | float_complex | SAME | SAME | Same input and same marshal hash. |
| slice_1_10_2 | optional_slice_probe | DIFFERENT | SAME | Same optional support boundary or exception behavior. |
| slice_neg10_none_neg1 | optional_slice_probe | DIFFERENT | SAME | Same optional support boundary or exception behavior. |
| slice_none_none_none | optional_slice_probe | DIFFERENT | SAME | Same optional support boundary or exception behavior. |
| zero_width_joiner_sequence | unicode_string | SAME | SAME | Same input and same marshal hash. |

### member_b_all_linux_x86_64_py3_9_results (Linux/x86_64, Python 3.9.25) vs member_b_all_windows_amd64_py3_12_results (Windows/AMD64, Python 3.12.10)

| Case | Category | Same marshal hash | Same exception | Interpretation |
| --- | --- | --- | --- | --- |
| ascii_plain | unicode_string | SAME | SAME | Same input and same marshal hash. |
| bytes_255_a | bytes_payload | SAME | SAME | Same input and same marshal hash. |
| bytes_256_a | bytes_payload | SAME | SAME | Same input and same marshal hash. |
| bytes_65535_a | bytes_payload | SAME | SAME | Same input and same marshal hash. |
| bytes_65536_a | bytes_payload | SAME | SAME | Same input and same marshal hash. |
| bytes_all_byte_values | bytes_payload | SAME | SAME | Same input and same marshal hash. |
| bytes_empty | bytes_payload | SAME | SAME | Same input and same marshal hash. |
| bytes_high_values_with_ascii | bytes_payload | SAME | SAME | Same input and same marshal hash. |
| bytes_single_nul | bytes_payload | SAME | SAME | Same input and same marshal hash. |
| chinese_text | unicode_string | SAME | SAME | Same input and same marshal hash. |
| complex_inf_neg_inf | float_complex | SAME | SAME | Same input and same marshal hash. |
| complex_nan_both | float_complex | SAME | SAME | Same input and same marshal hash. |
| complex_nan_imag | float_complex | SAME | SAME | Same input and same marshal hash. |
| complex_nan_real | float_complex | SAME | SAME | Same input and same marshal hash. |
| complex_payload_nan_imag | float_complex | SAME | SAME | Same input and same marshal hash. |
| complex_payload_nan_real | float_complex | SAME | SAME | Same input and same marshal hash. |
| complex_regular | float_complex | SAME | SAME | Same input and same marshal hash. |
| complex_zero_neg_zero | float_complex | SAME | SAME | Same input and same marshal hash. |
| composed_e_acute | unicode_string | DIFFERENT | SAME | Same input representation but Python major/minor differs; likely version-level marshal format difference. |
| constant_ellipsis | basic_scalar_constant | SAME | SAME | Same input and same marshal hash. |
| constant_false | basic_scalar_constant | SAME | SAME | Same input and same marshal hash. |
| constant_none | basic_scalar_constant | SAME | SAME | Same input and same marshal hash. |
| constant_true | basic_scalar_constant | SAME | SAME | Same input and same marshal hash. |
| crlf_string | unicode_string | SAME | SAME | Same input and same marshal hash. |
| decomposed_e_acute | unicode_string | SAME | SAME | Same input and same marshal hash. |
| emoji_text | unicode_string | SAME | SAME | Same input and same marshal hash. |
| float_huge_1e300 | float_complex | SAME | SAME | Same input and same marshal hash. |
| float_math_nan | float_complex | SAME | SAME | Same input and same marshal hash. |
| float_nan_constructor | float_complex | SAME | SAME | Same input and same marshal hash. |
| float_nan_payload_0x7ff0000000000001 | float_complex | SAME | SAME | Same input and same marshal hash. |
| float_nan_payload_0x7ff8000000000001 | float_complex | SAME | SAME | Same input and same marshal hash. |
| float_nan_payload_0x7ff8000000000002 | float_complex | SAME | SAME | Same input and same marshal hash. |
| float_neg_inf | float_complex | SAME | SAME | Same input and same marshal hash. |
| float_neg_one | float_complex | SAME | SAME | Same input and same marshal hash. |
| float_neg_zero | float_complex | SAME | SAME | Same input and same marshal hash. |
| float_pos_inf | float_complex | SAME | SAME | Same input and same marshal hash. |
| float_pos_one | float_complex | SAME | SAME | Same input and same marshal hash. |
| float_pos_zero | float_complex | SAME | SAME | Same input and same marshal hash. |
| float_tiny_1e_minus_300 | float_complex | SAME | SAME | Same input and same marshal hash. |
| lone_high_surrogate | unicode_string | SAME | SAME | Same input and same marshal hash. |
| non_bmp_character | unicode_string | SAME | SAME | Same input and same marshal hash. |
| nul_inside_string | unicode_string | SAME | SAME | Same input and same marshal hash. |
| recreated_complex_nan_both | float_complex | SAME | SAME | Same input and same marshal hash. |
| recreated_float_nan | float_complex | SAME | SAME | Same input and same marshal hash. |
| slice_1_10_2 | optional_slice_probe | DIFFERENT | SAME | Same optional support boundary or exception behavior. |
| slice_neg10_none_neg1 | optional_slice_probe | DIFFERENT | SAME | Same optional support boundary or exception behavior. |
| slice_none_none_none | optional_slice_probe | DIFFERENT | SAME | Same optional support boundary or exception behavior. |
| zero_width_joiner_sequence | unicode_string | SAME | SAME | Same input and same marshal hash. |

### member_b_all_linux_x86_64_py3_9_results (Linux/x86_64, Python 3.9.25) vs member_b_all_windows_amd64_py3_13_results (Windows/AMD64, Python 3.13.13)

| Case | Category | Same marshal hash | Same exception | Interpretation |
| --- | --- | --- | --- | --- |
| ascii_plain | unicode_string | SAME | SAME | Same input and same marshal hash. |
| bytes_255_a | bytes_payload | SAME | SAME | Same input and same marshal hash. |
| bytes_256_a | bytes_payload | SAME | SAME | Same input and same marshal hash. |
| bytes_65535_a | bytes_payload | SAME | SAME | Same input and same marshal hash. |
| bytes_65536_a | bytes_payload | SAME | SAME | Same input and same marshal hash. |
| bytes_all_byte_values | bytes_payload | SAME | SAME | Same input and same marshal hash. |
| bytes_empty | bytes_payload | SAME | SAME | Same input and same marshal hash. |
| bytes_high_values_with_ascii | bytes_payload | SAME | SAME | Same input and same marshal hash. |
| bytes_single_nul | bytes_payload | SAME | SAME | Same input and same marshal hash. |
| chinese_text | unicode_string | SAME | SAME | Same input and same marshal hash. |
| complex_inf_neg_inf | float_complex | SAME | SAME | Same input and same marshal hash. |
| complex_nan_both | float_complex | SAME | SAME | Same input and same marshal hash. |
| complex_nan_imag | float_complex | SAME | SAME | Same input and same marshal hash. |
| complex_nan_real | float_complex | SAME | SAME | Same input and same marshal hash. |
| complex_payload_nan_imag | float_complex | SAME | SAME | Same input and same marshal hash. |
| complex_payload_nan_real | float_complex | SAME | SAME | Same input and same marshal hash. |
| complex_regular | float_complex | SAME | SAME | Same input and same marshal hash. |
| complex_zero_neg_zero | float_complex | SAME | SAME | Same input and same marshal hash. |
| composed_e_acute | unicode_string | DIFFERENT | SAME | Same input representation but Python major/minor differs; likely version-level marshal format difference. |
| constant_ellipsis | basic_scalar_constant | SAME | SAME | Same input and same marshal hash. |
| constant_false | basic_scalar_constant | SAME | SAME | Same input and same marshal hash. |
| constant_none | basic_scalar_constant | SAME | SAME | Same input and same marshal hash. |
| constant_true | basic_scalar_constant | SAME | SAME | Same input and same marshal hash. |
| crlf_string | unicode_string | SAME | SAME | Same input and same marshal hash. |
| decomposed_e_acute | unicode_string | SAME | SAME | Same input and same marshal hash. |
| emoji_text | unicode_string | SAME | SAME | Same input and same marshal hash. |
| float_huge_1e300 | float_complex | SAME | SAME | Same input and same marshal hash. |
| float_math_nan | float_complex | SAME | SAME | Same input and same marshal hash. |
| float_nan_constructor | float_complex | SAME | SAME | Same input and same marshal hash. |
| float_nan_payload_0x7ff0000000000001 | float_complex | SAME | SAME | Same input and same marshal hash. |
| float_nan_payload_0x7ff8000000000001 | float_complex | SAME | SAME | Same input and same marshal hash. |
| float_nan_payload_0x7ff8000000000002 | float_complex | SAME | SAME | Same input and same marshal hash. |
| float_neg_inf | float_complex | SAME | SAME | Same input and same marshal hash. |
| float_neg_one | float_complex | SAME | SAME | Same input and same marshal hash. |
| float_neg_zero | float_complex | SAME | SAME | Same input and same marshal hash. |
| float_pos_inf | float_complex | SAME | SAME | Same input and same marshal hash. |
| float_pos_one | float_complex | SAME | SAME | Same input and same marshal hash. |
| float_pos_zero | float_complex | SAME | SAME | Same input and same marshal hash. |
| float_tiny_1e_minus_300 | float_complex | SAME | SAME | Same input and same marshal hash. |
| lone_high_surrogate | unicode_string | SAME | SAME | Same input and same marshal hash. |
| non_bmp_character | unicode_string | SAME | SAME | Same input and same marshal hash. |
| nul_inside_string | unicode_string | SAME | SAME | Same input and same marshal hash. |
| recreated_complex_nan_both | float_complex | SAME | SAME | Same input and same marshal hash. |
| recreated_float_nan | float_complex | SAME | SAME | Same input and same marshal hash. |
| slice_1_10_2 | optional_slice_probe | DIFFERENT | SAME | Same optional support boundary or exception behavior. |
| slice_neg10_none_neg1 | optional_slice_probe | DIFFERENT | SAME | Same optional support boundary or exception behavior. |
| slice_none_none_none | optional_slice_probe | DIFFERENT | SAME | Same optional support boundary or exception behavior. |
| zero_width_joiner_sequence | unicode_string | SAME | SAME | Same input and same marshal hash. |

### member_b_all_linux_x86_64_py3_9_results (Linux/x86_64, Python 3.9.25) vs member_b_all_windows_amd64_py3_9_results (Windows/AMD64, Python 3.9.13)

| Case | Category | Same marshal hash | Same exception | Interpretation |
| --- | --- | --- | --- | --- |
| ascii_plain | unicode_string | SAME | SAME | Same input and same marshal hash. |
| bytes_255_a | bytes_payload | SAME | SAME | Same input and same marshal hash. |
| bytes_256_a | bytes_payload | SAME | SAME | Same input and same marshal hash. |
| bytes_65535_a | bytes_payload | SAME | SAME | Same input and same marshal hash. |
| bytes_65536_a | bytes_payload | SAME | SAME | Same input and same marshal hash. |
| bytes_all_byte_values | bytes_payload | SAME | SAME | Same input and same marshal hash. |
| bytes_empty | bytes_payload | SAME | SAME | Same input and same marshal hash. |
| bytes_high_values_with_ascii | bytes_payload | SAME | SAME | Same input and same marshal hash. |
| bytes_single_nul | bytes_payload | SAME | SAME | Same input and same marshal hash. |
| chinese_text | unicode_string | SAME | SAME | Same input and same marshal hash. |
| complex_inf_neg_inf | float_complex | SAME | SAME | Same input and same marshal hash. |
| complex_nan_both | float_complex | SAME | SAME | Same input and same marshal hash. |
| complex_nan_imag | float_complex | SAME | SAME | Same input and same marshal hash. |
| complex_nan_real | float_complex | SAME | SAME | Same input and same marshal hash. |
| complex_payload_nan_imag | float_complex | SAME | SAME | Same input and same marshal hash. |
| complex_payload_nan_real | float_complex | SAME | SAME | Same input and same marshal hash. |
| complex_regular | float_complex | SAME | SAME | Same input and same marshal hash. |
| complex_zero_neg_zero | float_complex | SAME | SAME | Same input and same marshal hash. |
| composed_e_acute | unicode_string | SAME | SAME | Same input and same marshal hash. |
| constant_ellipsis | basic_scalar_constant | SAME | SAME | Same input and same marshal hash. |
| constant_false | basic_scalar_constant | SAME | SAME | Same input and same marshal hash. |
| constant_none | basic_scalar_constant | SAME | SAME | Same input and same marshal hash. |
| constant_true | basic_scalar_constant | SAME | SAME | Same input and same marshal hash. |
| crlf_string | unicode_string | SAME | SAME | Same input and same marshal hash. |
| decomposed_e_acute | unicode_string | SAME | SAME | Same input and same marshal hash. |
| emoji_text | unicode_string | SAME | SAME | Same input and same marshal hash. |
| float_huge_1e300 | float_complex | SAME | SAME | Same input and same marshal hash. |
| float_math_nan | float_complex | SAME | SAME | Same input and same marshal hash. |
| float_nan_constructor | float_complex | SAME | SAME | Same input and same marshal hash. |
| float_nan_payload_0x7ff0000000000001 | float_complex | SAME | SAME | Same input and same marshal hash. |
| float_nan_payload_0x7ff8000000000001 | float_complex | SAME | SAME | Same input and same marshal hash. |
| float_nan_payload_0x7ff8000000000002 | float_complex | SAME | SAME | Same input and same marshal hash. |
| float_neg_inf | float_complex | SAME | SAME | Same input and same marshal hash. |
| float_neg_one | float_complex | SAME | SAME | Same input and same marshal hash. |
| float_neg_zero | float_complex | SAME | SAME | Same input and same marshal hash. |
| float_pos_inf | float_complex | SAME | SAME | Same input and same marshal hash. |
| float_pos_one | float_complex | SAME | SAME | Same input and same marshal hash. |
| float_pos_zero | float_complex | SAME | SAME | Same input and same marshal hash. |
| float_tiny_1e_minus_300 | float_complex | SAME | SAME | Same input and same marshal hash. |
| lone_high_surrogate | unicode_string | SAME | SAME | Same input and same marshal hash. |
| non_bmp_character | unicode_string | SAME | SAME | Same input and same marshal hash. |
| nul_inside_string | unicode_string | SAME | SAME | Same input and same marshal hash. |
| recreated_complex_nan_both | float_complex | SAME | SAME | Same input and same marshal hash. |
| recreated_float_nan | float_complex | SAME | SAME | Same input and same marshal hash. |
| slice_1_10_2 | optional_slice_probe | DIFFERENT | SAME | Same optional support boundary or exception behavior. |
| slice_neg10_none_neg1 | optional_slice_probe | DIFFERENT | SAME | Same optional support boundary or exception behavior. |
| slice_none_none_none | optional_slice_probe | DIFFERENT | SAME | Same optional support boundary or exception behavior. |
| zero_width_joiner_sequence | unicode_string | SAME | SAME | Same input and same marshal hash. |

### member_b_all_windows_amd64_py3_10_results (Windows/AMD64, Python 3.10.11) vs member_b_all_windows_amd64_py3_11_results (Windows/AMD64, Python 3.11.9)

| Case | Category | Same marshal hash | Same exception | Interpretation |
| --- | --- | --- | --- | --- |
| ascii_plain | unicode_string | SAME | SAME | Same input and same marshal hash. |
| bytes_255_a | bytes_payload | SAME | SAME | Same input and same marshal hash. |
| bytes_256_a | bytes_payload | SAME | SAME | Same input and same marshal hash. |
| bytes_65535_a | bytes_payload | SAME | SAME | Same input and same marshal hash. |
| bytes_65536_a | bytes_payload | SAME | SAME | Same input and same marshal hash. |
| bytes_all_byte_values | bytes_payload | SAME | SAME | Same input and same marshal hash. |
| bytes_empty | bytes_payload | SAME | SAME | Same input and same marshal hash. |
| bytes_high_values_with_ascii | bytes_payload | SAME | SAME | Same input and same marshal hash. |
| bytes_single_nul | bytes_payload | SAME | SAME | Same input and same marshal hash. |
| chinese_text | unicode_string | SAME | SAME | Same input and same marshal hash. |
| complex_inf_neg_inf | float_complex | SAME | SAME | Same input and same marshal hash. |
| complex_nan_both | float_complex | SAME | SAME | Same input and same marshal hash. |
| complex_nan_imag | float_complex | SAME | SAME | Same input and same marshal hash. |
| complex_nan_real | float_complex | SAME | SAME | Same input and same marshal hash. |
| complex_payload_nan_imag | float_complex | SAME | SAME | Same input and same marshal hash. |
| complex_payload_nan_real | float_complex | SAME | SAME | Same input and same marshal hash. |
| complex_regular | float_complex | SAME | SAME | Same input and same marshal hash. |
| complex_zero_neg_zero | float_complex | SAME | SAME | Same input and same marshal hash. |
| composed_e_acute | unicode_string | SAME | SAME | Same input and same marshal hash. |
| constant_ellipsis | basic_scalar_constant | SAME | SAME | Same input and same marshal hash. |
| constant_false | basic_scalar_constant | SAME | SAME | Same input and same marshal hash. |
| constant_none | basic_scalar_constant | SAME | SAME | Same input and same marshal hash. |
| constant_true | basic_scalar_constant | SAME | SAME | Same input and same marshal hash. |
| crlf_string | unicode_string | SAME | SAME | Same input and same marshal hash. |
| decomposed_e_acute | unicode_string | SAME | SAME | Same input and same marshal hash. |
| emoji_text | unicode_string | SAME | SAME | Same input and same marshal hash. |
| float_huge_1e300 | float_complex | SAME | SAME | Same input and same marshal hash. |
| float_math_nan | float_complex | SAME | SAME | Same input and same marshal hash. |
| float_nan_constructor | float_complex | SAME | SAME | Same input and same marshal hash. |
| float_nan_payload_0x7ff0000000000001 | float_complex | SAME | SAME | Same input and same marshal hash. |
| float_nan_payload_0x7ff8000000000001 | float_complex | SAME | SAME | Same input and same marshal hash. |
| float_nan_payload_0x7ff8000000000002 | float_complex | SAME | SAME | Same input and same marshal hash. |
| float_neg_inf | float_complex | SAME | SAME | Same input and same marshal hash. |
| float_neg_one | float_complex | SAME | SAME | Same input and same marshal hash. |
| float_neg_zero | float_complex | SAME | SAME | Same input and same marshal hash. |
| float_pos_inf | float_complex | SAME | SAME | Same input and same marshal hash. |
| float_pos_one | float_complex | SAME | SAME | Same input and same marshal hash. |
| float_pos_zero | float_complex | SAME | SAME | Same input and same marshal hash. |
| float_tiny_1e_minus_300 | float_complex | SAME | SAME | Same input and same marshal hash. |
| lone_high_surrogate | unicode_string | SAME | SAME | Same input and same marshal hash. |
| non_bmp_character | unicode_string | SAME | SAME | Same input and same marshal hash. |
| nul_inside_string | unicode_string | SAME | SAME | Same input and same marshal hash. |
| recreated_complex_nan_both | float_complex | SAME | SAME | Same input and same marshal hash. |
| recreated_float_nan | float_complex | SAME | SAME | Same input and same marshal hash. |
| slice_1_10_2 | optional_slice_probe | DIFFERENT | SAME | Same optional support boundary or exception behavior. |
| slice_neg10_none_neg1 | optional_slice_probe | DIFFERENT | SAME | Same optional support boundary or exception behavior. |
| slice_none_none_none | optional_slice_probe | DIFFERENT | SAME | Same optional support boundary or exception behavior. |
| zero_width_joiner_sequence | unicode_string | SAME | SAME | Same input and same marshal hash. |

### member_b_all_windows_amd64_py3_10_results (Windows/AMD64, Python 3.10.11) vs member_b_all_windows_amd64_py3_12_results (Windows/AMD64, Python 3.12.10)

| Case | Category | Same marshal hash | Same exception | Interpretation |
| --- | --- | --- | --- | --- |
| ascii_plain | unicode_string | SAME | SAME | Same input and same marshal hash. |
| bytes_255_a | bytes_payload | SAME | SAME | Same input and same marshal hash. |
| bytes_256_a | bytes_payload | SAME | SAME | Same input and same marshal hash. |
| bytes_65535_a | bytes_payload | SAME | SAME | Same input and same marshal hash. |
| bytes_65536_a | bytes_payload | SAME | SAME | Same input and same marshal hash. |
| bytes_all_byte_values | bytes_payload | SAME | SAME | Same input and same marshal hash. |
| bytes_empty | bytes_payload | SAME | SAME | Same input and same marshal hash. |
| bytes_high_values_with_ascii | bytes_payload | SAME | SAME | Same input and same marshal hash. |
| bytes_single_nul | bytes_payload | SAME | SAME | Same input and same marshal hash. |
| chinese_text | unicode_string | SAME | SAME | Same input and same marshal hash. |
| complex_inf_neg_inf | float_complex | SAME | SAME | Same input and same marshal hash. |
| complex_nan_both | float_complex | SAME | SAME | Same input and same marshal hash. |
| complex_nan_imag | float_complex | SAME | SAME | Same input and same marshal hash. |
| complex_nan_real | float_complex | SAME | SAME | Same input and same marshal hash. |
| complex_payload_nan_imag | float_complex | SAME | SAME | Same input and same marshal hash. |
| complex_payload_nan_real | float_complex | SAME | SAME | Same input and same marshal hash. |
| complex_regular | float_complex | SAME | SAME | Same input and same marshal hash. |
| complex_zero_neg_zero | float_complex | SAME | SAME | Same input and same marshal hash. |
| composed_e_acute | unicode_string | DIFFERENT | SAME | Same input representation but Python major/minor differs; likely version-level marshal format difference. |
| constant_ellipsis | basic_scalar_constant | SAME | SAME | Same input and same marshal hash. |
| constant_false | basic_scalar_constant | SAME | SAME | Same input and same marshal hash. |
| constant_none | basic_scalar_constant | SAME | SAME | Same input and same marshal hash. |
| constant_true | basic_scalar_constant | SAME | SAME | Same input and same marshal hash. |
| crlf_string | unicode_string | SAME | SAME | Same input and same marshal hash. |
| decomposed_e_acute | unicode_string | SAME | SAME | Same input and same marshal hash. |
| emoji_text | unicode_string | SAME | SAME | Same input and same marshal hash. |
| float_huge_1e300 | float_complex | SAME | SAME | Same input and same marshal hash. |
| float_math_nan | float_complex | SAME | SAME | Same input and same marshal hash. |
| float_nan_constructor | float_complex | SAME | SAME | Same input and same marshal hash. |
| float_nan_payload_0x7ff0000000000001 | float_complex | SAME | SAME | Same input and same marshal hash. |
| float_nan_payload_0x7ff8000000000001 | float_complex | SAME | SAME | Same input and same marshal hash. |
| float_nan_payload_0x7ff8000000000002 | float_complex | SAME | SAME | Same input and same marshal hash. |
| float_neg_inf | float_complex | SAME | SAME | Same input and same marshal hash. |
| float_neg_one | float_complex | SAME | SAME | Same input and same marshal hash. |
| float_neg_zero | float_complex | SAME | SAME | Same input and same marshal hash. |
| float_pos_inf | float_complex | SAME | SAME | Same input and same marshal hash. |
| float_pos_one | float_complex | SAME | SAME | Same input and same marshal hash. |
| float_pos_zero | float_complex | SAME | SAME | Same input and same marshal hash. |
| float_tiny_1e_minus_300 | float_complex | SAME | SAME | Same input and same marshal hash. |
| lone_high_surrogate | unicode_string | SAME | SAME | Same input and same marshal hash. |
| non_bmp_character | unicode_string | SAME | SAME | Same input and same marshal hash. |
| nul_inside_string | unicode_string | SAME | SAME | Same input and same marshal hash. |
| recreated_complex_nan_both | float_complex | SAME | SAME | Same input and same marshal hash. |
| recreated_float_nan | float_complex | SAME | SAME | Same input and same marshal hash. |
| slice_1_10_2 | optional_slice_probe | DIFFERENT | SAME | Same optional support boundary or exception behavior. |
| slice_neg10_none_neg1 | optional_slice_probe | DIFFERENT | SAME | Same optional support boundary or exception behavior. |
| slice_none_none_none | optional_slice_probe | DIFFERENT | SAME | Same optional support boundary or exception behavior. |
| zero_width_joiner_sequence | unicode_string | SAME | SAME | Same input and same marshal hash. |

### member_b_all_windows_amd64_py3_10_results (Windows/AMD64, Python 3.10.11) vs member_b_all_windows_amd64_py3_13_results (Windows/AMD64, Python 3.13.13)

| Case | Category | Same marshal hash | Same exception | Interpretation |
| --- | --- | --- | --- | --- |
| ascii_plain | unicode_string | SAME | SAME | Same input and same marshal hash. |
| bytes_255_a | bytes_payload | SAME | SAME | Same input and same marshal hash. |
| bytes_256_a | bytes_payload | SAME | SAME | Same input and same marshal hash. |
| bytes_65535_a | bytes_payload | SAME | SAME | Same input and same marshal hash. |
| bytes_65536_a | bytes_payload | SAME | SAME | Same input and same marshal hash. |
| bytes_all_byte_values | bytes_payload | SAME | SAME | Same input and same marshal hash. |
| bytes_empty | bytes_payload | SAME | SAME | Same input and same marshal hash. |
| bytes_high_values_with_ascii | bytes_payload | SAME | SAME | Same input and same marshal hash. |
| bytes_single_nul | bytes_payload | SAME | SAME | Same input and same marshal hash. |
| chinese_text | unicode_string | SAME | SAME | Same input and same marshal hash. |
| complex_inf_neg_inf | float_complex | SAME | SAME | Same input and same marshal hash. |
| complex_nan_both | float_complex | SAME | SAME | Same input and same marshal hash. |
| complex_nan_imag | float_complex | SAME | SAME | Same input and same marshal hash. |
| complex_nan_real | float_complex | SAME | SAME | Same input and same marshal hash. |
| complex_payload_nan_imag | float_complex | SAME | SAME | Same input and same marshal hash. |
| complex_payload_nan_real | float_complex | SAME | SAME | Same input and same marshal hash. |
| complex_regular | float_complex | SAME | SAME | Same input and same marshal hash. |
| complex_zero_neg_zero | float_complex | SAME | SAME | Same input and same marshal hash. |
| composed_e_acute | unicode_string | DIFFERENT | SAME | Same input representation but Python major/minor differs; likely version-level marshal format difference. |
| constant_ellipsis | basic_scalar_constant | SAME | SAME | Same input and same marshal hash. |
| constant_false | basic_scalar_constant | SAME | SAME | Same input and same marshal hash. |
| constant_none | basic_scalar_constant | SAME | SAME | Same input and same marshal hash. |
| constant_true | basic_scalar_constant | SAME | SAME | Same input and same marshal hash. |
| crlf_string | unicode_string | SAME | SAME | Same input and same marshal hash. |
| decomposed_e_acute | unicode_string | SAME | SAME | Same input and same marshal hash. |
| emoji_text | unicode_string | SAME | SAME | Same input and same marshal hash. |
| float_huge_1e300 | float_complex | SAME | SAME | Same input and same marshal hash. |
| float_math_nan | float_complex | SAME | SAME | Same input and same marshal hash. |
| float_nan_constructor | float_complex | SAME | SAME | Same input and same marshal hash. |
| float_nan_payload_0x7ff0000000000001 | float_complex | SAME | SAME | Same input and same marshal hash. |
| float_nan_payload_0x7ff8000000000001 | float_complex | SAME | SAME | Same input and same marshal hash. |
| float_nan_payload_0x7ff8000000000002 | float_complex | SAME | SAME | Same input and same marshal hash. |
| float_neg_inf | float_complex | SAME | SAME | Same input and same marshal hash. |
| float_neg_one | float_complex | SAME | SAME | Same input and same marshal hash. |
| float_neg_zero | float_complex | SAME | SAME | Same input and same marshal hash. |
| float_pos_inf | float_complex | SAME | SAME | Same input and same marshal hash. |
| float_pos_one | float_complex | SAME | SAME | Same input and same marshal hash. |
| float_pos_zero | float_complex | SAME | SAME | Same input and same marshal hash. |
| float_tiny_1e_minus_300 | float_complex | SAME | SAME | Same input and same marshal hash. |
| lone_high_surrogate | unicode_string | SAME | SAME | Same input and same marshal hash. |
| non_bmp_character | unicode_string | SAME | SAME | Same input and same marshal hash. |
| nul_inside_string | unicode_string | SAME | SAME | Same input and same marshal hash. |
| recreated_complex_nan_both | float_complex | SAME | SAME | Same input and same marshal hash. |
| recreated_float_nan | float_complex | SAME | SAME | Same input and same marshal hash. |
| slice_1_10_2 | optional_slice_probe | DIFFERENT | SAME | Same optional support boundary or exception behavior. |
| slice_neg10_none_neg1 | optional_slice_probe | DIFFERENT | SAME | Same optional support boundary or exception behavior. |
| slice_none_none_none | optional_slice_probe | DIFFERENT | SAME | Same optional support boundary or exception behavior. |
| zero_width_joiner_sequence | unicode_string | SAME | SAME | Same input and same marshal hash. |

### member_b_all_windows_amd64_py3_10_results (Windows/AMD64, Python 3.10.11) vs member_b_all_windows_amd64_py3_9_results (Windows/AMD64, Python 3.9.13)

| Case | Category | Same marshal hash | Same exception | Interpretation |
| --- | --- | --- | --- | --- |
| ascii_plain | unicode_string | SAME | SAME | Same input and same marshal hash. |
| bytes_255_a | bytes_payload | SAME | SAME | Same input and same marshal hash. |
| bytes_256_a | bytes_payload | SAME | SAME | Same input and same marshal hash. |
| bytes_65535_a | bytes_payload | SAME | SAME | Same input and same marshal hash. |
| bytes_65536_a | bytes_payload | SAME | SAME | Same input and same marshal hash. |
| bytes_all_byte_values | bytes_payload | SAME | SAME | Same input and same marshal hash. |
| bytes_empty | bytes_payload | SAME | SAME | Same input and same marshal hash. |
| bytes_high_values_with_ascii | bytes_payload | SAME | SAME | Same input and same marshal hash. |
| bytes_single_nul | bytes_payload | SAME | SAME | Same input and same marshal hash. |
| chinese_text | unicode_string | SAME | SAME | Same input and same marshal hash. |
| complex_inf_neg_inf | float_complex | SAME | SAME | Same input and same marshal hash. |
| complex_nan_both | float_complex | SAME | SAME | Same input and same marshal hash. |
| complex_nan_imag | float_complex | SAME | SAME | Same input and same marshal hash. |
| complex_nan_real | float_complex | SAME | SAME | Same input and same marshal hash. |
| complex_payload_nan_imag | float_complex | SAME | SAME | Same input and same marshal hash. |
| complex_payload_nan_real | float_complex | SAME | SAME | Same input and same marshal hash. |
| complex_regular | float_complex | SAME | SAME | Same input and same marshal hash. |
| complex_zero_neg_zero | float_complex | SAME | SAME | Same input and same marshal hash. |
| composed_e_acute | unicode_string | SAME | SAME | Same input and same marshal hash. |
| constant_ellipsis | basic_scalar_constant | SAME | SAME | Same input and same marshal hash. |
| constant_false | basic_scalar_constant | SAME | SAME | Same input and same marshal hash. |
| constant_none | basic_scalar_constant | SAME | SAME | Same input and same marshal hash. |
| constant_true | basic_scalar_constant | SAME | SAME | Same input and same marshal hash. |
| crlf_string | unicode_string | SAME | SAME | Same input and same marshal hash. |
| decomposed_e_acute | unicode_string | SAME | SAME | Same input and same marshal hash. |
| emoji_text | unicode_string | SAME | SAME | Same input and same marshal hash. |
| float_huge_1e300 | float_complex | SAME | SAME | Same input and same marshal hash. |
| float_math_nan | float_complex | SAME | SAME | Same input and same marshal hash. |
| float_nan_constructor | float_complex | SAME | SAME | Same input and same marshal hash. |
| float_nan_payload_0x7ff0000000000001 | float_complex | SAME | SAME | Same input and same marshal hash. |
| float_nan_payload_0x7ff8000000000001 | float_complex | SAME | SAME | Same input and same marshal hash. |
| float_nan_payload_0x7ff8000000000002 | float_complex | SAME | SAME | Same input and same marshal hash. |
| float_neg_inf | float_complex | SAME | SAME | Same input and same marshal hash. |
| float_neg_one | float_complex | SAME | SAME | Same input and same marshal hash. |
| float_neg_zero | float_complex | SAME | SAME | Same input and same marshal hash. |
| float_pos_inf | float_complex | SAME | SAME | Same input and same marshal hash. |
| float_pos_one | float_complex | SAME | SAME | Same input and same marshal hash. |
| float_pos_zero | float_complex | SAME | SAME | Same input and same marshal hash. |
| float_tiny_1e_minus_300 | float_complex | SAME | SAME | Same input and same marshal hash. |
| lone_high_surrogate | unicode_string | SAME | SAME | Same input and same marshal hash. |
| non_bmp_character | unicode_string | SAME | SAME | Same input and same marshal hash. |
| nul_inside_string | unicode_string | SAME | SAME | Same input and same marshal hash. |
| recreated_complex_nan_both | float_complex | SAME | SAME | Same input and same marshal hash. |
| recreated_float_nan | float_complex | SAME | SAME | Same input and same marshal hash. |
| slice_1_10_2 | optional_slice_probe | DIFFERENT | SAME | Same optional support boundary or exception behavior. |
| slice_neg10_none_neg1 | optional_slice_probe | DIFFERENT | SAME | Same optional support boundary or exception behavior. |
| slice_none_none_none | optional_slice_probe | DIFFERENT | SAME | Same optional support boundary or exception behavior. |
| zero_width_joiner_sequence | unicode_string | SAME | SAME | Same input and same marshal hash. |

### member_b_all_windows_amd64_py3_11_results (Windows/AMD64, Python 3.11.9) vs member_b_all_windows_amd64_py3_12_results (Windows/AMD64, Python 3.12.10)

| Case | Category | Same marshal hash | Same exception | Interpretation |
| --- | --- | --- | --- | --- |
| ascii_plain | unicode_string | SAME | SAME | Same input and same marshal hash. |
| bytes_255_a | bytes_payload | SAME | SAME | Same input and same marshal hash. |
| bytes_256_a | bytes_payload | SAME | SAME | Same input and same marshal hash. |
| bytes_65535_a | bytes_payload | SAME | SAME | Same input and same marshal hash. |
| bytes_65536_a | bytes_payload | SAME | SAME | Same input and same marshal hash. |
| bytes_all_byte_values | bytes_payload | SAME | SAME | Same input and same marshal hash. |
| bytes_empty | bytes_payload | SAME | SAME | Same input and same marshal hash. |
| bytes_high_values_with_ascii | bytes_payload | SAME | SAME | Same input and same marshal hash. |
| bytes_single_nul | bytes_payload | SAME | SAME | Same input and same marshal hash. |
| chinese_text | unicode_string | SAME | SAME | Same input and same marshal hash. |
| complex_inf_neg_inf | float_complex | SAME | SAME | Same input and same marshal hash. |
| complex_nan_both | float_complex | SAME | SAME | Same input and same marshal hash. |
| complex_nan_imag | float_complex | SAME | SAME | Same input and same marshal hash. |
| complex_nan_real | float_complex | SAME | SAME | Same input and same marshal hash. |
| complex_payload_nan_imag | float_complex | SAME | SAME | Same input and same marshal hash. |
| complex_payload_nan_real | float_complex | SAME | SAME | Same input and same marshal hash. |
| complex_regular | float_complex | SAME | SAME | Same input and same marshal hash. |
| complex_zero_neg_zero | float_complex | SAME | SAME | Same input and same marshal hash. |
| composed_e_acute | unicode_string | DIFFERENT | SAME | Same input representation but Python major/minor differs; likely version-level marshal format difference. |
| constant_ellipsis | basic_scalar_constant | SAME | SAME | Same input and same marshal hash. |
| constant_false | basic_scalar_constant | SAME | SAME | Same input and same marshal hash. |
| constant_none | basic_scalar_constant | SAME | SAME | Same input and same marshal hash. |
| constant_true | basic_scalar_constant | SAME | SAME | Same input and same marshal hash. |
| crlf_string | unicode_string | SAME | SAME | Same input and same marshal hash. |
| decomposed_e_acute | unicode_string | SAME | SAME | Same input and same marshal hash. |
| emoji_text | unicode_string | SAME | SAME | Same input and same marshal hash. |
| float_huge_1e300 | float_complex | SAME | SAME | Same input and same marshal hash. |
| float_math_nan | float_complex | SAME | SAME | Same input and same marshal hash. |
| float_nan_constructor | float_complex | SAME | SAME | Same input and same marshal hash. |
| float_nan_payload_0x7ff0000000000001 | float_complex | SAME | SAME | Same input and same marshal hash. |
| float_nan_payload_0x7ff8000000000001 | float_complex | SAME | SAME | Same input and same marshal hash. |
| float_nan_payload_0x7ff8000000000002 | float_complex | SAME | SAME | Same input and same marshal hash. |
| float_neg_inf | float_complex | SAME | SAME | Same input and same marshal hash. |
| float_neg_one | float_complex | SAME | SAME | Same input and same marshal hash. |
| float_neg_zero | float_complex | SAME | SAME | Same input and same marshal hash. |
| float_pos_inf | float_complex | SAME | SAME | Same input and same marshal hash. |
| float_pos_one | float_complex | SAME | SAME | Same input and same marshal hash. |
| float_pos_zero | float_complex | SAME | SAME | Same input and same marshal hash. |
| float_tiny_1e_minus_300 | float_complex | SAME | SAME | Same input and same marshal hash. |
| lone_high_surrogate | unicode_string | SAME | SAME | Same input and same marshal hash. |
| non_bmp_character | unicode_string | SAME | SAME | Same input and same marshal hash. |
| nul_inside_string | unicode_string | SAME | SAME | Same input and same marshal hash. |
| recreated_complex_nan_both | float_complex | SAME | SAME | Same input and same marshal hash. |
| recreated_float_nan | float_complex | SAME | SAME | Same input and same marshal hash. |
| slice_1_10_2 | optional_slice_probe | DIFFERENT | SAME | Same optional support boundary or exception behavior. |
| slice_neg10_none_neg1 | optional_slice_probe | DIFFERENT | SAME | Same optional support boundary or exception behavior. |
| slice_none_none_none | optional_slice_probe | DIFFERENT | SAME | Same optional support boundary or exception behavior. |
| zero_width_joiner_sequence | unicode_string | SAME | SAME | Same input and same marshal hash. |

### member_b_all_windows_amd64_py3_11_results (Windows/AMD64, Python 3.11.9) vs member_b_all_windows_amd64_py3_13_results (Windows/AMD64, Python 3.13.13)

| Case | Category | Same marshal hash | Same exception | Interpretation |
| --- | --- | --- | --- | --- |
| ascii_plain | unicode_string | SAME | SAME | Same input and same marshal hash. |
| bytes_255_a | bytes_payload | SAME | SAME | Same input and same marshal hash. |
| bytes_256_a | bytes_payload | SAME | SAME | Same input and same marshal hash. |
| bytes_65535_a | bytes_payload | SAME | SAME | Same input and same marshal hash. |
| bytes_65536_a | bytes_payload | SAME | SAME | Same input and same marshal hash. |
| bytes_all_byte_values | bytes_payload | SAME | SAME | Same input and same marshal hash. |
| bytes_empty | bytes_payload | SAME | SAME | Same input and same marshal hash. |
| bytes_high_values_with_ascii | bytes_payload | SAME | SAME | Same input and same marshal hash. |
| bytes_single_nul | bytes_payload | SAME | SAME | Same input and same marshal hash. |
| chinese_text | unicode_string | SAME | SAME | Same input and same marshal hash. |
| complex_inf_neg_inf | float_complex | SAME | SAME | Same input and same marshal hash. |
| complex_nan_both | float_complex | SAME | SAME | Same input and same marshal hash. |
| complex_nan_imag | float_complex | SAME | SAME | Same input and same marshal hash. |
| complex_nan_real | float_complex | SAME | SAME | Same input and same marshal hash. |
| complex_payload_nan_imag | float_complex | SAME | SAME | Same input and same marshal hash. |
| complex_payload_nan_real | float_complex | SAME | SAME | Same input and same marshal hash. |
| complex_regular | float_complex | SAME | SAME | Same input and same marshal hash. |
| complex_zero_neg_zero | float_complex | SAME | SAME | Same input and same marshal hash. |
| composed_e_acute | unicode_string | DIFFERENT | SAME | Same input representation but Python major/minor differs; likely version-level marshal format difference. |
| constant_ellipsis | basic_scalar_constant | SAME | SAME | Same input and same marshal hash. |
| constant_false | basic_scalar_constant | SAME | SAME | Same input and same marshal hash. |
| constant_none | basic_scalar_constant | SAME | SAME | Same input and same marshal hash. |
| constant_true | basic_scalar_constant | SAME | SAME | Same input and same marshal hash. |
| crlf_string | unicode_string | SAME | SAME | Same input and same marshal hash. |
| decomposed_e_acute | unicode_string | SAME | SAME | Same input and same marshal hash. |
| emoji_text | unicode_string | SAME | SAME | Same input and same marshal hash. |
| float_huge_1e300 | float_complex | SAME | SAME | Same input and same marshal hash. |
| float_math_nan | float_complex | SAME | SAME | Same input and same marshal hash. |
| float_nan_constructor | float_complex | SAME | SAME | Same input and same marshal hash. |
| float_nan_payload_0x7ff0000000000001 | float_complex | SAME | SAME | Same input and same marshal hash. |
| float_nan_payload_0x7ff8000000000001 | float_complex | SAME | SAME | Same input and same marshal hash. |
| float_nan_payload_0x7ff8000000000002 | float_complex | SAME | SAME | Same input and same marshal hash. |
| float_neg_inf | float_complex | SAME | SAME | Same input and same marshal hash. |
| float_neg_one | float_complex | SAME | SAME | Same input and same marshal hash. |
| float_neg_zero | float_complex | SAME | SAME | Same input and same marshal hash. |
| float_pos_inf | float_complex | SAME | SAME | Same input and same marshal hash. |
| float_pos_one | float_complex | SAME | SAME | Same input and same marshal hash. |
| float_pos_zero | float_complex | SAME | SAME | Same input and same marshal hash. |
| float_tiny_1e_minus_300 | float_complex | SAME | SAME | Same input and same marshal hash. |
| lone_high_surrogate | unicode_string | SAME | SAME | Same input and same marshal hash. |
| non_bmp_character | unicode_string | SAME | SAME | Same input and same marshal hash. |
| nul_inside_string | unicode_string | SAME | SAME | Same input and same marshal hash. |
| recreated_complex_nan_both | float_complex | SAME | SAME | Same input and same marshal hash. |
| recreated_float_nan | float_complex | SAME | SAME | Same input and same marshal hash. |
| slice_1_10_2 | optional_slice_probe | DIFFERENT | SAME | Same optional support boundary or exception behavior. |
| slice_neg10_none_neg1 | optional_slice_probe | DIFFERENT | SAME | Same optional support boundary or exception behavior. |
| slice_none_none_none | optional_slice_probe | DIFFERENT | SAME | Same optional support boundary or exception behavior. |
| zero_width_joiner_sequence | unicode_string | SAME | SAME | Same input and same marshal hash. |

### member_b_all_windows_amd64_py3_11_results (Windows/AMD64, Python 3.11.9) vs member_b_all_windows_amd64_py3_9_results (Windows/AMD64, Python 3.9.13)

| Case | Category | Same marshal hash | Same exception | Interpretation |
| --- | --- | --- | --- | --- |
| ascii_plain | unicode_string | SAME | SAME | Same input and same marshal hash. |
| bytes_255_a | bytes_payload | SAME | SAME | Same input and same marshal hash. |
| bytes_256_a | bytes_payload | SAME | SAME | Same input and same marshal hash. |
| bytes_65535_a | bytes_payload | SAME | SAME | Same input and same marshal hash. |
| bytes_65536_a | bytes_payload | SAME | SAME | Same input and same marshal hash. |
| bytes_all_byte_values | bytes_payload | SAME | SAME | Same input and same marshal hash. |
| bytes_empty | bytes_payload | SAME | SAME | Same input and same marshal hash. |
| bytes_high_values_with_ascii | bytes_payload | SAME | SAME | Same input and same marshal hash. |
| bytes_single_nul | bytes_payload | SAME | SAME | Same input and same marshal hash. |
| chinese_text | unicode_string | SAME | SAME | Same input and same marshal hash. |
| complex_inf_neg_inf | float_complex | SAME | SAME | Same input and same marshal hash. |
| complex_nan_both | float_complex | SAME | SAME | Same input and same marshal hash. |
| complex_nan_imag | float_complex | SAME | SAME | Same input and same marshal hash. |
| complex_nan_real | float_complex | SAME | SAME | Same input and same marshal hash. |
| complex_payload_nan_imag | float_complex | SAME | SAME | Same input and same marshal hash. |
| complex_payload_nan_real | float_complex | SAME | SAME | Same input and same marshal hash. |
| complex_regular | float_complex | SAME | SAME | Same input and same marshal hash. |
| complex_zero_neg_zero | float_complex | SAME | SAME | Same input and same marshal hash. |
| composed_e_acute | unicode_string | SAME | SAME | Same input and same marshal hash. |
| constant_ellipsis | basic_scalar_constant | SAME | SAME | Same input and same marshal hash. |
| constant_false | basic_scalar_constant | SAME | SAME | Same input and same marshal hash. |
| constant_none | basic_scalar_constant | SAME | SAME | Same input and same marshal hash. |
| constant_true | basic_scalar_constant | SAME | SAME | Same input and same marshal hash. |
| crlf_string | unicode_string | SAME | SAME | Same input and same marshal hash. |
| decomposed_e_acute | unicode_string | SAME | SAME | Same input and same marshal hash. |
| emoji_text | unicode_string | SAME | SAME | Same input and same marshal hash. |
| float_huge_1e300 | float_complex | SAME | SAME | Same input and same marshal hash. |
| float_math_nan | float_complex | SAME | SAME | Same input and same marshal hash. |
| float_nan_constructor | float_complex | SAME | SAME | Same input and same marshal hash. |
| float_nan_payload_0x7ff0000000000001 | float_complex | SAME | SAME | Same input and same marshal hash. |
| float_nan_payload_0x7ff8000000000001 | float_complex | SAME | SAME | Same input and same marshal hash. |
| float_nan_payload_0x7ff8000000000002 | float_complex | SAME | SAME | Same input and same marshal hash. |
| float_neg_inf | float_complex | SAME | SAME | Same input and same marshal hash. |
| float_neg_one | float_complex | SAME | SAME | Same input and same marshal hash. |
| float_neg_zero | float_complex | SAME | SAME | Same input and same marshal hash. |
| float_pos_inf | float_complex | SAME | SAME | Same input and same marshal hash. |
| float_pos_one | float_complex | SAME | SAME | Same input and same marshal hash. |
| float_pos_zero | float_complex | SAME | SAME | Same input and same marshal hash. |
| float_tiny_1e_minus_300 | float_complex | SAME | SAME | Same input and same marshal hash. |
| lone_high_surrogate | unicode_string | SAME | SAME | Same input and same marshal hash. |
| non_bmp_character | unicode_string | SAME | SAME | Same input and same marshal hash. |
| nul_inside_string | unicode_string | SAME | SAME | Same input and same marshal hash. |
| recreated_complex_nan_both | float_complex | SAME | SAME | Same input and same marshal hash. |
| recreated_float_nan | float_complex | SAME | SAME | Same input and same marshal hash. |
| slice_1_10_2 | optional_slice_probe | DIFFERENT | SAME | Same optional support boundary or exception behavior. |
| slice_neg10_none_neg1 | optional_slice_probe | DIFFERENT | SAME | Same optional support boundary or exception behavior. |
| slice_none_none_none | optional_slice_probe | DIFFERENT | SAME | Same optional support boundary or exception behavior. |
| zero_width_joiner_sequence | unicode_string | SAME | SAME | Same input and same marshal hash. |

### member_b_all_windows_amd64_py3_12_results (Windows/AMD64, Python 3.12.10) vs member_b_all_windows_amd64_py3_13_results (Windows/AMD64, Python 3.13.13)

| Case | Category | Same marshal hash | Same exception | Interpretation |
| --- | --- | --- | --- | --- |
| ascii_plain | unicode_string | SAME | SAME | Same input and same marshal hash. |
| bytes_255_a | bytes_payload | SAME | SAME | Same input and same marshal hash. |
| bytes_256_a | bytes_payload | SAME | SAME | Same input and same marshal hash. |
| bytes_65535_a | bytes_payload | SAME | SAME | Same input and same marshal hash. |
| bytes_65536_a | bytes_payload | SAME | SAME | Same input and same marshal hash. |
| bytes_all_byte_values | bytes_payload | SAME | SAME | Same input and same marshal hash. |
| bytes_empty | bytes_payload | SAME | SAME | Same input and same marshal hash. |
| bytes_high_values_with_ascii | bytes_payload | SAME | SAME | Same input and same marshal hash. |
| bytes_single_nul | bytes_payload | SAME | SAME | Same input and same marshal hash. |
| chinese_text | unicode_string | SAME | SAME | Same input and same marshal hash. |
| complex_inf_neg_inf | float_complex | SAME | SAME | Same input and same marshal hash. |
| complex_nan_both | float_complex | SAME | SAME | Same input and same marshal hash. |
| complex_nan_imag | float_complex | SAME | SAME | Same input and same marshal hash. |
| complex_nan_real | float_complex | SAME | SAME | Same input and same marshal hash. |
| complex_payload_nan_imag | float_complex | SAME | SAME | Same input and same marshal hash. |
| complex_payload_nan_real | float_complex | SAME | SAME | Same input and same marshal hash. |
| complex_regular | float_complex | SAME | SAME | Same input and same marshal hash. |
| complex_zero_neg_zero | float_complex | SAME | SAME | Same input and same marshal hash. |
| composed_e_acute | unicode_string | SAME | SAME | Same input and same marshal hash. |
| constant_ellipsis | basic_scalar_constant | SAME | SAME | Same input and same marshal hash. |
| constant_false | basic_scalar_constant | SAME | SAME | Same input and same marshal hash. |
| constant_none | basic_scalar_constant | SAME | SAME | Same input and same marshal hash. |
| constant_true | basic_scalar_constant | SAME | SAME | Same input and same marshal hash. |
| crlf_string | unicode_string | SAME | SAME | Same input and same marshal hash. |
| decomposed_e_acute | unicode_string | SAME | SAME | Same input and same marshal hash. |
| emoji_text | unicode_string | SAME | SAME | Same input and same marshal hash. |
| float_huge_1e300 | float_complex | SAME | SAME | Same input and same marshal hash. |
| float_math_nan | float_complex | SAME | SAME | Same input and same marshal hash. |
| float_nan_constructor | float_complex | SAME | SAME | Same input and same marshal hash. |
| float_nan_payload_0x7ff0000000000001 | float_complex | SAME | SAME | Same input and same marshal hash. |
| float_nan_payload_0x7ff8000000000001 | float_complex | SAME | SAME | Same input and same marshal hash. |
| float_nan_payload_0x7ff8000000000002 | float_complex | SAME | SAME | Same input and same marshal hash. |
| float_neg_inf | float_complex | SAME | SAME | Same input and same marshal hash. |
| float_neg_one | float_complex | SAME | SAME | Same input and same marshal hash. |
| float_neg_zero | float_complex | SAME | SAME | Same input and same marshal hash. |
| float_pos_inf | float_complex | SAME | SAME | Same input and same marshal hash. |
| float_pos_one | float_complex | SAME | SAME | Same input and same marshal hash. |
| float_pos_zero | float_complex | SAME | SAME | Same input and same marshal hash. |
| float_tiny_1e_minus_300 | float_complex | SAME | SAME | Same input and same marshal hash. |
| lone_high_surrogate | unicode_string | SAME | SAME | Same input and same marshal hash. |
| non_bmp_character | unicode_string | SAME | SAME | Same input and same marshal hash. |
| nul_inside_string | unicode_string | SAME | SAME | Same input and same marshal hash. |
| recreated_complex_nan_both | float_complex | SAME | SAME | Same input and same marshal hash. |
| recreated_float_nan | float_complex | SAME | SAME | Same input and same marshal hash. |
| slice_1_10_2 | optional_slice_probe | DIFFERENT | SAME | Same optional support boundary or exception behavior. |
| slice_neg10_none_neg1 | optional_slice_probe | DIFFERENT | SAME | Same optional support boundary or exception behavior. |
| slice_none_none_none | optional_slice_probe | DIFFERENT | SAME | Same optional support boundary or exception behavior. |
| zero_width_joiner_sequence | unicode_string | SAME | SAME | Same input and same marshal hash. |

### member_b_all_windows_amd64_py3_12_results (Windows/AMD64, Python 3.12.10) vs member_b_all_windows_amd64_py3_9_results (Windows/AMD64, Python 3.9.13)

| Case | Category | Same marshal hash | Same exception | Interpretation |
| --- | --- | --- | --- | --- |
| ascii_plain | unicode_string | SAME | SAME | Same input and same marshal hash. |
| bytes_255_a | bytes_payload | SAME | SAME | Same input and same marshal hash. |
| bytes_256_a | bytes_payload | SAME | SAME | Same input and same marshal hash. |
| bytes_65535_a | bytes_payload | SAME | SAME | Same input and same marshal hash. |
| bytes_65536_a | bytes_payload | SAME | SAME | Same input and same marshal hash. |
| bytes_all_byte_values | bytes_payload | SAME | SAME | Same input and same marshal hash. |
| bytes_empty | bytes_payload | SAME | SAME | Same input and same marshal hash. |
| bytes_high_values_with_ascii | bytes_payload | SAME | SAME | Same input and same marshal hash. |
| bytes_single_nul | bytes_payload | SAME | SAME | Same input and same marshal hash. |
| chinese_text | unicode_string | SAME | SAME | Same input and same marshal hash. |
| complex_inf_neg_inf | float_complex | SAME | SAME | Same input and same marshal hash. |
| complex_nan_both | float_complex | SAME | SAME | Same input and same marshal hash. |
| complex_nan_imag | float_complex | SAME | SAME | Same input and same marshal hash. |
| complex_nan_real | float_complex | SAME | SAME | Same input and same marshal hash. |
| complex_payload_nan_imag | float_complex | SAME | SAME | Same input and same marshal hash. |
| complex_payload_nan_real | float_complex | SAME | SAME | Same input and same marshal hash. |
| complex_regular | float_complex | SAME | SAME | Same input and same marshal hash. |
| complex_zero_neg_zero | float_complex | SAME | SAME | Same input and same marshal hash. |
| composed_e_acute | unicode_string | DIFFERENT | SAME | Same input representation but Python major/minor differs; likely version-level marshal format difference. |
| constant_ellipsis | basic_scalar_constant | SAME | SAME | Same input and same marshal hash. |
| constant_false | basic_scalar_constant | SAME | SAME | Same input and same marshal hash. |
| constant_none | basic_scalar_constant | SAME | SAME | Same input and same marshal hash. |
| constant_true | basic_scalar_constant | SAME | SAME | Same input and same marshal hash. |
| crlf_string | unicode_string | SAME | SAME | Same input and same marshal hash. |
| decomposed_e_acute | unicode_string | SAME | SAME | Same input and same marshal hash. |
| emoji_text | unicode_string | SAME | SAME | Same input and same marshal hash. |
| float_huge_1e300 | float_complex | SAME | SAME | Same input and same marshal hash. |
| float_math_nan | float_complex | SAME | SAME | Same input and same marshal hash. |
| float_nan_constructor | float_complex | SAME | SAME | Same input and same marshal hash. |
| float_nan_payload_0x7ff0000000000001 | float_complex | SAME | SAME | Same input and same marshal hash. |
| float_nan_payload_0x7ff8000000000001 | float_complex | SAME | SAME | Same input and same marshal hash. |
| float_nan_payload_0x7ff8000000000002 | float_complex | SAME | SAME | Same input and same marshal hash. |
| float_neg_inf | float_complex | SAME | SAME | Same input and same marshal hash. |
| float_neg_one | float_complex | SAME | SAME | Same input and same marshal hash. |
| float_neg_zero | float_complex | SAME | SAME | Same input and same marshal hash. |
| float_pos_inf | float_complex | SAME | SAME | Same input and same marshal hash. |
| float_pos_one | float_complex | SAME | SAME | Same input and same marshal hash. |
| float_pos_zero | float_complex | SAME | SAME | Same input and same marshal hash. |
| float_tiny_1e_minus_300 | float_complex | SAME | SAME | Same input and same marshal hash. |
| lone_high_surrogate | unicode_string | SAME | SAME | Same input and same marshal hash. |
| non_bmp_character | unicode_string | SAME | SAME | Same input and same marshal hash. |
| nul_inside_string | unicode_string | SAME | SAME | Same input and same marshal hash. |
| recreated_complex_nan_both | float_complex | SAME | SAME | Same input and same marshal hash. |
| recreated_float_nan | float_complex | SAME | SAME | Same input and same marshal hash. |
| slice_1_10_2 | optional_slice_probe | DIFFERENT | SAME | Same optional support boundary or exception behavior. |
| slice_neg10_none_neg1 | optional_slice_probe | DIFFERENT | SAME | Same optional support boundary or exception behavior. |
| slice_none_none_none | optional_slice_probe | DIFFERENT | SAME | Same optional support boundary or exception behavior. |
| zero_width_joiner_sequence | unicode_string | SAME | SAME | Same input and same marshal hash. |

### member_b_all_windows_amd64_py3_13_results (Windows/AMD64, Python 3.13.13) vs member_b_all_windows_amd64_py3_9_results (Windows/AMD64, Python 3.9.13)

| Case | Category | Same marshal hash | Same exception | Interpretation |
| --- | --- | --- | --- | --- |
| ascii_plain | unicode_string | SAME | SAME | Same input and same marshal hash. |
| bytes_255_a | bytes_payload | SAME | SAME | Same input and same marshal hash. |
| bytes_256_a | bytes_payload | SAME | SAME | Same input and same marshal hash. |
| bytes_65535_a | bytes_payload | SAME | SAME | Same input and same marshal hash. |
| bytes_65536_a | bytes_payload | SAME | SAME | Same input and same marshal hash. |
| bytes_all_byte_values | bytes_payload | SAME | SAME | Same input and same marshal hash. |
| bytes_empty | bytes_payload | SAME | SAME | Same input and same marshal hash. |
| bytes_high_values_with_ascii | bytes_payload | SAME | SAME | Same input and same marshal hash. |
| bytes_single_nul | bytes_payload | SAME | SAME | Same input and same marshal hash. |
| chinese_text | unicode_string | SAME | SAME | Same input and same marshal hash. |
| complex_inf_neg_inf | float_complex | SAME | SAME | Same input and same marshal hash. |
| complex_nan_both | float_complex | SAME | SAME | Same input and same marshal hash. |
| complex_nan_imag | float_complex | SAME | SAME | Same input and same marshal hash. |
| complex_nan_real | float_complex | SAME | SAME | Same input and same marshal hash. |
| complex_payload_nan_imag | float_complex | SAME | SAME | Same input and same marshal hash. |
| complex_payload_nan_real | float_complex | SAME | SAME | Same input and same marshal hash. |
| complex_regular | float_complex | SAME | SAME | Same input and same marshal hash. |
| complex_zero_neg_zero | float_complex | SAME | SAME | Same input and same marshal hash. |
| composed_e_acute | unicode_string | DIFFERENT | SAME | Same input representation but Python major/minor differs; likely version-level marshal format difference. |
| constant_ellipsis | basic_scalar_constant | SAME | SAME | Same input and same marshal hash. |
| constant_false | basic_scalar_constant | SAME | SAME | Same input and same marshal hash. |
| constant_none | basic_scalar_constant | SAME | SAME | Same input and same marshal hash. |
| constant_true | basic_scalar_constant | SAME | SAME | Same input and same marshal hash. |
| crlf_string | unicode_string | SAME | SAME | Same input and same marshal hash. |
| decomposed_e_acute | unicode_string | SAME | SAME | Same input and same marshal hash. |
| emoji_text | unicode_string | SAME | SAME | Same input and same marshal hash. |
| float_huge_1e300 | float_complex | SAME | SAME | Same input and same marshal hash. |
| float_math_nan | float_complex | SAME | SAME | Same input and same marshal hash. |
| float_nan_constructor | float_complex | SAME | SAME | Same input and same marshal hash. |
| float_nan_payload_0x7ff0000000000001 | float_complex | SAME | SAME | Same input and same marshal hash. |
| float_nan_payload_0x7ff8000000000001 | float_complex | SAME | SAME | Same input and same marshal hash. |
| float_nan_payload_0x7ff8000000000002 | float_complex | SAME | SAME | Same input and same marshal hash. |
| float_neg_inf | float_complex | SAME | SAME | Same input and same marshal hash. |
| float_neg_one | float_complex | SAME | SAME | Same input and same marshal hash. |
| float_neg_zero | float_complex | SAME | SAME | Same input and same marshal hash. |
| float_pos_inf | float_complex | SAME | SAME | Same input and same marshal hash. |
| float_pos_one | float_complex | SAME | SAME | Same input and same marshal hash. |
| float_pos_zero | float_complex | SAME | SAME | Same input and same marshal hash. |
| float_tiny_1e_minus_300 | float_complex | SAME | SAME | Same input and same marshal hash. |
| lone_high_surrogate | unicode_string | SAME | SAME | Same input and same marshal hash. |
| non_bmp_character | unicode_string | SAME | SAME | Same input and same marshal hash. |
| nul_inside_string | unicode_string | SAME | SAME | Same input and same marshal hash. |
| recreated_complex_nan_both | float_complex | SAME | SAME | Same input and same marshal hash. |
| recreated_float_nan | float_complex | SAME | SAME | Same input and same marshal hash. |
| slice_1_10_2 | optional_slice_probe | DIFFERENT | SAME | Same optional support boundary or exception behavior. |
| slice_neg10_none_neg1 | optional_slice_probe | DIFFERENT | SAME | Same optional support boundary or exception behavior. |
| slice_none_none_none | optional_slice_probe | DIFFERENT | SAME | Same optional support boundary or exception behavior. |
| zero_width_joiner_sequence | unicode_string | SAME | SAME | Same input and same marshal hash. |

## Unicode 扩展观察

- `composed_e_acute` code points: `['U+00E9']`
- `decomposed_e_acute` code points: `['U+0065', 'U+0301']`
- 两者 marshal hash 是否相同：`False`
- 若 hash 不同，原因是底层 Unicode code points 不同，而不是 marshal 缺陷。

## slice 支持边界

slice case 是可选支持探测；如果当前 Python 报 `ValueError: unmarshallable object`，记录为版本支持边界，不作为失败。
