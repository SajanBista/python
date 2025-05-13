### Ex1: Program to check whether the numbers are same or not 
##x=int(input("Enter x value: "))
##y=int(input("Enter y value: "))
##if x == y: 
##    print("x is same as y") 
##else: 
##    print("x is different from y") 

# Ex2: Code block to use the test conditions later in some program.

x = 10 
y = 20
print("x =", x, "and ", "y =", y)
b1 = (x == 10) # assigns True to b1
print("b1 condition is: ", b1)
b2 = (x != 10) # assigns False to b2
print("b2 condition is: ", b2)
b3 = (x == 10 and y == 20) # assigns True to b3
print("b3 condition is: ", b3)
b4 = (x != 10 and y == 20) # assigns False to b4
print("b4 condition is: ", b4)
b5 = (x == 10 and y != 20) # assigns False to b5
print("b5 condition is: ", b5)
b6 = (x != 10 and y != 20) # assigns False to b6
print("b6 condition is: ", b6)
b7 = (x == 10 or y == 20) # assigns True to b7
print("b7 condition is: ", b7)
b8 = (x != 10 or y == 20) # assigns True to b8
print("b8 condition is: ", b8)
b9 = (x == 10 or y != 20) # assigns True to b9
print("b9 condition is: ", b9)
b10 = (x != 10 or y != 20) # assigns False to b10 
print("b10 condition is: ", b10)
