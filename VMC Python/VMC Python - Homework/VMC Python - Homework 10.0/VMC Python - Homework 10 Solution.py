#!/usr/bin/env python
# coding: utf-8

# In[17]:


#Question 1
file=open("new.txt", "wt")


# In[18]:


#Question 2
file.write("This is the solution of Assignment 10: Question 2.")


# In[19]:


file.close()
file.closed


# In[20]:


#Question 3
fileopen=open("new.txt", "rt")
fileopen.read()

