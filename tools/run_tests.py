# bleachspire/tools/run_tests.py
"""Run the test functions without pytest.

Handy on a machine where pip cannot install packages: every tests/test_*.py is
imported and each `test_*` function is called. Functions that ask for an
argument get a fresh temporary directory, like pytest's `tmp_path`.

Usage:  python tools/run_tests.py
"""

from __future__ import annotations

import importlib.util
import inspect
import shutil
import sys
import traceback
import uuid
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
TESTS = ROOT / "tests"


def load(path: Path):
    spec = importlib.util.spec_from_file_location(f"t_{path.stem}", path)
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


def main() -> int:
    passed = failed = 0
    scratch = ROOT / ".tmp"
    scratch.mkdir(exist_ok=True)
    for path in sorted(TESTS.glob("test_*.py")):
        module = load(path)
        for name, fn in inspect.getmembers(module, inspect.isfunction):
            if not name.startswith("test_"):
                continue
            params = inspect.signature(fn).parameters
            tmpdir = scratch / f"{path.stem}-{name}-{uuid.uuid4().hex[:8]}"
            tmpdir.mkdir(parents=True)
            try:
                if params:
                    fn(tmpdir)
                else:
                    fn()
                passed += 1
                print(f"PASS {path.name}::{name}")
            except Exception:
                failed += 1
                print(f"FAIL {path.name}::{name}")
                traceback.print_exc(limit=3)
            finally:
                shutil.rmtree(tmpdir, ignore_errors=True)
    print(f"{passed} passed, {failed} failed")
    return 1 if failed else 0


if __name__ == "__main__":
    raise SystemExit(main())
