"""Compare unified member B marshal result JSON files."""

from __future__ import annotations

import json
from itertools import combinations
from pathlib import Path
from typing import Any


BASE_DIR = Path(__file__).resolve().parent
RESULTS_DIR = BASE_DIR / "results"
OUTPUT_PATH = RESULTS_DIR / "member_b_all_cross_platform_comparison.md"


def markdown_escape(value: Any) -> str:
    """Escape Markdown table separators."""
    return str(value).replace("|", "\\|").replace("\n", " ")


def load_results() -> list[dict[str, Any]]:
    """Load every unified member B result JSON."""
    results = []
    for path in sorted(RESULTS_DIR.glob("member_b_all_*_results.json")):
        data = json.loads(path.read_text(encoding="utf-8"))
        environment = data.get("environment", {})
        label = "{stem} ({system}/{machine}, Python {version})".format(
            stem=path.stem,
            system=environment.get("platform_system", "unknown"),
            machine=environment.get("platform_machine", "unknown"),
            version=environment.get("sys_version", "unknown").split()[0],
        )
        results.append(
            {
                "path": path,
                "data": data,
                "label": label,
                "cases": {case["case"]: case for case in data.get("cases", [])},
            }
        )
    return results


def platform_summary(result: dict[str, Any]) -> dict[str, int]:
    """Count supported stable, unstable, and support-boundary cases."""
    stable = 0
    unstable = 0
    exceptions = 0
    for case in result["cases"].values():
        if case.get("exception_type"):
            exceptions += 1
        elif case.get("same_process_stable") is True:
            stable += 1
        else:
            unstable += 1
    return {"stable": stable, "unstable": unstable, "exceptions": exceptions}


def exception_signature(case: dict[str, Any] | None) -> tuple[Any, Any]:
    """Return the exception behavior for comparison."""
    if case is None:
        return ("missing", "missing")
    return (case.get("exception_type"), case.get("exception_message"))


def input_signature(case: dict[str, Any] | None) -> tuple[Any, ...]:
    """Return a representation signature for input-drift analysis."""
    if case is None:
        return ("missing",)
    category = case.get("category")
    if category == "unicode_string":
        return (
            category,
            case.get("repr"),
            case.get("type"),
            tuple(case.get("code_points", [])),
            case.get("utf8_sha256"),
        )
    if category == "bytes_payload":
        return (
            category,
            case.get("repr"),
            case.get("type"),
            case.get("bytes_length"),
            case.get("bytes_sha256"),
        )
    return (category, case.get("repr"), case.get("type"))


def same_hash(case_a: dict[str, Any] | None, case_b: dict[str, Any] | None) -> bool:
    """Return whether two successful marshal hashes match."""
    return (
        case_a is not None
        and case_b is not None
        and case_a.get("marshal_sha256") is not None
        and case_a.get("marshal_sha256") == case_b.get("marshal_sha256")
    )


def python_major_minor(result: dict[str, Any]) -> tuple[str, str]:
    """Return the Python major/minor version for one result."""
    version = result["data"].get("environment", {}).get("sys_version", "")
    parts = version.split()[0].split(".") if version else []
    if len(parts) >= 2:
        return (parts[0], parts[1])
    return ("unknown", "unknown")


def interpretation(
    result_a: dict[str, Any],
    result_b: dict[str, Any],
    case_a: dict[str, Any] | None,
    case_b: dict[str, Any] | None,
) -> str:
    """Explain one pairwise case comparison."""
    if case_a is None or case_b is None:
        return "Case missing from one platform result."
    same_exception = exception_signature(case_a) == exception_signature(case_b)
    if case_a.get("exception_type") or case_b.get("exception_type"):
        if same_exception:
            return "Same optional support boundary or exception behavior."
        return "Different exception behavior; check Python version support."
    if same_hash(case_a, case_b):
        return "Same input and same marshal hash."
    if input_signature(case_a) != input_signature(case_b):
        return "Input representation differs, so hash difference is input-driven."
    if python_major_minor(result_a) != python_major_minor(result_b):
        return "Same input representation but Python major/minor differs; likely version-level marshal format difference."
    return "Same input representation and Python major/minor but marshal hash differs; potential instability."


