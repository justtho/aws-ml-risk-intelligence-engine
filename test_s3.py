from aws_utils.s3_storage import upload_file, list_files

uploaded_path = upload_file(
    "data/sample_cases.csv",
    "datasets/sample_cases.csv"
)

print("Uploaded to:", uploaded_path)

print("Files in bucket:")
print(list_files())