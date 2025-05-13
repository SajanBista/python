# Correct indentation
# One TAB (or a continuous four white spaces) is the standard indentation
print("Python is important for Data Science")
print("Pandas is important for Data Science")

# Correct indentation, note that if statement here is an example of suites
x = 1
if x == 1:
    print('x has a value of 1')
    print('If x = 1; then this if block will execute')
    print("This is for indentation check")
else:
   print ('x does NOT have a value of 1')
   print("This is for indentation check")

print ("I don't know who is x, because I am not in if block")
#%%
# incorrect indentation, program will generate a syntax error
# due to the space character inserted at the beginning of second line
print("Python is important for Data Science")
print("Pandas is important for Data Science")

# Incorrect indentation, program will generate a syntax error
# due to the wrong indentation in the else statement
x = 0
if x == 2:
    print('x has a value of 2')     # press TAB before print statement
else:
    print('x does NOT have a value of 2')
    print("This line is not in line with the above print statement")
#%%