# Perform division operation.

# Get two integers from the user

print('Please enter two numbers to divide.')
dividend = int(input('Please enter the first number to divide: '))
divisor = int(input('Please enter the second number to divide: '))

# If possible, divide them and report the result

if divisor != 0:
    print(dividend, '/', divisor, "=", dividend / divisor)

#-------------------------------------------------------------
# Alternative division

# Get two integers from the user
dividend = int(input('Please enter the number to divide: '))
divisor = int(input('Please enter dividend: '))

# If possible, divide them and report the result
if divisor != 0:
    quotient = dividend/divisor
    print(dividend, '/', divisor, "=", quotient)
    print('Program finished')
#%%
x = 8
if x < 10: y = x


print('y = ', y)
#%%
x = 8
if x < 10:
    y1 = x #pass
    print('y1 = ', y1)
y = x
print('y = ', y)
#%%