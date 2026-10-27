"""Tests for agentic-monitoring-plugin structure and specifications."""

import json
from pathlib import Path

PLUGIN_ROOT = Path(__file__).resolve().parent.parent


def test_plugin_manifest_valid():
    manifest_file = PLUGIN_ROOT / "plugin.json"
    assert manifest_file.exists(), "plugin.json must exist"
    data = json.loads(manifest_file.read_text(encoding="utf-8"))
    assert data.get("name") == "agentic-monitoring-plugin"
    assert data.get("license") == "MIT"


def test_license_exists():
    license_file = PLUGIN_ROOT / "LICENSE"
    assert license_file.exists(), "LICENSE must exist"
    content = license_file.read_text(encoding="utf-8")
    assert "MIT License" in content
    assert "Greg PFISTER" in content


def test_contributing_exists():
    contrib_file = PLUGIN_ROOT / "CONTRIBUTING.md"
    assert contrib_file.exists(), "CONTRIBUTING.md must exist"
    content = contrib_file.read_text(encoding="utf-8")
    assert "agentic-monitoring-plugin" in content


def test_monitoring_agent_exists():
    agent_file = PLUGIN_ROOT / "agents" / "monitoring" / "agent.md"
    assert agent_file.exists(), "agents/monitoring/agent.md must exist"
    content = agent_file.read_text(encoding="utf-8")
    assert "name: monitoring" in content
    assert "Telemetry Monitor" in content


def test_central_agent_guide_exists():
    central_file = PLUGIN_ROOT / "agents" / "agent.md"
    assert central_file.exists(), "agents/agent.md must exist"
    content = central_file.read_text(encoding="utf-8")
    assert "name: agent" in content
    assert "Monitoring Subagents" in content


def test_monitoring_skill_exists():
    skill_file = PLUGIN_ROOT / "skills" / "monitoring" / "SKILL.md"
    assert skill_file.exists(), "skills/monitoring/SKILL.md must exist"
    content = skill_file.read_text(encoding="utf-8")
    assert "name: monitoring" in content
    assert "Intervention Gate" in content


def test_rules_exist():
    rules_file = PLUGIN_ROOT / "rules" / "AGENTS.md"
    assert rules_file.exists(), "rules/AGENTS.md must exist"
    content = rules_file.read_text(encoding="utf-8")
    assert "Monitoring Guidelines" in content
