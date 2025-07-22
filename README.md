# ETL Pipeline: Weather Data to AWS S3

I built this project while learning how to work with APIs, clean up data using Python, and move it into AWS cloud storage. It's a basic but functional end-to-end ETL (Extract, Transform, Load) pipeline that uses public weather data and sends it to an S3 bucket.

The idea was to simulate the kind of small automation a data engineer might build to feed dashboards or prep data for analysis.

---

## What It Does

- Pulls weather data for Washington, DC using a free public API
- Converts that data from JSON into a clean table using pandas
- Saves the result to a local CSV file
- Uploads the CSV to an AWS S3 bucket using Boto3

Everything is done in Python and kept lightweight.

---

## Tech Used

- Python 3.14  
- pandas  
- requests  
- boto3  
- AWS S3 (Simple Storage Service)  
- VS Code  

---

## File Breakdown

| File | Purpose |
|------|---------|
| `main.py` | Extract and transform weather data from the API |
| `upload_to_s3.py` | Upload the cleaned CSV file to AWS S3 |
| `weather_dc.csv` | Final output file |

---

## Why I Made This

I'm learning to work with real-world data tools, especially cloud storage and automation. This small project helped me get hands-on with the core parts of a cloud data pipeline: connecting to APIs, processing data, and working with AWS.

It’s not a huge system, but it reflects how real pipelines work at a basic level.

---

## Notes

If I had more time, I’d:
- Set this up on a schedule using AWS Lambda or Airflow
- Write better error handling and logging
- Add support for more locations beyond just DC

---

## About Me

I'm Michael Great. I’m currently building up my skills in cloud data engineering and looking for an entry-level opportunity where I can grow on real-world projects like this one.

GitHub: [https://github.com/your-username](https://github.com/your-username)  
LinkedIn: [https://linkedin.com/in/your-profile](https://linkedin.com/in/your-profile)
