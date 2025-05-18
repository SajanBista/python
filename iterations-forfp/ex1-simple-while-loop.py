# Why we need Iterations:

# Printing numbers from 1 to 5 using print statement
print(1)
print(2)
print(3)
print(4)
print(5)
#%%
# The same can be achieved using the "while" Loop
count = 1          # Initialize counter
while count <= 5:  # Should we continue?
    print(count)   # Display counter, then
    count += 1     # Increment counter

#%%
# Let’s check the program with the count = 6 instead of 5 and see what happens:
count = 6         # Initialize counter; check the program with count = 6
while count <= 5: # Should we continue?
    print(count)  # Display counter, then
    count += 1    # Increment counter
#%%
# Code to count the number of correct entries of "Y or y"
# Counts up from zero. The user continues the count by entering
# 'Y'. The user discontinues the count by entering 'N'.

count = 0                           # The current count
entry = 'Y'                         # Count to begin with

while entry != 'N' and entry != 'n':
    # Print the current value of count
    print(count)
    entry = input('Please enter "Y" to continue or "N" to quit: ')
    if entry == 'Y' or entry == 'y':
        count += 1                  # Keep counting
    # Check for "bad" entry
    elif entry != 'N' and entry != 'n':
        print('"' + entry + '" is not a valid choice')
    # else must be 'N' or 'n'
#%%
# Allow the user to enter a sequence of nonnegative
# integers. The user ends the list with a negative
# integer. At the end the sum of the nonnegative
# numbers entered is displayed. The program prints
# zero if the user provides no nonnegative numbers.

entry = 0   # Ensure the loop is entered
sum = 0     # Initialize sum

# Request input from the user
print("Enter numbers to sum, negative number ends list:")

while entry >= 0:               # A negative number exits the loop
    entry = int(input("Enter positive numbers for addition: "))        # Get the value
    if entry >= 0:              # Is number nonnegative?
        sum += entry            # Only add it if it is nonnegative
print("Sum =", sum)             # Display the sum
#%%
# In Python, sometimes it is convenient to use a simple value as conditional
# expression in an if or while statement
x = int(input()) # Get integer from user
while x:
    print(x)        # Print x only if x is nonzero
    x -= 1          # Decrement x

# is equivalent to
x = int(input())    # Get integer from user
while x != 0:
    print(x)        # Print x only if x is nonzero
    x -= 1          # Decrement x
#%%
# How to use floating point numbers properly in any loops
# Example below shows an incorrect way of using the floating point number.
x = 0.0
while x != 1.0:
    print(x)
    x += 0.1
print("Done")
#%%
# The correct method is either using x += 0.125 or using x <= 1.0 in the while statement
# Using x += 0.125 in increment statement
x = 0.0
while x != 1.0:
    print(x)
    x += 0.125
print("Done")

# Using x <= 0.1 in while statement
x = 0.0
while x <= 1.0:
    print(x)
    x += 0.1
print("Done")
#%%

