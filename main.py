import requests
import pandas as pd

# Step 1: Get weather forecast for Washington, DC using a public weather API
url = "https://api.open-meteo.com/v1/forecast?latitude=38.8951&longitude=-77.0364&hourly=temperature_2m"

response = requests.get(url)
data = response.json()

# Step 2: Extract hourly temperature data
hourly_data = data["hourly"]
df = pd.DataFrame(hourly_data)

# Step 3: Save to CSV
df.to_csv("weather_dc.csv", index=False)

print("✅ Weather data saved to weather_dc.csv")
