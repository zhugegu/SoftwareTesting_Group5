# 成员 B：浮点数与复数 marshal 深层精度测试摘要

## 测试环境

- platform.platform(): `Windows-10-10.0.26100-SP0`
- platform.system(): `Windows`
- platform.machine(): `AMD64`
- platform.python_implementation(): `CPython`
- sys.version: `3.10.11 (tags/v3.10.11:7d4cc5a, Apr  5 2023, 00:38:17) [MSC v.1929 64 bit (AMD64)]`
- marshal.version: `4`

## 总览

- 测试用例总数：23
- 同平台稳定 case 数量：23
- 同平台不稳定 case 数量：0

## 同平台不稳定 Case

无。

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

## 测试发现

本轮成员 B 测试在当前平台共执行 23 个 float/complex 相关 case，所有 case 在同一进程内重复 marshal 后 SHA-256 哈希均保持一致。该结果支持 R1.1 和 R3.1 在当前环境下成立。对于不同 NaN payload，测试记录了各自的 bit pattern 和首次 marshal 字节流哈希，可用于后续结合其他系统结果验证 R3.2 中的跨平台或跨 payload 差异。
