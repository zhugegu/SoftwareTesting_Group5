# 成员 B：浮点数与复数 marshal 深层精度测试摘要

## 测试环境

- platform.platform(): `Windows-2025Server-10.0.26100-SP0`
- platform.system(): `Windows`
- platform.machine(): `AMD64`
- platform.python_implementation(): `CPython`
- sys.version: `3.13.13 (tags/v3.13.13:01104ce, Apr  7 2026, 19:25:48) [MSC v.1944 64 bit (AMD64)]`
- marshal.version: `4`

## 总览

- 测试用例总数：48
- 同平台稳定 case 数量：45
- 同平台不稳定 case 数量：3

## 同平台不稳定 Case

- `slice_none_none_none`
- `slice_1_10_2`
- `slice_neg10_none_neg1`

## NaN 相关结果汇总

- `float_nan_constructor`：唯一哈希数量为 1，稳定性为 稳定。
- `float_math_nan`：唯一哈希数量为 1，稳定性为 稳定。
- `float_nan_payload_0x7ff8000000000001`：唯一哈希数量为 1，稳定性为 稳定。
- `float_nan_payload_0x7ff8000000000002`：唯一哈希数量为 1，稳定性为 稳定。
- `float_nan_payload_0x7ff0000000000001`：唯一哈希数量为 1，稳定性为 稳定。
- `complex_nan_real`：唯一哈希数量为 1，稳定性为 稳定。
- `complex_nan_imag`：唯一哈希数量为 1，稳定性为 稳定。
- `complex_nan_both`：唯一哈希数量为 1，稳定性为 稳定。
- `complex_payload_nan_real`：唯一哈希数量为 1，稳定性为 稳定。
- `complex_payload_nan_imag`：唯一哈希数量为 1，稳定性为 稳定。
- `recreated_float_nan`：唯一哈希数量为 1，稳定性为 稳定，唯一 bit pattern 数量为 1。
- `recreated_complex_nan_both`：唯一哈希数量为 1，稳定性为 稳定，唯一 bit pattern 数量为 1。

## 用例明细

