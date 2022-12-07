# Import necessary libraries
import pandas as pd
import numpy as np

# Load the data from a CSV file into a Pandas dataframe
data = pd.read_csv('pacemaker_data.csv')

# Inspect the first few rows of the data to make sure it was loaded correctly
print(data.head())

# Check for missing values and handle them as necessary
print(data.isnull().sum())
data = data.dropna()

# Extract the relevant columns from the dataframe
times = data['Timestamp'].values
pace_intervals = data['Pace Interval (ms)'].values

# Calculate some summary statistics
mean_pace_interval = np.mean(pace_intervals)
median_pace_interval = np.median(pace_intervals)
max_pace_interval = np.max(pace_intervals)
min_pace_interval = np.min(pace_intervals)

# Print the results
print("Mean pace interval:", mean_pace_interval)
print("Median pace interval:", median_pace_interval)
print("Max pace interval:", max_pace_interval)
print("Min pace interval:", min_pace_interval)
