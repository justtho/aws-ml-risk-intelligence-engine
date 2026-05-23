import boto3
from aws.config import AWS_REGION, S3_BUCKET_NAME

s3 = boto3.client("s3", region_name=AWS_REGION)

def download_file_from_s3(s3_key, local_file_path):
    s3.download_file(S3_BUCKET_NAME, s3_key, local_file_path)
    return local_file_path