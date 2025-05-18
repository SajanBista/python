# Python File Handling:
# To kknow the current working directory we need to use below steps
import os
os.getcwd()
#%%
# To change the directory we have to use 'chdir' method in os module
os.chdir(r'C:\\Users\\Admin\\Desktop')
# To see the number of files and directories we have to use 'listdir' in os
os.listdir()
#%%
# To work with the file we have four options mainly:
# Read, Write, Open and Close Steps
# If the File exists then we can use open, then read, read/write and close steps
# If the file doesn't exists in the directory we need to create it first.
# Python write method will create the file if it doesn't exists
# Let's move back to the current working directory
os.chdir(r'F:\\UDEMY_PYTHON_TUTORIAL\\file_handling')
os.listdir()
#%%
# To create new file or override the existing file use the mode 'w'
# 'w' is only for writing not for reading
file = open('text1.txt', 'w')
# If we try to read we will get an error.
file.read()
#%%
# Let's write something for this file.
file.write('This is first line in text1 file')
file.write('This is second line in text1 file')
# After writing the file we need to close before we can access it for reading
file.close()
#%%
# Now let's open the file again and read with read only mode 'r'
file = open('text1.txt', 'r')
file.read()
file.close()
#%%
# If we try to write we will get an error.
file = open('text1.txt', 'r')
file.read()
file.write("\nThird line")
file.close()
#%%
# 'r+'	It opens the file to read & write both. The file pointer exists at the beginning.
file = open('text1.txt', 'r+')
file.read()
file.write("\nThis is Third line")
file.read()
file.close()
#%%
# The 'w+' method will oeverride the existing data and then rewrite the file from beginning
# It allows both writing & reading but overrides the existing data, so care must be teken while
# --using it.
file = open('text1.txt', 'w+')
file.write("\nThis is 4th line")
# We can't read the line/lines because the cursor is at the end of the text & is waiting for
# another line to be written.
file.read()
file.close()
#%%
# To read from the beginning we need to move our cursor to the beginning point
# For that we have to use 'seek()' method with 'int' number to specify the coursor position
file = open('text1.txt', 'r+')
file.tell()
file.seek(0)
file.read()
file.tell()
file.close()
#%%
# Now we have only one line in our file that is "This is 4th line"
# Let's use the append method to append & read the lines for the demo1 file.
file = open('text1.txt', 'a+')
file.write("\nThis is 5th line")
# To Write or append list of lines we can use writelines
file.writelines(["\nThis is 6th line", "\nThis is 7th line", "\nThis is 8th line"])
file.seek(0)
file.read()
file.close()
#%%
# To read lines one by one we can use 'readline' method
file = open('text1.txt', 'r+')
file.readline()
file.readline()
# To read multiple lines at once use 'readlines' method
file.readlines()
# To See where is the cursor point use "tell' method
file.tell()
# To Move the cursor point to the specific position use 'seek' method
file.seek(17)
# To read again the lines from the cursor position use either 'readline' or 'readlines'
file.readlines()
# Let's check the cursor position once again
file.tell()
# Let's bring back to the original position
file.seek(0)
# Now if we read the lines from 'readlines' we can able to read all the lines in the file.
file.readlines()
file.close()
#%%
import shutil
source_path = r"F:\\UDEMY_PYTHON_TUTORIAL\\file_handling\\text1.txt"
dest_path = r"F:\\UDEMY_PYTHON_TUTORIAL\\file_handling\\text2.txt"
# If the file doesn't exists, the copy method will create the file automatically
shutil.copy(source_path, dest_path)
# Now to read the file contents use file read method
file = open('text2.txt', 'r')
file.readlines()
file.close()
#%%
# Renaming the file
# To rename the file, we have to use os.rename method. Which uses old name & new name.
import os
os.rename('text2.txt', 'demo3.txt')
os.listdir()
#%%
# Remove file with absolute path or relative path
# Before deleting let's create one more file for safer side
shutil.copy('demo3.txt', 'text2.txt')
os.listdir()
os.remove("demo3.txt")
#%%
# To move file from location to another location we can use
# shutil.move(source_path, dest_path)
# Let's create one more file for safer side with shutil.copy method
shutil.copy('text2.txt', 'text3.txt')
source_path = r"F:\\UDEMY_PYTHON_TUTORIAL\\file_handling\\text3.txt"
dest_path = r'C:\\Users\\Admin\\Desktop\\text3.txt'
# Move method is equivalent to cut method in os.
shutil.move(source_path, dest_path)
os.listdir( r'C:\\Users\\Admin\\Desktop')
#%%
# Finally we can use 'with open() as <filename for buffer>:
# And for loop to read or write multiple lines at once.
with open("text2.txt", 'r+') as file:
    file.write("\nHi")
    file.writelines(["\nWelcome To Python", "\nFor Engineers"])
    file.readlines()

#%%
# print statement will ommit the \n line breaker and display the nice text inside the file.
file = open('text2.txt', 'r')
for line in file:
    print(line, end='')
file.close()
#%%
# To see only particular charectors in the file we can pass the specific number inside
# read() method
file = open('text2.txt', 'r')
file.read(5)
# To read rest of the lines we can use readlines
file.readlines()
file.close()
#%%
# readable() in Python
# This returns True if the object is readable.
file = open('text2.txt', 'r')
file.readable()
file.readline(-1) # will read next line
file.readline()
file.readline()
file.readline()
file.readline()
file.readline()
file.readline()
file.readline()
file.readline()
file.readline()
file.readline()
# seekable() in Python
# This returns True if the file stream supports random access.
file.seekable()
# writable() in Python
# This returns True if the stream can be written to.
file.writable()
file.write("\n This is last line")
#%%

#%%

#%%

#%%

#%%

#%%

#%%

#%%

#%%

#%%

#%%

#%%

#%%

#%%

#%%

#%%

#%%

#%%

#%%

#%%

#%%

#%%

#%%

#%%

#%%

#%%

#%%

#%%

#%%

