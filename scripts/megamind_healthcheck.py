from __future__ import annotations

import ast
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
REQUIRED_PATHS = (
    "README.md",
    "main.py",
    "requirements.txt",
    "Makefile",
    ".env.template",
    ".megamind/execution-body.yml",
)
PYTHON_FILES = ("main.py",)


def main() -> int:
    missing = [relative for relative in REQUIRED_PATHS if not ROOT.joinpath(relative).exists()]
    syntax_errors: list[str] = []
    for relative in PYTHON_FILES:
        path = ROOT / relative
        if not path.exists():
            continue
        try:
            ast.parse(path.read_text(encoding="utf-8"), filename=str(path))
        except (OSError, SyntaxError, UnicodeError) as exc:
            syntax_errors.append(f"{relative}: {exc}")

    python_ok = sys.version_info >= (3, 11)
    ready = python_ok and not missing and not syntax_errors
    report = {
        "body_id": "deep-research-agent",
        "check_type": "static_zero_secret",
        "python": sys.version.split()[0],
        "python_ok": python_ok,
        "missing_paths": missing,
        "syntax_errors": syntax_errors,
        "structurally_ready": ready,
        "runtime_tested": False,
        "next_commands": [
            "make install-requirements",
            "playwright install chromium --with-deps --no-shell",
            "python main.py",
        ],
        "truth_note": "This check does not install dependencies, read .env, launch a browser, call providers, or execute research tools.",
    }
    print(json.dumps(report, indent=2, sort_keys=True))
    return 0 if ready else 1


if __name__ == "__main__":
    raise SystemExit(main())
