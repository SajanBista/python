# Abnormal Loop Termination

# If we look at the code below, it demonstrates the top-exit behavior.
x = 10
while x == 10:
    print('First print statement in the while loop')
    print('2nd print statement in the while loop')
    print('3rd print statement in the while loop')
    x = 6 # Assigning new value to x makes Condition no longer true; do we exit immediately?
    break
    print('4th print statement in the while loop') # No, this line will be displayed
    # break
#%%
# This code sums up only the positive numbers and ends on recieving the -ve numbers.
entry = 0               # Ensure the loop is entered
sum = 0                 # Initialize sum

# Request input from the user
print("Enter numbers to sum, negative number ends list:")

while True:                                     # Loop forever? Not really
    entry = int(input("Enter the number:"))     # Get the value
    if entry < 0:                               # Is number negative number?
        break                                   # If so, exit the loop
    sum += entry                                # Add entry to running sum

print("Sum =", sum)                             # Display the sum

#%%
# We can use the breakstatement inside a forloop as well.
word = input("Enter text (no X's, please): ")
vowel_count = 0
for c in word:
    if c == 'A' or c == 'a' or c == 'E' or c == 'e' \
        or c == 'I' or c == 'i' or c == 'O' or c == 'o' or c == 'U' or c == 'u':
        print(c, ', ', sep='', end='')      # Print the vowel
        vowel_count += 1                    # Count the vowel
    elif c == 'X' or c =='x':               # break the loop if x is found in the word.
        break

print(' (', vowel_count, ' vowels)', sep='')

#%%
# The continue Statement
"""The continue statement is similar to the break statement, except the continue
statement does not necessarily exit the loop"""
sum = 0
done = False
while not done:
    val = int(input("Enter positive integer (999 quits):"))
    if val < 0:
        print("Negative value", val, "ignored")
        continue                                # Skip rest of body for this iteration
    if val != 999:
        print("Tallying", val)
        sum += val
    else:
        done = (val == 999)                     # 999 entry exits loop

print("sum =", sum)
#%%
# We can use else part of the if-else control flow instead of 'continue' statement
# Here is the program flow.
print(" This control flow uses no 'continue' statement")
sum = 0
done = False
while not done:
    val = int(input("Enter positive integer (999 quits):"))
    if val < 0:
        print("Negative value", val, "ignored")
    else:
        if val != 999:
            print("Tallying", val)
            sum += val
        else:
            done = (val == 999)                   # 999 entry exits loop
print("sum =", sum)
#%%



#%%
