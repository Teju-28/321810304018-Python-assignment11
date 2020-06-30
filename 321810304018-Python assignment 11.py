#!/usr/bin/env python
# coding: utf-8

# ## 1.Write a python program to sum all the items in a list.

# In[1]:


list=[]
num=int(input('How many numbers: ')) 
for n in range(num):
    numbers=int(input('Enter number: '))
    list.append(numbers)
print("Sum of elements in given list is :",sum(list))


# ## 2.Write a python program to multiplies all the items in a list.

# In[3]:


import numpy
list=[]
num=int(input('How many numbers: ')) 
for n in range(num):
    numbers=int(input('Enter number: '))
    list.append(numbers)
print("Product of elements in given list is :",numpy.prod(list))


# ## 3.Write a python program to get the largest and smallest number from a list.

# In[6]:


list=[]
num=int(input('How many numbers: ')) 
for n in range(num):
    numbers=int(input('Enter number: '))
    list.append(numbers)
print("Maximum element in the list is :",max(list),"\nMinimum element in the list is :",min(list))


# ## 4.Write python program to remove duplicates from a list.

# In[8]:


a=[]
num=int(input('How many numbers: ')) 
for n in range(num):
    numbers=int(input('Enter number: '))
    a.append(numbers)
b=set()
unique=[]
for n in a:
    if n not in b:
        unique.append(n)
        b.add(n)
print("Non-duplicate items:")
print(unique)


# ## 5.Write a python program to check a list is empty or not.

# In[9]:


a=[]
if len(a) == 0:
    print("The list is empty")


# ## 6.Write a python program to clone or copy a list.

# In[14]:


list1=[1,2,3]
list2=list1[:]
print("Before cloning:",list1)
print("After cloning:",list2)


# ## 7.Write a python program to print specified list after removing the 0th,4th elements.

# In[16]:


color=['Red','Green','White','Black','Pink','Yellow']
color=[x for (i,x) in enumerate(color) if i not in (0,4,5)]
print(color)


# ## 8.Write a python program to print the numbers of a specified list after removing even numbers from it.

# In[17]:


num=[7,8,120,25,44,20,27]
num=[x for x in num if x%2!=0]
print(num)


# ## 9.Write a python program to shuffle and print a specified list.

# In[18]:


from random import shuffle
color=['Red','Green','White','Black','Pink','Yellow']
shuffle(color)
print(color)


# ## 10.Write a python program to get the difference between the two lists.

# In[28]:


a=[1,2,3,4,5]
d=[4,5]
print(set(a)-set(d))

