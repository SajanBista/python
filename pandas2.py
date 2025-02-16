import pandas as pd 

#importing  the csv  file
data=pd.read_csv('ecommerce_sales.csv')


#Clean the data: Handle missing values
data.isnull().sum()

#format dates 
data["Date"] = pd.to_datetime(data["Date"], format= "%Y-%m-%d")


#print(data)
#fix data types.
print(data.dtypes)
data["Quantity"]=pd.to_numeric(data["Date"],errors="coerce")
data["Price"]=pd.to_numeric(data["Price"],errors="coerce")
data["Total Sales"]=pd.to_numeric(data["Total Sales"],errors="coerce")

#Total revenue per category
revenue_per_category = data.groupby("Category")["Total Sales"].sum().reset_index()
revenue_per_category = revenue_per_category.sort_values(by="Total Sales", ascending = False)

print(revenue_per_category)

"""

Average order value"""

#Monthly sales trend
#Firstly extract Year-Month
data["Year-Month"]=data["Date"].dt.to_period("M")

monthly_sales=data.groupby("Year-Month")["Total Sales"].sum().reset_index()

print(monthly_sales)


#Top 5 best-selling products
# Total quantity sold per product
best_selling_products = data.groupby("Product")["Quantity"].sum().reset_index()

# Sort by quantity sold
best_selling_products = best_selling_products.sort_values(by="Quantity", ascending=False)


top_5_products = best_selling_products.head(5)
print(top_5_products)


# Calculate total sales per order
data["Order Total"] = data["Quantity"] * data["Price"]

# Calculate the average order value
average_order_value = data.groupby("Order ID")["Order Total"].sum().mean()
print("Average Order Value:", average_order_value)


import matplotlib.pyplot as plt
monthly_sales.plot(x="Year-Month", y="Total Sales", kind="line", title="Monthly Sales Trend")
plt.show()