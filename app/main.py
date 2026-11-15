import sys, os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from http.server import BaseHTTPRequestHandler, HTTPServer
import json
from app.agents.supervisor import supervisor_node
from app.agents.sql_detective import sql_detective_node
from app.agents.audit_agents import anomaly_node, compliance_node
class H(BaseHTTPRequestHandler):
    def _send(self, data):
        b = json.dumps(data).encode()
        self.send_response(200)
        self.send_header("Content-Type", "application/json")
        self.send_header("Content-Length", str(len(b)))
        self.end_headers()
        self.wfile.write(b)
    def log_message(self, *a):
        pass
    def do_GET(self):
        if self.path == "/health":
            self._send({"status": "healthy", "architecture": "FIN-SWARM Multi-Agent Engine Active"})
        else:
            self._send({"message": "FIN-SWARM is running. POST /audit to start audit."})
    def do_POST(self):
        n = int(self.headers.get("Content-Length", 0))
        body = json.loads(self.rfile.read(n).decode() or "{}")
        q = body.get("query", "")
        state = {"user_query": q, "ledger_data": [], "anomalies": [], "compliance_issues": [], "final_report": "", "next_agent": "", "retry_count": 0}
        state = supervisor_node(state)
        state = sql_detective_node(state)
        state = anomaly_node(state)
        state = compliance_node(state)
        self._send({"query": q, "routed_to": state["next_agent"], "ledger": state["ledger_data"], "anomalies": state["anomalies"], "compliance": state["compliance_issues"], "report": state["final_report"]})
if __name__ == "__main__":
    print("FIN-SWARM running on http://127.0.0.1:8000")
    HTTPServer(("127.0.0.1", 8000), H).serve_forever()
