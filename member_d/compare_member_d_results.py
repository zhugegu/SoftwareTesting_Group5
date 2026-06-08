"""Compare member D marshal results across platforms and Python versions.

This script reads all member_d_all_*_results.json files under member_d/results
and generates a cross-platform Markdown summary report.

The report is intended to support the final testing report for member D:
recursive/cyclic structures, deep nesting, unsupported types, shared references,
marshal version arguments, and invalid byte-stream loads.
"""

from __future__ import annotations

import json
from collections import defaultdict
from pathlib import Path
from typing import Any


BASE_DIR = Path(__file__).resolve().parent
RESULTS_DIR = BASE_DIR / "results"
OUTPUT_PATH = RESULTS_DIR / "member_d_cross_platform_summary.md"


def load_json_files() -> list[dict[str, Any]]:
    """Load all member D JSON result files."""
    json_files = sorted(RESULTS_DIR.glob("member_d_all_*_results.json"))
    results = []

    for path in json_files:
        data = json.loads(path.read_text(encoding="utf-8"))
        data["_source_file"] = path.name
        results.append(data)

    return results


def flatten_cases(cases: list[dict[str, Any]]) -> list[dict[str, Any]]:
    """Flatten top-level cases and nested subcases."""
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


def env_label(data: dict[str, Any]) -> str:
    """Return a compact environment label."""
    env = data["environment"]
    system = env.get("platform_system", "unknown")
    machine = env.get("platform_machine", "unknown")
    py_ver = env.get("python_version_major_minor", "unknown")
    return f"{system} / {machine} / Python {py_ver}"


def env_sort_key(data: dict[str, Any]) -> tuple[str, str, str]:
    """Sort environments by system, Python version, and machine."""
    env = data["environment"]
    return (
        str(env.get("platform_system", "")),
        str(env.get("python_version_major_minor", "")),
        str(env.get("platform_machine", "")),
    )


def status_for_item(item: dict[str, Any]) -> str:
    """Return PASS, EXPECTED_EXCEPTION, or FAIL for a flattened result item."""
    if item.get("operation") == "loads":
        if item.get("stable_behavior") is True:
            return "PASS"
        return "FAIL"

    if item.get("exception_type") is not None:
        return "EXPECTED_EXCEPTION"

    if item.get("same_process_stable") is True:
        return "PASS"

    return "FAIL"


def short_hash(value: str | None, length: int = 12) -> str:
    """Shorten a hash for table display."""
    if not value:
        return "-"
    return value[:length] + "..."


def escape_md(value: Any) -> str:
    """Escape text for Markdown tables."""
    text = str(value)
    return text.replace("|", "\\|").replace("\n", " ")


def collect_case_statuses(
    all_results: list[dict[str, Any]],
) -> dict[str, dict[str, Any]]:
    """Collect per-case status across all environments."""
    case_map: dict[str, dict[str, Any]] = {}

    for data in all_results:
        label = env_label(data)
        flat_items = flatten_cases(data["cases"])

        for item in flat_items:
            case_id = item.get("case_id", "-")
            if case_id not in case_map:
                case_map[case_id] = {
                    "case_id": case_id,
                    "requirements": set(),
                    "operation": item.get("operation", "-"),
                    "parent": item.get("parent_case_id", "-"),
                    "statuses": {},
                    "hashes": defaultdict(list),
                    "exceptions": defaultdict(list),
                    "roundtrip_values": defaultdict(list),
                }

            for requirement in item.get("requirement_ids", []):
                case_map[case_id]["requirements"].add(requirement)

            status = status_for_item(item)
            case_map[case_id]["statuses"][label] = status

            hash_value = item.get("marshal_sha256")
            if hash_value:
                case_map[case_id]["hashes"][hash_value].append(label)

            exception_type = item.get("exception_type")
            if exception_type:
                message = item.get("exception_message")
                signature = f"{exception_type}: {message}"
                case_map[case_id]["exceptions"][signature].append(label)

            roundtrip_correct = item.get("roundtrip_correct")
            if roundtrip_correct is not None:
                case_map[case_id]["roundtrip_values"][str(roundtrip_correct)].append(
                    label
                )

    return case_map


