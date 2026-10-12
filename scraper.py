import requests
from bs4 import BeautifulSoup

url = "https://www.scrapethissite.com/pages/simple/"

response = requests.get(url)

soup = BeautifulSoup(response.text, "html.parser")

countries = soup.find_all("div", class_="country")[:20]

country_list = []

for country in countries:

    name = country.find(
        "h3",
        class_="country-name"
    ).text.strip()

    capital = country.find(
        "span",
        class_="country-capital"
    ).text.strip()

    population = int(
        country.find(
            "span",
            class_="country-population"
        ).text.strip()
    )

    area = float(
        country.find(
            "span",
            class_="country-area"
        ).text.strip()
    )

    country_list.append({
        "name": name,
        "capital": capital,
        "population": population,
        "area": area
    })

for country in country_list:
    print(country)
if __name__ == "__main__":
    for country in country_list:
        print(country)
