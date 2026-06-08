# 成员 B：marshal 浮点数、复数与标量二进制边界稳定性测试报告

报告日期：2026-06-08
作者：成员 B

代码仓库：`https://github.com/zhugegu/SoftwareTesting_Group5.git`

---

## 摘要

本报告针对 Python 标准库 `marshal` 模块中成员 B 负责的“浮点数与复数深层精度测试”进行总结，核心目标是验证相同输入对象在重复 `marshal.dumps()` 后是否产生完全一致的字节流哈希，并观察浮点特殊值、复数特殊值和 NaN payload 在跨平台结果中的表现。

当前成员 B 原分工测试已经覆盖 `R1.1`、`R1.2`、`R3.1`、`R3.2`。最新 GitHub Actions 结果覆盖 Ubuntu、macOS、Windows 三个操作系统，以及 Python 3.9、3.10、3.11、3.12、3.13 五个版本，共 15 个运行环境。每个环境统一执行 48 个 case，其中 45 个支持 marshal 的 case 全部同进程稳定，0 个同进程不稳定；3 个 slice case 记录为版本支持边界，不作为缺陷。除此之外，我额外扩展了非容器、非代码对象的标量与二进制边界输入测试，包括 Unicode 字符串、bytes 边界、基础标量常量和 slice 支持探测。

结论：成员 B 的原分工任务可以判定为已完成；扩展测试增强了对 `marshal` 字节级稳定性的说明，但不与其他成员的整数、容器、递归异常和 code object 分工重复。

---

## 引言

`marshal` 是 Python 内部使用的序列化模块，常用于 `.pyc` 文件相关场景。本测试从“相同输入应产生相同字节流”这一稳定性要求出发，对成员 B 负责的浮点数和复数输入进行验证。由于浮点值存在 `NaN`、正负无穷、`-0.0`、不同 NaN payload 等特殊表示，本分工重点关注这些值在同进程重复 marshal 和跨操作系统比较中的表现。

在原分工之外，本报告还记录了一组扩展测试：非容器、非代码对象的标量与二进制边界输入。该扩展用于观察 Unicode 底层 code points、bytes 边界长度和基础常量在 marshal 输出中的字节级稳定性。

---

## 测试策略

### 2.1 使用的测试技术

| 测试技术 | 使用位置 | 说明 |
|---|---|---|
| 等价类划分 | 普通 float、普通 complex、基础标量常量 | 选取常规代表值验证 marshal 的基本确定性。 |
| 边界值测试 | `-0.0`、`inf`、`nan`、NaN payload、bytes 长度 255/256/65535/65536 | 覆盖最容易出现二进制表示差异的边界。 |
| 重复执行稳定性测试 | 所有 case | 每个输入重复 marshal 100 次，比较 SHA-256 哈希唯一数量。 |
| 跨平台比较 | macOS、Linux、Windows 结果 JSON | 按 case name 对齐比较 repr、type、异常行为和 marshal 哈希。 |
| 白盒导向的输入选择 | NaN payload bit pattern | 通过指定 IEEE-754 bit pattern 构造 NaN，观察底层位模式是否影响 marshal 字节流。 |

### 2.2 为什么不使用某些技术

- 变异测试：本任务重点是字节流确定性，变异体的正确性判定成本较高。
- 形式化验证：`marshal` 格式属于 Python 内部格式，不适合作为跨版本长期稳定协议做形式化证明。
- 大规模模糊测试：成员 B 的边界集中在 float/complex 精度语义，随机生成复杂结构容易与成员 C、D 的容器和递归分工重复。

---

## 测试环境

### 3.1 已有结果覆盖

