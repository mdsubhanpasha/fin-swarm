from http.server import HTTPServer, BaseHTTPRequestHandler
import json
import urllib.parse
from app.agents.supervisor import SupervisorOrchestrator

orchestrator = SupervisorOrchestrator()

class FinSwarmHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path == "/health" or self.path == "/":
            response = {
                "status": "operational",
                "engine": "FIN-SWARM Multi-Agent Swarm (Pure Python Enterprise Core)",
                "copyright": "© 2026 Mohammad Subhan Pasha. All Rights Reserved."
            }
            self.send_response(200)
            self.send_header("Content-Type", "application/json")
            self.end_headers()
            self.wfile.write(json.dumps(response).encode("utf-8"))
        else:
            self.send_response(404)
            self.end_headers()

    def do_POST(self):
        if self.path == "/audit":
            content_length = int(self.headers.get('Content-Length', 0))
            post_data = self.rfile.read(content_length)
            try:
                data = json.loads(post_data.decode("utf-8"))
                query = data.get("query", "Audit Q3 ledger for anomalous vendor payouts")
                result = orchestrator.route_and_execute(query)
                
                self.send_response(200)
                self.send_header("Content-Type", "application/json")
                self.end_headers()
                self.wfile.write(json.dumps(result).encode("utf-8"))
            except Exception as e:
                error_resp = {"error": str(e)}
                self.send_response(500)
                self.send_header("Content-Type", "application/json")
                self.end_headers()
                self.wfile.write(json.dumps(error_resp).encode("utf-8"))
        else:
            self.send_response(404)
            self.end_headers()

def run(server_class=HTTPServer, handler_class=FinSwarmHandler, port=8000):
    server_address = ('', port)
    httpd = server_class(server_address, handler_class)
    print(f"FIN-SWARM Enterprise Engine running on port {port}...")
    httpd.serve_forever()

if __name__ == "__main__":
    run()