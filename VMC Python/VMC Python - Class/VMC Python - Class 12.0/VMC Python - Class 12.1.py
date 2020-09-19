#!/usr/bin/env python
# coding: utf-8

# In[8]:


#break statement
n=int(input("Please enter an integer: "))
for i in range (1, n+1):
    if i==2:
        break
    print(i)


# In[9]:


#continue statement
n=int(input("Please enter an integer: "))
for i in range (1, n+1):
    if i==2:
        continue
    print(i)


# In[10]:


#pass statement
n=int(input("Please enter an integer: "))
for i in range (1, n+1):
    pass

