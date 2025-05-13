# LISTS
# Definition:

name_list = ['Pruthvi', 'Raja', 'Python', 'Welcome', 1, 2, 3, 4, 5]
print(name_list)
print(type(name_list))
#%%
help(list)
print(dir(list))

#%%
# Creation of List

# Creating an empty List
List = []
print("Blank List: ")
print(List)

# Creating a List of elements
name_list = ['Pruthvi', 'Raja', 'Python', 'Welcome', 1, 2, 3, 4, 5]
print("\nList of elements: ")
print(name_list)
#%%
# Creating a List of strings and accessing
# using index
name_list = ['Hello', 'Pruthvi', 'Raja', 'Welcome', 'To', 'Python', 'Tutorial']
print('name_list:\n', name_list, sep='')
print("\nList Items: ")
print(name_list[0])
print(name_list[1])
#%%
# List may contain duplicate elements or repeated elements
rep_list = ['Pruthvi', 'Raja', 'Python', 'Welcome', 'Welcome', 1, 2, 3, 4, 5, 5]
print("List with repeated items:")
print(rep_list)

#%%
""" Multi-ways to create lists """
# All the list objects are the objects of the list class in Python. Use the list() constructor to convert from other sequence types such as tuple, set, dictionary, string to list.

#list from homogeneous or heterogeneous elements
nums=[1,2,3,4]
print(type(nums))

# creating lists from the string
mylist=list('Hello')
print(mylist)

# creating list from the dictionary
nums=list({1:'one',2:'two'})
print(nums)

# list from the tuple
nums=list((10, 20, 30))
print(nums)

# list from the set
nums=list({100, 200, 300})
print(nums)

#%%
""" Nested lists OR MULTI-DIMENSIONAL LISTS """

nested_list = [['Pruthvi', 'Raja', 'Python', 'Welcome'], 'Welcome', 1, 2, 3, 4, 5, 5]
print("Nested List:")
print(nested_list)
list2 = ['Pruthvi', 'Raja', 'Python', 'Welcome']
nested_list2 = [list2, 'Welcome', 1, 2, 3, 4, 5, 5]
print('Nested List With Variable "list2" as the list element:')
print(nested_list2)
#%%
""" CREATING MULTIDIMENSIONAL LISTS """

# Nested lists or multi-dimensional lists
nested_list_1d = ['Pruthvi', 'Raja', 'Python', 'Welcome', 'Welcome', 1, 2, 3, 4, 5, 5]
print(type(nested_list_1d))
nested_list_2d = [['Pruthvi', 'Raja'], 'Python', 'Welcome', 'Welcome', 1, 2, 3, 4, 5, 5]
print(type(nested_list_2d))
nested_list_3d = [[['Pruthvi', 'Raja'], ['Python', 'Welcome']], 'Welcome', 1, 2, 3, 4, 5, 5]
print(type(nested_list_3d))
#%%
"""ACCESSING MULTIDIMENSIONAL LIST ELEMENTS"""

# Accessing multi-dimentional lists
sublist_2d = nested_list_2d[0]
print(sublist_2d)
print(type(sublist_2d))
# element at the 0th index position in sublist_2d
print(sublist_2d[0])
# element at the 1st index position in sublist_2d
print(sublist_2d[1])
# checking the type of first element in the 2d list
print(type(sublist_2d[0]))
# we can use the direct multiindexing method to access the elements from the
# multidimensional lists
# accessing the element at the 0th index position of first-nested list
# using multi-index method
print(nested_list_2d)
print(nested_list_2d[0][0])
# accessing the element at the 1st index position of first-nested list
print(nested_list_2d[0][1])
# accessing the element at the 1st index position of 2d list
print(nested_list_2d[1])
# accessing the element at the 2nd index position of 2d list
print(nested_list_2d[2])
#%% Similarly we can Access 3d list elements
""" ACCESSING 3DIM LIST ELEMENTS """

print((nested_list_3d))
# accessing the 2d list from the 3d list
list_2d = nested_list_3d[0]
print(list_2d)
# accessing first sublist from the 2d list
first_sublist_in_2d = list_2d[0]
print(first_sublist_in_2d)
# accessing the element at the 0th index position in first_sublist_in_2d
print(first_sublist_in_2d[0])
# accessing the element at the 1st index position in first_sublist_in_2d
print(first_sublist_in_2d[1])

