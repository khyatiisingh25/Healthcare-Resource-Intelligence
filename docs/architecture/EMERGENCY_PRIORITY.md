# Emergency Priority Engine

## Purpose

The Emergency Priority Engine ranks emergency resource requests so that the most urgent requests can be handled first.

The initial prototype will use an explainable rule-based scoring system.

## Inputs

Each request may contain:

- Urgency level
- Required-by time
- Required quantity
- Resource availability
- Resource rarity
- Request status

## Priority Factors

The priority score considers:

- Urgency
- Time remaining
- Resource availability
- Resource rarity

## Initial Scoring

Each factor is normalized to a 0–100 range.

Initial weights:

- Urgency: 40%
- Time remaining: 30%
- Resource availability: 20%
- Resource rarity: 10%

Final Priority Score:

Priority Score =
    Urgency × 0.40
  + Time Remaining × 0.30
  + Availability × 0.20
  + Rarity × 0.10

Higher score = higher priority.

## Priority Levels

The system may classify requests as:

- CRITICAL
- HIGH
- MEDIUM
- LOW

## Ranking

Emergency requests are sorted by priority score in descending order.

Critical requests should appear first on the emergency dashboard.

## Example

A blood request required within 30 minutes with very limited available units should receive a higher priority than a non-urgent request required several hours later.

## Human Verification

The priority score is a decision-support mechanism.

Authorized healthcare personnel remain responsible for final prioritization and emergency action.

## MVP Scope

The initial prototype will use synthetic/demo data.

The engine will not make autonomous medical decisions.