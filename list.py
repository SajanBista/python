"""# #list typically store homogeneous data that mean of same data type.

# numbers=[45,70,80,64,32]
# #print(numbers)
# print(numbers[2])
# print(len(numbers))
# #modifying list
# numbers[1]=80
# print(numbers)

string='this is the practice of list'
print(string[2])
string[2]='r'
print(string)# assignment of string is  not possible in the case of string
numbers=[45,70,80,64,32]
b=numbers[0]+numbers[1]+numbers[2]+numbers[3]+numbers[4]
print(b)"""
"""#append in list using empty list
a_list=[]
for i in range(2,21,2):
    a_list +=[i]

print(a_list)

letters=[]
letters +='python programming'
print(letters)


#concatenating list  

list1=[2,3,4,5]
list2=[6,7,8,9]
concatenating_list= list1+list2
print(concatenating_list)

for i in range(len(concatenating_list)):
    print(f'{i}:{concatenating_list[i]}')


for a in range(2,5,2):
    print(f'{i}:{[a]}')

list= print(append(list1[10]))"""

"""create a function cube_list that cube element of a list. 
Call the function with the list numbers containing 1 through 10. show numbers after the call

def cube_list(values):
    for i in range (len(values)):
        values[i] **=3

numbers=[]
for i in range(10):
    numbers_new = int(input(f"Enter the value of numbers[{i}]: "))
    numbers.append(numbers_new)
print(numbers)
cube_list(numbers)
print(numbers)

characters=[]
characters +='birthday'

print(characters)

list1=[2,3,4,5]
list2=[6,7,8,9]
print(list1.extend(list2))

list3=['ram','shyam','hari']
list4=['jack','joe','jimmy']


def finding_square(numbers):
    for  i in range(len(numbers)):
        numbers[i] **=2


numbers=[]

for i in range(5):
    new=(input(f'enter the number for {[i]}:'))
    numbers.append(new)
print(numbers)
F=finding_square(numbers)
print(numbers)



#sorting list 

numbers=[10,2,4,7,0,3]
numbers.sort()
print(numbers)
numbers.sort(reverse= True)
print(numbers)

letters='this is the string'
ascending_letters= sorted(letters)
print(ascending_letters)
print(numbers.index(2))
print(numbers.index(0))




counting the number of occurances of an items 

a=56
b=90
c=a+b
print(c)"""

"""using lamda rather than function.
numbers=[2,34,5,6,7]
print(list(filter(lambda x:x %2 !=0,numbers)))#lamda is the inbuilt function or simply it is a function without name.

print(9<10)
print(ord('R'))
list= ['red','orange','blue','ample']
print(min(list,key=lambda s:s.lower()))
print(max(list,key=lambda s:s.lower()))"""

"""iterative backward through  a sequece
numbers=[10,3,8,9,11,2,5]
reversed_numbers=[item *2 for item in reversed(numbers)]
print(reversed_numbers)

foods=['Cookies','apple','banana','Bacon','Grapes']
foods.sort()
a=sorted(foods)
print(a)
print(foods)"""

"""mapping sequence
numbers=[10,2,20,9,80,8,1]
print(list(map(lambda x:x *2, numbers)))

numbers = list(range(1,16))
# new_list=list(filter(lambda x:x%2==0,numbers))
# print(new_list)

# square=list(map(lambda x:x**2,numbers))
# print(square)

print(list(map(lambda x:x**2,filter(lambda x:x%2==0,numbers))))

Map a list of the three Fahrenheit temperature 41,32,and 212 to the list of tuple containing the fahrenheit temperatures and 
their celsius equivalents. convert Fahrenheit temperature to celsius with the given formula:
                        celsuis = (Fahrenheit-32)*5/9          
Fahrenheit=[41,32,212]
result=list(map(lambda x:(x,(x-32)*(5/9)),filter(lambda x:x ,Fahrenheit)))
print(result)"""
"""combining iterables into tuples of corresponding elements
name=['Asmita','Bishal','samiksha','kabin']
their_grade=[3.2,3.5,3.6,3.2]
for name, gpa in zip(name,their_grade):
    print(f'gpa={gpa}     name={name}')"""

"""two dimensional list"""

# a=[[43,34,54,65],[65,45,34,65],[45,54,34,43,53]]
# print(a)
# for row in a:
#     for item in row:
#         print(item, end='  ')
#     print()
# for i, row in enumerate(a):
#     for j, item in enumerate(row):
#         print(f'a[{i}][{j}]={item}',end=' ')
#     print()


#simulation and static visualizations

import matplotlib.pyplot as plt
import numpy as np
import random
import seaborn as sns
rolls=[random.randrange(1,7)for i in range(60)]
values,frequencies=np.unique(rolls,return_counts=True)  
title=f'rolling a six-sided Die{len(rolls):,} times'
sns.set_style('whitegrid')
axes=sns.barplot(x=values,y=frequencies,hue=values,palette='bright',legend=True)

axes.set_title(title)
axes.set(xlabel='Die value',ylabel='frequency')
axes.set_ylim(top=max(frequencies)*1.10)
for bar, frequency in zip(axes.patches,frequencies):
    text_x=bar.get_x()+bar.get_width()/2.0
    text_y=bar.get_height()
    text=f'{frequency:,}\n{frequency/len(rolls):.3%}'
    axes.text(text_x,text_y,text,fontsize=11,ha='center',va='bottom')

plt.show()










    