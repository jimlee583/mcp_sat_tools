# MCP Satellite Tools

This repository contains a **Model Context Protocol (MCP)** server implemented in Python that exposes satellite engineering tools for use by AI agents such as Cursor, ChatGPT, or custom MCP clients.

The intent is to provide **deterministic, structured engineering calculations** (power budgets, link budgets, etc.) that AI systems can call programmatically instead of estimating or hallucinating results.

---

## What This Repository Contains

- A local MCP server built with the MCP Python SDK
- Example MCP tools exposed as callable functions
- A demo client that connects to the server and calls tools
- A clean Python project layout suitable for expansion

Current tools:
- `add` – simple demo tool (sanity check)
- `compute_power_budget` – stub satellite power budget calculator

---

## Project Structure

mcp_sat_tools/
├── pyproject.toml
├── README.md
├── client.py
└── mcp_sat_tools/
├── init.py
├── server.py
└── tools/
├── init.py
├── demo_add.py
└── power_budget.py


---

## Requirements

- Python 3.10 or newer (tested with Python 3.13)
- Git
- Virtual environment support

---

## Setup

### Create and activate a virtual environment

```bash
python3 -m venv .venv

source .venv/bin/activate

git clone https://github.com/modelcontextprotocol/python-sdk.git
pip install ./python-sdk

python - << 'EOF'
from mcp.server.fastmcp import FastMCP
print("FastMCP imported OK")

python -m mcp_sat_tools.server

http://localhost:8000/mcp

python client.py


EOF
