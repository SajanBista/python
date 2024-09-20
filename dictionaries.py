""" Dictionararies is always in the form of {'key':'value'} form where key should always be unique 
but values can be same 
example:
dict={'ram':'30 years old','hari':'25 years old'} #this is valid dictionary

dict={'ram':'30','ram':'25'} # this is invalid as ram cannot be  30 and 25 at a single time"""

"""iterating through dictionaries
days_per_month={'january':31,'february':28,'march':31}
for months, days in days_per_month.items():#item assign the key and values to the particular variables
    print(f'{months} have {days}')"""

""" Basic dictionary operations

1. Accessing the value by key  

dict={'ram':24, 'shyam':30,'hari':24,'bishal':22}

print(f'{dict['ram']}is the age of ram')


#2.updating the values of an existing key-value pair 
a=dict['jack']=18
print(f'{a}\tis the recent added  data ')
#3.deleting the key and value pair

del dict['ram']


print(dict)
attempting  to trace non existing key  cause keyerror

#3 testing  whether a dictionary contains a specified key or  not 

b='shyam' in dict
print(b)
c='ram' in dict
print(c)
"""

#dictionary methods key and values
"""earlier we used item to iterate in tuples  now similarly we will use keys and values

days_per_month={'january':31,'february':28,'march':31}
for month_name in days_per_month.keys():
    print(month_name,end=' ')
for days_name in days_per_month.values():
    print(days_name,end='\n')

# Now using view 

months_=days_per_month.keys()
for key in months_:
    print(key,end= ' ')

#converting keys and values to list

list(days_per_month.keys())
list(days_per_month.values())
a=list(days_per_month.items())
print(a)

# sorting 
print('the sorted list  of values (i.e months) is:' )
for months in sorted(days_per_month.keys()):
    
    print(months, end=' ')

print("the sorted list of  values (i.e days ) is:")
for days in sorted(days_per_month.values()):
    print(days, end=' ')

"""

""" creating the grade book of student as  in the form of example

marksheet={'jack':[93,90,70,34,50],
            'joe':[54,72,80,98,99],
            'jerry':[90,90,90,90,90]}
all_marksheet_total=0
all_marks_count=0
for name, grade in marksheet.items():
     total_mark=sum(grade)
     print(f' Average mark obtained by {name} is {total_mark/len(grade)} \n')
     all_marksheet_total += total_mark
     all_marks_count+=len(grade)
print(f"class average result is:{all_marksheet_total/all_marks_count}")

#word count in 
text=("this is the text for  word cound and word count counts the total words repeated words are given in intger form")

word_count={}

#count occurance of each unique words
for word in text.split():
    if word in word_count:
        word_count[word] +=1
    else:
        word_count[word]=1

print(f'{"WORDS":<20}COUNT')

for word,count in sorted(word_count.items()):
    print(f'{word:<20}{count}')

print(f'the total unique words are{len(word_count)}')


#python standard library module collections

from collections import Counter 
text=('sunday morning love you monday morning love you i wanna love you everyday')
Counter =Counter(text.split()) 
print(Counter)
for words,count in (Counter.items()):
    print(f'{words:<12}{count}')
    

#use comprehension to create a  list of 50 random integers in the range(1-5).Summarize them with a counter. Display the result in two column foramt
import random
from collections import Counter
number=[random.randrange(1,5) for i in range(50)]
print(Counter)
Counter=Counter(number)
for numbers,count in sorted(Counter.items()):#what i found is while working in  text or mixed data we should use split  but not if their is integer value only
    print(f'{numbers:<12}{count}')

#updating in dictionary

#first creating  empty dictionary

name={}
name.update({'ram':24})

print(name)

#dictionary comprehension
 
months={'january':30,'february':28,'march':12} # these are the months and number of days  i went to college 
months2={number:name for name,number in months.items()}
print(months2)"""



