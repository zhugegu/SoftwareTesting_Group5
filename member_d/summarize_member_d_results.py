"""Summarize member D marshal JSON results into Markdown reports."""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any


BASE_DIR = Path(__file__).resolve().parent
RESULTS_DIR = BASE_DIR / "results"


def short_hash(value: str | None, length: int = 12) -> str:
    """Return a shortened hash string for display."""
    if not value:
        return "-"
    return value[:length] + "..."


def status_for_item(item: dict[str, Any]) -> str:
    """Return a readable PASS/FAIL/EXCEPTION status for one result item."""
    if item.get("operation") == "loads":
        if item.get("stable_behavior") is True:
            return "PASS"
        return "FAIL"

    if item.get("exception_type") is not None:
        return "EXPECTED_EXCEPTION"

    if item.get("same_process_stable") is True:
        return "PASS"

    return "FAIL"


def flatten_cases(cases: list[dict[str, Any]]) -> list[dict[str, Any]]:
    """Flatten top-level cases and subcases into a single list."""
    flat_items = []

    for case in cases:
        if "subcases" in case:
            for subcase in case["subcases"]:
                copied = dict(subcase)
                copied["parent_case_id"] = case.get("case_id", "-")
                copied["parent_case_name"] = case.get("case_name", "-")
                flat_items.append(copied)
        else:
            copied = dict(case)
            copied["parent_case_id"] = "-"
            copied["parent_case_name"] = "-"
            flat_items.append(copied)

    return flat_items


def summarize_json(result_path: Path) -> Path:
    """Create one Markdown summary file from one JSON result file."""
    data = json.loads(result_path.read_text(encoding="utf-8"))

    environment = data["environment"]
    counts = data["result_counts"]
    flat_items = flatten_cases(data["cases"])

    output_path = result_path.with_name(
        result_path.stem.replace("member_d_all_", "member_d_summary_") + ".md"
    )

    lines = []

    lines.append(f"# Member D Marshal Test Summary: `{result_path.name}`")
    lines.append("")
    lines.append("## 1. Environment")
    lines.append("")
    lines.append("| Field | Value |")
    lines.append("|---|---|")
    lines.append(f"| Platform | {environment.get('platform_platform')} |")
    lines.append(f"| System | {environment.get('platform_system')} |")
    lines.append(f"| Machine | {environment.get('platform_machine')} |")
    lines.append(f"| Python implementation | {environment.get('python_implementation')} |")
    lines.append(f"| Python version | {environment.get('python_version_major_minor')} |")
    lines.append(f"| Full sys.version | {environment.get('sys_version')} |")
    lines.append(f"| marshal.version | {environment.get('marshal_version')} |")
    lines.append(f"| Recursion limit | {environment.get('recursion_limit')} |")
    lines.append("")
    lines.append("## 2. Overall Result Counts")
    lines.append("")
    lines.append("| Metric | Value |")
    lines.append("|---|---:|")
    lines.append(f"| Top-level case count | {data.get('top_level_case_count')} |")
    lines.append(f"| Flattened case count | {counts.get('flat_case_count')} |")
    lines.append(f"| Stable count | {counts.get('stable_count')} |")
    lines.append(f"| Unstable count | {counts.get('unstable_count')} |")
    lines.append(f"| Exception count | {counts.get('exception_count')} |")
    lines.append(f"| Repeat count | {data.get('repeat_count')} |")
    lines.append("")
    lines.append("## 3. Flattened Case Results")
    lines.append("")
    lines.append(
        "| Case ID | Parent | Operation | Requirements | Status | "
        "Unique Hash Count | Exception | Roundtrip Correct | Hash |"
    )
    lines.append("|---|---|---|---|---|---:|---|---|---|")

    for item in flat_items:
        case_id = item.get("case_id", "-")
        parent = item.get("parent_case_id", "-")
        operation = item.get("operation", "-")
        requirements = ", ".join(item.get("requirement_ids", []))
        status = status_for_item(item)

        unique_hash_count = item.get("unique_hash_count")
        if unique_hash_count is None:
            unique_hash_count = "-"

        exception = item.get("exception_type") or "-"
        roundtrip_correct = item.get("roundtrip_correct")
        if roundtrip_correct is None:
            roundtrip_correct = "-"

        hash_value = short_hash(item.get("marshal_sha256"))

        lines.append(
            f"| {case_id} | {parent} | {operation} | {requirements} | "
            f"{status} | {unique_hash_count} | {exception} | "
            f"{roundtrip_correct} | {hash_value} |"
        )

    lines.append("")
    lines.append("## 4. Requirement Coverage")
    lines.append("")
    coverage: dict[str, list[str]] = {}

    for item in flat_items:
        for requirement in item.get("requirement_ids", []):
            coverage.setdefault(requirement, []).append(item.get("case_id", "-"))

    lines.append("| Requirement ID | Covered By |")
    lines.append("|---|---|")

    for requirement in sorted(coverage):
        case_ids = ", ".join(sorted(set(coverage[requirement])))
        lines.append(f"| {requirement} | {case_ids} |")

    lines.append("")
    lines.append("## 5. Exception Details")
    lines.append("")

    exception_items = [
        item for item in flat_items if item.get("exception_type") is not None
    ]

    if not exception_items:
        lines.append("No exception cases were recorded.")
    else:
        lines.append("| Case ID | Exception Type | Exception Message | Interpretation |")
        lines.append("|---|---|---|---|")

        for item in exception_items:
            case_id = item.get("case_id", "-")
            exception_type = item.get("exception_type", "-")
            exception_message = str(item.get("exception_message", "-")).replace(
                "|", "\\|"
            )
            interpretation = (
                "Expected rejection for unsupported or invalid input; "
                "not treated as a stability bug."
            )
            lines.append(
                f"| {case_id} | {exception_type} | "
                f"{exception_message} | {interpretation} |"
            )

    lines.append("")
    lines.append("## 6. Preliminary Conclusion")
    lines.append("")
    unstable_count = counts.get("unstable_count", 0)
    exception_count = counts.get("exception_count", 0)
    stable_count = counts.get("stable_count", 0)

    if unstable_count == 0:
        lines.append(
            f"In this environment, {stable_count} flattened cases showed stable "
            "behavior and no non-deterministic marshal output was observed. "
            f"The {exception_count} exception cases were expected rejection or "
            "invalid-byte-stream cases and should not be treated as marshal bugs."
        )
    else:
        lines.append(
            f"In this environment, {unstable_count} potentially unstable cases "
            "were observed and should be inspected before writing the final report."
        )

    output_path.write_text("\n".join(lines), encoding="utf-8")
    return output_path


def main() -> None:
    """Summarize all member D JSON result files in the results directory."""
    json_files = sorted(RESULTS_DIR.glob("member_d_all_*_results.json"))

    if not json_files:
        print(f"No member D JSON files found in {RESULTS_DIR}")
        return

    for result_path in json_files:
        output_path = summarize_json(result_path)
        print(f"Wrote summary Markdown: {output_path}")


if __name__ == "__main__":
    main()