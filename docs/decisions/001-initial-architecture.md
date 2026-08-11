# 001 — Initial Architecture Decision

## Decision

The project will use a modular architecture consisting of:

- React frontend
- FastAPI backend
- PostgreSQL database
- Python-based AI/ML layer
- Resource matching and recommendation logic

## Reason

This architecture allows the team to develop frontend, backend, data/ML, and visualization components in parallel while keeping the system modular.

## Data

The internal hackathon prototype will use synthetic/demo healthcare data.

No real-time nationwide healthcare or blood-bank availability will be claimed.

## Human Verification

AI predictions and resource recommendations will support human decision-making rather than automatically making critical healthcare decisions.

## Status

Accepted