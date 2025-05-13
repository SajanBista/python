""" TUPLES """
# Tuples:
#
""" Tuple is a collection of Python objects much like a list.
The sequence of values stored in a tuple can be of any type, and they are indexed
by integers. """
#%%
# Values of a tuple are syntactically separated by 'commas'.
""" Creating a Tuple"""
tuple1 = (1, 2, 3, 4)
print(tuple1)
# Check the type using type method
print(type(tuple1))
#%%
# Creation of Python tuple without the use of parentheses is known as Tuple Packing.
tuple2 = 1, 2, 3, 4, 5, 6, 7, 8, 9, 10
print(tuple2)
#%%
# We can create an empty tuple with the help of () only
tuple3 = ()
print(tuple3)
#%%
# We can use lists to create a tuple, for that we need to pass the list as an object
# inside the 'tuple' object
list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
tuple4 = tuple(list1)
print(tuple4)
#%%
# Tuples can contain heterogeneous data type means elements with different data types
tuple5 = ('Pruthvi', "Welcome", 'To', "Python", 'Course', 1, 2, 3, [10, 20, 30])
print(tuple5)
print(type(tuple5))
#%%
# To create a single element tuple, we need to use "," after the single element
tuple6 = (1,)
print(tuple6)
#%%
# We can repeat the tuple elements isnside the tuple with multiplication operator
tuple7 = tuple4 * 2
print(tuple7)
#%%
" TUPLE ATTRIBUTES & METHODS USING DIR "
# Since tuples are immutable, we can't find more methods or attributes on them
# compared to lists and other mutable data types
print(dir(tuple))
#%% These are the attributes and methos
""" ['__add__', '__class__', '__class_getitem__', '__contains__', '__delattr__',
'__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__',
'__getitem__', '__getnewargs__', '__gt__', '__hash__', '__init__',
'__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__mul__',
'__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__rmul__',
'__setattr__', '__sizeof__', '__str__', '__subclasshook__', 'count', 'index'] """
#%%
# index( )	Find in the tuple and returns the index of the given value where it's available
#           0           1        2      3           4     5  6  7      8
tuple8 = ('Pruthvi', "Welcome", 'To', "Python", 'Course', 1, 2, 3, [10, 20, 30])
print(tuple8.index('To'))
print(tuple8.index("Python", 4, 8))
print(tuple8.index("Python", 3, 8))
#%%
# count( )	Returns the frequency of occurrence of a specified value
tuple9 = ('Pruthvi', "Welcome", 'To', "Python", 'Course', 1, 2, 3, 3, [10, 20, 30])
print(tuple9.count('To'))
print(tuple9.count(3))
#%%
""" Applying Built-In Functions On Tuples """
"""
Built-in Function :	Description
all():	  Returns true if all element are true or if tuple is empty
any():	  eturn true if any element of the tuple is true. if tuple is empty, return false
len():	  Returns length of the tuple or size of the tuple
enumerate():	Returns enumerate object of tuple
max():	return maximum element of given tuple
min():	return minimum element of given tuple
sum():	Sums up the numbers in the tuple
sorted():	input elements in the tuple and return a new sorted list
tuple():	Convert an iterable to a tuple.
"""
#%%
# "all" method
# Returns true if all element are true or if tuple is empty
tuple10 = ('Pruthvi', "Welcome", 'To', "Python", 'Course', 1, 2, 3, 3, [10, 20, 30])
print(all(tuple10))
tuple11 = ()
print(all(tuple11))
tuple12 = (0,)
print(all(tuple12))
#%%
tuple13 = ('Pruthvi', "Welcome", 'To', "Python", 'Course', 1, 2, 3, 3, [10, 20, 30])
print(any(tuple13))
tuple14 = () # We can use (0,) to check for the False as 0 is considered as False in Python
print(any(tuple14))
#%%
# len():	  Returns length of the tuple or size of the tuple
print(len(tuple13))
#%%
# max():	return maximum element of given tuple
# For this method all the elements must be of the same type
tuple15 = (1, 2, 3, 3, 10, 20, 30)
print(max(tuple15))
# If we use strings lowercase letters are given highest priority than uppercase letters
# Between a-z 'w' is the highest alphabet and hence the word "Welcome" is the max element
tuple16 = ('pruthvi', "welcome", 'to', "python", 'course')
print(max(tuple16))
#%%
# min():	return minimum element of given tuple
tuple17 = (1, 2, 3, 3, 10, 20, 30)
print(min(tuple17))
# If we use strings uppercase letters are given highest priority than lowercase letters
# Between A-Z 'p' is the highest alphabet and hence the word "Python" is the min element
tuple18 = ('pruthvi', "welcome", 'to', "Python", 'course')
print(min(tuple18))
#
tuple19 = ('pruthvi', "welcome", 'to', "Python", 'Course')
print(min(tuple19))
#%%
# sum():	Sums up the numbers in the tuple
tuple20 = (1, 2, 3, 3, 10, 20, 30)
print(sum(tuple20))
#%%
# sorted():	input elements in the tuple and return a new sorted list
tuple21 = (40, 2, 3, 5, 50, 20, 30)
print(sorted(tuple21))
#%%
# We can use the in-built tuple function to get the original tuple after sorted
tuple22 = tuple(sorted(tuple21))
print(tuple22)
#%%
""" Since Tuples are Immutable objects We Can't Apply Arithmetic Operators On Tuples"""
# We can use concatinatio method to add two tuples with the '+' operator
tuple23 = (1, 2, 3, 4, 5)
tuple24 = (3, 4, 5, 6, 7)
tuple25 = tuple23 + tuple24
print(tuple25)
#%%
# Tuple Unpacking
# In unpacking of tuple number of variables on the left-hand side should be equal
# to a number of values in a given tuple
a, b, c, d, e = tuple23
print(a, b)
#%%
"""  INDEXING & SLICING IN TUPLES"""
# Index method has Start and End index positions like [start:end]
# Lower index position is inclusive & end index position is exclusive
tuple26 = ('Pruthvi', 'Raja', 'Python', 'Welcome', 1,  2,  3,  4,  5,  5)
#      0,       1,       2,       3,       4,  5,  6,  7,  8,  9
# ('Pruthvi', 'Raja', 'Python', 'Welcome', 1,  2,  3,  4,  5,  5)
# To get the range of values mention the start and end index positions

