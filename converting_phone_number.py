"""import pandas as pd
import numpy as np

# Load CSV
df = pd.read_csv('lauriethepauth__chien_data.csv')

# Cleaning function
def make_dialable(raw):
    if pd.isna(raw):
        return ""
    return str(raw).replace("(0)", "").replace(".", "")

# Apply cleaning
df['phone_number'] = df['phone_number'].apply(make_dialable)

# Preview result
print(df['phone_number'].head())

# Save to new file
df.to_csv('phone_cleaned.csv', index=False, encoding='utf-8')

print("✔ Cleaned CSV saved as phone_cleaned.csv")


import pandas as pd
import numpy as np 

df = pd.read_csv('lauriethepaut__centrale_data.csv')



def make_dialable(raw):
    if pd.isna(raw):
        return ""
    number = str(raw).replace(".", "")  # remove dots
    if number.startswith("0"):
        number = number[1:]  # remove leading 0
    return "+33" + number  # add country code


df['Phone Number'] = df['Phone Number'].apply(make_dialable)

print(df['Phone Number'].head())

df.to_csv('phone_cleaned__centrale_data.csv', index=False, encoding = 'utf-8')

"""

"""
import numpy as np
import pandas as pd
# Load CSV
df = pd.read_csv('phone_cleaned__chien_data.csv')



df.rename(columns={
    'url': 'URL',
    'company_name': 'Company Name',
    'first_name':'First Name',
    'last_name':'Last Name',
    'phone_number':'Phone Number',
    'zip_code':'Zipcode',
    'dog_breed':'Dog Breed',
    'address':'Address',
    'website_url':'Website Url',
    'street_number': 'Street Number',
    'city':'City',
}, inplace=True)

print(df.columns.tolist())

df.to_csv('phone_cleaned__chien_data_renamed.csv', index=False, encoding='utf-8')

"""
"""
import pandas as pd

# Load the two CSV files
df1 = pd.read_csv('chien.csv')
df2 = pd.read_csv('centrale.csv')

# Get the list of columns
columns1 = set(df1.columns.tolist())
columns2 = set(df2.columns.tolist())

# Columns in both files
common_columns = columns1 & columns2
print("Common Columns:", common_columns)

# Columns only in first file
only_in_df1 = columns1 - columns2
print("Columns only in first file:", only_in_df1)

# Columns only in second file
only_in_df2 = columns2 - columns1
print("Columns only in second file:", only_in_df2)

"""

# import pandas as pd

# # Load both CSVs
# df1 = pd.read_csv('centrale.csv')
# df2 = pd.read_csv('chien.csv')

# # Make a list of columns in df2 that are NOT in df1, except the 'Phone Number' key
# additional_columns = [col for col in df2.columns if col not in df1.columns and col != 'Phone Number']

# # Merge df2 into df1 on 'Phone Number', keeping only additional columns
# merged_df = pd.merge(df1, df2[['Phone Number'] + additional_columns], on='Phone Number', how='outer')

# # Optional: preview result
# print(merged_df.head())

# # Save merged CSV
# merged_df.to_csv('Merged.csv', index=False, encoding='utf-8')

# print("Merged.csv")


# import pandas as pd

# # Load both CSVs
# df1 = pd.read_csv('centrale.csv')
# df2 = pd.read_csv('chien.csv')

# # Start with all columns from df1
# merged_df = df1.copy()

# # Merge rows from df2 based on Phone Number
# for index, row in df2.iterrows():
#     phone = row['Phone Number']
#     if phone in merged_df['Phone Number'].values:
#         # Phone number exists: update only empty columns in merged_df
#         for col in df2.columns:
#             if col != 'Phone Number' and (col not in merged_df.columns or merged_df.loc[merged_df['Phone Number'] == phone, col].iloc[0] == ''):
#                 if col not in merged_df.columns:
#                     merged_df[col] = ''
#                 merged_df.loc[merged_df['Phone Number'] == phone, col] = row[col]
#     else:
#         # Phone number doesn't exist: append the row
#         merged_df = pd.concat([merged_df, pd.DataFrame([row])], ignore_index=True)

# # Fill remaining NaN with empty string
# merged_df = merged_df.fillna('')

# # Preview
# print(merged_df.head())

# # Save final merged CSV
# merged_df.to_csv('Merged_exact.csv', index=False, encoding='utf-8')

# print(" Merged_exact.csv saved!")


import pandas as pd

# Load CSVs
df1 = pd.read_csv('centrale.csv')
df2 = pd.read_csv('chien.csv')

# Convert phone numbers to set for fast comparison
phones_df1 = set(df1['Phone Number'])
phones_df2 = set(df2['Phone Number'])

# Intersection = phone numbers present in both files
common_phones = phones_df1 & phones_df2

print(f"Number of phone numbers present in both files: {len(common_phones)}")
