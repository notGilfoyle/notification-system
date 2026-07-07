from fastapi import FastAPI

app = FastAPI(title="Notification Service")


@app.get("/")
def health():
    return {
        "service": "Notification System",
        "status": "running"
    }