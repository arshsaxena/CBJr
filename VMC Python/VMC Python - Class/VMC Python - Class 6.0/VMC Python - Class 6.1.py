#!/usr/bin/env python
# coding: utf-8

# In[8]:


li=[1, 2, 3, 4]
arsh=iter(li)
print(next(arsh))
print(next(arsh))
print(next(arsh))
print(next(arsh))


# In[9]:


li=[1, 2, 3, 4]
for i in li:
    print(i)


# In[1]:


import turtle
t=turtle.Screen()
p=turtle.Turtle()
for i in range (50):
    p.forward(10)
    p.left(10)
turtle.done()


# In[7]:


li=[1, 2, 3, 4]
it=iter(li)
while True:
    print(next(it))


# In[16]:


a=1245678
it=iter(a)
print(it)

