"""Compare member B marshal result hashes across platform JSON files."""

from __future__ import annotations

import json
from itertools import combinations
from pathlib import Path
from typing import Any


BASE_DIR = Path(__file__).resolve().parent
RESULTS_DIR = BASE_DIR / "results"
OUTPUT_PATH = RESULTS_DIR / "cross_platform_comparison.md"
FLOAT_COMPLEX_TOPIC = "float and complex deep precision marshal tests"


def markdown_escape(value: Any) -> str:
    """Escape Markdown table separators."""
    return str(value).replace("|", "\\|").replace("\n", " ")


def all_cases(data: dict[str, Any]) -> list[dict[str, Any]]:
    """Return fixed object cases and recreated NaN cases together."""
    return data.get("cases", []) + data.get("recreated_nan_cases", [])


def platform_label(path: Path, data: dict[str, Any]) -> str:
    """Create a readable platform label for comparison output."""
    environment = data.get("environment", {})
    system = environment.get("platform_system") or "unknown"
    machine = environment.get("platform_machine") or "unknown"
    return f"{path.stem} ({system}/{machine})"


def load_results() -> list[dict[str, Any]]:
    """Load every platform result JSON from the results directory."""
    loaded = []
    for path in sorted(RESULTS_DIR.glob("*_results.json")):
        data = json.loads(path.read_text(encoding="utf-8"))
        if data.get("topic") != FLOAT_COMPLEX_TOPIC:
            continue
        loaded.append(
            {
                "path": path,
                "label": platform_label(path, data),
                "cases": {case["case"]: case for case in all_cases(data)},
            }
        )
    return loaded


def skipped_result_files() -> list[Path]:
    """Return result files that are not part of the float/complex suite."""
    skipped = []
    for path in sorted(RESULTS_DIR.glob("*_results.json")):
        data = json.loads(path.read_text(encoding="utf-8"))
        if data.get("topic") != FLOAT_COMPLEX_TOPIC:
            skipped.append(path)
    return skipped


def is_nan_related(case_name: str, *cases: dict[str, Any] | None) -> bool:
    """Return whether a case name or note is NaN-related."""
    if "nan" in case_name.lower():
        return True
    return any(
        case is not None and "nan" in case.get("note", "").lower()
        for case in cases
    )


def note_for_pair(
    case_name: str,
    case_a: dict[str, Any] | None,
    case_b: dict[str, Any] | None,
) -> str:
    """Explain missing cases or hash differences for a pair."""
    notes = []
    if is_nan_related(case_name, case_a, case_b):
        notes.append("NaN-related case")
    if case_a is None or case_b is None:
        notes.append("Case missing from one platform result")
        return "; ".join(notes)
    if case_a.get("first_hash") == case_b.get("first_hash"):
        notes.append("First marshal hash is identical")
    else:
        notes.append("First marshal hash differs")
    return "; ".join(notes)


def write_skipped(results: list[dict[str, Any]]) -> None:
    """Write a graceful skip message when fewer than two platforms exist."""
    lines = [
        "# 成员 B：跨平台 marshal 哈希比对",
        "",
        "Only one platform result found. Cross-platform comparison was skipped.",
        "",
    ]
    if results:
        lines.append(f"- Found: `{results[0]['path'].name}`")
        lines.append("")
    OUTPUT_PATH.write_text("\n".join(lines), encoding="utf-8")


def skipped_section(paths: list[Path]) -> list[str]:
    """Document result files read but excluded from this comparison."""
    if not paths:
        return []
    lines = [
        "## Skipped Result Files",
        "",
        (
            "The following `*_results.json` files were not part of the "
            "float/complex suite and were excluded from this comparison:"
        ),
        "",
    ]
    lines.extend(f"- `{path.name}`" for path in paths)
    lines.append("")
    return lines


def summary_lines(has_difference: bool) -> list[str]:
    """Return a high-level cross-platform comparison summary."""
    if has_difference:
        return [
            "## Overall Result",
            "",
            "At least one compared float/complex marshal hash is DIFFERENT.",
            "",
        ]
    return [
        "## Overall Result",
        "",
        (
            "All compared float/complex marshal hashes are identical across "
            "the tested platforms."
        ),
        "",
    ]


def main() -> None:
    """Generate a Markdown comparison for all available platform pairs."""
    RESULTS_DIR.mkdir(parents=True, exist_ok=True)
    results = load_results()
    skipped_paths = skipped_result_files()

    if len(results) < 2:
        write_skipped(results)
        print(f"Wrote cross-platform comparison Markdown: {OUTPUT_PATH}")
        return

    lines = [
        "# 成员 B：跨平台 marshal 哈希比对",
        "",
    ]
    lines.extend(skipped_section(skipped_paths))
    has_difference = False

    for result_a, result_b in combinations(results, 2):
        label_a = result_a["label"]
        label_b = result_b["label"]
        lines.extend(
            [
                f"## {label_a} vs {label_b}",
                "",
                (
                    "| Case | System A Hash | System B Hash | "
                    "Cross-platform Same | Note |"
                ),
                "| --- | --- | --- | --- | --- |",
            ]
        )

        case_names = sorted(set(result_a["cases"]) | set(result_b["cases"]))
        for case_name in case_names:
            case_a = result_a["cases"].get(case_name)
            case_b = result_b["cases"].get(case_name)
            hash_a = case_a.get("first_hash", "N/A") if case_a else "N/A"
            hash_b = case_b.get("first_hash", "N/A") if case_b else "N/A"
            same_hash = (
                case_a is not None
                and case_b is not None
                and hash_a == hash_b
            )
            comparison = "SAME" if same_hash else "DIFFERENT"
            if not same_hash:
                has_difference = True
            lines.append(
                "| {case} | {hash_a} | {hash_b} | {same} | {note} |".format(
                    case=markdown_escape(case_name),
                    hash_a=markdown_escape(hash_a),
                    hash_b=markdown_escape(hash_b),
                    same=comparison,
                    note=markdown_escape(
                        note_for_pair(case_name, case_a, case_b)
                    ),
                )
            )
        lines.append("")

    lines[2:2] = summary_lines(has_difference)
    OUTPUT_PATH.write_text("\n".join(lines), encoding="utf-8")
    print(f"Wrote cross-platform comparison Markdown: {OUTPUT_PATH}")


if __name__ == "__main__":
    main()
