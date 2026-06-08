"""Generate a Markdown summary for member B marshal test results."""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any


BASE_DIR = Path(__file__).resolve().parent
RESULTS_DIR = BASE_DIR / "results"


def yes_no(value: bool) -> str:
    """Render a boolean in a compact report-friendly form."""
    return "Yes" if value else "No"


def markdown_escape(value: Any) -> str:
    """Escape Markdown table separators."""
    return str(value).replace("|", "\\|").replace("\n", " ")


def all_cases(data: dict[str, Any]) -> list[dict[str, Any]]:
    """Return fixed object cases and recreated NaN cases together."""
    return data.get("cases", []) + data.get("recreated_nan_cases", [])


def is_stable(case: dict[str, Any]) -> bool:
    """Read the stability flag used by either case family."""
    if "same_process_stable" in case:
        return bool(case["same_process_stable"])
    return bool(case.get("stable_when_recreated"))


def nan_related_cases(cases: list[dict[str, Any]]) -> list[dict[str, Any]]:
    """Filter cases whose names or notes are NaN-related."""
    return [
        case
        for case in cases
        if "nan" in case.get("case", "").lower()
        or "nan" in case.get("note", "").lower()
    ]


def case_note(case: dict[str, Any]) -> str:
    """Create a concise table note for a result case."""
    pieces = []
    if case.get("note"):
        pieces.append(case["note"])
    if "float_bit_pattern" in case:
        pieces.append(f"bits={case['float_bit_pattern']}")
    if "real_bit_pattern" in case and "imag_bit_pattern" in case:
        pieces.append(
            "real={real}, imag={imag}".format(
                real=case["real_bit_pattern"],
                imag=case["imag_bit_pattern"],
            )
        )
    if "unique_bit_pattern_count" in case:
        pieces.append(
            "unique bit patterns={count}".format(
                count=case["unique_bit_pattern_count"],
            )
        )
    return "; ".join(pieces)


def environment_section(environment: dict[str, Any]) -> list[str]:
    """Build the environment section."""
    return [
        "## 测试环境",
        "",
        f"- platform.platform(): `{environment.get('platform_platform')}`",
        f"- platform.system(): `{environment.get('platform_system')}`",
        f"- platform.machine(): `{environment.get('platform_machine')}`",
        "- platform.python_implementation(): "
        f"`{environment.get('python_implementation')}`",
        f"- sys.version: `{environment.get('sys_version')}`",
        f"- marshal.version: `{environment.get('marshal_version')}`",
        "",
    ]


def table_section(cases: list[dict[str, Any]]) -> list[str]:
    """Build the required full case table."""
    lines = [
        "## 用例明细",
        "",
        "| Case | Type | Same-process stable | Unique hash count | Note |",
        "| --- | --- | --- | --- | --- |",
    ]
    for case in cases:
        lines.append(
            "| {case} | {type_} | {stable} | {unique_hash_count} | {note} |".format(
                case=markdown_escape(case.get("case", "")),
                type_=markdown_escape(case.get("type", "")),
                stable=yes_no(is_stable(case)),
                unique_hash_count=case.get("unique_hash_count", ""),
                note=markdown_escape(case_note(case)),
            )
        )
    lines.append("")
    return lines


def nan_summary_section(cases: list[dict[str, Any]]) -> list[str]:
    """Build a focused NaN result summary."""
    nan_cases = nan_related_cases(cases)
    lines = ["## NaN 相关结果汇总", ""]
    if not nan_cases:
        lines.extend(["未发现 NaN 相关 case。", ""])
        return lines

    for case in nan_cases:
        bit_count = case.get("unique_bit_pattern_count")
        bit_text = ""
        if bit_count is not None:
            bit_text = f"，唯一 bit pattern 数量为 {bit_count}"
        template = (
            "- `{case}`：唯一哈希数量为 {hash_count}，"
            "稳定性为 {stable}{bits}。"
        )
        lines.append(
            template.format(
                case=case.get("case", ""),
                hash_count=case.get("unique_hash_count", ""),
                stable="稳定" if is_stable(case) else "不稳定",
                bits=bit_text,
            )
        )
    lines.append("")
    return lines


def findings_section(
    total: int,
    stable_count: int,
    unstable: list[dict[str, Any]],
) -> list[str]:
    """Build the Chinese findings paragraph for direct report reuse."""
    if unstable:
        unstable_names = "、".join(f"`{case['case']}`" for case in unstable)
        finding = (
            "本轮成员 B 测试在当前平台共执行 "
            f"{total} 个 float/complex 相关 case，其中 {stable_count} 个 case "
            "在同一进程内重复 marshal 后保持 SHA-256 哈希一致。"
            f"发现同平台不稳定 case：{unstable_names}。"
            "这说明这些输入在当前环境下未满足 R1.1/R3.1 "
            "所要求的同环境确定性，"
            "需要进一步检查对象构造方式、"
            "NaN bit pattern 或解释器实现差异。"
        )
    else:
        finding = (
            "本轮成员 B 测试在当前平台共执行 "
            f"{total} 个 float/complex 相关 case，所有 case 在同一进程内"
            "重复 marshal 后 SHA-256 哈希均保持一致。该结果支持 R1.1 "
            "和 R3.1 在当前环境下成立。对于不同 NaN payload，"
            "测试记录了各自的 bit pattern 和首次 marshal 字节流哈希，"
            "可用于"
            "后续结合其他系统结果验证 R3.2 中的跨平台或跨 payload "
            "差异。"
        )

    return [
        "## 测试发现",
        "",
        finding,
        "",
    ]


def summarize_result(result_path: Path) -> Path:
    """Read one JSON result and write its Markdown summary."""
    data = json.loads(result_path.read_text(encoding="utf-8"))
    cases = all_cases(data)
    unstable = [case for case in cases if not is_stable(case)]
    stable_count = len(cases) - len(unstable)
    environment = data.get("environment", {})

    lines = [
        "# 成员 B：浮点数与复数 marshal 深层精度测试摘要",
        "",
    ]
    lines.extend(environment_section(environment))
    lines.extend(
        [
            "## 总览",
            "",
            f"- 测试用例总数：{len(cases)}",
            f"- 同平台稳定 case 数量：{stable_count}",
            f"- 同平台不稳定 case 数量：{len(unstable)}",
            "",
        ]
    )
    if unstable:
        lines.extend(["## 同平台不稳定 Case", ""])
        lines.extend(f"- `{case['case']}`" for case in unstable)
        lines.append("")
    else:
        lines.extend(["## 同平台不稳定 Case", "", "无。", ""])

    lines.extend(nan_summary_section(cases))
    lines.extend(table_section(cases))
    lines.extend(findings_section(len(cases), stable_count, unstable))

    summary_path = RESULTS_DIR / f"member_b_summary_{result_path.stem}.md"
    summary_path.write_text("\n".join(lines), encoding="utf-8")
    return summary_path


def main() -> None:
    """Generate one Markdown summary for every result JSON."""
    result_paths = sorted(RESULTS_DIR.glob("*_results.json"))
    if not result_paths:
        raise FileNotFoundError(f"No result JSON files found in {RESULTS_DIR}")

    for result_path in result_paths:
        summary_path = summarize_result(result_path)
        print(f"Wrote summary Markdown: {summary_path}")


if __name__ == "__main__":
    main()
