from fastapi import FastAPI

app = FastAPI(
    title="DocuMind AI",
    description="Upload documents. Ask questions. Get grounded answers.",
    version="0.1.0"
)

@app.get("/")
def health_check():
    return {"status": "DocuMind AI backend running"}
