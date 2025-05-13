# CONTROL FLOWS:
# simple if statement

age = int(input("Enter your age in number: "))

print('Your age is :', age)

if age >= 18:
    print("You can vote with your voter ID proof.")
    print("You can also vote with any Govt.ID proof if you have a name.")


if age < 18:
    print("Your age is not 18, so you can't vote now.")
