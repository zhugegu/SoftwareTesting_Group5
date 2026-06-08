# 成员 B 统一测试跨平台比较

## 环境列表

- `member_b_all_darwin_arm64_py3_9_results.json`: macOS-26.5-arm64-arm-64bit; implementation=CPython; marshal_version=4

## 单平台同进程稳定性

| Platform | Case count | Stable supported | Unstable supported | Exception/support boundary |
| --- | ---: | ---: | ---: | ---: |
| member_b_all_darwin_arm64_py3_9_results (Darwin/arm64, Python 3.9.6) | 48 | 45 | 0 | 3 |

## 跨平台比较

Cross-platform comparison skipped: fewer than two unified platform results were found.

## Unicode 扩展观察

- `composed_e_acute` code points: `['U+00E9']`
- `decomposed_e_acute` code points: `['U+0065', 'U+0301']`
- 两者 marshal hash 是否相同：`False`
- 若 hash 不同，原因是底层 Unicode code points 不同，而不是 marshal 缺陷。

## slice 支持边界

slice case 是可选支持探测；如果当前 Python 报 `ValueError: unmarshallable object`，记录为版本支持边界，不作为失败。
