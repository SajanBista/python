import pandas as pd
import matplotlib.pyplot as plt 

# Load the dataset with tab-separated values
data = pd.read_csv("messiGoal.csv", sep="\t")

# Clean the column names by removing leading/trailing spaces
data.columns = data.columns.str.strip()

# Step 1: Clean the data by removing rows where "Minute" is not numeric
# Check unique values in "Minute" column
print("Unique values in 'Minute' column before cleaning:")
print(data["Minute"].unique())

# Remove rows where "Minute" is not a valid number
data = data[pd.to_numeric(data["Minute"], errors='coerce').notna()]

# Clean "Minute" column by removing extra characters like "'" and convert to integers
data["Minute"] = data["Minute"].str.replace("'", "").astype(int)

# Step 2: Calculate total goals
total_goals = len(data)
print(f"Total goals scored by Messi: {total_goals}")

# Step 3: Calculate home vs. away goals
home_goals = len(data[data["Venue"] == "H"])
away_goals = len(data[data["Venue"] == "A"])
print(f"Goals at home: {home_goals}, Goals away: {away_goals}")

# Step 4: Analyze goal timing
# Group goals by minute intervals
minute_intervals = pd.cut(data["Minute"], bins=[0, 15, 30, 45, 60, 75, 90], right=False)
goal_distribution = minute_intervals.value_counts().sort_index()

# Print goal distribution
print("Goal distribution by minute intervals:")
print(goal_distribution)

# Plot the goal distribution
goal_distribution.plot(kind="bar", color="skyblue", edgecolor="black")
plt.title("Messi's Goal Distribution by Minute Intervals")
plt.xlabel("Minute Intervals")
plt.ylabel("Number of Goals")
plt.xticks(rotation=0)
plt.show()