# To get values we can use index method
print(tuple26[0])
print(tuple26[2])
# Negative index starts from -1 from the right side
#      -10,     -9,      -8,       -7,    -6, -5, -4, -3, -2, -1
# ['Pruthvi', 'Raja', 'Python', 'Welcome', 1,  2,  3,  4,  5,  5]
print(tuple26[-6])

# SLICING IN TUPLES
print(tuple26[0:3])
# If we don't mention the start index by default it is set to '0'
# To print elements from beginning to a range used:
print(tuple26[:4])
# If we don't mention the end index position by default it is set to 'len(list)-1'
# To print elements from a specific Index till the end of the tuple length
print(tuple26[3:])
# If start > end in [start:end], then empty tuple will be created
# start should be greater than end in positive indexing
print(tuple26[5:2])
# We can use negative index
# Negative index starts from -1 from the right side
#      -10,     -9,      -8,       -7,    -6, -5, -4, -3, -2, -1
# ['Pruthvi', 'Raja', 'Python', 'Welcome', 1,  2,  3,  4,  5,  5]
# Here also we can access the particular emement like value at '-8'
print(tuple26[-8])

# If there is no end position in -ive indexing by default it is set to -1
print(tuple26[-8:])

# If there is no start position in -ve indexing by default it is set to last
# lowest negative index position
# whatever may be the case the end index position will be excluded
print(tuple26[:-7])

# We can traverse in positive direction in negative index slicing
# Means in [start:end] start should be lowest negative index position
# And end should be highest negative index position
print(tuple26[-8:-3]) # Here -8 < -3 Or we can say that -3 > -8
# Since slicing always goes from left to right and -8 is in left
# most position then -3, (-8 is the lowest index position than -3)

# If we reverse the index positions we will get an empty tuple
print(tuple26[-3:-8])
# Here -3 > -8 but we need lowest negative index position -8 at the start
# and the highest index position -3 at the end to get the range of values

# We can traverse in the positivee direction then in [start:end]
# Start should be -ve and end should be +ve like [-ve:+ve]
print(tuple26[-8:6])