| 系统 | 架构 | Python 版本 | 统一结果文件 | 结果概况 |
|---|---|---|---|---|
| macOS / Darwin | arm64 | 3.9.6 | `member_b_all_darwin_arm64_py3_9_results.json` | 48 case；45 稳定；0 不稳定；3 个 slice 支持边界 |
| macOS / Darwin | arm64 | 3.10.11 | `member_b_all_darwin_arm64_py3_10_results.json` | 48 case；45 稳定；0 不稳定；3 个 slice 支持边界 |
| macOS / Darwin | arm64 | 3.11.9 | `member_b_all_darwin_arm64_py3_11_results.json` | 48 case；45 稳定；0 不稳定；3 个 slice 支持边界 |
| macOS / Darwin | arm64 | 3.12.10 | `member_b_all_darwin_arm64_py3_12_results.json` | 48 case；45 稳定；0 不稳定；3 个 slice 支持边界 |
| macOS / Darwin | arm64 | 3.13.13 | `member_b_all_darwin_arm64_py3_13_results.json` | 48 case；45 稳定；0 不稳定；3 个 slice 支持边界 |
| Linux | x86_64 | 3.9.25 | `member_b_all_linux_x86_64_py3_9_results.json` | 48 case；45 稳定；0 不稳定；3 个 slice 支持边界 |
| Linux | x86_64 | 3.10.20 | `member_b_all_linux_x86_64_py3_10_results.json` | 48 case；45 稳定；0 不稳定；3 个 slice 支持边界 |
| Linux | x86_64 | 3.11.15 | `member_b_all_linux_x86_64_py3_11_results.json` | 48 case；45 稳定；0 不稳定；3 个 slice 支持边界 |
| Linux | x86_64 | 3.12.13 | `member_b_all_linux_x86_64_py3_12_results.json` | 48 case；45 稳定；0 不稳定；3 个 slice 支持边界 |
| Linux | x86_64 | 3.13.13 | `member_b_all_linux_x86_64_py3_13_results.json` | 48 case；45 稳定；0 不稳定；3 个 slice 支持边界 |
| Windows | AMD64 | 3.9.13 | `member_b_all_windows_amd64_py3_9_results.json` | 48 case；45 稳定；0 不稳定；3 个 slice 支持边界 |
| Windows | AMD64 | 3.10.11 | `member_b_all_windows_amd64_py3_10_results.json` | 48 case；45 稳定；0 不稳定；3 个 slice 支持边界 |
| Windows | AMD64 | 3.11.9 | `member_b_all_windows_amd64_py3_11_results.json` | 48 case；45 稳定；0 不稳定；3 个 slice 支持边界 |
| Windows | AMD64 | 3.12.10 | `member_b_all_windows_amd64_py3_12_results.json` | 48 case；45 稳定；0 不稳定；3 个 slice 支持边界 |
| Windows | AMD64 | 3.13.13 | `member_b_all_windows_amd64_py3_13_results.json` | 48 case；45 稳定；0 不稳定；3 个 slice 支持边界 |

### 3.2 GitHub Actions 多系统多版本计划

已新增 `.github/workflows/member-b-marshal-stability.yml`，用于在 GitHub Actions 中运行：

| 维度 | 覆盖 |
|---|---|
| 操作系统 | `ubuntu-latest`、`macos-latest`、`windows-latest` |
| Python 版本 | `3.9`、`3.10`、`3.11`、`3.12`、`3.13` |
| 运行内容 | 统一测试脚本、原 float/complex 脚本、扩展 scalar/binary 脚本 |
| 产物 | JSON 结果、跨平台 Markdown 比较报告、单平台摘要报告 |

该 workflow 已在分支 `member-b-marshal-tests` 上通过 push 触发并成功完成，运行链接为 `https://github.com/zhugegu/SoftwareTesting_Group5/actions/runs/27129174317`。本地 `member_b/results/` 已同步保存该次 GitHub Actions 生成的 JSON 与 Markdown artifacts。

---

## 正式测试内容

### 4.1 需求提炼

成员 B 对应参考分工中的以下需求：

| 主分类域 ID | 子需求 ID | 需求名称 | 成员 B 覆盖方式 | 完成状态 |
|---|---|---|---|---|
| R1：核心基准确定性 | R1.1 | 核心等价确定性 | 每个 case 在同一进程内重复 marshal 100 次并比较 SHA-256 | 已完成 |
| R1：核心基准确定性 | R1.2 | 跨操作系统一致性 | 汇总 macOS、Linux、Windows JSON，按 case 对齐比较 marshal hash | 已完成；已补充 GitHub Actions 继续验证 |
| R3：浮点与复数特殊值 | R3.1 | 浮点特殊值常规确定性 | 覆盖 `NaN`、`inf`、`-0.0` 以及复数中的特殊值 | 已完成 |
| R3：浮点与复数特殊值 | R3.2 | NaN 载荷跨平台变异性 | 通过指定 NaN bit pattern 生成不同 payload 并记录 hash/bit pattern | 已完成 |

### 4.2 原分工测试用例表

