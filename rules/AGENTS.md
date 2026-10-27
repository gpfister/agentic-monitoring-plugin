# Monitoring Guidelines & Standards — agentic-monitoring-plugin

This rule set applies whenever the `agentic-monitoring-plugin` is active in an Antigravity session.

---

## 1. Stream Surveillance & Safety
- **Non-Destructive Observation**: Monitoring workers must strictly perform read/tail operations on target streams. Do not kill or alter target processes unless explicitly requested by the user during a pause gate.
- **Buffer & Resource Management**: Guard against unbound in-memory buffering when tailing high-throughput log streams. Process logs in bounded windows.

---

## 2. Interactive Pause Gate Protocol
- When an anomaly or error is detected:
  1. Halt surveillance immediately to prevent log cascading.
  2. Synthesize an actionable `MonitoringAlert` capturing the root error and stack trace.
  3. Prompt the user with specific, actionable remediation choices via `ask_question`.

---

## 3. Communication & Links
- Keep alert summaries high-signal and concise.
- Always provide clickable markdown links using the `file://` scheme when referencing local log files, configuration paths, or source files implicated in stack traces.
