from ml.pipeline.feature_preparation import prepare_features
from ml.pipeline.postprocessing import (
    classify_shortage_risk,
    calculate_restock_quantity,
)


def test_prepare_features():
    data = {
        "current_stock": 500,
        "minimum_stock": 100,
        "safety_stock": 150,
        "avg_daily_consumption": 50,
        "recent_consumption_trend": 0.10,
        "lead_time_days": 5,
        "historical_consumption": 45,
    }

    features = prepare_features(data)

    assert features["current_stock"] == 500.0
    assert features["avg_daily_consumption"] == 50.0


def test_shortage_risk():
    assert classify_shortage_risk(3, 5) == "CRITICAL"
    assert classify_shortage_risk(6, 5) == "HIGH"
    assert classify_shortage_risk(10, 5) == "MEDIUM"
    assert classify_shortage_risk(20, 5) == "LOW"


def test_restock_quantity():
    quantity = calculate_restock_quantity(
        current_stock=100,
        avg_daily_consumption=50,
        lead_time_days=5,
        safety_stock=100,
    )

    assert quantity == 250