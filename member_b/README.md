# Member B marshal stability tests

This folder contains member B's test code, generated evidence files, and report
for the Python `marshal` stability assignment.

## Files

- `member_b_marshal_tests.py`: the single unified test entrypoint for all member B required and extension cases.
- `compare_member_b_all_results.py`: unified cross-platform comparison report generator.
- `compare_cross_platform.py`: original float/complex comparison report generator.
- `compare_scalar_binary_extensions.py`: scalar/binary comparison report generator.
- `summarize_member_b_results.py`: per-result Markdown summary generator.
- `member_b_personal_test_report.md`: member B personal report.
- `results/`: JSON results, Markdown reports, and local logs.

## Local run

```bash
python member_b/member_b_marshal_tests.py
python member_b/compare_member_b_all_results.py
```

For report generation:

```bash
python member_b/compare_cross_platform.py
python member_b/compare_scalar_binary_extensions.py
python member_b/compare_member_b_all_results.py
python member_b/summarize_member_b_results.py
```

## GitHub Actions

The workflow in `.github/workflows/member-b-marshal-stability.yml` runs this
folder on Ubuntu, macOS, and Windows across Python 3.9, 3.10, 3.11, 3.12, and
3.13. It uploads JSON result artifacts and Markdown comparison reports.
