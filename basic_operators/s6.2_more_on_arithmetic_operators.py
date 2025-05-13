#More On Arithmetic Operators
# We can use operators to combine values and variables and form more complex expressions.
#%%
num1 = 4
num2 = 8
total = num1 + num2
# print statement can be used to express in the form mathemetic expression
print(num1, '+', num2, '=', total)
#%%

#%%
# Two operators, ‘+’ and ‘-‘, can be used as unary operators
x, y, z = 3, -4, 0
# if we use unary ‘-‘ operator to inverse the expressions, like;
x = -x
y = -y
z = -z
print(x, y, z)
print(-(5-4))
#%%
# All the arithmetic operators are subject to the limitations of the data types on which they operate

value1 = 2.0**10
print(value1)
value2 = 2.0**100
print(value2)
value3 = 2.0**1000
print(value3)
value4 = 2.0**10000
print(value4)
#%%
# Truncation
print(25//4, 4//25)
print(13 // 5)
# Remainder with the modulus operator
print(25 % 4, 4 % 25)

# The / operator applied to two integers produces a ﬂoating-point result
print(25/4, 4/25)
#%%
# More lines by using the backslash (\) symbol at the end of an incomplete line
ten = 10.0
ten_by_three = 10.0 / 3.0
zero = ten - ten_by_three - ten_by_three - ten_by_three \
       - ten_by_three - ten_by_three - ten_by_three \
       - ten_by_three - ten_by_three - ten_by_three \
       -ten_by_three
print(zero)
#%%

#%%
# Python statement spread over two lines in the source code
x = (int(input('Please enter an integer'))

     + (y - 2) + 16) * 2

y = 10
x = (int(input('Please enter an integer: '))
     + (y - 2) + 16


     ) * 2
#%%
one = 1.0
one_fourth = 1.0 / 4.0
zero = one - one_fourth - one_fourth - one_fourth - one_fourth
print(zero)
#%%
# Mixed Type Expressions
x = 4
y = 2.5
addition = x + y
print(addition)
#%%
# OPERATOR PRECEDENCE AND ASSOCIATIVITY
# Precedence
# Associativity
print(2 + 3 * 4 / 2)
#%%
print(2 + 3 * 4)
#%%
print((2 - 3) - 4)
print(2 - (3 - 4))
#%%
print( -(3) + 2)
#%%
print(- (3 + 2))
#%%
# Chained Assignement
w = x = y = z = 0
print(w, x, y, z)
#%%
# Formatting Expressions
# 3x + 2y - 5
3*x + 2*y - 5
result = (3 * x) + (2 * y) - 5
#%%
# Errors in Python
# Syntax Errors
# Runtime Errors
# Logic Errors
#%%
# Syntax Errors
x = y + 2
y + 2 = x
x = y
y = x
#%%
x = ) 2 + 4)
#%%
x = 'Hello"
#%%
z = 1
if z == 1:
    x = 2
    y = 3

print(x, y)
#%%
# Runtime Errors
del y
x = y + 2
x = int(input("Enter the value > 0"))
y = int(input("Enter the value > 0:" ))
z = x / y
#%%
# Logic Errors
dF, dC = 0, 0
dC = (5 / 9) * (dF - 32)
print(dC)
dF = float(input("Enter the temp in degrees F: "))
dC = (5 / 9) * (dF - 32)
print(dF)
print(dC)
#%%
x = 2
y = 3
y = 2
#%%

#%%

#%%

#%%

#%%

#%%

#%%

#%%

#%%

#%%

#%%

#%%

#%%

#%%

#%%

#%%

#%%

#%%

#%%

#%%

#%%

#%%

#%%


#%%

#%%

#%%

#%%

#%%

#%%

#%%

#%%

#%%

#%%

#%%

#%%

#%%

#%%

#%%

#%%