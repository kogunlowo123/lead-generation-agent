# Lead Generation Agent

[![CI](https://github.com/kogunlowo123/lead-generation-agent/actions/workflows/ci.yml/badge.svg)](https://github.com/kogunlowo123/lead-generation-agent/actions/workflows/ci.yml)
[![Python 3.11+](https://img.shields.io/badge/python-3.11+-blue.svg)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](https://opensource.org/licenses/MIT)

> **Category**: Sales | **Cloud**: MULTI-CLOUD | **LLM**: gpt-4o

Lead generation agent that identifies potential customers from multiple data sources, scores leads by fit and intent, enriches contact data, and feeds qualified leads into the sales pipeline.

---

## Domain-Specific Tools

| Tool | Description |
|------|-------------|
| `search_prospects` | Search for potential leads matching ideal customer profile |
| `score_lead` | Score a lead based on firmographic, technographic, and intent data |
| `enrich_contact` | Enrich lead contact data with verified email, phone, and social profiles |
| `qualify_lead` | Qualify lead against BANT or MEDDIC framework |
| `add_to_pipeline` | Add a qualified lead to the sales pipeline |

## API Endpoints

| Method | Path | Description |
|--------|------|-------------|
| `POST` | `/api/v1/lead-generation/execute` | Execute primary action |
| `POST` | `/api/v1/lead-generation/analyze` | Run analysis |
| `GET` | `/api/v1/lead-generation/metrics` | Get metrics |
| `PUT` | `/api/v1/lead-generation/configure` | Configure settings |
| `POST` | `/api/v1/lead-generation/report` | Generate report |

## Features

- Lead
- Generation
- Analytics
- Automation

## Integrations

- Salesforce
- Hubspot
- Outreach
- Apollo
- Linkedin Sales Navigator

## Architecture

```
lead-generation-agent/
├── src/
│   ├── agent/              # Domain-specific agent logic
│   │   ├── lead_generation_agent_agent.py  # Main agent with domain tools
│   │   ├── tools.py        # 5 domain-specific tools
│   │   └── prompts.py      # Expert system prompts
│   ├── api/                # FastAPI routes
│   │   └── routes/
│   │       ├── domain.py   # 5 domain-specific endpoints
│   │       └── health.py   # Health check
│   ├── connectors/         # 5 integration connectors
│   ├── config/             # Settings and configuration
│   ├── models/             # Domain-specific Pydantic schemas
│   ├── rag/                # RAG pipeline
│   ├── mcp/                # MCP server
│   └── a2a/                # Agent-to-agent protocol
├── tests/
├── infrastructure/         # Terraform, K8s, Helm, Docker
├── dashboard/              # Next.js frontend
└── docs/                   # Architecture and deployment docs
```

## Quick Start

```bash
# Install
pip install -e ".[dev]"

# Run
make dev

# Test
make test

# Docker
docker compose up -d
```

## Primary Service

**CRM + Sales Engagement + LLM**

---

Built as part of the Enterprise AI Agent Platform.
