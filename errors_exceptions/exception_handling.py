# EXCEPTION HANDLING IN PYTHON

#%%
# Try & Except Block
#%%
# Working With Try and Except Clauss

try:
     for i in range(0, 5):
         print(4 / i)
except:
     print("You divided by 0")
     print('This prints because the exception was handled')
#%%

# We know About "ZeroDvisionError":

a, b = 1, 0
print(a / b)
#%%

# The range statement starts from zero if we don't provide any start value

try:
     for i in range(5):
         print(4 / i)
except ZeroDivisionError:
     print("You tried to divide by 0")
     print('This prints because the exception was handled')
#%%

# We know that we can't use --> (int + str) to perform an addition.
# MULTIPLE EXCEPTS

a, b = 6, 0
try:
    print('20' + 10)  #TypeError
    print(a / b)    #ZeroDivisionError
    print("This statement will not execute")

except TypeError:
    print("You added values of incompatible types")
except ZeroDivisionError:
    print("You tried to divide by 0")
#%%

# EXCEPT BLOCK WITHOUT EXCEPTION (Means the statements like ZeroDevisionError)

a, b = 6, 0
try:
     print(a / b)
except:
    print("You tried to divide by 0")

print("This is out of try and except block")
#%%

# First "Type Error" Exception Will Be Identified & Then "ZeroDivisionError"

a, b = 6, 0
try:
    print('20' + 10)
    print(a / b)
except(TypeError, ZeroDivisionError):
    print("You added values of incompatible types and tried to devide by zero")
#%%

# General Except Block After All Excepts:

try:
    # print('5' + 5)
    print(add)
    print(1 / 0)
except NameError:
    print("Here add does not exist")
except ZeroDivisionError:
    print("Cannot divide by 0")
except:
    print("All exceptions are evaluated & need correction ")
#%%

# But there should be only one generic or default except block for one try block

try:
    print(1/0)
except:
    raise
except:
    print("Raised exception caught")

print("Bye")
#%%

# FINALLY BLOCK IN PYTHON

try:
    print('4' + 9)
    print(1 / 0)
except TypeError:
    print("You added values of incompatible types")
except ZeroDivisionError:
    print("Cannot divide by 0")
finally:
    print("This will print whatever may be")
#%%
# Finally runs even if the interpreter fail to catch exception

try:
    print(7 / 0)
except ZeroDivisionError:
    print(5 / 0)
finally:
    print("This will print whatever may be")
#%%

# Error Type Without Raise Keyword

print(5 / 0)

# Raise Keyword In Python

a = int(input("Enter a: "))
b = int(input("Enter b: "))
if b == 0:
    raise ZeroDivisionError

#%%
# Raise Keyword In Try and Except Blocks:

a = int(input("Enter a: "))
b = int(input("Enter b: "))
try:
    if b == 0:
        raise ZeroDivisionError
except:
    print("You tried to divid by 0")

print("Will this print? Yes")
#%%
# Raise Keyword Without Any Specified Exception In Python

try:
    print('5' + 9)
except:
    print("Type Error")
    #raise
#%%
# Raise With An Argument In Python

try:
    print('5' + 9)
except:
    raise TypeError("Inappropriate Type Error For int with str")
#%%

# Assertions In Python
assert(True)
assert(1 == 0)


#%%
# Using "raise" keyword in 'except' block.

try:
    print(10)
    assert 2 + 4 == 6
    print(20)
    assert 1 + 5 == 4
    print(30)
except:
    print("An assert failed.")
    raise
finally:
    print("Okay")

print("Bye")
#%%
# Without Using "raise" keyword in 'except' block.

try:
    print(10)
    assert 2 + 4 == 6
    print(20)
    assert 1 + 5 == 4, "This is a TypeError"
    print(30)
except:
    print("An assert failed.")
    raise
finally:
    print("Okay")

print("Bye")
#%%
# A Second Argument in assert statement along with False expression

assert False, "This is a TypeError"
#%%
class OwnError(Exception):
    print("This is a problem")

raise OwnError("Own Error Message For User Errors")

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

