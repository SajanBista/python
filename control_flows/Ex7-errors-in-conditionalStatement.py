# Errors in conditional statements:
# value = 10
# value < 0 or value > 10
# value > 0 and value <= 10
# x > 0 or x <= 10 (True always -> Tautology)
# False always -> contradictions
value = int(input())
if value < 0 or value > 10:
    print(value)
# 
x = 4
if 1 <= x <= 3:
    print("ok")
#
if (x == 1) or 2 or 3:
    print("ok")
# 
if (x == 1) or x == 2 or x == 3:
    print("ok")
#%%
# Digit to word converter (Syntax error)
value = int(input("Please enter an integer in the range 0...5: "))
answer = "not in range"     # Default answer
if value == 0:
    answer = "zero"
elif value == 1:
    answer = "one"
elif value == 2:
    answer = "two"          #
elif value == 3:
    answer = "three"        # Replace m by n
elif value == 4:
    answer = "four"
elif value == 5:
    answer = "five"
print("The number you entered was", answer)
#%%