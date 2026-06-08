# 成员 B：浮点数与复数 marshal 深层精度测试摘要

## 测试环境

- platform.platform(): `macOS-15.7.7-arm64-arm-64bit`
- platform.system(): `Darwin`
- platform.machine(): `arm64`
- platform.python_implementation(): `CPython`
- sys.version: `3.11.9 (v3.11.9:de54cf5be3, Apr  2 2024, 07:12:50) [Clang 13.0.0 (clang-1300.0.29.30)]`
- marshal.version: `4`

## 总览

- 测试用例总数：25
- 同平台稳定 case 数量：22
- 同平台不稳定 case 数量：3

## 同平台不稳定 Case

- `slice_none_none_none`
- `slice_1_10_2`
- `slice_neg10_none_neg1`

## NaN 相关结果汇总

未发现 NaN 相关 case。

## 用例明细

| Case | Type | Same-process stable | Unique hash count | Note |
| --- | --- | --- | --- | --- |
| ascii_plain | str | Yes | 1 |  |
| chinese_text | str | Yes | 1 |  |
| emoji_text | str | Yes | 1 |  |
| nul_inside_string | str | Yes | 1 |  |
| crlf_string | str | Yes | 1 |  |
| non_bmp_character | str | Yes | 1 |  |
| composed_e_acute | str | Yes | 1 |  |
| decomposed_e_acute | str | Yes | 1 |  |
| lone_high_surrogate | str | Yes | 1 |  |
| zero_width_joiner_sequence | str | Yes | 1 |  |
| bytes_empty | bytes | Yes | 1 |  |
| bytes_single_nul | bytes | Yes | 1 |  |
| bytes_high_values_with_ascii | bytes | Yes | 1 |  |
| bytes_all_byte_values | bytes | Yes | 1 |  |
| bytes_255_a | bytes | Yes | 1 |  |
| bytes_256_a | bytes | Yes | 1 |  |
| bytes_65535_a | bytes | Yes | 1 |  |
| bytes_65536_a | bytes | Yes | 1 |  |
| constant_none | NoneType | Yes | 1 |  |
| constant_true | bool | Yes | 1 |  |
| constant_false | bool | Yes | 1 |  |
| constant_ellipsis | ellipsis | Yes | 1 |  |
| slice_none_none_none | slice | No | 0 |  |
| slice_1_10_2 | slice | No | 0 |  |
| slice_neg10_none_neg1 | slice | No | 0 |  |

## 测试发现

本轮成员 B 测试在当前平台共执行 25 个 float/complex 相关 case，其中 22 个 case 在同一进程内重复 marshal 后保持 SHA-256 哈希一致。发现同平台不稳定 case：`slice_none_none_none`、`slice_1_10_2`、`slice_neg10_none_neg1`。这说明这些输入在当前环境下未满足 R1.1/R3.1 所要求的同环境确定性，需要进一步检查对象构造方式、NaN bit pattern 或解释器实现差异。
