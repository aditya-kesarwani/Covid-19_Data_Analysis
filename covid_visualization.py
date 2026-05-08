import pandas as pd
import matplotlib.pyplot as plt

# Read cleaned dataset
df = pd.read_csv("cleaned_covid_dataset.csv")

# Light pastel colors
colors = [
    "#FFB3BA",
    "#BAFFC9",
    "#BAE1FF",
    "#FFFFBA",
    "#D7BAFF",
    "#FFD6A5",
    "#A0E7E5",
    "#B4F8C8",
    "#FBE7C6",
    "#CDB4DB"
]

# Figure size
plt.figure(figsize=(8,8))

# Pie chart
plt.pie(
    df["Deaths"],
    labels=df["Country"],
    autopct='%1.1f%%',
    colors=colors
)

# Title
plt.title("COVID-19 Death Percentage by Country")

# Save graph
plt.savefig("covid_pie_chart.png")

# Show graph
plt.show()