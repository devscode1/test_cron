from fastapi import FastAPI
from datetime import datetime

app = FastAPI()

@app.on_event("startup")
async def startup_event():
    print(f"SERVER STARTED AT: {datetime.now()}")

@app.get("/")
def root():
    return {
        "status": "API is running",
        "timestamp": str(datetime.now())
    }

@app.get("/health")
def health():
    return {
        "status": "healthy",
        "server_time": str(datetime.now())
    }