# directly we can apply multi-index method to access the elements 3d list
# accessing 2d list from the 3d list
print(nested_list_3d[0])
# accessing the first sublist from the 2d list extracted from the 3d list
print(nested_list_3d[0][0])
# accessing the element at the 0th index position in the first sublist of 2d list
print(nested_list_3d[0][0][0])
# accessing the element at the 1st index position in the first sublist of 2d list
print(nested_list_3d[0][0][1])
# accessing the second sublist in 2d list
print(nested_list_3d[0][1])
# accessing the element at the 1st index position in the second sublist of 2d list
print(nested_list_3d[0][1][1])
#%%
""" INDEX ERROR """

# If we try to use the index position which is greater than the lentht of the list
# then we get out of index position error
nested_list_1d = ['Pruthvi', 'Raja', 'Python', 'Welcome', 'Welcome', 1, 2, 3, 4, 5, 5]
print(len(nested_list_1d))
print(nested_list_1d[10]) # final element is at "len(list)-1"
print(nested_list_1d[11])
#%%
""" ACCESSING USING NEGATIVE INDEXING """

list1d = ['Pruthvi', 'Raja', 'Python', 'Welcome', 1, 2, 3, 4, 5, 5]
print(len(list1d))
# Positive index starts from 0 from the left side
#      0,       1,       2,       3,       4,  5,  6,  7,  8,  9
# ['Pruthvi', 'Raja', 'Python', 'Welcome', 1,  2,  3,  4,  5,  5]
print(list1d[0])
print(list1d[9])
# Negative index starts from -1 from the right side
#      -10,     -9,      -8,       -7,    -6, -5, -4, -3, -2, -1
# ['Pruthvi', 'Raja', 'Python', 'Welcome', 1,  2,  3,  4,  5,  5]
print(list1d[-1])
print(list1d[-2])
print(list1d[-3])
print(list1d[-4])
print(list1d[-5])
print(list1d[-10])
#%%
""" How to get the length of the List """
# We can use the 'len' function to get the length of the list
list1d = ['Pruthvi', 'Raja', 'Python', 'Welcome', 1, 2, 3, 4, 5, 5]
print(len(list1d))
#%%
""" We can use Input function to create a list from the user entered values"""

string = input("Enter any type of elements separated by space:" )
list_from_string = string.split(sep=' ')
print(list_from_string)
#%%
""" How to get range of values from the list"""
# WE CAN USE SLICING METHOD TO SLICE THE RANGE OF VALUES BETWEEN
# LOWER AND UPPER INDEX POSITION

""" We can get substrings and sublists using a slice. In Python List,
there are multiple ways to print the whole list with all the elements,
but to print a specific range of elements from the list, we use the Slice
operation. """
list1d = ['Pruthvi', 'Raja', 'Python', 'Welcome', 1, 2, 3, 4, 5, 5]
print(len(list1d))
# Index method has Start and End index positions like [start:end]
# Lower index position is inclusive & end index position is exclusive
#      0,       1,       2,       3,       4,  5,  6,  7,  8,  9
# ['Pruthvi', 'Raja', 'Python', 'Welcome', 1,  2,  3,  4,  5,  5]
# To get the range of values mention the start and end index positions
print(list1d[0:3])
# If we don't mention the start index by default it is set to '0'
# To print elements from beginning to a range used:
print(list1d[:4])
# If we don't mention the end index position by default it is set to 'len(list)-1'
# To print elements from a specific Index till the end of the list length
print(list1d[3:])
# If start > end in [start:end], then empty string will be created
# start should be greater than end in positive indexing
print(list1d[5:2])
# We can use negative index
# Negative index starts from -1 from the right side
#      -10,     -9,      -8,       -7,    -6, -5, -4, -3, -2, -1
# ['Pruthvi', 'Raja', 'Python', 'Welcome', 1,  2,  3,  4,  5,  5]
# Here also we can access the particular emement like value at '-8'
print(list1d[-8])

# If there is no end position in -ive indexing by default it is set to -1
print(list1d[-8:])

# If there is no start position in -ve indexing by default it is set to last
# lowest negative index position
# whatever may be the case the end index position will be excluded
print(list1d[:-7])

# We can traverse in positive direction in negative index slicing
# Means in [start:end] start should be lowest negative index position
# And end should be highest negative index position
print(list1d[-8:-3]) # Here -8 < -3 Or we can say that -3 > -8
# Since slicing always goes from left to right and -8 is in left
# most position then -3, (-8 is the lowest index position than -3)

# If we reverse the index positions we will get an empty list
print(list1d[-3:-8])
# Here -3 > -8 but we need lowest negative index position -8 at the start
# and the highest index position -3 at the end to get the range of values

# We can traverse in the positivee direction then in [start:end]
# Start should be -ve and end should be +ve like [-ve:+ve]
print(list1d[-8:6])

