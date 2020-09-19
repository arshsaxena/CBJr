#!/usr/bin/env python
# coding: utf-8

# In[3]:


d={"Arsh": "aVlogger"}
type(d)


# In[4]:


d["Arsh"]


# In[37]:


d.keys()


# In[7]:


d.values()


# In[25]:


d2={"Pineapple": {"Small": 90, "Large": 120},
  "Mango": 80,
  "Bananas": 60,
  "Grapes": 120}


# In[13]:


d2


# In[15]:


d2.values()


# In[17]:


d2.keys()


# In[20]:


d2["Pineapple"]["Small"]


# In[21]:


d2["Lichi"]=100


# In[22]:


d2


# In[23]:


d2.clear()


# In[26]:


d2


# In[33]:


#Set show only unique values.
s={1, 2, 4, 3, 4, 12, 34}
type(s)


# In[28]:


s


# In[35]:


s1={"Arsh", "Arsh", 1, 1, 1}
s1

