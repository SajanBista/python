# Ex1 Nested if statement

# To check the number between 0 and 10
# value = int(input("Please enter an integer value in the range 0...10: "))
# if value >= 0 :         # First check
#     if value <= 10:     # Second check
#         print("In range")

# print("Done")

# Ex2: To check the number between 0 and 10 only with single if statement

value = int(input("Please enter an integer value in the range 0...10: "))
if value >= 0 and value <= 10 : # Only one, slightly more complicated check
    print("In range")
print("Done")


# Ex3: Must and should use else part

value = int(input("Please enter an integer value in the range 0...10: "))
if value >= 0:          # First check
    if value <= 10:     # Second check
        print(value, "is in range")
    else:
        print(value, "is too large")
else:
    print(value, "is too small")

print("Done")