# Reversing the indexing positions will give an empty string
print(list1d[6:-8])
#%%
# Positive indexing
#      0,       1,       2,       3,       4,  5,  6,  7,  8,  9
# ['Pruthvi', 'Raja', 'Python', 'Welcome', 1,  2,  3,  4,  5,  5]

# Negative indexing
#      -10,     -9,      -8,       -7,    -6, -5, -4, -3, -2, -1
# ['Pruthvi', 'Raja', 'Python', 'Welcome', 1,  2,  3,  4,  5,  5]

# We can go in positive direction by skipping the index position mentioned
# in the [start::] after :: like ::skip_position
print(list1d[2::2]) # It will skip every 2nd position element after 2 till the end

# We can use -ve skipping to go in reverse direction
print(list1d[2::-1])

# Skipping alternative element in negative direction
print(list1d[8::-2]) # every second element is skipped in negative direction

# We can reverse the entire list and store as a new list using ::-1
reversed_list = list1d[::-1]
print(reversed_list)
#%%
# To get the copy of the original list we can use [:]
list2_copy_list1d = list1d[:]
print(list2_copy_list1d)
#%%

""" Built in List Methods"""

# Using dir
print(dir(list))
""" ['__add__', '__class__', '__class_getitem__', '__contains__',
'__delattr__', '__delitem__', '__dir__', '__doc__', '__eq__', '__format__',
 '__ge__', '__getattribute__', '__getitem__', '__gt__', '__hash__',
 '__iadd__', '__imul__', '__init__', '__init_subclass__', '__iter__',
 '__le__', '__len__', '__lt__', '__mul__', '__ne__', '__new__',
 '__reduce__', '__reduce_ex__', '__repr__', '__reversed__', '__rmul__',
 '__setattr__', '__setitem__', '__sizeof__', '__str__', '__subclasshook__',
 'append', 'clear', 'copy', 'count', 'extend', 'index', 'insert', 'pop',
 'remove', 'reverse', 'sort'] """
#%%

# Let's beggin with 'append' method
# Used for appending and adding elements to List. It is used to add
# elements to the last position of the List in Python.
# It will append but not return the output
list2 = [1, 2, 3, 4, 'Pruthvi']
list2.append(9)
print(list2)
list2.append([10, 11])
print(list2)
list2.append((12, 13))
print(list2)
print(list2.append('Welcome'))
print(list2)
#%%
# "insert()"
# Inserts an element at the specified index position.
list3 = [1, 2, 3, 4, 'Pruthvi']
print(list3.insert(2, 'I am'))
print(list3)
#%%
# "extend"
# Adds contents to the end of List.
list4 = [1, 2, 3, 4, 'Pruthvi']
list4.extend([5, 6, 'Welcome', 10])
print(list4)
#%%
# "index()"
# This will give the index of the first occurence of the list element if
# is present in the list
# It accepts 'start' and 'end' index position to search the list element
# Index  0, 1, 2, 3,   4
list5 = [1, 2, 3, 4, 'Pruthvi']
# Searching the 4 without start and end index positions
print(list5.index(4))
# Searching the value 4 with start and end index positions
print(list5.index(4, 3, 4))
# Seraching with different index positions
# If start index position is less than the actual index position of the first
# occurence of the list element then, it will give item not found error.
print(list5.index(2, 2, 4))
# If the start index is equal to the index of the  element then we will get
# the index position same as the start index position
print(list5.index(2, 1, 4))

# If the end index position is greater than the index of the element, then
# we will no error but the position of the element within the range
print(list5.index(2, 1, 5))
# If the end index position is less than the index of the element, then we
# will get an value not found error
print(list5.index('Pruthvi', 1, 3))
#%%
# 'copy' method
# It will give the shallow copy the original list
list6 = [1, 2, 3, 4, 'Pruthvi']
list7 = list6.copy()
print(list7)
#%%
# "clear" method
# This method will clear all the elements of the list
list8 = [1, 2, 3, 4]
print(list8)
list8.clear()
print(list8)
#%%
# "count" method
# This method will return the frequency of appearence of the given element.

list9 = [1, 2, 3, 4, 1, 2, 3, 4, 6]
list9.count(2)
list9.count(4)
list9.count(6)
#%%
# pop(): Removes and returns the last value from the List or the given index value.
list10 = [1, 2, 3, 4, 'Pruthvi', 10]
list10.pop()
print(list10)
# If we use index then it will remove & return element at specified index position
print(list10.pop(2)) # Here the we have used the index position 2
print(list10)
# We can't use multiple index positions & range index in 'pop' method
# print(list10.pop(2, 3)) # This will give an error
#%%
# remove():	Removes a given object from the List.
list11 = [1, 2, 3, 4, 'Pruthvi', 10]
print(list11)
print(list11.remove(2))
print(list11)
# remove method takes only one argument at a time,  not multiple or index range
# list11.remove(3, 4) # this will give an error
#%%
# reverse():  Reverses objects of the List in place.
list12 = [1, 2, 3, 4, 'Pruthvi', 10]
# The reverse is inplace
list12.reverse()
print(list12)
#%%
# sort()	Sort a List in ascending, descending, or user-defined order
list13 = [1, 5, 3, 4, 20, 10]
list13.sort()
print(list13)
# If reverse is True, then descending order will takes place
list13.sort(reverse=True)
print(list13)


