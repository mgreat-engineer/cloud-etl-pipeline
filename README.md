# Cloud ETL Pipeline – Weather Data to AWS S3

This project demonstrates how to build a simple, cloud-ready ETL (Extract, Transform, Load) pipeline using Python and AWS services.

---

## 🚀 Project Overview

I designed this pipeline to extract real-time weather data from a public API, clean and format the data using Python (Pandas), and upload the final output to an AWS S3 bucket for cloud storage.

---

## 🧠 Key Concepts Demonstrated

- **ETL Process**: Automating the full Extract → Transform → Load cycle
- **API Integration**: Fetching structured JSON data using Python’s `requests` library
- **Data Cleaning**: Using Pandas to organize and convert raw JSON into a tabular format
- **AWS Integration**: Uploading files to Amazon S3 using the Boto3 SDK
- **Cloud Readiness**: Preparing data for scalable, cloud-based storage and access

---

## 🔧 Tools & Technologies

- Python 3.14
- Pandas
- Requests
- AWS S3 (Simple Storage Service)
- Boto3 (AWS SDK for Python)
- VS Code

---

## 🧩 Files Included

| File | Description |
|------|-------------|
| `main.py` | Extracts weather data from an open API and saves it as a CSV |
| `upload_to_s3.py` | Uploads the CSV file to an AWS S3 bucket |
| `weather_dc.csv` | Sample output file with hourly weather data for Washington, DC |

---

## 📦 Sample Use Case

This type of pipeline is foundational in any cloud data stack. It’s the same structure used in:
- Daily weather feeds
- Marketing analytics imports
- Financial reporting pipelines
- Data warehousing jobs

---

## 📌 Outcome

Successfully tested the full pipeline:
- API data was cleaned and transformed locally
- Output saved in `.csv` format
- Final file uploaded to AWS S3 for cloud-based access

---

## 👨🏽‍💻 Author

**Michael Great**  
Cloud Data Engineer (Entry-Level)  
[GitHub Profile](https://github.com/your-username) | [LinkedIn](https://linkedin.com/in/your-profile)

---


