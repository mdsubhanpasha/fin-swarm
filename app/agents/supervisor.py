def supervisor_route(state):
    q = state.get("user_query","").lower()
    if "anomal" in q or "fraud" in q:
        return "anomaly"
    if "compliance" in q or "tax" in q:
        return "compliance"
    return "sql"
def supervisor_node(state):
    state["next_agent"] = supervisor_route(state)
    return state