| Case | Type | Same-process stable | Unique hash count | Note |
| --- | --- | --- | --- | --- |
| float_pos_zero | float | Yes | 1 | Ordinary float 0.0; bits=0x0000000000000000 |
| float_neg_zero | float | Yes | 1 | Ordinary float -0.0; bits=0x8000000000000000 |
| float_pos_one | float | Yes | 1 | Ordinary float 1.0; bits=0x3ff0000000000000 |
| float_neg_one | float | Yes | 1 | Ordinary float -1.0; bits=0xbff0000000000000 |
| float_tiny_1e_minus_300 | float | Yes | 1 | Ordinary tiny float; bits=0x01a56e1fc2f8f359 |
| float_huge_1e300 | float | Yes | 1 | Ordinary huge float; bits=0x7e37e43c8800759c |
| float_pos_inf | float | Yes | 1 | Positive infinity; bits=0x7ff0000000000000 |
| float_neg_inf | float | Yes | 1 | Negative infinity; bits=0xfff0000000000000 |
| float_nan_constructor | float | Yes | 1 | NaN from float('nan'); bits=0x7ff8000000000000 |
| float_math_nan | float | Yes | 1 | NaN from math.nan; bits=0x7ff8000000000000 |
| float_nan_payload_0x7ff8000000000001 | float | Yes | 1 | Quiet NaN payload 0x7ff8000000000001; bits=0x7ff8000000000001 |
| float_nan_payload_0x7ff8000000000002 | float | Yes | 1 | Quiet NaN payload 0x7ff8000000000002; bits=0x7ff8000000000002 |
| float_nan_payload_0x7ff0000000000001 | float | Yes | 1 | NaN payload 0x7ff0000000000001; bits=0x7ff0000000000001 |
| complex_regular | complex | Yes | 1 | Regular complex; real=0x3ff8000000000000, imag=0xc004000000000000 |
| complex_zero_neg_zero | complex | Yes | 1 | Complex signed zero; real=0x0000000000000000, imag=0x8000000000000000 |
| complex_inf_neg_inf | complex | Yes | 1 | Complex with infinities; real=0x7ff0000000000000, imag=0xfff0000000000000 |
| complex_nan_real | complex | Yes | 1 | Complex with NaN real part; real=0x7ff8000000000000, imag=0x3ff0000000000000 |
| complex_nan_imag | complex | Yes | 1 | Complex with NaN imaginary part; real=0x3ff0000000000000, imag=0x7ff8000000000000 |
| complex_nan_both | complex | Yes | 1 | Complex with NaN in both parts; real=0x7ff8000000000000, imag=0x7ff8000000000000 |
| complex_payload_nan_real | complex | Yes | 1 | Complex with payload NaN real part; real=0x7ff8000000000001, imag=0x3ff0000000000000 |
| complex_payload_nan_imag | complex | Yes | 1 | Complex with payload NaN imaginary part; real=0x3ff0000000000000, imag=0x7ff8000000000001 |
| recreated_float_nan | float | Yes | 1 | Each iteration creates a new float('nan'); unique bit patterns=1 |
| recreated_complex_nan_both | complex | Yes | 1 | Each iteration creates complex(float('nan'), float('nan')); unique bit patterns=1 |
| ascii_plain | str | Yes | 1 | Plain ASCII baseline string. |
| chinese_text | str | Yes | 1 | Chinese BMP characters. |
| emoji_text | str | Yes | 1 | String containing an emoji. |
| nul_inside_string | str | Yes | 1 | String with embedded NUL. |
| crlf_string | str | Yes | 1 | String containing CRLF. |
| non_bmp_character | str | Yes | 1 | Single non-BMP character. |
| composed_e_acute | str | Yes | 1 | Precomposed Latin small e with acute. |
| decomposed_e_acute | str | Yes | 1 | Latin e plus combining acute mark. |
| lone_high_surrogate | str | Yes | 1 | Lone high surrogate code point. |
| zero_width_joiner_sequence | str | Yes | 1 | Emoji sequence joined by U+200D zero width joiner. |
| bytes_empty | bytes | Yes | 1 | Empty bytes baseline. |
| bytes_single_nul | bytes | Yes | 1 | Single embedded NUL byte. |
| bytes_high_values_with_ascii | bytes | Yes | 1 | NUL, high byte values, and ASCII bytes. |
| bytes_all_byte_values | bytes | Yes | 1 | All byte values 0-255. |
| bytes_255_a | bytes | Yes | 1 | Length boundary just below 256. |
| bytes_256_a | bytes | Yes | 1 | Length boundary at 256. |
| bytes_65535_a | bytes | Yes | 1 | Length boundary just below 65536. |
| bytes_65536_a | bytes | Yes | 1 | Length boundary at 65536. |
| constant_none | NoneType | Yes | 1 | None singleton scalar constant. |
| constant_true | bool | Yes | 1 | True boolean scalar constant. |
| constant_false | bool | Yes | 1 | False boolean scalar constant. |
| constant_ellipsis | ellipsis | Yes | 1 | Ellipsis scalar constant. |
| slice_none_none_none | slice | No | 0 | Optional marshal support probe for empty slice. |
| slice_1_10_2 | slice | No | 0 | Optional marshal support probe for positive stepped slice. |
| slice_neg10_none_neg1 | slice | No | 0 | Optional marshal support probe for negative stepped slice. |

## 测试发现

本轮成员 B 测试在当前平台共执行 48 个 float/complex 相关 case，其中 45 个 case 在同一进程内重复 marshal 后保持 SHA-256 哈希一致。发现同平台不稳定 case：`slice_none_none_none`、`slice_1_10_2`、`slice_neg10_none_neg1`。这说明这些输入在当前环境下未满足 R1.1/R3.1 所要求的同环境确定性，需要进一步检查对象构造方式、NaN bit pattern 或解释器实现差异。
