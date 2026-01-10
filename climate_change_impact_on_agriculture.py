import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load Your Dataset
df = pd.read_csv("climate_change_impact_on_agriculture_2024.csv")

# Display first few rows
print(df.head())

# Get basic info about the dataset
print(df.info())

# Summary statistics
print(df.describe())

# Basic Cleaning (if needed)

# Remove spaces and make column names lowercase
df.columns = df.columns.str.strip().str.lower()

# Check for missing data
print(df.isnull().sum())

# Fill missing numeric values (if any) wthcolumn mean
df.fillna(df.mean(numeric_only=True), inplace=True)

# Explore General Climate Trends

# Temperatue Over Time
plt.figure(figsize=(10,6))
sns.lineplot(data=df, x="year", y="average_temperature_c")
plt.title("Average Temperature Over Time")
plt.xlabel("Year")
plt.ylabel("Temperature ( ̊ C)")
plt.show()

# Precipitation Over Time
plt.figure(figsize=(10,6))
sns.lineplot(data=df, x="year", y="total_precipitation_mm")
plt.title("Precipitation Trends Over Years")
plt.xlabel("Year")
plt.ylabel("Total Precipitation (mm)")
plt.show()

# Relationship Between Climate and Crop Yield

# Temperature vs. Crop Yield
plt.figure(figsize=(8,6))
sns.scatterplot(data=df, x="average_temperature_c", y="crop_yield_mt_per_ha", hue="crop_type")
plt.xlabel("Average Temperature ( ̊ C)")
plt.ylabel("Crop Yield (tons/ha")
plt.show()

# Precipitation vs. Crop Yield
plt.figure(figsize=(8,2))
sns.scatterplot(data=df, x="total_precipitation_mm",y="crop_yield_mt_per_ha", hue="region")
plt.title("Precipitation vs Crop Yield by Region")
plt.xlabel("Precipitation (mm)")
plt.ylabel("Crop Yield (tons/ha)")
plt.show()

# Economic and Environmental Impacts

# CO2 Emissions vs Economic Impact
plt.figure(figsize=(8,6))
sns.scatterplot(data=df, x="co2_emissions_mt", y="economic_impact_million_usd", hue="country")
plt.title("CO2 Emissions vs Economic Impact")
plt.xlabel("CO2 Emission (MT)")
plt.ylabel("EconomicImpact (Million USD")
plt.show()

#Yield vs. Economic Impact
plt.figure(figsize=(8,2))
sns.scatterplot(data=df, x="crop_yield_mt_per_ha", y="economic_impact_million_usd", hue="region")
plt.title("Crop Yield vs Economic Impact")
plt.xlabel("Crop Yield (tons/ha)")
plt.ylabel("Economic Impact (Million USD)")
plt.show()

# Correlation Analysis
# Find out which variables are most related:
plt.figure(figsize=(6,4))
sns.heatmap(df.corr(numeric_only=True), annot=True, cmap="coolwarm")
plt.title("Correlation Between Climate and Agricultural Variables")
plt.show()

# Visualizing Regional Effects
# We’ll use grouping, aggregation, and visualization to find and display these patterns.

# Average Crop Yield by Region
plt.figure(figsize=(10,6))
region_yield = df.groupby("region")["crop_yield_mt_per_ha"].mean().sort_values(ascending=False)
sns.barplot(x=region_yield.values, y=region_yield.index, palette="viridis")
plt.title("Average Crop Yield by Region")
plt.xlabel("Average Crop Yield (tons/ha)")
plt.ylabel("Region")
plt.show()

# Average Temperature by Region
plt.figure(figsize=(10,6))
region_temp = df.groupby("region")["average_temperature_c"].mean().sort_values()
sns.barplot(x=region_temp.values, y=region_temp.index, palette="coolwarm")
plt.title("Average Temperature by Region")
plt.xlabel("Temperature (°C)")
plt.ylabel("Region")
plt.show()

# Economic Impact by Region
plt.figure(figsize=(10,6))
region_econ = df.groupby("region")["economic_impact_million_usd"].mean().sort_values(ascending=False)
sns.barplot(x=region_econ.values, y=region_econ.index, palette="magma")
plt.title("Average Economic Impact by Region")
plt.xlabel("Economic Impact (Million USD)")
plt.ylabel("Region")
plt.show()

# Correlation Between Extreme Weather and Yield
plt.figure(figsize=(8,6))
sns.scatterplot(data=df, x="extreme_weather_events", y="crop_yield_mt_per_ha", hue="region", alpha=0.7)
plt.title("Extreme Weather Events vs Crop Yield by Region")
plt.xlabel("Number of Extreme Weather Events")
plt.ylabel("Crop Yield (tons/ha)")
plt.show()

# Setup the Dashboard Layout

# We’ll use a 2x2 grid of charts to summarize key insights.
plt.figure(figsize=(14,10))

# 1. Temperature trend over time
plt.subplot(2,2,1)
sns.lineplot(data=df, x="year", y="average_temperature_c", color="red")
plt.title("Average Temperature Over Time")
plt.xlabel("Year")
plt.ylabel("Temperature (°C)")

# 2. Precipitation trend over time
plt.subplot(2,2,2)
sns.lineplot(data=df, x="year", y="total_precipitation_mm", color="blue")
plt.title("Total Precipitation Over Time")
plt.xlabel("Year")
plt.ylabel("Precipitation (mm)")

# 3. Relationship: Temperature vs. Crop Yield
plt.subplot(2,2,3)
sns.scatterplot(data=df, x="average_temperature_c", y="crop_yield_mt_per_ha", hue="crop_type", alpha=0.7)
plt.title("Temperature vs Crop Yield")
plt.xlabel("Temperature (°C)")
plt.ylabel("Crop Yield (tons/ha)")

# 4. CO2 Emissions vs Economic Impact
plt.subplot(2,2,4)
sns.scatterplot(data=df, x="co2_emissions_mt", y="economic_impact_million_usd", hue="country")
plt.title("CO2 Emissions vs Economic Impact")
plt.xlabel("CO2 Emission (MT)")
plt.ylabel("EconomicImpact (Million USD")

plt.tight_layout()
plt.show()

