# FIN-SWARM
### Autonomous Multi-Agent Financial Forensics & Regulatory Compliance Engine

> One Prompt -> Full Audit. Supervisor Agent -> SQL Detective -> Anomaly Investigator -> Compliance Agent -> Executive Report.

**Problem:** Enterprise audits take weeks. Manual ledger checks miss fraud.
**Solution:** FIN-SWARM audits ledgers autonomously.

### Architecture
User Query -> Supervisor -> [SQL Detective, Anomaly, Compliance] -> Reporter -> Executive Report

### Features
- Self-Correcting SQL Agent
- Benfords Law + Isolation Forest Fraud Detection
- Read-Only Guardrails - No DELETE / UPDATE / DROP
- LangGraph Checkpointing
- Live Streaming via FastAPI

### Tech Stack
LangGraph | Groq Llama-3-70B | PostgreSQL + pgvector | FastAPI | Docker Compose | Redis

### Quick Start
docker compose up --build
POST /audit {"query": "Audit Q3 ledger for anomalous vendor payouts"}
