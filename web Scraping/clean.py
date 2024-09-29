import pandas as pd

# Load the CSV file
df = pd.read_csv('zendesk_data.csv')

# Filter out rows where 'Title' and 'Content' contain the unwanted phrases
df_cleaned = df[~((df['Title'] == 'No Title') & (df['Content'] == 'No Content'))]

# Save the cleaned DataFrame to a new CSV
df_cleaned.to_csv('cleaned_file.csv', index=False)

print("Cleaning completed. Filtered CSV saved as 'cleaned_file.csv'.")
