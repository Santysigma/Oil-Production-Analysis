import pandas as pd

url = "https://ourworldindata.org/grapher/oil-production-by-country.csv?v=1&csvType=full&useColumnShortNames=true"

df = pd.read_csv(url, storage_options={'User-Agent': 'Our World In Data data fetch/1.0'})

print(df.shape)
print(df.head())
print(df.columns)
world = df[df["entity"] == "World"]

import matplotlib.pyplot as plt

plt.plot(world["year"], world["oil_production_twh"])
plt.title("Global Oil Production Over Time")
plt.xlabel("Year")
plt.ylabel("Oil Production (TWh)")
plt.savefig("global_oil_production.png")
plt.show()