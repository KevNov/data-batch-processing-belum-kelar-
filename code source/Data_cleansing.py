import pandas as pd
import numpy as np

# Read in the CSV file
df = pd.read_csv('C:\\Users\\kevnov\\Documents\\Data batch processing\\source data\\people-100.csv')

# Remove duplicates
df = df.drop_duplicates()

# Remove missing values
df = df.dropna()

# Save the cleaned dataframe to a new CSV file
df.to_csv('source data/dataclean-people-100.csv', index=False)

print('Data cleansing success')
