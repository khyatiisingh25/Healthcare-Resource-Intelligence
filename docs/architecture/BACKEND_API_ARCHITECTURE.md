# Backend API Architecture

## Purpose

The backend provides REST APIs connecting the React frontend, PostgreSQL database, AI/ML services, and resource coordination logic.

## Backend Layers

```text
React Frontend
      ↓
FastAPI Routes
      ↓
Service Layer
      ↓
AI / Matching / Priority Services
      ↓
Database Layer
      ↓
PostgreSQL