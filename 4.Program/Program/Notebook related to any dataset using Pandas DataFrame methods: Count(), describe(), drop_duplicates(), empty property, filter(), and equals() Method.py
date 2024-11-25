# Importing libraries
import pandas as pd
import numpy as np

# Creating the DataFrame
data = {
    'Name': ['Alice', 'Bob', 'Charlie', 'David', 'Alice', 'Eve'],
    'Age': [25.0, 30.0, 35.0, 40.0, 25.0, np.nan],
    'City': ['New York', 'Los Angeles', 'New York', 'Chicago', 'New York', 'Los Angeles']
}
df = pd.DataFrame(data)

# 1. Using count() to count the not-null/NA entries
not_null_count = df.count()
print("Count of not-null/NA entries:\n", not_null_count)

# 2. Using describe() to give the statistical description of the dataframe
statistical_description = df.describe()
print("\nStatistical description of the dataframe:\n", statistical_description)

# 3. Drop duplicates using drop_duplicates()
df_no_duplicates = df.drop_duplicates()
print("\nDataFrame after dropping duplicates:\n", df_no_duplicates)

# 4. Check whether the dataframe is empty using empty property
is_empty = df.empty
print("\nIs the original DataFrame empty?\n", is_empty)

# 5. Filter the records containing city as 'New York'
new_york_df = df[df['City'] == 'New York']
print("\nRecords containing City as 'New York':\n", new_york_df)

# 6. Create a copy of the dataframe and compare the original and the copy
df_copy = pd.DataFrame(data)
are_equal = df.equals(df_copy)
print("\nAre the original DataFrame and its copy equal?\n", are_equal)
