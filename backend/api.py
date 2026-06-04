from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def home():
    return {
        "project": "Autonomous Data Engineer Agent Platform",
        "status": "Running"
    }