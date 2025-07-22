# Cloud ETL Pipeline – Weather Data to AWS S3

This project demonstrates how to build a simple, cloud-ready ETL (Extract, Transform, Load) pipeline using Python and AWS services.

## Project Overview

The pipeline extracts real-time weather data from a public API, transforms the raw JSON response using Python (Pandas), and loads the cleaned dataset into an AWS S3 bucket for cloud storage. This structure mimics real-world data workflows used by data engineering teams to automate ingestion and storage.

## Key Concepts Demonstrated

- Extracting structured data from a RESTful API
- Transforming raw JSON into tabular format using Pandas
- Saving cleaned data in CSV format
- Uploading files to Amazon S3 using the Boto3 SDK
- Managing access and credentials securely with AWS IAM and CLI

## Tools and Technologies

- Python 3.14
- Pandas
- Requests
- AWS S3 (Simple Storage Service)
- Boto3 (AWS SDK for Python)
- VS Code

## Files Included

| File               | Description                                                |
|--------------------|------------------------------------------------------------|
| `main.py`          | Extracts and transforms hourly weather data from the API   |
| `upload_to_s3.py`  | Uploads the final CSV file to an AWS S3 bucket             |
| `weather_dc.csv`   | Example output file showing hourly temperature in DC       |

## Use Case

This project simulates a foundational use case for cloud-based ETL pipelines. Similar patterns are used for:

- Ingesting and storing third-party API data
- Automating data collection in analytics platforms
- Feeding data warehouses like Amazon Redshift or BigQuery
- Supporting real-time reporting workflows

## Outcome

This project demonstrates a complete local-to-cloud pipeline. It successfully:

- Pulled data from a public API
- Cleaned and stored the data in CSV format
- Uploaded the file to a cloud environment (AWS S3) using Python

## Author

Michael Great  
Entry-Level Cloud Data Engineer  
GitHub: [https://github.com/your-username](https://github.com/your-username)  
LinkedIn: [https://linkedin.com/in/your-profile](https://linkedin.com/in/your-profile)
