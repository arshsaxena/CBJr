#!/usr/bin/env python
# coding: utf-8

# In[7]:


#Objects are of immutable data type.
a=5
id(a)


# In[4]:


a=10
id(a)


# In[8]:


#Strings are of immutable data type.
h="Arsh"
id(h)


# In[6]:


h="Arsh Saxena"
id(h)


# In[2]:


l=["Arsh"]
id(l)


# In[3]:


l.append("Saxena")
print(l)
id(l)


# In[4]:


a="Arsh"
h="Arsh"
id(a)


# In[6]:


id(h)


# In[8]:


print(a)
print(h)
id(a)==id(h)


# In[9]:


a="Arsh"
h="arsh"
id(a)


# In[10]:


id(h)


# In[11]:


id(a)==id(h)


# In[16]:


"a"=="A"

