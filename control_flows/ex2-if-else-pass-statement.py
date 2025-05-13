# Pass statement and how it works?:

# Using without pass statement:
x = int(input("Enter the value of x: "))
if x < 0:
    pass # Do nothing (This will not work!)
else:
    print(x)
#%%
### Using pass statement:
if x < 0:
    pass # Do subtraction operation.
else:
    print(x)
#%%
# This is equivalent to writing;
if x >= 0:
    print(x)
#%%
# Use of non-functional else block;
if x == 2:
    print(x)
# else:
#     pass # Do nothing if x is not equal to 2
#%%
# Floating Point Equality
# (==)
# Checking the differences
# Example1
d1 = 1.11 - 1.10
d2 = 2.11 - 2.10
print(d1)
print(d2)
if d1 == d2:
    print("Same")
else:
    print("Different")
#%%
# Example2 Alternative to Example1 But Effective
d1 = 1.11 - 1.10
d2 = 2.11 - 2.10
print(d1)
print(d2)
diff = d1 - d2
if diff < 0:
    diff = -diff
if diff < 0.000001:
    print('Same')
else:
    print('Different')
#%%