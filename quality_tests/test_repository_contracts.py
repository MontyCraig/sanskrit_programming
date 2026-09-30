from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def test_required_repo_files_exist() -> None:
    required_files = [
        ROOT / "README.md",
        ROOT / "CLAUDE.md",
        ROOT / "requirements-dev.txt",
        ROOT / "pytest.ini",
        ROOT / ".github/workflows/markdown-lint.yml",
        ROOT / ".github/workflows/cgaas-gate.yml",
        ROOT / ".github/workflows/tddaas-gates.yml",
    ]

    missing = [str(path.relative_to(ROOT)) for path in required_files if not path.exists()]
    assert not missing, f"Missing repository files: {missing}"


def test_task_phase_files_exist() -> None:
    phase_files = [ROOT / "tasks" / f"phase{number}_tasks.md" for number in range(1, 10)]
    missing = [str(path.relative_to(ROOT)) for path in phase_files if not path.exists()]
    assert not missing, f"Missing phase plans: {missing}"


def test_language_prototypes_exist() -> None:
    assert (ROOT / "src/core/number.sam").exists()
    assert (ROOT / "tests/core/number_test.sam").exists()


def test_markdown_entrypoints_have_titles() -> None:
    markdown_files = [
        ROOT / "README.md",
        ROOT / "CLAUDE.md",
        ROOT / "community/CONTRIBUTING.md",
        ROOT / "docs/reports/REPO_AUDIT_2026-04-05.md",
    ]

    for path in markdown_files:
        lines = [line.strip() for line in path.read_text(encoding="utf-8").splitlines() if line.strip()]
        assert lines, f"{path.name} is empty"
        assert lines[0].startswith("#"), f"{path.name} should start with a markdown heading"


def test_claude_mentions_quality_workflows() -> None:
    claude_text = (ROOT / "CLAUDE.md").read_text(encoding="utf-8").lower()
    assert "tddaas-gates.yml" in claude_text
    assert "cgaas-gate.yml" in claude_text
