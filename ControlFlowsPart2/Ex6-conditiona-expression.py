# Conditional expression and its use

# Without conditional expression

# Get the dividend and divisor from the user
dividend = int(input('Enter dividend: '))
divisor = int(input('Enter divisor: '))
# We want to divide only if divisor is not zero; otherwise,
# we will print an error message
if divisor != 0:
    print(dividend/divisor)
else:
    print('Error, cannot divide by zero')

# WITH conditional expression
# Get the dividend and divisor from the user
dividend = int(input('Enter dividend: '))
divisor = int(input('Enter divisor: '))
# We want to divide only if divisor is not zero; otherwise,
# we will print an error message
# Var   = expression1      if condition    else  expression2
message = dividend/divisor if divisor != 0 else 'Error, cannot divide by zero'
print("Message:", message)


# Finding absolute value:
# Acquire a number from the user and print its absolute value.
n = int(input("Enter a number: "))
print('|', n, '| = ', (-n if n < 0 else n), sep='')
# Without sep
# print('|', n, '| = ', (-n if n < 0 else n))
