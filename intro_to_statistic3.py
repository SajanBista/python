import numpy as np

quartiles = np.quantile(food_consumption['co2_emission'], [0.25, 0.5, 0.75])
print(quartiles)
# Calculate the six quantiles (quintiles - splitting into 5 pieces)
quintiles = np.quantile(food_consumption["co2_emission"], np.linspace(0, 1, 6))

# Print the quintiles
print(quintiles)  

# Calculate the eleven quantiles (deciles - splitting into 10 pieces)
deciles = np.quantile(food_consumption["co2_emission"], np.linspace(0, 1, 11))

# Print the deciles
print(deciles)  
