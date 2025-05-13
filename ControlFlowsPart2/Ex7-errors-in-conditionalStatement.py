# Errors in conditional statements:
# value = 10
# value < 0 or value > 10
# value > 0 and value <= 10
x = 2
if 1 <= x <= 3:
    print("ok")

# Digit to word converter (Syntax error)
value = int(input("Please enter an integer in the range 0...5: "))
answer = "not in range" # Default answer
if value == 0:
    answer = "zero"
elif value == 1:
    answer = "one"
elif value == 2:
    answer = "two"          #
elif value == 3:
    amswer = "three"        # Replace m by n
elif value == 4:
    answer = "four"
elif value == 5:
    answer = "five"
print("The number you entered was", answer)
