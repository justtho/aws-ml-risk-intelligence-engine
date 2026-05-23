import boto3
from aws.config import AWS_REGION, S3_BUCKET_NAME

s3 = boto3.client("s3", region_name=AWS_REGION)

def upload_file_to_s3(local_file_path, s3_key):
    s3.upload_file(local_file_path, S3_BUCKET_NAME, s3_key)
    return f"s3://{S3_BUCKET_NAME}/{s3_key}"