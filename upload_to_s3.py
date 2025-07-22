import boto3

# Replace with your actual bucket name
bucket_name = "cloud-etl-jide-001"  # Your actual S3 bucket name
file_path = "weather_dc.csv"        # The file you saved locally
s3_key = "weather_dc.csv"           # The name it will have in the cloud

# Connect to AWS S3
s3 = boto3.client("s3")

# Upload the file
try:
    s3.upload_file(file_path, bucket_name, s3_key)
    print("✅ File uploaded to AWS S3 successfully!")  # <-- Python code only goes here
except Exception as e:
    print("❌ Upload failed:", e)
