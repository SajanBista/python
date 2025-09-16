import math
print("enter the total number of x and y")
x=int(input("number of x: "))
y=int(input("number of y: "))

print(f"the total number of x ={x} and y = {y} as per you")
x_values =[]
y_values =[]
print("enter  all the values of x")
for i in range(x):
    val = int(input(f"x[{i+1}]"))
    x_values.append(val)
print(f"the values of x that you entered are: {x_values}")

for i in range(y):
    val = int(input(f"y[{i+1}]"))
    y_values.append(val)
print(f"the values of y that you entered are: {y_values}")

# taking n as a input
n = len(x_values)

# finding x * y
xy = []
for i in range(len(x_values)):
    xy.append(x_values[i]*y_values[i])
print(" the product of x and y are: ", xy)
xy_sum = sum(xy)
print("the sum of xy is : ",xy_sum)

# sum of x and y's
x_sum = sum(x_values)
print("the total sum of x is : ",x_sum)

y_sum = sum(y_values)
print("the total sum of y is : ",y_sum)

#finding the square of each item in the list
x_square = [val*val for val in  x_values] # using list comprehension method
print("the value of x square are : ",x_square)

y_square =[val*val for val in y_values]
print("the values of y square are:", y_square)


x_sum_square = sum(x_square)
print("the total sum of square of x is : ",x_sum_square)
y_sum_square = sum(y_square)
print("the total sum of square of y is : ",y_sum_square)

# finding the square of total x
x_sum_whole_square = x_sum**2
y_sum_whole_square = y_sum**2

print("the square of total x is :",x_sum_whole_square)
print("the square of the total y  is :",y_sum_whole_square )



upper_part = (n*xy_sum)-(x_sum * y_sum)
lower_part = math.sqrt((n*x_sum_square - x_sum_whole_square) * (n*y_sum_square - y_sum_whole_square))
r = upper_part/lower_part

print("the correlation of the given inputs  is : ", r)







    