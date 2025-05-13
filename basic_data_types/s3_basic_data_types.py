# BASIC DATA TYPES IN PYTHON
# Let’s see the different types one by one in python interpreter and their types.

none = None 		              # singleton null object
print(type(none))
#%%
boolean = bool(True)
print(type(boolean))
#%%
integer = 1
print(type(integer))
#%%
Long = 3.142300000000012345456
print(type(Long))
#%%
# Float
Float = 3.14
print(type(Float))
#%%
Float_inf = float('-inf')
print(type(Float_inf))
#%%
Float_nan = float('nan')
print(type(Float_nan))
#%%
# complex object type, note the usage of letter j
Complex = 2+8j
print(type(Complex))
#%%
# string can be enclosed in single or double quote
string = 'this is a string'
print(type(string))
#%%
me_also_string = "also me"
print(type(me_also_string))
#%%
List = [1, True, 'ML']		 	# Values can be changed
print(type(List))
#%%
Tuple = (1, True, 'ML') 		# Values can not be changed
print(type(Tuple))
#%%
Set = set([1,2,2,2,3,4,5,5])		 # Duplicates will not be stored
print(Set)
print(type(Set))
#%%
# Use a dictionary when you have a set of unique keys that map to values
Dictionary = {'a':'A', 2:'AA', True:1, False:0}
print(type(Dictionary))
#%%





