# Group by 'country' and sum 'co2_emission'
emissions_by_country = food_consumption.groupby('country')['co2_emission'].sum().reset_index()

# Print the resulting DataFrame
print(emissions_by_country)
