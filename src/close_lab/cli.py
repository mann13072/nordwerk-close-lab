"""Command-line entry points for the bounded first implementation session."""

from __future__ import annotations

import argparse
import compileall
import sys
from pathlib import Path

from .business_events import generate_smoke_events
from .chart_of_accounts import build_chart_of_accounts
from .config import PROJECT_ROOT, SMOKE_SEED
from .export import export_smoke
from .journal_engine import post_events
from .master_data import build_master_data
from .validation import validate_smoke


def build_smoke():
    master_data = build_master_data()
    accounts = build_chart_of_accounts()
    events = generate_smoke_events(seed=SMOKE_SEED)
    results = post_events(events, master_data, accounts)
    return master_data, accounts, events, results


def _output_directory(path: str | None) -> Path:
    return Path(path) if path else PROJECT_ROOT / "data" / "raw" / "smoke_test"


def command_syntax_check() -> int:
    source_dir = PROJECT_ROOT / "src"
    test_dir = PROJECT_ROOT / "tests"
    ok = compileall.compile_dir(str(source_dir), quiet=1) and compileall.compile_dir(str(test_dir), quiet=1)
    print("syntax-check: PASS" if ok else "syntax-check: FAIL")
    return 0 if ok else 1


def command_generate(output_dir: Path) -> int:
    master_data, accounts, events, results = build_smoke()
    hashes = export_smoke(output_dir, events, results, master_data)
    print(f"generated events={len(events)} headers={len(results)} lines={sum(len(result.lines) for result in results)}")
    print(f"seed={SMOKE_SEED} output={output_dir.resolve()}")
    for name, digest in sorted(hashes.items()):
        print(f"{name}: {digest}")
    return 0


def command_validate() -> int:
    master_data, accounts, events, results = build_smoke()
    issues = validate_smoke(events, results, accounts, master_data)
    if issues:
        print("validate-smoke: FAIL")
        for issue in issues:
            print(f"- {issue}")
        return 1
    print(
        "validate-smoke: PASS "
        f"events={len(events)} headers={len(results)} lines={sum(len(result.lines) for result in results)} "
        "AR_items=20 AR_positive_open=8 AP_items=17 AP_positive_open=11"
    )
    return 0


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="NordWerk smoke-test accounting kernel")
    subparsers = parser.add_subparsers(dest="command", required=True)
    subparsers.add_parser("syntax-check", help="compile source and test modules")
    generate = subparsers.add_parser("generate-smoke", help="generate canonical smoke-test CSV exports")
    generate.add_argument("--output-dir", help="override the smoke-test output directory")
    subparsers.add_parser("validate-smoke", help="run positive smoke-test accounting controls")
    return parser


def main(argv: list[str] | None = None) -> int:
    args = build_parser().parse_args(argv)
    if args.command == "syntax-check":
        return command_syntax_check()
    if args.command == "generate-smoke":
        return command_generate(_output_directory(args.output_dir))
    if args.command == "validate-smoke":
        return command_validate()
    raise AssertionError(f"unknown command: {args.command}")


if __name__ == "__main__":
    sys.exit(main())
