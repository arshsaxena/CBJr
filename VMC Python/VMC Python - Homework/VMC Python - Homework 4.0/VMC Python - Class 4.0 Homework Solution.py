#!/usr/bin/env python
# coding: utf-8

# In[6]:


#Question 1
name=input("What is your name? ")
h=0
for a in name:
    h+=1
print("Length of the given name:", h,)


# In[3]:


#Question 2
rows=int(input("Rows: "))
for i in range(rows):
    print("#"*rows)


# In[4]:


#Question 2
rows=int(input("Rows: "))
columns=int(input("Colums: "))
for i in range(rows):
    for k in range(columns):
        print("#", end="")
    print()


# In[10]:


#Question 3
rows=6
for a in range(rows):
    for i in range(a):
        print(a, end=" ")
    print(" ")

