# Database Schema

## 1. Facility

Stores information about healthcare facilities.

Fields:

- id
- name
- facility_type
- address
- city
- latitude
- longitude
- contact_number
- created_at

Facility types may include:

- Hospital
- PHC
- CHC
- Blood Bank

---

## 2. Medicine

Stores information about medicines/resources.

Fields:

- id
- name
- category
- unit
- created_at

---

## 3. Inventory

Stores the current stock of a medicine at a facility.

Fields:

- id
- facility_id
- medicine_id
- current_stock
- minimum_stock
- safety_stock
- updated_at

---

## 4. Consumption History

Stores historical medicine consumption.

Fields:

- id
- facility_id
- medicine_id
- date
- quantity_consumed

---

## 5. Emergency Request

Stores requests for healthcare resources.

Fields:

- id
- requesting_facility_id
- medicine_id
- required_quantity
- urgency_level
- required_by
- status
- created_at

---

## 6. Resource Transfer

Stores resource transfer recommendations/actions between facilities.

Fields:

- id
- source_facility_id
- destination_facility_id
- medicine_id
- quantity
- status
- created_at

---

## 7. Blood Inventory

Stores blood availability information.

Fields:

- id
- facility_id
- blood_group
- available_units
- last_updated
- verification_status

---

## 8. Blood Request

Stores emergency blood requirements.

Fields:

- id
- requesting_facility_id
- blood_group
- required_units
- urgency_level
- required_by
- status
- created_at

---

## Important Data Rule

All data used during the internal hackathon prototype will be synthetic/demo data.

Blood availability must display:

- Last updated time
- Verification status

The system must not claim guaranteed real-time availability.