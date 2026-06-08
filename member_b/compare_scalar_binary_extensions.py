"""Compare member B scalar/binary marshal results across platforms."""

from __future__ import annotations

import json
from itertools import combinations
from pathlib import Path
from typing import Any


BASE_DIR = Path(__file__).resolve().parent
RESULTS_DIR = BASE_DIR / "results"
OUTPUT_PATH = RESULTS_DIR / "scalar_binary_cross_platform_comparison.md"


def markdown_escape(value: Any) -> str:
    """Escape Markdown table separators."""
    return str(value).replace("|", "\\|").replace("\n", " ")


def platform_label(path: Path, data: dict[str, Any]) -> str:
    """Create a readable platform label for comparison output."""
    environment = data.get("environment", {})
    system = environment.get("platform_system") or "unknown"
    machine = environment.get("platform_machine") or "unknown"
    py_version = environment.get("sys_version", "unknown").split()[0]
    return f"{path.stem} ({system}/{machine}, Python {py_version})"


def load_results() -> list[dict[str, Any]]:
    """Load every scalar/binary platform result JSON."""
    loaded = []
    for path in sorted(RESULTS_DIR.glob("scalar_binary_*_results.json")):
        data = json.loads(path.read_text(encoding="utf-8"))
        loaded.append(
            {
                "path": path,
                "data": data,
                "label": platform_label(path, data),
                "cases": {case["case"]: case for case in data.get("cases", [])},
            }
        )
    return loaded


def exception_signature(case: dict[str, Any] | None) -> tuple[Any, Any]:
    """Return the exception behavior used for platform comparison."""
    if case is None:
        return ("missing", "missing")
    return (case.get("exception_type"), case.get("exception_message"))


def input_signature(case: dict[str, Any] | None) -> tuple[Any, ...]:
    """Return the logical input signature for detecting representation drift."""
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


def same_repr_and_type(case_a: dict[str, Any] | None, case_b: dict[str, Any] | None) -> bool:
    """Return whether two cases have the same repr and Python type name."""
    return (
        case_a is not None
        and case_b is not None
        and case_a.get("repr") == case_b.get("repr")
        and case_a.get("type") == case_b.get("type")
    )


def same_marshal_hash(case_a: dict[str, Any] | None, case_b: dict[str, Any] | None) -> bool:
    """Return whether two successful marshal hashes are identical."""
    return (
        case_a is not None
        and case_b is not None
        and case_a.get("marshal_sha256") is not None
        and case_a.get("marshal_sha256") == case_b.get("marshal_sha256")
    )


def python_major_minor(result: dict[str, Any]) -> tuple[str, str]:
    """Return the Python major/minor version from one result."""
    version = result["data"].get("environment", {}).get("sys_version", "")
    release = version.split()[0] if version else ""
    parts = release.split(".")
    if len(parts) >= 2:
        return (parts[0], parts[1])
    return ("unknown", "unknown")


def platform_cell(case: dict[str, Any] | None) -> str:
    """Return the table cell value for one platform/case combination."""
    if case is None:
        return "N/A"
    if case.get("marshal_sha256") is not None:
        return case["marshal_sha256"]
    if case.get("exception_type") is not None:
        return case["exception_type"]
    return "N/A"


def interpretation(
    case_a: dict[str, Any] | None,
    case_b: dict[str, Any] | None,
    same_python_minor: bool,
) -> str:
    """Explain the comparison result for one case pair."""
    if case_a is None or case_b is None:
        return "Case missing from one platform result."
    same_exception = exception_signature(case_a) == exception_signature(case_b)
    if case_a.get("exception_type") or case_b.get("exception_type"):
        if same_exception:
            return "Same version support boundary or same exception behavior."
        return "Different exception behavior; check Python version support boundary."
    if same_marshal_hash(case_a, case_b):
        return "Same input and same marshal hash."
    if input_signature(case_a) != input_signature(case_b):
        return "Input representation differs, so hash difference is input-driven."
    if not same_python_minor:
        return "Same input representation but Python major/minor differs; likely version-level marshal format difference."
    return "Same input representation but marshal hash differs; potential instability."


def stability_summary(result: dict[str, Any]) -> dict[str, int]:
    """Count stable, unstable, and exception cases for one platform."""
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


def case_hash(result: dict[str, Any], case_name: str) -> str | None:
    """Return one case hash from a result, if present."""
    case = result["cases"].get(case_name)
    if not case:
        return None
    return case.get("marshal_sha256")


def first_available_case(results: list[dict[str, Any]], case_name: str) -> dict[str, Any] | None:
    """Return the first available case by name."""
    for result in results:
        case = result["cases"].get(case_name)
        if case:
            return case
    return None


