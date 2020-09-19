#!/usr/bin/env python
# coding: utf-8

# In[2]:


def x(a):
    return a**2
x(14)


# In[4]:


x=lambda a: a**2
x(2)


# In[6]:


def linear(x, y):
    return 2*(x**2)+y
linear(14, 2)


# In[7]:


linear1=lambda x, y: 2*(x**2)+y
linear(14, 2)


# In[10]:


#List Comprehensions
d=[]
for i in range(1, 6):
    d.append(i**2)
d


# In[12]:


d1=[i**2 for i in range (1, 6)]
d1


# In[20]:


even=[]
for i in range (0, 21, 2):
    even.append(i)
even    


# In[19]:


even1=[i for i in range (0, 21, 2)]
even


# In[26]:


odd=[]
for i in range (1, 21, 2):
    odd.append(i)
odd    


# In[24]:


odd1=[i for i in range (1, 21, 2)]
odd

