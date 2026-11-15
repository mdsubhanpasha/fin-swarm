BANNED = ["DELETE","UPDATE","DROP","INSERT","ALTER","TRUNCATE"]
def validate_sql(sql):
    u = sql.upper()
    return not any(b in u for b in BANNED) and u.strip().startswith("SELECT")
def sql_detective_node(state):
    state["ledger_data"] = [
        {"id": 1, "vendor": "Acme Corp", "amount": 12500, "category": "vendor_payout"},
        {"id": 2, "vendor": "Acme Corp", "amount": 12500, "category": "vendor_payout"},
        {"id": 3, "vendor": "Globex", "amount": 99999, "category": "vendor_payout"},
    ]
    return state
