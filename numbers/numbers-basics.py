# Python Numbers
# Python numeric types: int, float and complex numbers
# Int
#help(int)
#dir(int)
# The Integer type in Python is represented using a int class.
a = 5
print(a)
#%% type method
print(type(a))
#%% long value
a = 1234567890000012345678900000
print(type(a))
#%%
# Python isinstance() function:
print(isinstance(a, bool))
print(isinstance(a, int))
#%%
# Exponential e to create exponential numbers of base 10
a = 2e2         # It is equivalent to 2 * 10 ** 2
print(a)
print(type(a))
print()
b = 2 * 10 ** 2
print(type(b))
#%%
# Python float
a = 1.123445000002
print(a)
# A float value is only accurate upto 15 decimal places.
a = 1.2345890000000012347898
print(a)
#%%
# division results in floating point number.
a = 2
b = 3
divide = a / b
print(divide)
#%%
# Python Complex Numbers -> a + bj
z = 2 + 3j
print(z)
print(type(z))

#%%
# providing coefficient for 'j' is mandatory to create complex number
z = 3 + j
print(z)
# It results an error.
#%%
# We can use 1 to create complex number with the imaginary part
z = 3 + 1j
print(z)
#%%
a = 2 + 2j
b = 1 + 1j
# We can use arithmetic operations on complex numbers as well,
# Remember that j^2 = -1
print(a + b)
print(a - b)    # (2 + 2j) - (1 + 1j)
print(a * b)    # (2 + 2j) * (1 + 1j) = 2 + 2j + 2j -2
print(a / b)    # (2 + 2j) / (1 + 1j)
print((1j)**2)
#%%
# We can also use inplace assignment operator on complex number
a = 2 + 2j   # a += b
a += 2 + 4j     # a = a + b
print(a)
#%%
# Writing numbers in binary, octal, and hexadecimal in Python
# We can write a binary number using the prefix 0b or 0B
bn1 = 0b1011
print(type(bn1))
print(bn1)
bn2 = 0B1011
print(bn2)
#%%
# We can convert the binary numbers in to an int using int function
print(int(0b1011))
#%%
# Octal Numbers in Python : Uses prefix 0o or 0O
oc1 = 0o1234
print(oc1)
oc2 = 0O1234
print(oc2)

#%%
#  Octal number has the numbers from 0-7
oc3 = 0o12347
print(oc3)
#%%
# Hexadecimal Numbers in Python
# The hexadecimal number system has numbers 0-9 and then A-F.
# and the prefix as 0x or 0X.
hexa1 = 0x1234
print(hexa1)
hexa2 = 0x12A   #
print(hexa2)
#%%
print(0XA)
print(0XB)
print(0XC)
print(0XD)
print(0XE)
print(0XF)
#%%
# Python Conversion Functions
# int() in Python
num1 = 2.745678
print(num1)
num2 = int(num1)
print(num2)

#%%
# We can't convert complex to int
a = 2 + 2j
b = int(a)
c = 2j
d = int(c)
#%%
# We can convert floats, binary, octal and hexadecimal number to an int
print(int(0b1011))
print(int(0o1234))
print(int(0x1234))
#%%
print(float(12))
print(float(2 + 7j)) # It results an error
print(float(0b1011))
print(float(0o1234))
print(float(0x1234))
#%%
# complex() in Python
print(complex(2, 3))
print(complex(2))
print(complex(8j))
print(complex(2 + 3.784j))
a = 4
b = 3
print(complex(a, b))
#%%
# bin() in Python
print(bin(10))
print(bin(200))
print(bin(255))
print(bin(256))
#%%
# We can' convert float and complex numbers to binary form.
print(bin(12.0))
print(bin(2 + 5j))
#%%
# oct() in Python
print(oct(9))
print(oct(255))
print(oct(200.78)) # It returns error
#%%

#%%
# hex() in Python
print(hex(255))
print(hex(234.9))
print(hex(0))
print(hex(1))
print(hex(9))
print(hex(10))
print(hex(10+2j))
#%%
# Number Type Conversion
# Implicit Type Conversion
x = 99
y = 1.111
z = x + y
print(z)
print(type(z))

#%%
# Explicit Type Conversion
a = 30
b = 'Pruthvi'
print(type(str(a)))
print(str(a) + ' ' + b)
#%%
# MATH Module Methods To Work With The Numerical Data
import math as m
# ceil  -- Up to the nearest integer value
# floor -- Down to the nearest integer value
a = 1.7
print(m.ceil(a))
print(m.floor(a))
#%%
# Degrees and Radians
# math module provides constants like - pi
print(m.pi)
print(m.degrees(m.pi))
print(m.radians(90))
#%%
# sin and cos functions
# sin()
# cos()
# tan()
r_90 = m.radians(90)
print(r_90)
print(m.sin(r_90))
r_90 = m.radians(90)
print(r_90)
print(m.cos(r_90))
print(m.tan(r_90))
#%%
# Factorial function
# Factorial of 4 = 4*3*2*1
print(m.factorial(4))
#%%
# fabs and trunc
print(m.fabs(-100))
print(m.trunc(-12.56))
#%%
# pow and log
x = 2
y = 3
print(m.pow(x, y)) # 2^3
print(m.log(100))

#%%
# isinf(), isfinite(), isnan()
print(m.isfinite(m.inf))
print(m.isinf(m.nan))
print(m.isnan(4))
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



























