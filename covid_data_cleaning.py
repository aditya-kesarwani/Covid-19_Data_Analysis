import pandas as pd
import numpy as np

# Read CSV file
df = pd.read_csv("covid_dataset.csv")

# Print original dataset
print("Original Dataset:\n")
print(df)

# Check missing values
print("\nMissing Values:\n")
print(df.isnull().sum())

# Fill missing values using average
df["ConfirmedCases"].fillna(df["ConfirmedCases"].mean(), inplace=True)
df["RecoveredCases"].fillna(df["RecoveredCases"].mean(), inplace=True)
df["Deaths"].fillna(df["Deaths"].mean(), inplace=True)
df["Vaccinated"].fillna(df["Vaccinated"].mean(), inplace=True)

# Print cleaned dataset
print("\nCleaned Dataset:\n")
print(df)

# NumPy Calculations
average_cases = np.mean(df["ConfirmedCases"])
maximum_cases = np.max(df["ConfirmedCases"])
minimum_cases = np.min(df["ConfirmedCases"])

print("\nAverage Confirmed Cases:", average_cases)
print("Maximum Confirmed Cases:", maximum_cases)
print("Minimum Confirmed Cases:", minimum_cases)

# Save cleaned dataset
df.to_csv("cleaned_covid_dataset.csv", index=False)

print("\nCleaned dataset saved successfully!")