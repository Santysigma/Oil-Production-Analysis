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
plt.close()

price_url = "https://ourworldindata.org/grapher/crude-oil-prices.csv?v=1&csvType=full&useColumnShortNames=true"
price_df = pd.read_csv(price_url, storage_options={'User-Agent': 'Our World In Data data fetch/1.0'})

print(price_df.shape)
print(price_df.head())
print(price_df.columns)

merged = pd.merge(world, price_df, on="year", suffixes=("_production", "_price"))
print(merged.shape)
print(merged.head())
print(merged.tail())

fig, ax1 = plt.subplots()

ax1.plot(merged["year"], merged["oil_production_twh"], color="tab:blue")
ax1.set_xlabel("Year")
ax1.set_ylabel("Oil Production (TWh)", color="tab:blue")

ax2 = ax1.twinx()
ax2.plot(merged["year"], merged["oil_price_crude_current_dollars_per_m3"], color="tab:red")
ax2.set_ylabel("Oil Price ($ per m³)", color="tab:red")

plt.title("Global Oil Production vs. Price (1900-2025)")
plt.savefig("production_vs_price.png")
plt.close()