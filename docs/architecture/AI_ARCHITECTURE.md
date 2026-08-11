# AI Architecture

## 1. AI Components

The platform contains two primary intelligence components:

1. Medicine Shortage Prediction
2. Resource Matching and Recommendation

---

## 2. Medicine Shortage Prediction

Medicine shortage prediction will use historical consumption and current inventory information to estimate future shortage risk.

### Input Features

- Current stock
- Historical consumption
- Average daily consumption
- Recent consumption trend
- Minimum stock level
- Safety stock
- Supplier lead time

### Outputs

- Predicted days until shortage
- Shortage risk
- Recommended restock quantity

### Initial Model

The initial prototype will use a supervised machine learning regression/classification approach using scikit-learn.

The exact model will be selected after evaluating the synthetic dataset.

Possible models include:

- Random Forest
- Gradient Boosting
- Linear Regression

A simple baseline model will be established before using a more complex model.

---

## 3. Shortage Risk

The system will classify shortage risk into:

- LOW
- MEDIUM
- HIGH
- CRITICAL

The classification will consider predicted shortage timing and safety stock requirements.

---

## 4. Restocking Recommendation

The recommended restocking quantity will consider:

- Expected consumption during lead time
- Safety stock
- Current inventory
- Expected future demand

The recommendation will be explainable rather than being a random ML output.

---

## 5. Resource Matching

Resource matching will use a rule-based scoring system rather than a machine learning model.

Candidate facilities will be ranked using:

- Resource availability
- Required quantity
- Distance
- Emergency urgency
- Facility safety stock
- Future demand

The system will return ranked candidate sources and an explanation for the recommendation.

---

## 6. Explainability

Every AI recommendation should provide understandable information about why it was generated.

Example:

"Facility B recommended because it has sufficient surplus stock, is 12 km away, and can fulfill the requested quantity without falling below its safety stock."

---

## 7. Human Decision Support

AI outputs are recommendations.

Final healthcare resource decisions remain with authorized human users.

The prototype must not autonomously make critical medical decisions.