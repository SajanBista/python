# 'while-else' and 'for-else' statements

# 'while-else' statement usage. Finding the avg of five unknown numbers.
# Add five nonnegative numbers supplied by the user
count = sum = 0
print('Please provide five nonnegative numbers when prompted')
while count < 5:
    # Get value from the user
    val = float(input('Enter number: '))
    if val < 0:
        print('Negative numbers not acceptable! Terminating')
        break
    count += 1
    sum += val
else:
    print('Average =', sum/count)
#%%
# We can replace the else part of the while loop using if-else statement.
# Add five nonnegative numbers supplied by the user
count = sum = 0
print('Please provide five nonnegative numbers when prompted')
while count < 5:
# Get value from the user
    val = float(input('Enter number: '))
    if val < 0:
        break
    count += 1
    sum += val
if count < 5:
    print('Negative numbers not acceptable! Terminating')
else:
    print('Average =', sum/count)

#%%
# A for statement with an else block works similarly to the while/else statement.
word = input('Enter text (no X\'s, please): ')
vowel_count = 0
for c in word:
    if c == 'A' or c == 'a' or c == 'E' or c == 'e' \
        or c == 'I' or c == 'i' or c == 'O' or c == 'o'  or  c == 'U' or c == 'u':
        print(c, ', ', sep='', end='') # Print the vowel
        vowel_count += 1 # Count the vowel
    elif c == 'X' or c =='x':
        print('X not allowed')
        break
else:
    print(' (', vowel_count, ' vowels)', sep='')

#%%








