import pandas as pd
import matplotlib.pyplot as plt 

# Step 1: Load the data from the CSV file
data = pd.read_csv("messiGoal.csv")

# Step 2: Clean the data by removing rows with missing "Minute" values
data = data.dropna(subset=["Minute"])

# Step 3: Count the total goals Messi scored
total_goals = len(data)
print(f"Total goals scored by Messi: {total_goals}")

# Step 4: Count how many goals Messi scored at home and away
home_goals = len(data[data["Venue"] == "H"])  # 'H' for home games
away_goals = len(data[data["Venue"] == "A"])  # 'A' for away games
print(f"Goals at home: {home_goals}, Goals away: {away_goals}")

# Step 5: Clean the "Minute" column (remove apostrophes and convert to integers)
data["Minute"] = data["Minute"].str.replace("'", "").astype(int)

# Step 6: Group Messi's goals into minute intervals (e.g., 0-15, 15-30)
minute_intervals = pd.cut(data["Minute"], bins=[0, 15, 30, 45, 60, 75, 90], right=False)

# Step 7: Count the number of goals in each minute interval
goal_distribution = minute_intervals.value_counts().sort_index()

# Step 8: Display the goal distribution in minute intervals
print("Goals by minute intervals:")
print(goal_distribution)

# Step 9: Create a bar chart to visualize the goal distribution
goal_distribution.plot(kind="bar", color="skyblue", edgecolor="black")
plt.title("Messi's Goal Distribution by Minute Intervals")  # Title of the chart
plt.xlabel("Minute Intervals")  # X-axis label
plt.ylabel("Number of Goals")  # Y-axis label
plt.xticks(rotation=0)  # Keep the labels horizontal
plt.show()  # Display the chart


