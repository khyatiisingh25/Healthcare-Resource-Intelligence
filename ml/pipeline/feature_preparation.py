"""
Feature preparation for the medicine shortage prediction pipeline.

This module converts inventory and consumption data into the
features expected by the shortage prediction model.
"""

from typing import Any, Dict


REQUIRED_FEATURES = [
    "current_stock",
    "minimum_stock",
    "safety_stock",
    "avg_daily_consumption",
    "recent_consumption_trend",
    "lead_time_days",
    "historical_consumption",
]


def prepare_features(data: Dict[str, Any]) -> Dict[str, float]:
    """
    Prepare model-ready features from inventory and consumption data.

    Parameters
    ----------
    data : dict
        Raw inventory and consumption information.

    Returns
    -------
    dict
        Features required by the shortage prediction model.

    Raises
    ------
    ValueError
        If a required feature is missing or invalid.
    """

    missing_features = [
        feature for feature in REQUIRED_FEATURES if feature not in data
    ]

    if missing_features:
        raise ValueError(
            f"Missing required features: {', '.join(missing_features)}"
        )

    features = {}

    for feature in REQUIRED_FEATURES:
        value = data[feature]

        if value is None:
            raise ValueError(f"Feature '{feature}' cannot be None.")

        try:
            features[feature] = float(value)
        except (TypeError, ValueError):
            raise ValueError(
                f"Feature '{feature}' must contain a numeric value."
            )

        if features[feature] < 0:
            raise ValueError(
                f"Feature '{feature}' cannot be negative."
            )

    return features