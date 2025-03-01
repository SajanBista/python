# Create a histogram of restaurant_groups and show plot
import numpy as np 
import pandas as pd 
import matplotlib.pyplot as plt
restaurant_groups['group_size'].hist(bins=[2, 3, 4, 5, 6])
plt.show()

# Create probability distribution
size_dist = restaurant_groups['group_size'].value_counts() / len(restaurant_groups)


# Reset index and rename columns
size_dist = size_dist.reset_index()
size_dist.columns = ['group_size', 'prob']

print(size_dist)

# Create probability distribution
size_dist = restaurant_groups['group_size'].value_counts() / restaurant_groups.shape[0]
# Reset index and rename columns
size_dist = size_dist.reset_index()
size_dist.columns = ['group_size', 'prob']

# Calculate expected value
expected_value = np.sum(size_dist['group_size'] * size_dist['prob'])
print(expected_value)
# Create probability distribution
size_dist = restaurant_groups['group_size'].value_counts() / restaurant_groups.shape[0]
# Reset index and rename columns
size_dist = size_dist.reset_index()
size_dist.columns = ['group_size', 'prob']

# Expected value
expected_value = np.sum(size_dist['group_size'] * size_dist['prob'])

# Subset groups of size 4 or more
groups_4_or_more = size_dist[size_dist['group_size'] >= 4]


# Sum the probabilities of groups_4_or_more
prob_4_or_more = prob_4_or_more = groups_4_or_more['prob'].sum()

print(prob_4_or_more)
