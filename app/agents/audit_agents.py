def anomaly_node(state):
    data = state.get("ledger_data", [])
    state["anomalies"] = [d for d in data if d["amount"] > 50000]
    return state
def compliance_node(state):
    issues = []
    if state.get("anomalies"):
        issues.append("High-value payout needs US GAAP approval + tax withholding check")
    state["compliance_issues"] = issues
    state["final_report"] = f"Audit done. Rows: {len(state.get('ledger_data',[]))}, Anomalies: {len(state.get('anomalies',[]))}, Issues: {issues}"
    return state
