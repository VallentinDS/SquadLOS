import boto3
import os

s3 = boto3.client("s3")
bucket_name = "squadlos.com"
logs_folder = "logs"
local_folder = "logs"

response = s3.list_objects_v2(Bucket=bucket_name, Prefix=logs_folder)

for obj in response.get("Contents", []):
    # Skip first object which is the folder itself
    if obj["Key"] == logs_folder + "/":
        continue
    file_key = obj["Key"]
    file_name = os.path.basename(file_key)
    local_file_path = os.path.join(local_folder, file_name)
    s3.download_file(bucket_name, file_key, local_file_path)
    print(f"Downloaded {file_name} to {local_file_path}")
