# "for" Loop # Numeric values starts from "0" in Python.
for n in (1, 2, 3, 4, 5, 6, 7, 8, 9, 10):
    print(n)
#%%
# 'for' loop using "range" function
for n in range(0, 11):      # range(start, end, step) --> |0 --- |11
    print(n)
#%%
# General form of "range" function:- range( begin,end,step )

# 'for' loop to iterate in reverse direction using "range" function
for n in range(21, 4, -3):
    print(n, end=' ')
#%%
# 'for' loop to sum from 1 to 100
sum = 0 # Initialize sum
for i in range(1, 10):
    sum += i
print(sum)
#%%
# We can use a for loop to iterate over the characters that comprise a string
word = input('Enter a word: ')
for letter in word:
    print(letter, end =' ' )

#%%
# 'for' loop to iterate over a literal string.
for c in 'PRUTHVIRAJA L':
    print('[', c, ']', end='', sep='')
print()
print()
print()
print()
#%%
# 'for' loop  can be used to count the number of vowels in the text provided by the user
word = input('Enter text: ')
vowel_count = 0
for c in word:
    if c == 'A' or c == 'a' or c == 'E' or c == 'e' \
    or c == 'I' or c == 'i' or c == 'O' or c == 'o' or c == 'U' or c == 'u':
        print(c, ', ', sep='', end='') # Print the vowel
        vowel_count += 1 # Count the vowel
print(' (', vowel_count, ' vowels)', sep='')

#%%
# Nested loops

# Try to bridge a nested loop to display a product matrics
# Get the number of rows and columns in the table
size = int(input("Please enter the table size: "))
# Print a size x size multiplication table
# First initialize the row number
for row in range(1, size + 1):
    # Initialize the column number
    for col in range(1, size + 1):
        # Get the position of each matrics element
        print("Row#", row, "Col#", col, sep='', end=' ')
    print()

#%%
# Converting the above program to matrix product form
# Get the number of rows and columns in the table
size = int(input("Please enter the table size: "))
# Print a size x size multiplication table
for row in range(1, size + 1):
    for column in range(1, size + 1):
        product = row*column          # Compute product
        print(product, end='  ')     # Display product
    print()                           # Move cursor to next row

#%%
# We can use string formatter to line up the column values.
#%%
# Nested loops are necessary when an iterative process itself must be repeated.
# Let's talk about the permutation of the letters in word.
# The first letter varies from A to C
for first in 'ABC':
    for second in 'ABC': # The second varies from A to C
        if second != first: # No duplicate letters allowed
            for third in 'ABC': # The third varies from A to C
                # Don't duplicate first or second letter
                if third != first and third != second:
                    print(first + second + third)
#%%
#

for first in 'ABC':                             # The first letter varies from A to C
    for second in 'ABC':                        # The second varies from A to C
        if second != first:                     # No duplicate letters allowed
            for third in 'ABC':                 # The third varies from A to C
                # Don't duplicate first or second letter
                if third != first and third != second:
                    print(first + second + third)
# Total for loops (3rd inner most loop * 2nd inner most loop * 1st outer most loop)
# The control flow loop operation goes from inner most loop to outermost loop
# Once it enters in to the inner most loop from the ourter most loop.
# Moving from 1st for loop to 3rd for loop with the condition in 2nd for loop
# 1st for loop (A)
# 2nd for loop (A) and Condition (A != A)  - False
# Body of the if statement will not be evaluated.
# 2nd for loop (B) and Condition (B != A)  - True
# Body of the if statement will be evaluated and 3rd for loop activate to loop itself
# Now we are at 3rd for loop
# 3rd for loop (A) and Condition (A != A and A != B) - False
# Since we are in inner most 3rd loop, this loop repeats itself first
# 3rd for loop (B) and Condition (B != A and B != B) - False
# 3rd for loop (C) and Condition (C != A and C != B) - True [it prints ABC]
# 3rd for loop completed its looping for the second element (B) in the 2nd for loop
# AGAIN THE CONTROL FLOW CHECK FOR LAST ELEMENT IN THE 2ND LOOP (i.e C)
# We are at 2nd for loop
# 2nd for loop (C) and Condition (C != A)  - True
# Body of the if statement will be evaluated and 3rd for loop will activate to loop itself again
# 3rd for loop (A) and Condition (A != A and A != C) - False
# 3rd for loop (B) and Condition (B != A and B != C) - True [it prints ACB]
# We are at 3rd for loop still with the last element (C)
# 3rd for loop (C) and Condition (C != A and C != C) - False

# SIMILARLY WE NEED TO ANALYZE THE CODE FOR REMAINING 2 ELEMENTS OF THE 1ST FOR LOOP
#%%
# Try executing the prgram to print Each string in a permutation of ABCD.

#

#%%
