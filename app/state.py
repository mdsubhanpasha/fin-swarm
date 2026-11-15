from typing import TypedDict, List
class AuditState(TypedDict):
    user_query: str
    ledger_data: list
    anomalies: list
    compliance_issues: list
    final_report: str
    next_agent: str
    retry_count: int
