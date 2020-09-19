#!/usr/bin/env python
# coding: utf-8

# In[15]:


n=int(input("Please enter a number: "))
row=1
while row<=n:
    print(str(row)*n)
    row+=1


# In[24]:


n=int(input("Please enter a number: "))
row=1
while row<=n:
    print(" "*row, "*")
    row+=1


# In[34]:


n=int(input("Please enter a number: "))
row=1
while row<=n:
    print("* "*row)
    row+=1