| 测试类别 | 代表 case | 需求 ID | 测试原则 | 当前结果 |
|---|---|---|---|---|
| 普通 float | `float_pos_zero`、`float_pos_one`、`float_tiny_1e_minus_300`、`float_huge_1e300` | R1.1 | 等价类、边界值 | 同进程稳定 |
| 符号零 | `float_neg_zero`、`complex_zero_neg_zero` | R1.1、R3.1 | 边界值 | 同进程稳定 |
| 无穷值 | `float_pos_inf`、`float_neg_inf`、`complex_inf_neg_inf` | R1.1、R3.1 | 边界值 | 同进程稳定 |
| NaN 构造值 | `float_nan_constructor`、`float_math_nan`、`recreated_float_nan` | R1.1、R3.1、R3.2 | 边界值、重复执行 | 同进程稳定 |
| NaN payload | `float_nan_payload_0x7ff8000000000001`、`float_nan_payload_0x7ff8000000000002`、`float_nan_payload_0x7ff0000000000001` | R3.2 | 白盒导向边界 | 同进程稳定，可跨平台比较 |
| 复数 NaN | `complex_nan_real`、`complex_nan_imag`、`complex_nan_both`、`complex_payload_nan_real`、`complex_payload_nan_imag` | R1.1、R3.1、R3.2 | 组合边界 | 同进程稳定 |

### 4.3 扩展测试用例表

扩展测试不属于成员 B 原始必做项，但仍围绕“非容器、非代码对象”的标量与二进制输入，不测试整数边界、集合/dict 顺序、递归/共享引用或 code object，因此不与其他成员重复。

| 扩展类别 | 代表 case | 测试目的 | 当前结果 |
|---|---|---|---|
| Unicode 字符串 | `ascii_plain`、`chinese_text`、`emoji_text`、`non_bmp_character`、`lone_high_surrogate` | 验证不同 Unicode 输入在 marshal 字节流上的稳定性 | 支持 case 同进程稳定 |
| Unicode 视觉相似边界 | `composed_e_acute`、`decomposed_e_acute` | 区分 human-perceived equality 与 byte-level equality | 两者 hash 不同，原因是 code points 不同 |
| bytes 边界 | `bytes_empty`、`bytes_single_nul`、`bytes_all_byte_values`、`bytes_255_a`、`bytes_256_a`、`bytes_65535_a`、`bytes_65536_a` | 验证 NUL、高字节值和长度边界不会破坏稳定性 | 支持 case 同进程稳定 |
| 基础常量 | `constant_none`、`constant_true`、`constant_false`、`constant_ellipsis` | 验证基础标量常量的稳定性 | 同进程稳定 |
| slice 支持探测 | `slice_none_none_none`、`slice_1_10_2`、`slice_neg10_none_neg1` | 观察当前 Python 是否支持 marshal slice | 当前记录 `ValueError: unmarshallable object`，作为版本支持边界 |

### 4.4 需求-用例可追溯性矩阵

| 用例组 | R1.1 | R1.2 | R3.1 | R3.2 | B 扩展 |
|---|---|---|---|---|---|
| 普通 float | X | X |  |  |  |
| `-0.0` / `inf` | X | X | X |  |  |
| NaN 构造值 | X | X | X | X |  |
| NaN payload | X | X | X | X |  |
| 复数特殊值 | X | X | X | X |  |
| Unicode 字符串 | X | X |  |  | X |
| bytes 边界 | X | X |  |  | X |
| 基础标量常量 | X | X |  |  | X |
| slice 支持探测 |  |  |  |  | X |

---

## 测试执行与结果

### 5.1 本地统一入口执行结果

本次统一入口 `member_b_marshal_tests.py` 已在 GitHub Actions 三系统五版本矩阵运行，输出文件保存在 `member_b/results/`。核心汇总文件包括：

- `member_b/results/member_b_all_cross_platform_comparison.md`
- `member_b/results/cross_platform_comparison.md`
- `member_b/results/scalar_binary_cross_platform_comparison.md`
- `member_b/results/member_b_all_*_results.json`

执行摘要：

| 指标 | 数值 |
|---|---:|
| 运行环境数 | 15 |
| 每个环境总 case 数 | 48 |
| 每个环境支持 marshal 且同进程稳定 case | 45 |
| 每个环境支持 marshal 但同进程不稳定 case | 0 |
| 每个环境异常/支持边界 case | 3 |
| repeat_count | 100 |

### 5.2 原 float/complex 跨平台结果

最新 `cross_platform_comparison.md` 显示：所有已比较的 float/complex marshal 哈希在测试平台之间一致。也就是说，在当前三系统五版本结果集合中，成员 B 原始分工未发现同进程不稳定；在相同 Python 版本或可比较场景下也未发现 float/complex 的异常跨平台差异。

### 5.3 扩展 scalar/binary 结果

扩展测试在 macOS 和 Linux 两个架构结果中均未发现同进程不稳定。Linux aarch64 与 Linux x86_64 的扩展结果完全一致。macOS Python 3.9 与 Linux Python 3.12 在 `composed_e_acute` 上存在 marshal hash 差异，但输入底层表示相同，且 Python major/minor 不同，因此当前报告将其解释为可能的 Python 版本级 marshal 格式差异，而不是操作系统或架构缺陷。

