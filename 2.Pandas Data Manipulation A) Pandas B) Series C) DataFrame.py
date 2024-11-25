import pandas as pd

# Sample data
data = {
    'Name': ['Saransh', 'Shiwali', 'Shivansh', 'Sukruti', 'Shaan'],
    'Age': [19, 20, 25, 22, 23],
    'City': ['New Delhi', 'Banglore', 'Hyderabad', 'Mumbai', 'Pune']
}

# Create a DataFrame
df = pd.DataFrame(data)

# Display the first few rows
print("# Display the first few rows")
print(df.head())

# Display basic information about the DataFrame
print("\n# Display basic information about the DataFrame")
print(df.info())

# Summary statistics of numerical columns
print("\n# Summary statistics of numerical columns")
print(df.describe())

# Filter rows where Age is less than 30
filtered_df = df[df['Age'] < 30]
print("\n# Filter rows where Age is less than 30")
print(filtered_df)
