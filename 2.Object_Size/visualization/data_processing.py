import pandas as pd
from scipy import stats
import math
import re

# Read the excel file
file_path = "Object_Size_M5_Benchmark.xlsx"
df = pd.read_excel(file_path, engine='openpyxl')

# Filter rows where any column contains the word 'Overhead'
overhead_rows = df[df.apply(lambda row: row.astype(str).str.contains('Overhead').any(), axis=1)]

# Regular expression pattern to match "Overhead: X seconds" and extract X
pattern = r"Overhead: (\d+(\.\d+)?) seconds"

# Create a dictionary to store arrays for each column
arrays_dict = {}

# Iterate over each column in the dataframe
for col in overhead_rows.columns:
    # Extract the overhead values using the regex pattern
    extracted_values = overhead_rows[col].astype(str).str.extract(pattern)[0]

    # Convert the extracted values to float (NaN for non-matching cells)
    arrays_dict[col] = extracted_values.dropna().astype(float)

# Calculate mean, standard deviation, and 99% confidence interval
def get_stats(data):
    if len(data) <= 10:
        return None, None, None  # Not enough data
    data = data[10:]
    mean = data.mean()
    std_dev = data.std()
    confidence_level = 0.99
    degrees_freedom = len(data) - 1
    confidence_interval = stats.t.interval(confidence_level, degrees_freedom, mean, std_dev/math.sqrt(len(data)))
    return mean, std_dev, confidence_interval

# Print the arrays
for col, data_series in arrays_dict.items():
    mean, std, confidence = get_stats(data_series)
    if mean is not None:
        print(f"Column: {col}")
        print(f"Mean: {mean}")
        print(f"Standard Deviation: {std}")
        print(f"99% Confidence Interval: {confidence}")
        print("----------------------------")