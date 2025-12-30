import boto3
from app.config import settings

s3_client = boto3.client(
    's3',
    aws_access_key_id=settings.aws_access_key_id,
    aws_secret_access_key=settings.aws_secret_access_key,
    region_name=settings.aws_region
)

def upload_file_to_s3(file_obj, key:str):
    s3_client.upload_fileobj(
        file_obj, 
        settings.s3_bucket_name, 
        key
        )