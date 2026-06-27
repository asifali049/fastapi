from fastapi import FastAPI

app = FastAPI(
    title="Hospital Management API",
    version="1.0.0",
    description="Hospital Management System Backend using FastAPI"
)

@app.get("/")
def home():
    return {
        "message": "Hospital API Running Successfully"
    }