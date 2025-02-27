import pandas as pd

# Creating a DataFrame from a dictionary
data = {
    'Name': ['Alice', 'Bob', 'David'],
    'Age': [25, 30, 35],
    'City': ['New York', 'Seoul', 'Los Angeles']  # Corrected city names
}

df = pd.DataFrame(data)
print("Original DataFrame:")
print(df)

# Save DataFrame to CSV
df.to_html('data.html', index=False)

# Read the CSV file
df2 = pd.read_csv('customers-100.csv')

# Save DataFrame to JSON with the correct file path
df2.to_json(r'customers-100.json', index=False)  # Fixed path and extension
df2.to_html(r'customers-100.html', index=False)
print("\nDataFrame after reading from CSV:")
print(df2)

# Print the 'Name' column
print("\nNames column:")
print(df['Name'])

# Filter based on condition (Age > 30)
print("\nFiltered Data (Age > 30):")
print(df[df['Age'] > 30])

# Sort by Age in descending order
print("\nSorted Data by Age (Descending):")
print(df.sort_values(by='Age', ascending=False))

# Group by City and count occurrences
print("\nGrouped Data by City:")
print(df.groupby('City').count())

# Fill NaN values (if any) with "Unknown"
print("\nDataFrame after filling NaN values (if any):")
print(df.fillna("Unknown"))  # Currently, this does nothing since no NaN values exist.
