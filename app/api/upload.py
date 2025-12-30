from fastapi import APIRouter, UploadFile, File
from app.services.s3_service import upload_file_to_s3
import uuid

router = APIRouter()

@router.post("/")
async def upload_document(file: UploadFile = File(...)):
    file_key = f"documents/{uuid.uuid4()}_{file.filename}"
    upload_file_to_s3(file.file, file_key)
    return {
        "message": "File uploaded successfully",
        "s3_key": file_key
    }