def write_markdown(results: list[dict[str, Any]]) -> None:
    """Write the scalar/binary cross-platform comparison Markdown."""
    lines = [
        "# 成员 B：标量与二进制边界 marshal 稳定性扩展测试",
        "",
        "## 环境列表",
        "",
    ]

    if not results:
        lines.extend(
            [
                "No scalar/binary result JSON files were found.",
                "",
            ]
        )
    else:
        for result in results:
            environment = result["data"].get("environment", {})
            lines.append(
                "- `{name}`: {platform_info}; implementation={impl}; "
                "marshal_version={marshal_version}".format(
                    name=result["path"].name,
                    platform_info=environment.get("platform_platform", "unknown"),
                    impl=environment.get("python_implementation", "unknown"),
                    marshal_version=environment.get("marshal_version", "unknown"),
                )
            )
        lines.append("")

    lines.extend(
        [
            "## 每个平台同进程稳定性总结",
            "",
            "| Platform | Stable cases | Unstable cases | Exception/support-boundary cases |",
            "| --- | ---: | ---: | ---: |",
        ]
    )
    for result in results:
        summary = stability_summary(result)
        lines.append(
            "| {platform} | {stable} | {unstable} | {exceptions} |".format(
                platform=markdown_escape(result["label"]),
                stable=summary["stable"],
                unstable=summary["unstable"],
                exceptions=summary["exceptions"],
            )
        )
    lines.append("")

    lines.extend(
        [
            "## 跨平台比较表",
            "",
        ]
    )
    if len(results) < 2:
        lines.extend(
            [
                "Cross-platform comparison skipped: fewer than two platform results were found.",
                "",
            ]
        )
    else:
        for result_a, result_b in combinations(results, 2):
            same_python_minor = python_major_minor(result_a) == python_major_minor(result_b)
            lines.extend(
                [
                    f"### {result_a['label']} vs {result_b['label']}",
                    "",
                    (
                        "| Case | Category | Platform A | Platform B | Same marshal hash | "
                        "Same exception | Interpretation |"
                    ),
                    "| --- | --- | --- | --- | --- | --- | --- |",
                ]
            )
            case_names = sorted(set(result_a["cases"]) | set(result_b["cases"]))
            for case_name in case_names:
                case_a = result_a["cases"].get(case_name)
                case_b = result_b["cases"].get(case_name)
                category = (
                    case_a.get("category")
                    if case_a is not None
                    else case_b.get("category", "N/A")
                    if case_b is not None
                    else "N/A"
                )
                same_hash = same_marshal_hash(case_a, case_b)
                same_exception = exception_signature(case_a) == exception_signature(case_b)
                repr_type = same_repr_and_type(case_a, case_b)
                lines.append(
                    "| {case} | {category} | {platform_a} | {platform_b} | "
                    "{same_hash} | {same_exception} | {note} |".format(
                        case=markdown_escape(case_name),
                        category=markdown_escape(category),
                        platform_a=markdown_escape(platform_cell(case_a)),
                        platform_b=markdown_escape(platform_cell(case_b)),
                        same_hash="SAME" if same_hash else "DIFFERENT",
                        same_exception="SAME" if same_exception else "DIFFERENT",
                        note=markdown_escape(
                            f"same repr/type={repr_type}; {interpretation(case_a, case_b, same_python_minor)}"
                        ),
                    )
                )
            lines.append("")

    composed = first_available_case(results, "composed_e_acute")
    decomposed = first_available_case(results, "decomposed_e_acute")
    composed_hash = composed.get("marshal_sha256") if composed else None
    decomposed_hash = decomposed.get("marshal_sha256") if decomposed else None
    lines.extend(
        [
            "## composed_e_acute 与 decomposed_e_acute 分析",
            "",
            (
                "`composed_e_acute` 和 `decomposed_e_acute` 在视觉上相似，但底层 Unicode "
                "code points 不同。"
            ),
        ]
    )
    if composed and decomposed:
        lines.extend(
            [
                f"- composed code points: `{composed.get('code_points')}`",
                f"- decomposed code points: `{decomposed.get('code_points')}`",
                (
                    "- marshal hash: "
                    f"`{composed_hash}` vs `{decomposed_hash}`; "
                    f"same={composed_hash == decomposed_hash}"
                ),
            ]
        )
        if composed_hash != decomposed_hash:
            lines.append(
                "- Hash differs because the input Unicode code points differ; this is not a marshal defect."
            )
        else:
            lines.append(
                "- Hash is identical in this run, but the case still documents the boundary between byte-level equality and human-perceived equality."
            )
    else:
        lines.append("- Cases were not available in the loaded result files.")
    lines.append("")

    lines.extend(
        [
            "## bytes length boundary 分析",
            "",
            (
                "The bytes cases cover empty payloads, embedded NUL, high byte values, all byte "
                "values, and length boundaries at 255/256 and 65535/65536."
            ),
            (
                "If these cases remain same-process stable and cross-platform hashes match, embedded "
                "NUL and high byte values do not break marshal stability for raw bytes payloads."
            ),
            "",
            "## slice 支持边界分析",
            "",
        ]
    )
    slice_cases = [
        "slice_none_none_none",
        "slice_1_10_2",
        "slice_neg10_none_neg1",
    ]
    slice_lines = []
    for result in results:
        for case_name in slice_cases:
            case = result["cases"].get(case_name)
            if case and case.get("exception_type"):
                slice_lines.append(
                    f"- `{result['label']}` `{case_name}`: {case.get('exception_type')}: {case.get('exception_message')}"
                )
    if slice_lines:
        lines.extend(slice_lines)
        lines.append(
            "- These exceptions indicate Python version marshal support boundaries and are not treated as test failures."
        )
    else:
        lines.append(
            "- No slice marshal exceptions were recorded in the loaded results."
        )
    lines.append("")

    OUTPUT_PATH.write_text("\n".join(lines), encoding="utf-8")


def main() -> None:
    """Generate the scalar/binary comparison Markdown."""
    RESULTS_DIR.mkdir(parents=True, exist_ok=True)
    results = load_results()
    write_markdown(results)
    print(f"Wrote scalar/binary comparison Markdown: {OUTPUT_PATH}")


if __name__ == "__main__":
    main()