# Reversing the indexing positions will give an empty tuple
print(tuple26[6:-8])
#%%
# Slicing with "::" operator
# Positive indexing
#      0,       1,       2,       3,       4,  5,  6,  7,  8,  9
# ('Pruthvi', 'Raja', 'Python', 'Welcome', 1,  2,  3,  4,  5,  5)

# Negative indexing
#      -10,     -9,      -8,       -7,    -6, -5, -4, -3, -2, -1
# ('Pruthvi', 'Raja', 'Python', 'Welcome', 1,  2,  3,  4,  5,  5)

# We can go in positive direction by skipping the index position mentioned
# in the [start::] after :: like ::skip_position
print(tuple26[2::2]) # It will skip every 2nd position element after 2 till the end

# We can use -ve skipping to go in reverse direction
print(tuple26[2::-1])

# Skipping alternative element in negative direction
print(tuple26[8::-2]) # every second element is skipped in negative direction

# We can reverse the entire list and store as a new list using ::-1
reversed_tuple = tuple26[::-1]
print(reversed_tuple)
#%%
# Tuples are immutable and hence they do not allow deletion of a part of it
# The entire tuple gets deleted by the use of del() method.
tuple27 = (1, 2, 3, 4, 5)
print(tuple27)
# Deleting using 'del' methos
del tuple27
# We can't access the tuple after its deletion
print(tuple27)
#%%
""" Tuples Are Immutable Elements """
tuple27[2] = 50
#%%

#%%

#%%

#%%

#%%

#%%

#%%

#%%

#%%

#%%

#%%

#%%

#%%

#%%

#%%

#%%

#%%

#%%

#%%

#%%

#%%

#%%

#%%

#%%

#%%

#%%

#%%

#%%

#%%

#%%

#%%

#%%

#%%

#%%

#%%

#%%

#%%

#%%

#%%

#%%

#%%

#%%

#%%

#%%

#%%

#%%

#%%

#%%

#%%

#%%

#%%

#%%

#%%

#%%

#%%

#%%

#%%

#%%

#%%

#%%

#%%

#%%

#%%

#%%

#%%

#%%

#%%

#%%

#%%

#%%

#%%

#%%

#%%

#%%

#%%

#%%

#%%

#%%

#%%

#%%

#%%

#%%

#%%

#%%

#%%

#%%

#%%

#%%

#%%

#%%

#%%

#%%

#%%

#%%

#%%

#%%

#%%

#%%

#%%

#%%

#%%

#%%

#%%

#%%

#%%

#%%

#%%

#%%

#%%

#%%

#%%

#%%

#%%

#%%

#%%

#%%

#%%

#%%

#%%

#%%

#%%

#%%

#%%

#%%

#%%

#%%

#%%

#%%

#%%

#%%

#%%

#%%

#%%

#%%

#%%

#%%

#%%

#%%

#%%

#%%

#%%

#%%

#%%

#%%

#%%

#%%

#%%

#%%

#%%

#%%

#%%

#%%

#%%

#%%

#%%

#%%

#%%

#%%

#%%

#%%

#%%

#%%

#%%

#%%

#%%

#%%

#%%

#%%

#%%

#%%

#%%

#%%

#%%

#%%

#%%

#%%

#%%

#%%

#%%

#%%

#%%

#%%

#%%

#%%

#%%

#%%

#%%

#%%

#%%

#%%

#%%

#%%

#%%

#%%

#%%

#%%

#%%

#%%

#%%

#%%

#%%

#%%

#%%

#%%

#%%

#%%

#%%

#%%

#%%

#%%

#%%

#%%

#%%

#%%

#%%

#%%

#%%

#%%

#%%

#%%

#%%

#%%

#%%

#%%

#%%

#%%

#%%

#%%

#%%

#%%

#%%

#%%

#%%

#%%

#%%

#%%

#%%

#%%

#%%

#%%

#%%

#%%

#%%

#%%

#%%

#%%

#%%

#%%

#%%

#%%

#%%

#%%

#%%

#%%

#%%

#%%

#%%

#%%

#%%

#%%

#%%

#%%

#%%

#%%

#%%

#%%

#%%

#%%

#%%

#%%

