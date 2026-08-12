# Resource Matching Engine

## Purpose

The Resource Matching Engine identifies and ranks healthcare facilities that can provide a requested medicine or resource.

The engine uses an explainable rule-based scoring system.

It does not use machine learning in the initial prototype.

## Inputs

The engine receives:

- Requesting facility
- Resource/medicine
- Required quantity
- Emergency urgency
- Required-by time

For each candidate facility:

- Available stock
- Safety stock
- Distance from requesting facility
- Estimated future demand
- Facility status

## Candidate Filtering

A facility should first pass basic eligibility checks.

A candidate is considered eligible when:

1. The required resource is available.
2. Available stock is greater than or equal to the requested quantity.
3. The transfer will not reduce stock below the facility's safety stock.
4. The facility is active/available.

Only eligible facilities proceed to scoring.

## Scoring Factors

Each eligible facility receives a score based on:

- Availability
- Surplus stock
- Distance
- Emergency urgency
- Future stock safety

Higher score = better candidate.

## Initial Scoring Model

The prototype will use a weighted score:

Final Score =
    Availability Score × 0.30
  + Surplus Score × 0.25
  + Distance Score × 0.20
  + Urgency Score × 0.15
  + Safety Score × 0.10

All component scores should be normalized to a 0–100 range.

## Ranking

Candidate facilities are sorted by Final Score in descending order.

The system returns:

- Ranked candidates
- Recommended source
- Recommended transfer quantity
- Score
- Explanation

## Example Explanation

"Facility B is recommended because it has sufficient surplus stock, is located close to the requesting facility, and can fulfill the request without falling below its safety stock."

## Human Verification

The recommendation is a decision-support output.

A human user must verify resource availability before initiating a transfer.

## Future Improvements

The matching engine may later incorporate:

- Real-time verified inventory
- Travel time
- Road conditions
- Facility capacity
- Multiple-resource optimization
- More advanced optimization algorithms

These are outside the initial MVP scope.
