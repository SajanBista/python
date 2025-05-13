# Pass statement and how it works?:

# Using without pass statement:
x = int(input("Enter the value of x: "))
##if x < 0:
##    # Do nothing (This will not work!)
##else:
##    print(x)

### Using pass statement:
if x < 0:
    pass # Do subtraction operation.
else:
    print(x)

# This is equivalent to writing;
if x >= 0:
    print(x)

# Use of non-functional else block;
if x == 2:
    print(x)
else:
    pass # Do nothing if x is not equal to 2
