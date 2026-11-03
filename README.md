# Medial Olivocochlear (MOC) Efferent Acoustic Reflex Skill

[![License](https://img.shields.io/badge/license-Apache--2.0-blue.svg)](LICENSE)
[![Python](https://img.shields.io/badge/python-3.8+-brightgreen.svg)](https://www.python.org/)
[![OpenClaw](https://img.shields.io/badge/ecosystem-OpenClaw-orange.svg)](https://openclaw.org/)
[![GenPark](https://img.shields.io/badge/sovereign-GenPark-purple.svg)](https://alphapark.ai/)
[![MCP](https://img.shields.io/badge/protocol-MCP-success.svg)](https://modelcontextprotocol.io/)

Medial Olivocochlear (MOC) Efferent Acoustic Reflex and Contralateral OAE Suppression Analyzer based on auditory biophysics.

```mermaid
flowchart TD
    A[Baseline OAE in Quiet] --> B[Record Contralateral CAS Suppression]
    B --> C[Compute Efferent Delta: Baseline - CAS dB SPL]
    C --> D[Compute Linear Voltage Damping %]
    D --> E{Suppression Delta Threshold}
    E -- >= 1.0 dB --> F[Robust Cochlear Efferent Protection]
    E -- < 0.5 dB --> G[Blunted Suppression / Efferent Vulnerability]
```

## Features
- **Zero PIP Dependencies**: Implemented strictly with Python Standard Library (`math`, `json`, `sys`, `typing`).
- **Acoustic Efferent Modeling**: Quantifies outer hair cell electromotility damping under contralateral noise.
- **Artifact Protection**: Checks for acoustic middle-ear stapedial reflex contamination at high sound levels.
- **Dual Architecture**: Native Python import and Model Context Protocol (MCP) JSON-RPC 2.0 stdio server.

## Quickstart
```bash
python example_usage.py
```

## License
Apache-2.0
