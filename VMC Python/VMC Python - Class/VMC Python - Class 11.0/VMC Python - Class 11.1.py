#!/usr/bin/env python
# coding: utf-8

# In[1]:


a=10
a=15
print(a)


# In[5]:


a=10
def arsh():
    a=15
    print("This a is inside funtion.", a)
    print(id(a))
arsh()
print("This a is outside funtion.", a)
print(id(a))


# In[10]:


#a is in global scope.
a=10
def arshu():
    #b is in local scope.
    b=20
    print(a)
arshu()


# In[11]:


#a is in global scope.
a=10
def arshu():
    #b is in local scope.
    b=20
    return b
    print(a)
arshu()


# In[12]:


def abc():
    pass


# In[14]:


a=10
def arsh():
    global a
    a=20
    print(20)
arsh()
print(a)

