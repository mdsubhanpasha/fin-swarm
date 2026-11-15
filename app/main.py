from fastapi import FastAPI
app = FastAPI(title="FIN-SWARM")
@app.get("/health")
def health():
    return {"status": "healthy", "architecture": "FIN-SWARM Multi-Agent Engine Active"}
@app.get("/")
def root():
    return {"message": "FIN-SWARM is running. POST /audit to start audit."}
