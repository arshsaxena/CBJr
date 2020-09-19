#!/usr/bin/env python
# coding: utf-8

# In[1]:


a="Hey there! I am Arsh Saxena. I am learning Python and Web Development at Coding Blocks Junior."


# In[2]:


a


# In[ ]:


#File Handing
#Creating a text file
#Read and write a text file.


# In[7]:


file=open("TextFile.txt", "wt")
content="I have created this using Python."
file.write(content)


# In[8]:


file.close()


# In[10]:


file.closed


# In[13]:


file=open("TextFile.txt", "rt")
file.read()


# In[31]:


file.close()


# In[32]:


#Not opening right now, some error. :( 
rel=open("../Test/NewTextFile.txt", "rt")
rel.read()


# In[33]:


binary=open("bin.txt", "wb")
binary.write(b"This is binary data.")
binary.close()


# In[34]:


binary=open("bin.txt", "rt")
binary.read()


# In[35]:


binary=open("bin.txt", "rb")
binary.read()


# In[36]:


binary.close()

