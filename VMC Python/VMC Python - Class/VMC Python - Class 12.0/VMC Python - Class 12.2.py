#!/usr/bin/env python
# coding: utf-8

# In[1]:


a=14
h=14
a==h


# In[3]:


id(a)==id(h)


# In[8]:


a=300
h=300
a==h


# In[9]:


a is h


# In[10]:


id(a)==id(h)


# In[11]:


id(a), id(h)


# In[12]:


a=2
id(a)


# In[13]:


id(2)


# In[14]:


id(0)


# In[15]:


s="Hello!"
id(s)


# In[16]:


id("Hello!")


# In[18]:


s1="Hello!"
s==s1


# In[19]:


s is s1


# In[ ]:


#If you want to check for same memory address then use "is".
#If you want to check for same values, not memory address then use "==".

