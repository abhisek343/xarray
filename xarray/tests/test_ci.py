from __future__ import annotations

from pathlib import Path

REPO_ROOT = Path(__file__).parents[2]


def test_last_release_benchmark_environment_installs_rattler() -> None:
    environment = (REPO_ROOT / "ci/requirements/environment.yml").read_text()

    assert any(line.strip() == "- py-rattler" for line in environment.splitlines())


def test_last_release_benchmark_propagates_asv_failures() -> None:
    workflow = (
        REPO_ROOT / ".github/workflows/benchmarks-last-release.yml"
    ).read_text()
    lines = [line.strip() for line in workflow.splitlines()]

    pipefail_line = lines.index("set -euo pipefail")
    asv_line = next(
        index for index, line in enumerate(lines) if line.startswith("asv continuous ")
    )

    assert pipefail_line < asv_line