def summarize_case_outcome(case_info: dict[str, Any], env_count: int) -> str:
    """Summarize one case across all environments."""
    statuses = case_info["statuses"]
    status_values = list(statuses.values())

    if len(status_values) < env_count:
        return "INCOMPLETE"

    if all(status == "PASS" for status in status_values):
        return "PASS_ALL"

    if all(status == "EXPECTED_EXCEPTION" for status in status_values):
        return "EXPECTED_EXCEPTION_ALL"

    if all(status in {"PASS", "EXPECTED_EXCEPTION"} for status in status_values):
        return "MIXED_EXPECTED"

    return "CHECK_REQUIRED"


def write_summary(all_results: list[dict[str, Any]]) -> Path:
    """Write the cross-platform Markdown summary."""
    RESULTS_DIR.mkdir(parents=True, exist_ok=True)

    sorted_results = sorted(all_results, key=env_sort_key)
    case_map = collect_case_statuses(sorted_results)
    env_count = len(sorted_results)

    total_flat_cases = []
    for data in sorted_results:
        total_flat_cases.extend(flatten_cases(data["cases"]))

    unstable_total = sum(
        data.get("result_counts", {}).get("unstable_count", 0)
        for data in sorted_results
    )

    lines = []

    lines.append("# Member D Cross-Platform Marshal Test Summary")
    lines.append("")
    lines.append("## 1. Scope")
    lines.append("")
    lines.append(
        "This summary aggregates member D marshal stability results across "
        "GitHub Actions environments. The tested scope includes cyclic "
        "references, deep nesting boundaries, unsupported types, shared "
        "references, marshal version arguments, and invalid byte-stream "
        "deserialization."
    )
    lines.append("")
    lines.append("## 2. Environment Matrix")
    lines.append("")
    lines.append("| # | Source File | System | Machine | Python | marshal.version | Flat Cases | Stable | Unstable | Exceptions |")
    lines.append("|---:|---|---|---|---|---:|---:|---:|---:|---:|")

    for index, data in enumerate(sorted_results, start=1):
        env = data["environment"]
        counts = data.get("result_counts", {})
        lines.append(
            f"| {index} | `{data.get('_source_file')}` | "
            f"{escape_md(env.get('platform_system'))} | "
            f"{escape_md(env.get('platform_machine'))} | "
            f"{escape_md(env.get('python_version_major_minor'))} | "
            f"{escape_md(env.get('marshal_version'))} | "
            f"{counts.get('flat_case_count')} | "
            f"{counts.get('stable_count')} | "
            f"{counts.get('unstable_count')} | "
            f"{counts.get('exception_count')} |"
        )

    lines.append("")
    lines.append("## 3. Overall Result")
    lines.append("")
    lines.append("| Metric | Value |")
    lines.append("|---|---:|")
    lines.append(f"| Environment count | {env_count} |")
    lines.append(f"| Total flattened executions | {len(total_flat_cases)} |")
    lines.append(f"| Total unstable cases reported | {unstable_total} |")
    lines.append("")

    if unstable_total == 0:
        lines.append(
            "No non-deterministic marshal output was observed in the aggregated "
            "GitHub Actions results. All unstable counts reported by the per-"
            "environment summaries were zero."
        )
    else:
        lines.append(
            "At least one environment reported an unstable case. The detailed "
            "case matrix below should be inspected before writing the final "
            "report."
        )

    lines.append("")
    lines.append("## 4. Requirement Coverage")
    lines.append("")
    requirement_map: dict[str, set[str]] = defaultdict(set)

    for case_id, case_info in case_map.items():
        for requirement in case_info["requirements"]:
            requirement_map[requirement].add(case_id)

    lines.append("| Requirement ID | Covered Cases |")
    lines.append("|---|---|")

    for requirement in sorted(requirement_map):
        covered = ", ".join(sorted(requirement_map[requirement]))
        lines.append(f"| {requirement} | {covered} |")

    lines.append("")
    lines.append("## 5. Cross-Environment Case Outcome Matrix")
    lines.append("")
    lines.append(
        "| Case ID | Requirements | Operation | Parent | Cross-Env Outcome | "
        "Distinct Hashes | Exception Signatures |"
    )
    lines.append("|---|---|---|---|---|---:|---:|")

    for case_id in sorted(case_map):
        case_info = case_map[case_id]
        requirements = ", ".join(sorted(case_info["requirements"]))
        outcome = summarize_case_outcome(case_info, env_count)
        distinct_hashes = len(case_info["hashes"])
        exception_signatures = len(case_info["exceptions"])

        lines.append(
            f"| {case_id} | {requirements} | "
            f"{escape_md(case_info['operation'])} | "
            f"{escape_md(case_info['parent'])} | "
            f"{outcome} | {distinct_hashes} | {exception_signatures} |"
        )

    lines.append("")
    lines.append("## 6. Expected Exception Summary")
    lines.append("")
    lines.append("| Case ID | Exception Signature | Environment Count |")
    lines.append("|---|---|---:|")

    exception_rows = []

    for case_id in sorted(case_map):
        case_info = case_map[case_id]
        for signature, labels in case_info["exceptions"].items():
            exception_rows.append((case_id, signature, len(labels)))

    if exception_rows:
        for case_id, signature, count in exception_rows:
            lines.append(f"| {case_id} | {escape_md(signature)} | {count} |")
    else:
        lines.append("| - | No exception signatures recorded | 0 |")

    lines.append("")
    lines.append("## 7. Hash Diversity Notes")
    lines.append("")
    lines.append(
        "Distinct hash counts in this cross-platform summary should be interpreted "
        "carefully. Different Python versions and marshal format versions are not "
        "required to produce identical byte streams. The main stability property "
        "tested by member D is same-environment determinism: the same input should "
        "produce one unique SHA-256 hash across repeated marshal.dumps() calls, "
        "or fail consistently for expected invalid inputs."
    )
    lines.append("")
    lines.append("| Case ID | Distinct Hash Count | Example Hashes |")
    lines.append("|---|---:|---|")

    for case_id in sorted(case_map):
        hashes = sorted(case_map[case_id]["hashes"])
        if not hashes:
            continue
        examples = ", ".join(short_hash(value) for value in hashes[:5])
        if len(hashes) > 5:
            examples += ", ..."
        lines.append(f"| {case_id} | {len(hashes)} | {examples} |")

    lines.append("")
    lines.append("## 8. Final Aggregated Conclusion")
    lines.append("")

    if unstable_total == 0:
        lines.append(
            "Across the collected member D GitHub Actions results, the test suite "
            "did not observe same-process non-determinism. Cyclic structures, "
            "deep nested structures below the tested recursion boundary, shared "
            "references, marshal version parameter cases, and invalid byte-stream "
            "loads all behaved deterministically within each environment. The "
            "recorded exceptions were expected boundary or unsupported-input "
            "behaviors, such as overly deep nesting and unmarshallable object "
            "types."
        )
    else:
        lines.append(
            "The aggregated result contains potentially unstable cases. These "
            "cases should be examined in the original JSON files before drawing "
            "a final conclusion."
        )

    OUTPUT_PATH.write_text("\n".join(lines), encoding="utf-8")
    return OUTPUT_PATH


def main() -> None:
    """Generate the member D cross-platform summary."""
    all_results = load_json_files()

    if not all_results:
        print(f"No member D JSON result files found under {RESULTS_DIR}")
        return

    output_path = write_summary(all_results)
    print(f"Loaded {len(all_results)} JSON result files.")
    print(f"Wrote cross-platform summary: {output_path}")


if __name__ == "__main__":
    main()