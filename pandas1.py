import pandas as pd 
import numpy as np

np.random.seed(42)


dates = pd.date_range(start="2025-01-01", periods=10, freq='D')
product =["shoes","shorts","sport wears","ladies items"]

data = {
    "date":np.random.choice(dates,10),
    "Product":np.random.choice(product,10),
    "Price":np.random.randint(21,201,10),
    "Quantity":np.random.randint(1,6,10)
}

df=pd.DataFrame(data)
print(data)

df["Total Sales"] = df["Price"] * df["Quantity"]

total_revenue = df["Total Sales"].sum()

best_selling_product = df.groupby("Product")["Total Sales"].sum().idxmax()

average_price = df["Price"].mean()

print(total_revenue)
print(best_selling_product)
print(average_price)