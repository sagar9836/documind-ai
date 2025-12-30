from pydantic import BaseModel
from dotenv import load_dotenv
import os

load_dotenv()

class Settings(BaseModel):
    aws_access_key_id: str = os.getenv("AWS_ACCESS_KEY_ID")
    aws_secret_access_key: str = os.getenv("AWS_SECRET_ACCESS_KEY")
    aws_region: str = os.getenv("AWS_REGION")
    s3_bucket_name: str = os.getenv("S3_BUCKET_NAME")

settings = Settings()
