"""
Medicine shortage prediction pipeline.

This module connects:
1. Feature preparation
2. ML model prediction
3. Prediction post-processing

The actual trained model will be connected later.
"""

from typing import Any, Dict

from .feature_preparation import prepare_features
from .postprocessing import build_prediction_output


class ShortagePredictionPipeline:
    """
    Pipeline for generating medicine shortage predictions.
    """

    def __init__(self, model: Any = None):
        """
        Initialize the pipeline.

        Parameters
        ----------
        model : object, optional
            Trained ML model.

            This is intentionally optional because the trained model
            will be provided by the ML development stage later.
        """
        self.model = model

    def predict(self, data: Dict[str, Any]) -> Dict[str, Any]:
        """
        Generate a shortage prediction.

        Parameters
        ----------
        data : dict
            Inventory and consumption information.

        Returns
        -------
        dict
            Standardized shortage prediction output.
        """

        if self.model is None:
            raise RuntimeError(
                "No trained ML model is connected to the pipeline yet."
            )

        features = prepare_features(data)

        # Keep feature order consistent with the model specification.
        feature_values = [
            features["current_stock"],
            features["minimum_stock"],
            features["safety_stock"],
            features["avg_daily_consumption"],
            features["recent_consumption_trend"],
            features["lead_time_days"],
            features["historical_consumption"],
        ]

        predicted_days_until_shortage = self.model.predict(
            [feature_values]
        )[0]

        return build_prediction_output(
            facility_id=int(data["facility_id"]),
            medicine_id=int(data["medicine_id"]),
            predicted_days_until_shortage=float(
                predicted_days_until_shortage
            ),
            current_stock=features["current_stock"],
            avg_daily_consumption=features["avg_daily_consumption"],
            lead_time_days=features["lead_time_days"],
            safety_stock=features["safety_stock"],
        )