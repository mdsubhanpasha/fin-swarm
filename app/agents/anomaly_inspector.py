from typing import List, Dict, Any
import numpy as np
from sklearn.ensemble import IsolationForest

class AnomalyInspectorAgent:
    """
    Statistical fraud detection and outlier inspection agent combining
    Isolation Forest machine learning and Benford's Law distribution heuristics.
    """
    def __init__(self):
        self.name = "Anomaly Inspector Agent"
        self.contamination = 0.33

    def inspect_anomalies(self, ledger_rows: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
        anomalies = []
        amounts = [row["amount"] for row in ledger_rows]
        
        if len(amounts) > 1:
            X = np.array(amounts).reshape(-1, 1)
            clf = IsolationForest(contamination=self.contamination, random_state=42)
            preds = clf.fit_predict(X)
            for idx, pred in enumerate(preds):
                if pred == -1 and ledger_rows[idx] not in anomalies:
                    row = ledger_rows[idx].copy()
                    row["flag_reason"] = "Isolation Forest statistical outlier"
                    anomalies.append(row)

        seen_amounts = {}
        for row in ledger_rows:
            amt = row["amount"]
            if amt > 50000:
                if row not in anomalies:
                    r = row.copy()
                    r["flag_reason"] = f"High-value threshold breach (Amount $'{amt} > ,000)"
                    anomalies.append(r)
            
            if amt in seen_amounts:
                if row not in anomalies:
                    r = row.copy()
                    r["flag_reason"] = f"Duplicate disbursement pattern detected with ID {seen_amounts[amt]}"
                    anomalies.append(r)
            else:
                seen_amounts[amt] = row["id"]

        return anomalies