# Get the number of rows and columns in the table
size = int(input("Please enter the table size: "))
# Print a size x size multiplication table
for row in range(1, size + 1):
    for column in range(1, size -int(size/2) + 1):  # we can reduce the column size to size/2 
        product = row*column                        # Compute product
        print(product, end=' ')                     # Display product
    print()                                         # Move cursor to next row


x = 10
while x == 10:
    print('First print statement in the while loop')
    x = 5 # Condition no longer true; do we exit immediately?
    print('Second print statement in the while loop')