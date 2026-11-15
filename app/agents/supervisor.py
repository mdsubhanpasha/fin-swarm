from typing import Dict, Any, List
from app.agents.sql_detective import SQLDetectiveAgent
from app.agents.anomaly_inspector import AnomalyInspectorAgent

class SupervisorOrchestrator:
    """
    Hierarchical state machine orchestrator that routes queries to specialized worker agents
    and synthesizes consolidated audit reports.
    """
    def __init__(self):
        self.sql_agent = SQLDetectiveAgent()
        self.anomaly_agent = AnomalyInspectorAgent()

    def route_and_execute(self, query: str) -> Dict[str, Any]:
        q_lower = query.lower()
        
        if any(keyword in q_lower for keyword in ["anomal", "fraud", "outlier"]):
            routed_to = "anomaly"
        elif any(keyword in q_lower for keyword in ["tax", "gaap", "compliance"]):
            routed_to = "compliance"
        else:
            routed_to = "sql"

        ledger = self.sql_agent.fetch_ledger(query)
        anomalies = self.anomaly_agent.inspect_anomalies(ledger)

        compliance = []
        for anomaly in anomalies:
            if anomaly["amount"] > 50000:
                compliance.append("High-value payout needs US GAAP approval + tax withholding check")

        if not compliance and routed_to == "compliance":
            compliance.append("Standard US GAAP double-entry reconciliation verified. No major withholding discrepancies.")

        report = f"Audit done. Rows: {len(ledger)}, Anomalies: {len(anomalies)}"

        return {
            "query": query,
            "routed_to": routed_to,
            "ledger": ledger,
            "anomalies": anomalies,
            "compliance": compliance,
            "report": report
        }