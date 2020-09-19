#!/usr/bin/env python
# coding: utf-8

# In[5]:


t=(1, 2, 3, 4, 5)
type(t)


# In[7]:


t1=("Arsh", "Saxena")
type(t1)


# In[8]:


#Tuples are iterable.
t2=("Arsh", "Saxena")
for i in t2:
    print(i)


# In[11]:


t3=12345
for x in i:
    print(x)


# In[12]:


t4=("Arsh", "Saxena")
length=0
for i in t4:
    length+=1
print(length)


# In[20]:


#Tuples are immutable.
t5=("arsh", "Saxena")
t5[0]


# In[17]:


l1=["arsh", "Saxena"]
id(l1)


# In[18]:


l1[0]="Arsh"


# In[19]:


l1


# In[21]:


t5[0]="Arsh"


# In[22]:


t5


# In[29]:


l2=list(t5)
l2[0]="Arsh"
t5=tuple(l2)
t5

