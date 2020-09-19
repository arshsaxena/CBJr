#!/usr/bin/env python
# coding: utf-8

# In[13]:


a=10
def outer():
    x=20
    def inner():
        global x
        x=30
        print(x)
    return x, inner(), x
outer()


# In[14]:


a=10
def outer():
    x=20
    def inner():
        nonlocal x
        x=30
        print(x)
    return x, inner(), x
outer()


# In[15]:


a=10
def outer():
    x=20
    def inner():
        x=30
        print(x)
    return x, inner()
outer()

