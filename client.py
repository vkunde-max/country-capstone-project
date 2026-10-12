import requests
import pandas as pd

response = requests.get(
    "http://127.0.0.1:8000/countries"
)

data = response.json()

df = pd.DataFrame(
    data,
    columns=[
        "name",
        "capital",
        "population",
        "area"
    ]
)

print(df)

df.to_csv(
    "exported_countries.csv",
    index=False
)

print("CSV Exported Successfully")