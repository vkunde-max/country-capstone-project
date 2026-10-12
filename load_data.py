from scraper import country_list
from database import CountryDatabaseManager

db = CountryDatabaseManager()

for country in country_list:
    db.insert_country(country)

print("20 countries inserted successfully!")