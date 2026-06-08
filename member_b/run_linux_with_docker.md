# 成员 B：用 Docker 运行 Linux 版 marshal 测试

本文档说明如何在 macOS 上用 Docker 运行 Linux 容器中的 Python 3.12，
生成 Linux 平台的 `marshal` float/complex 测试结果，并与本机 macOS
结果做跨平台比较。

## 前置条件

1. 安装并启动 Docker Desktop for Mac。
2. 在项目根目录运行命令，也就是包含 `tests/member_b_float_complex/`
   的目录。
3. 当前目录会被挂载到容器的 `/workspace`，测试结果会直接写回本机
   `tests/member_b_float_complex/results/`。

## 一键运行脚本

推荐直接运行：

```bash
sh tests/member_b_float_complex/run_linux_docker_tests.sh
```

脚本会执行：

- `python:3.12-slim` 默认 Linux 平台测试
- `python:3.12-slim` 的 `linux/amd64` 平台测试
- 生成/重命名 Linux JSON 结果
- 重新运行 `compare_cross_platform.py`

生成的 Linux 结果文件名为：

- `tests/member_b_float_complex/results/linux_aarch64_py3_12_results.json`
- `tests/member_b_float_complex/results/linux_x86_64_py3_12_results.json`

## 手动运行：默认 Linux 平台

在 Apple Silicon Mac 上，Docker 默认通常会运行 `linux/arm64` 镜像；
在 Intel Mac 上，默认通常会运行 `linux/amd64` 镜像。

```bash
docker run --rm \
  -v "$PWD":/work \
  -w /work \
  python:3.12-slim \
  python tests/member_b_float_complex/test_marshal_float_complex.py
```

该命令会先按脚本内的新规则生成类似下面的文件：

- `linux_aarch64_py3_12_results.json`
- `linux_x86_64_py3_12_results.json`

## 手动运行：linux/arm64

```bash
docker run --rm \
  --platform linux/arm64 \
  -v "$PWD":/work \
  -w /work \
  python:3.12-slim \
  python tests/member_b_float_complex/test_marshal_float_complex.py
```

常见输出文件：

```text
tests/member_b_float_complex/results/linux_aarch64_py3_12_results.json
```

## 手动运行：linux/amd64

```bash
docker run --rm \
  --platform linux/amd64 \
  -v "$PWD":/work \
  -w /work \
  python:3.12-slim \
  python tests/member_b_float_complex/test_marshal_float_complex.py
```

常见输出文件：

```text
tests/member_b_float_complex/results/linux_x86_64_py3_12_results.json
```

## 如何生成 linux_results.json

如果报告或组内汇总要求使用统一文件名 `linux_results.json`，可以在完成
某一次 Linux 测试后复制或重命名：

```bash
cp tests/member_b_float_complex/results/linux_aarch64_py3_12_results.json \
  tests/member_b_float_complex/results/linux_results.json
```

或对 amd64 结果执行：

```bash
cp tests/member_b_float_complex/results/linux_x86_64_py3_12_results.json \
  tests/member_b_float_complex/results/linux_results.json
```

注意：为了跨平台比较更清楚，建议保留带架构和 Python 版本的原始结果文件。

## 生成 Markdown 摘要

`summarize_member_b_results.py` 会遍历 `results` 目录下所有
`*_results.json`，并为每个 JSON 生成一个摘要：

```bash
python3 tests/member_b_float_complex/summarize_member_b_results.py
```

输出示例：

```text
tests/member_b_float_complex/results/member_b_summary_linux_aarch64_py3_12_results.md
tests/member_b_float_complex/results/member_b_summary_linux_x86_64_py3_12_results.md
```

## 重新运行跨平台比较

当 `results` 目录中有两个或多个 `*_results.json` 后，运行：

```bash
python3 tests/member_b_float_complex/compare_cross_platform.py
```

输出文件：

```text
tests/member_b_float_complex/results/cross_platform_comparison.md
```

比较脚本会读取所有 `*_results.json`，按 case name 对齐，并对所有平台结果
两两比较。若同一 case 的 `first_hash` 不同，表格中会标记为 `DIFFERENT`。
