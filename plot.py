import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("exported_countries.csv")

plt.figure(figsize=(10, 6))

plt.scatter(
    df["population"],
    df["area"]
)

plt.title("Population vs Area")
plt.xlabel("Population")
plt.ylabel("Area")

plt.grid(True)

plt.savefig("population_vs_area.png")

plt.show()