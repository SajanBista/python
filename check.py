import pandas as pd

df = pd.read_csv("data.csv")

df['street_number'] = df['street_number'].apply(
    lambda x: str(int(x)) if pd.notna(x) and x == int(x) else ('' if pd.isna(x) else str(x))
)


# detect phone numbers with 4 or 5 digits
mask_short_phone = df['phone_number'].str.len().isin([4, 5])

# move those values into zip_code
df.loc[mask_short_phone, 'zip_code'] = df.loc[mask_short_phone, 'phone_number']

# clear phone_number for those rows
df.loc[mask_short_phone, 'phone_number'] = ''


# Remove ALL phone numbers shorter than 9 digits
df.loc[df['phone_number'].str.len() < 9, 'phone_number'] = ''


df.to_csv("cleanedZip.csv", index=False)
