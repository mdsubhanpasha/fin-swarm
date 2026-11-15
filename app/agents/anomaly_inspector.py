import pandas as pd
import numpy as np
from sklearn.ensemble import IsolationForest

class AnomalyInspectorAgent:
    def __init__(self, contamination=0.05):
        self.model = IsolationForest(contamination=contamination, random_state=42)
        self.name = "Anomaly Inspector Agent"

    def detect_outliers(self, df: pd.DataFrame, amount_column: str = "amount") -> pd.DataFrame:
        """Applies Isolation Forest to detect fraudulent or anomalous ledger transactions."""
        if amount_column not in df.columns:
            raise ValueError(f"Column {amount_column} not found in dataframe.")
        
        X = df[[amount_column]].values
        self.model.fit(X)
        df["anomaly_score"] = self.model.decision_function(X)
        df["is_anomaly"] = self.model.predict(X)
        df["is_anomaly"] = df["is_anomaly"] == -1
        return df
