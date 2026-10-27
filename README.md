# agentic-monitoring-plugin

Telemetry, stream surveillance, and log monitoring companion plugin for [Google Antigravity](https://antigravity.google).

## Overview
`agentic-monitoring-plugin` provides dedicated subagents and progressive-disclosure skills to watch application logs, Docker containers, and serial ports (`/dev/tty*`) continuously in the background. It intercepts errors and crashes early with interactive pause gates.

## Features
- **Declarative Subagent (`@monitoring`)**: Background streaming worker defined in [`agents/monitoring/agent.md`](file:///Users/gpfister/Development/Projects/gpfister/agentic/agentic-monitoring-plugin/agents/monitoring/agent.md).
- **Progressive Skill (`monitoring`)**: Surveillance runbook and trigger instructions in [`skills/monitoring/SKILL.md`](file:///Users/gpfister/Development/Projects/gpfister/agentic/agentic-monitoring-plugin/skills/monitoring/SKILL.md).
- **Interactive Anomaly Gate**: Immediately halts log cascading and queries the user via Antigravity's `ask_question` tool.
- **Rules (`rules/AGENTS.md`)**: Enforces safe log streaming, bounded buffers, and clean formatting.

## Installation & Activation

```bash
# Enable in Antigravity session:
agy plugin enable agentic-monitoring-plugin
```

## Contributing
See [CONTRIBUTING.md](file:///Users/gpfister/Development/Projects/gpfister/agentic/agentic-monitoring-plugin/CONTRIBUTING.md) for contribution guidelines and testing practices.

## License
This project is licensed under the [MIT License](file:///Users/gpfister/Development/Projects/gpfister/agentic/agentic-monitoring-plugin/LICENSE).
