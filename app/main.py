from fastapi import FastAPI
from app.api import upload

app = FastAPI(
    title="DocuMind AI",
    description="Upload documents. Ask questions. Get grounded answers.",
    version="0.1.0"
)

app.include_router(
    upload.router,
    prefix="/upload",
    tags=["Upload"]
)

@app.get("/")
def health_check():
    return {"status": "DocuMind AI backend running"}
