# Program to illustrate arithmitic operation
# Variable x holds 9 and variable y holds 2
x = 9
y = 2
# Addition
print("Addition, x + y = ", x + y)             # returns addition
#%%
# Subtraction
print("Subtraction, x - y = ", x - y)           # returns subtraction
#%%
# Multiplication
print("Multiplication, x * y = ", x * y)        # returns multipication
#%%
# Simple Division
print("Simple Division, x / y = ", x / y)       # returns quotient
#%%
# Modulus
print("Modulus Division, x % y = ", x % y)      # returns reminder
#%%
# Integer division rounded towards minus infinity
# returns quotient rounded to next smallest hole number
print("Floor Division, x // y = ", x // y)
#%%
# Exponent
print("Exponent, x ** y = ", x ** y)            # returns x to the power of y
#%%

#%%
# Comparison operators
# Variable x holds 10 and variable y holds 5
x = 10
y = 5
# Equality check operation
print( "Equal check, x(10) == y(5) ", x == y)
#%%
# Not Equality check operation
print( "Not Equal check, x(10) != y(5) ", x != y)
#%%
# Strictly Less than check operation
print ("Less than check, x(10) < y(5) ", x < y)
#%%
# Strictly Greater than check operation
print("Greater than check, x(10) > y(5) ", x > y)
#%%
# Less than or equal check operation
print("Less than or equal to check, x(10) <= y(5) ", x <= y)
#%%
# Greater than or equal to check operation
print("Greater than or equal to check, x(10) >= y(5) ", x >= y)

#%%

# Assignment Operators
# Variable x holds 6 and variable y holds 2
x = 6 ; y = 2
#%%
x += y       # x = x + y
print( "Value of a post x+=y is ", x)
#%%
x = 6 ; y = 2
x -= y       # x = x - y
print( "Value of a post x+=y is ", x)

#%%
x = 6 ; y = 2
x *= y       # x = x * y
print( "Value of a post x*=y is ", x)
#%%
x = 6 ; y = 2
x /= y       # x = x / y
print ("Value of a post x/=y is ", x)
#%%
x = 6 ; y = 2
x %= y       # x = x % y
print( "Value of a post x%=y is ", x)
#%%
x = 6 ; y = 2
x //= y      # x = x // y
print ("Value of a post x//=y is ", x)
#%%
x = 6 ; y = 2
x **= y      # x = x ** y
print("Value of x post x**=y is ", x)
#%%
# Logical operators
# Let's check first for the boolean values

x = True
y = False
#%%
# Logical AND operation
print(' x and y is', x and y) # True and True
#%%
# Logical OR operation
print(' x or y is', x or y)
#%%
# Logical NOT operation
print(' not x is', not x)
print(' not y is', not y)
#%%

a = 1 # True
b = 0 # False
#%%
# Logical AND operation
print('a and b is', a and b)    # 1 and 0 --> True and False
#%%
# Logical OR operation
print('a or b is', a or b)
#%%
# Logical NOT operation
print('not b is', not b)
print('not b is', not a)
#%%
# Bitwise Operators

# Basic six bitwise operations
# Let x = 10 (in binary 0000 1010) and y = 12 (in binary 0000 1100)
x = 10 # 0000 1010
y = 12 # 0000 1100
#%%
print(x & y) # Bitwise AND     results 0000 1000
#%%
print(x | y) # Bitwise OR      results 0000 1110
#%%
print(x ^ y) # Bitwise XOR     results 0000 0110
#%%

# Right Shift 0000 1010 first shipt(0000 0101)
# second shift(0000 0010)
print(x >> 2)
#%%
# Left shift
print(x << 2)  # first Shift(0001 0100) second shipt (0010 1000)
#%%
print(~x)      # Bitwise NOT (1111 0101)

#%%
# Identity Operators
# Get the attribute values  for var1 and var2
var1 = 5 ; print(var1)
print(id(var1))     # use "id(variable name)" to get the identity of variable entered
#%%
var2 = 5 ; print(var2)
print(id(var2))
#%%
# Get the attribute values  for var3 and var4
var3 = 'Hello' ; print(var3)
print(id(var3))
#%%
var4 = 'Hello' ; print(var4)
print(id(var4))
#%%
# Get the attribute values  for var5 and var6
var5 = [1,2,3] ; print(var5)
print(id(var5))
#%%
var6 = [1,2,3] ; print(var6)
print(id(var6))
#%%
# Now Let's check the identity operation
print(var1 is var2) ; # print(var1 is not var2)
print(var3 is var4)
print(var5 is var6)

#%%
# Membership operators
# In Python everything we enter is casesensitive

var1 = 'Hello world'              # string
var2 = {1:'a', 2:'b', 'all':4}    # dictionary
#%%
print('H' in var1)       # check H is present in var1 or not
#%%
print('hello' in var1)   # Hello is present in var1 not hello
#%%
print('hello' not in var1)  # Hello is present in var1 not hello
#%%
print(1 in var2)         # check 1 is present in var2 or not
#%%
print(2 in var2)         # check 2 is present in var2 or not
#%%
print('a' in var2)       # check a is present in var2 or not
#%%
print('all' in var2)      # check all is present in var2 or not

#%%


















