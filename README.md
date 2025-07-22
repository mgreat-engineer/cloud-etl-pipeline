# Cloud ETL Project: Weather Data to AWS S3

This project demonstrates a simple **ETL pipeline** using Python, public APIs, and Amazon Web Services (AWS).

### 🔧 Tools Used:
- Python 3.14
- Pandas
- Requests
- AWS S3
- Boto3 (AWS SDK for Python)

### 📈 What the Pipeline Does:
1. **Extract** – Pulls hourly weather data from a public API (Open-Meteo)
2. **Transform** – Cleans and structures the data into a Pandas DataFrame
3. **Load** – Saves the data to a CSV file and uploads it to an AWS S3 bucket

### 📁 Files in This Project:
- `main.py`: Extracts and transforms the data
- `upload_to_s3.py`: Uploads the final file to AWS S3
- `weather_dc.csv`: Example output data

✅ This is a foundational project for entry-level **Cloud Data Engineer** roles.