`composed_e_acute` 与 `decomposed_e_acute` 在每个平台内都产生不同 hash，这是预期现象：前者 code points 为 `['U+00E9']`，后者为 `['U+0065', 'U+0301']`。视觉相似不等于字节级相同，这不是 marshal 缺陷。

### 5.4 非预期行为列表

| 编号 | 现象 | 是否缺陷 | 解释 |
|---|---|---|---|
| 1 | 当前 Python 对 slice 执行 `marshal.dumps()` 报 `ValueError: unmarshallable object` | 否 | slice 是可选支持探测，记录为 Python 版本支持边界。 |
| 2 | `composed_e_acute` 与 `decomposed_e_acute` hash 不同 | 否 | 二者底层 Unicode code points 不同。 |
| 3 | 不同 Python 主次版本之间的 `composed_e_acute` hash 可能不同 | 暂不作为缺陷 | 输入底层 code points 相同，但 Python major/minor 不同；报告解释为版本级 marshal 格式差异，不归因于操作系统或架构缺陷。 |

---

## 测试套件完整性与局限性

### 6.1 完整性

- 原分工要求的 `R1.1`、`R1.2`、`R3.1`、`R3.2` 均已有测试用例覆盖。
- float/complex 用例覆盖普通值、极小值、极大值、正负无穷、正负零、NaN、不同 NaN payload、复数中特殊值组合。
- 每个 case 重复 marshal 100 次，并记录哈希列表、唯一哈希数量、首次 marshal 字节流、bit pattern 等可复核数据。
- 已有结果包含 macOS、Linux、Windows 三类系统；GitHub Actions workflow 已用同一测试入口在三系统和 Python 3.9-3.13 上统一执行通过。
- 扩展测试补充了 Unicode、bytes、基础常量和 slice 支持边界，有助于说明 `marshal` 对非容器、非代码对象标量输入的字节级稳定性。

### 6.2 局限性

- 本报告已经同步 GitHub Actions 三系统五版本 artifacts，但这些 artifacts 是一次运行结果，不代表穷尽所有硬件、编译选项和 Python 小版本。
- Windows、Linux、macOS 的 GitHub-hosted runner 环境由 GitHub 提供，不能覆盖所有真实用户机器配置。
- Python 官方不承诺 `marshal` 跨版本格式稳定，因此跨 Python major/minor 的 hash 差异不应直接判定为缺陷。
- 本分工刻意不测试整数边界、容器随机顺序、递归/共享引用和 code object，以避免与成员 A、C、D、E 重复。

---

## 结论

成员 B 的原始分工可以判定为已完成。测试用例已经覆盖 float/complex 深层精度场景，包含 NaN、Inf、`-0.0`、不同 NaN payload 和复数中特殊值组合；当前已有 macOS、Linux、Windows 结果显示，所有 float/complex case 在同进程内重复 marshal 均稳定，跨平台比较也未发现 marshal 哈希差异。这支持 `R1.1`、`R1.2`、`R3.1`、`R3.2` 在当前测试数据下成立。

扩展测试进一步说明：对于非容器、非代码对象的 Unicode、bytes 和基础标量常量，`marshal` 在当前平台同进程内也表现稳定。bytes 中的 embedded NUL、高字节值和长度边界不会破坏稳定性；视觉相似的 Unicode 字符串如果底层 code points 不同，marshal hash 不同是合理结果；slice 不支持 marshal 是版本支持边界，不作为错误。

后续如果还要继续增强，可以把 GitHub Actions 的 Markdown 汇总报告进一步自动提交回仓库，或增加 CPython 以外解释器的观察性测试。但对于当前成员 B 分工，已有测试范围和结果已经足够支撑完成结论。

---

## 参考文献

- Python 标准库 `marshal` 文档
- Python 源码 `Python/marshal.c`
- IEEE 754 浮点数标准

---

## 附录 A：测试代码与结果文件

### A.1 测试代码文件

- `member_b_marshal_tests.py`
- `compare_cross_platform.py`
- `compare_scalar_binary_extensions.py`
- `compare_member_b_all_results.py`
- `summarize_member_b_results.py`
- `run_linux_docker_tests.sh`
- `.github/workflows/member-b-marshal-stability.yml`

### A.2 关键结果文件

- `results/cross_platform_comparison.md`
- `results/scalar_binary_cross_platform_comparison.md`
- `results/member_b_all_cross_platform_comparison.md`
- `results/member_b_all_darwin_arm64_py3_9_results.json`
- `results/member_b_all_*_results.json`
