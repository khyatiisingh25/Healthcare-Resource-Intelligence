# Frontend Architecture

## 1. Technology

- React
- JavaScript/TypeScript
- REST API integration
- Responsive dashboard UI

## 2. Main Screens

### Dashboard

Shows:

- Total facilities
- Medicine shortage alerts
- Critical emergency requests
- Blood/resource alerts
- Recent resource transfers

### Inventory

Shows:

- Facility inventory
- Medicine stock
- Minimum stock
- Safety stock
- Stock status
- Predicted shortage risk

### Shortage Predictions

Shows:

- Medicine
- Facility
- Predicted days until shortage
- Risk level
- Recommended restock quantity

### Emergency Requests

Shows:

- Request ID
- Facility
- Resource
- Required quantity
- Urgency
- Required-by time
- Status

### Resource Matching

Shows:

- Request details
- Recommended source facility
- Available quantity
- Distance
- Matching score
- Alternative facilities
- Recommendation explanation

### Blood Emergency

Shows:

- Blood group
- Required units
- Potential sources
- Available units
- Distance
- Last updated time
- Verification status

## 3. Frontend Flow

```text
Dashboard
    ↓
User selects module
    ↓
React component
    ↓
API request
    ↓
FastAPI backend
    ↓
API response
    ↓
UI update