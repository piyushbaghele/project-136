import pandas as pd

# Assuming your CSV file is named 'stars_data.csv'
df = pd.read_csv('C:/Users/punam/Desktop/whitehatjr/classs136/project-136/star_with_gravity.csv')

# Create a list from the columns of the DataFrame
columns_list = df.columns.tolist()

# Make a list of dictionaries from this data
data_list = df.to_dict(orient='records')

print(data_list)