# Errors and Exceptions Introduction

#%%
# Syntax Error
print('Hello Welcome')
#%%
# One more example of syntax error
if 2 > 1:                    # We have missed ":" in if statement
    print("2")
#%%
import builtins
print(help(builtins))
print(dir(builtins))
#%%
# Python Exceptions
a = int(input("Enter the value of a: "))
b = int(input("Enter the value of b: "))
division = a / b
# We will get "ZeroDivisionError: division by zero" if we use "0" for b
print("Division of a divided by b is: ", division)
#%%
# Built-in Exceptions
# AssertionError in python
# help('assert')
assert(1==1)
assert(1 == 2)
#%%
# AttributeError in python
# help("AttributeError")
value1 = 10
value1.find()
#%%
# EOFError in Python
# This Python exception raises when the input() read
# function reaches the end-of-file condition means Read beyond end of file.
# help("EOFError")
#%%
# FloatingPointError in Python

# When a floating point operation fails, this python error occurs.

#%%
# GeneratorExit in python

# This raises when a generator’s close() method is called.
#%%
# ImportError in Python

# When the imported module isn’t found, an ImportError occurs.
from pandas import text
#%%

#%%
# IndexErrorin Python

# When you access an index, on a sequence, that is out of range, you get an IndexError.
list1 = [1, 2, 3, 4]
list1[3]
#%%
# KeyError in Python

# This raises when a key isn’t found in a dictionary.
dict1={1:1,2:2, 3:4}
dict1[5]
#%%
# KeyboardInterrupt in Python
# This one occurs when the user hits the interrupt key (Ctrl + C).
# while True:
#     print("Hello Welcome")
#%%
# MemoryError in Python

# This raises when an operation runs out of memory.
#%%
# ModuleNotFoundError in Python

# When you import a module that does not exist, you will get the ModuleNotFoundError.
import pandas as pd
#%%
# NameError in Python

# A NameError occurs when a name isn’t found in a scope or not defined so far
bird #= 'hen'
#%%
# NotImplementedError in Python

# An abstract method raises a NotImplementedError.
#%%
# OSError in Python

# OS Error is raised when a system operation causes a system-related error.
#%%
# OverflowError in Python

# This raises when the result of an arithmetic operation is too large to be represented.
#%%
# ReferenceError in Python

# This is raised when a weak reference proxy is used to access a garbage collected referent.
#%%
# RuntimeError in Python

# When an error does not fall under any specific category, we call it a RuntimeError.
#%%
# StopIteration in Python

# The next() function raises StopIteration to indicate that no further item is to be returned by the iterator.
def count():
    n=3
    while(n>0):
        yield n
        n-=1
c=count()
# Use 'next(c)' untill the intepreter through "stop iteration" error.
#%%
# IndentationError in Python

# An IndentationError raises on incorrect indentation.
print("hi")
print("Hi")
#%%
# TabError in Python

# When the indentation is inconsistent in tabs and spaces, there’s a TabError.

#%%
# SystemError in Python
# When the interpreter detects an internal error, it’s a SystemError.
#%%
# SystemExit in Python

# The sys.exit() function raises this one.
#%%
# TypeError in Python

# When you apply a function or an operation to an object of incorrect type, you get a TypeError.
summation = 2 + '3'
#%%
# UnboundLocalError in Python

# You get an UnboundLocalError when you try to access a local variable without first assigning a value to it.
def count():
    a = 0
    a += 1
    print(a)
# Calling after defining the count
count()
#%%
# UnicodeEncodeError in Python

# This is a Unicode error during encoding.
#%%
# UnicodeDecodeError in Python

# The Unicode error during decoding is termed UnicodeDecodeError.
#%%
# UnicodeTranslateError in Python

# A UnicodeTranslateError occurs during translating.
#%%
# ValueError in Python

# You get a ValueError when you send in an argument of the correct type, but an improper value.
# If we use floating point number instead of integer type we get an error.
a = int(input())
print(a)
#%%
# ZeroDivisionError in Python
a = 1
b = 0
c = a / b
print(c)
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