def first_case(results: list[dict[str, Any]], case_name: str) -> dict[str, Any] | None:
    """Return the first matching case from loaded results."""
    for result in results:
        case = result["cases"].get(case_name)
        if case is not None:
            return case
    return None


def write_markdown(results: list[dict[str, Any]]) -> None:
    """Write the unified comparison Markdown."""
    lines = [
        "# 成员 B 统一测试跨平台比较",
        "",
        "## 环境列表",
        "",
    ]
    if not results:
        lines.extend(["No unified result JSON files were found.", ""])
    for result in results:
        environment = result["data"].get("environment", {})
        lines.append(
            "- `{name}`: {platform_info}; implementation={impl}; marshal_version={marshal_version}".format(
                name=result["path"].name,
                platform_info=environment.get("platform_platform", "unknown"),
                impl=environment.get("python_implementation", "unknown"),
                marshal_version=environment.get("marshal_version", "unknown"),
            )
        )
    lines.append("")

    lines.extend(
        [
            "## 单平台同进程稳定性",
            "",
            "| Platform | Case count | Stable supported | Unstable supported | Exception/support boundary |",
            "| --- | ---: | ---: | ---: | ---: |",
        ]
    )
    for result in results:
        summary = platform_summary(result)
        lines.append(
            "| {platform} | {case_count} | {stable} | {unstable} | {exceptions} |".format(
                platform=markdown_escape(result["label"]),
                case_count=len(result["cases"]),
                stable=summary["stable"],
                unstable=summary["unstable"],
                exceptions=summary["exceptions"],
            )
        )
    lines.append("")

    lines.extend(["## 跨平台比较", ""])
    if len(results) < 2:
        lines.extend(
            [
                "Cross-platform comparison skipped: fewer than two unified platform results were found.",
                "",
            ]
        )
    else:
        for result_a, result_b in combinations(results, 2):
            lines.extend(
                [
                    f"### {result_a['label']} vs {result_b['label']}",
                    "",
                    "| Case | Category | Same marshal hash | Same exception | Interpretation |",
                    "| --- | --- | --- | --- | --- |",
                ]
            )
            for case_name in sorted(set(result_a["cases"]) | set(result_b["cases"])):
                case_a = result_a["cases"].get(case_name)
                case_b = result_b["cases"].get(case_name)
                category = (
                    case_a.get("category")
                    if case_a is not None
                    else case_b.get("category", "N/A")
                    if case_b is not None
                    else "N/A"
                )
                lines.append(
                    "| {case} | {category} | {same_hash} | {same_exception} | {note} |".format(
                        case=markdown_escape(case_name),
                        category=markdown_escape(category),
                        same_hash="SAME" if same_hash(case_a, case_b) else "DIFFERENT",
                        same_exception=(
                            "SAME"
                            if exception_signature(case_a) == exception_signature(case_b)
                            else "DIFFERENT"
                        ),
                        note=markdown_escape(interpretation(result_a, result_b, case_a, case_b)),
                    )
                )
            lines.append("")

    composed = first_case(results, "composed_e_acute")
    decomposed = first_case(results, "decomposed_e_acute")
    lines.extend(["## Unicode 扩展观察", ""])
    if composed and decomposed:
        same = composed.get("marshal_sha256") == decomposed.get("marshal_sha256")
        lines.extend(
            [
                f"- `composed_e_acute` code points: `{composed.get('code_points')}`",
                f"- `decomposed_e_acute` code points: `{decomposed.get('code_points')}`",
                f"- 两者 marshal hash 是否相同：`{same}`",
                "- 若 hash 不同，原因是底层 Unicode code points 不同，而不是 marshal 缺陷。",
                "",
            ]
        )
    else:
        lines.extend(["- Unicode composed/decomposed cases were not available.", ""])

    lines.extend(
        [
            "## slice 支持边界",
            "",
            "slice case 是可选支持探测；如果当前 Python 报 `ValueError: unmarshallable object`，记录为版本支持边界，不作为失败。",
            "",
        ]
    )
    OUTPUT_PATH.write_text("\n".join(lines), encoding="utf-8")


def main() -> None:
    """Generate the unified comparison Markdown."""
    RESULTS_DIR.mkdir(parents=True, exist_ok=True)
    results = load_results()
    write_markdown(results)
    print(f"Wrote unified comparison Markdown: {OUTPUT_PATH}")


if __name__ == "__main__":
    main()
