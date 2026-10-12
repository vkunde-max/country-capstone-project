from database import CountryDatabaseManager

db = CountryDatabaseManager()

print("All Countries:")
print(db.get_all_countries())

print("\nOne Country:")
print(db.get_country("India"))

from database import CountryDatabaseManager

db = CountryDatabaseManager()

print(db.get_country("Andorra"))