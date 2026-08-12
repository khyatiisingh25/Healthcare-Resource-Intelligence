"""
Post-processing for medicine shortage prediction.

Converts the model's predicted shortage timing into:
- shortage risk
- recommended restock quantity
"""

from typing import Dict


def classify_shortage_risk(
    predicted_days_until_shortage: float,
    lead_time_days: float,
) -> str:
    """
    Classify shortage risk based on predicted shortage timing.

    Risk levels:
    - CRITICAL: shortage expected within lead time
    - HIGH: shortage expected within 7 days
    - MEDIUM: shortage expected within 14 days
    - LOW: shortage expected after 14 days
    """

    if predicted_days_until_shortage <= lead_time_days:
        return "CRITICAL"

    if predicted_days_until_shortage <= 7:
        return "HIGH"

    if predicted_days_until_shortage <= 14:
        return "MEDIUM"

    return "LOW"


def calculate_restock_quantity(
    current_stock: float,
    avg_daily_consumption: float,
    lead_time_days: float,
    safety_stock: float,
) -> int:
    """
    Calculate a basic recommended restock quantity.

    The recommendation covers expected consumption during supplier
    lead time while maintaining the required safety stock.
    """

    lead_time_demand = avg_daily_consumption * lead_time_days

    required_stock = lead_time_demand + safety_stock

    restock_quantity = required_stock - current_stock

    return max(0, round(restock_quantity))


def build_prediction_output(
    facility_id: int,
    medicine_id: int,
    predicted_days_until_shortage: float,
    current_stock: float,
    avg_daily_consumption: float,
    lead_time_days: float,
    safety_stock: float,
) -> Dict:
    """
    Build the final standardized shortage prediction response.
    """

    shortage_risk = classify_shortage_risk(
        predicted_days_until_shortage,
        lead_time_days,
    )

    recommended_restock_quantity = calculate_restock_quantity(
        current_stock,
        avg_daily_consumption,
        lead_time_days,
        safety_stock,
    )

    return {
        "facility_id": facility_id,
        "medicine_id": medicine_id,
        "predicted_days_until_shortage": round(
            predicted_days_until_shortage, 2
        ),
        "shortage_risk": shortage_risk,
        "recommended_restock_quantity": recommended_restock_quantity,
    }