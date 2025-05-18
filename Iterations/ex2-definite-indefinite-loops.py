# Definite Vs Idefinite Loops.
# Example1 for definite loop

n = 1
while n <= 10:
    print(n)
    n += 1
#%%
# Example2 for definite loop
n = 1
stop = int(input("Enter the number: "))
while n <= stop:
    print(n)
    n += 1
#%%
# Example3 for Indefinite loop
done = False                # Enter the loop at least once
while not done:
    entry = int(input("Enter the number: "))    # Get value from user
    if entry == 999:    # Did user provide the magic number?
        done = True     # If so, get out
    else:
        print(entry)    # If not, print it and continue
#%%

