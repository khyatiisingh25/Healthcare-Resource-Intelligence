# API Contract

## Base URL

/api/v1

---

## Facilities

### GET /facilities

Returns the list of healthcare facilities.

### POST /facilities

Creates a new healthcare facility.

---

## Inventory

### GET /inventory

Returns inventory records.

### POST /inventory

Adds or updates medicine inventory.

### GET /inventory/{inventory_id}

Returns a specific inventory record.

---

## Consumption

### POST /consumption

Records medicine consumption.

### GET /consumption/{medicine_id}

Returns consumption history for a medicine.

---

## Predictions

### GET /predictions/{medicine_id}

Returns shortage prediction for a medicine.

Example response:

{
  "medicine_id": 1,
  "shortage_risk": "HIGH",
  "predicted_shortage_days": 4,
  "recommended_restock_quantity": 150
}

---

## Emergency Requests

### POST /requests

Creates a resource requirement request.

### GET /requests

Returns emergency/resource requests.

### GET /requests/{request_id}

Returns a specific request.

---

## Resource Matching

### POST /matching/recommend

Finds and ranks potential resource sources.

Example response:

{
  "request_id": 1,
  "recommended_source": {
    "facility_id": 4,
    "facility_name": "Facility B",
    "available_quantity": 200,
    "recommended_transfer_quantity": 50
  },
  "reason": "Sufficient surplus and close distance"
}

---

## Blood

### GET /blood/inventory

Returns available blood inventory with last-updated information.

### POST /blood/requests

Creates an emergency blood request.

### GET /blood/matches/{request_id}

Returns potential blood sources.

---

## Important Rule

All APIs are currently designed for the internal hackathon prototype.

Data is synthetic/demo data unless explicitly verified.

Blood availability must include:

- Last updated timestamp
- Verification status

The system must not guarantee real-time availability.