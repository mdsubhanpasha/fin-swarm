from typing import List, Dict, Any

class SQLDetectiveAgent:
    """
    Read-only Text-to-SQL general ledger inspector.
    Returns structured ledger transaction rows.
    """
    def __init__(self):
        self.name = "SQL Detective Agent"

    def fetch_ledger(self, query: str) -> List[Dict[str, Any]]:
        ledger_data = [
            {"id": 1, "vendor": "Acme Corp", "amount": 12500, "account": "2010-AP", "date": "2026-08-14"},
            {"id": 2, "vendor": "Acme Corp", "amount": 12500, "account": "2010-AP", "date": "2026-08-15"},
            {"id": 3, "vendor": "Globex", "amount": 99999, "account": "2020-Accrued", "date": "2026-09-02"}
        ]
        return ledger_data