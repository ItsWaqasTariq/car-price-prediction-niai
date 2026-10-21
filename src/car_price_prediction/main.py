from fastapi import FastAPI

app = FastAPI(
    title="Car Price Prediction API",
    description="API for the AI-Based Pakistani Car Price Prediction System",
    version="0.1.0",
)


@app.get("/health", tags=["Health"])
def health_check():
    return {"status": "ok"}