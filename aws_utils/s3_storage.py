from aws_utils.s3_client import get_s3_client
from aws_utils.config import S3_BUCKET_NAME

def upload_file(local_path, s3_key):
    s3 = get_s3_client()
    s3.upload_file(local_path, S3_BUCKET_NAME, s3_key)
    return f"s3://{S3_BUCKET_NAME}/{s3_key}"

def download_file(s3_key, local_path):
    s3 = get_s3_client()
    s3.download_file(S3_BUCKET_NAME, s3_key, local_path)
    return local_path

def list_files(prefix=""):
    s3 = get_s3_client()
    response = s3.list_objects_v2(
        Bucket=S3_BUCKET_NAME,
        Prefix=prefix
    )

    if "Contents" not in response:
        return []

    return [item["Key"] for item in response["Contents"]]