# Sorting the strings based on the alphabetical charectors appearence in order
# A B C D E F G H I J K L M N O P Q R S T U V W X Y Z
# In ascending order capital letters are given highest priority
list14 = ['Good', 'Apple', 'For', 'Health', 'health']
list14.sort()
print(list14)

# In descending order small letters are given highest priority
list14.sort(reverse=True)
print(list14)
#%%
# Sorting using user defined order
# Sorting using second order of each iterable elements in list
list15 = [(1, 2, 4), (3, 3, 3), (3, 1, 1), (2, 1, 2)]
def second(val):
    return val[1]
list15.sort(key=second)
print(list15)
#%%
# We can apply some of the built in math functions on the list
# 'Sum' method : This will sum all the elements of the list if they are numbers
list16 = [1, 5, 3, 4, 20, 10]
print(sum(list16))
#%%
# 'Multiplication with number'
list17 = [1, 5, 3, 4, 20, 10]
print(list17*3)
#%%
# We can concatinate two lists using '+' operator
list18 = [1, 2, 3, 4, 5]
list19 = [10, 11, 12, 13]
print(list18 + list19)
print(sum(list18 + list19))
#%%
# 'max' function
print(max(list16))
#%%
# 'min' function
print(min(list16))
#%%
# 'del': Element to be deleted is mentioned using list name and index.
list20 = [1, 5, 3, 4, 20, 10]
del list20[2] # This will delete element at 2nd index position i.e. 3
print(list20)
#%%
list20 = [1, 5, 3, 4, 20, 10]
del list20[2:4] # end is excluded in the index range
print(list20)
# To del entire list just use the name of the list
del list20
# If we try to call and display the deleted list we will get an error
print(list20)
#%%
# Let's see the logical operators on Lists
list21 = [1, 2, 3, 4, 5, 6, 7, 8]
print(2 in list21)
print(2 not in list21)
print(20 not in list21)
#%%
# Converting List to String using join Method
list22 = ['Welcome', 'To', 'Python', 'For', 'Engineers']
print(" ".join(list22))
#%%
# Iterating through the lists using for loop
list23 = [1, 2, 3, 4, 5, 6, 7, 8]
for item in list23:
    item_multi2 = item * 2
    print('List (item', item, 'Multiplied by 2):',  item_multi2)
#%%
# List comprhension:
list24 = [1, 2, 3, 4, 5, 6, 7, 8]
# Expression
#       expression for element in Old-list if condition
list25 = [item * 2 for item in list24 if item > 0]
print(list25)
#%%
# List comprehension with two lists and for loop to add each elements of the lists
list26 = [1, 2, 3, 4, 5, 6, 7, 8]
list27 = [3, 3, 3, 3, 3, 3, 3, 3]
list28 = [list26[i] + list27[i] for i in range(len(list26))]
print(list28)
# It works like below
# print(list26[0] + list27[0])
#%%
# Comparing two lists with the help of comparison operators
# This function returns 1 if the first list is “greater” than the second list
list26 = [1, 2, 3, 4, 5, 6, 7, 8]
list27 = [2, 0, 4, 3, 3, 3, 3, 3]
if list26 == list27:
    print(" Both the lists are equal")
elif list26 > list27:
    print("List26 is greater than list27")
elif list26 < list27:
    print("List27 is greater than list26")
else:
    print("Lists are not comparable")
#%%
""" Lists Are The Mutable Elements """
list26 = [1, 2, 3, 4, 5, 6, 7, 8]
print("List26 before changing the value at index position 3:")
print(list26)
list26[3] = 20
print("List26 after changing the value at index position 3:")
print(list26)
list26[4:7] = [50, 50, 50]
print("List26 after changing the values at index range 4 to 7:")
print(list26)
print(len(list26))
list26[8] = 40
print(list26)
#%%
#%%
#%%
#%%
#%%
#%%
#%%
#%%
#%%
#%%
#%%
#%%
#%%
#%%
#%%
#%%
#%%
#%%
#%%
#%%
#%%
#%%
#%%
#%%
#%%
#%%
#%%
#%%
#%%
#%%
