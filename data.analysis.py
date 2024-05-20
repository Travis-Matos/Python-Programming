import pandas as pd

# load sample CSV data
df = pd.read_csv('sample.csv')

# Display basic information
print(df.info())

# Display the frist 5 rows of the dataframe
print(df.head())
