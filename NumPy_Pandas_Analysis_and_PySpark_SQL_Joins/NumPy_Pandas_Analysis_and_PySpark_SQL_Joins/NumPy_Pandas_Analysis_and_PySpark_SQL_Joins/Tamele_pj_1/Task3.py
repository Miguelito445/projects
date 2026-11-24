import pandas as pd
import numpy as np

ID_ET = 70274
month1_ET = 1 + ID_ET % 12
month2_ET = month1_ET + 1 if month1_ET < 12 else 1

print("Name: Eric")
print("Surname: Tamele")
print("ID: 70274")

print(f"Month 1: {month1_ET} (March)")
print(f"Month 2: {month2_ET} (April)")

try:
    data_ET = pd.read_csv('Seattle2014.csv')
except FileNotFoundError:
    print("Error: Seattle2014.csv file not found in directory.")
    exit()

data_ET['DATE'] = pd.to_datetime(data_ET['DATE'], format='%Y%m%d')
data_ET['MONTH'] = data_ET['DATE'].dt.month

months_data_ET = data_ET[data_ET['MONTH'].isin([month1_ET, month2_ET])].copy()

prcp_ET = months_data_ET['PRCP']

rainy_days_ET = np.sum(prcp_ET > 0)

rainy_prcp_ET = prcp_ET[prcp_ET > 0]
min_prcp_ET = np.min(rainy_prcp_ET) if len(rainy_prcp_ET) > 0 else 0
avg_prcp_ET = np.mean(rainy_prcp_ET) if len(rainy_prcp_ET) > 0 else 0
max_prcp_ET = np.max(rainy_prcp_ET) if len(rainy_prcp_ET) > 0 else 0

total_prcp_ET = np.sum(prcp_ET)

print(f"\nRainy days (PRCP > 0): {rainy_days_ET}")
print(f"Minimum precipitation on rainy days: {min_prcp_ET:.2f}")
print(f"Average precipitation on rainy days: {avg_prcp_ET:.2f}")
print(f"Maximum precipitation on rainy days: {max_prcp_ET:.2f}")
print(f"Total precipitation for months {month1_ET} and {month2_ET}: {total_prcp_ET:.2f}")