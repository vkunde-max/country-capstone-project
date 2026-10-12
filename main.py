from fastapi import FastAPI
from database import CountryDatabaseManager

app = FastAPI()

db = CountryDatabaseManager()

@app.get("/")
def home():
    return {"message": "Country API Running"}

@app.get("/countries")
def get_all_countries():
    return db.get_all_countries()

@app.get("/countries/{country_name}")
def get_country(country_name: str):
    return db.get_country(country_name)