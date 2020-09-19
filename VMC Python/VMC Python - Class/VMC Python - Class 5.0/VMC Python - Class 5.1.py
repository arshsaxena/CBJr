#!/usr/bin/env python
# coding: utf-8

# In[32]:


a=int(input("a="))
for i in range(1, a+1):
    for j in range(i):
        print(i, end=" ")
    print()


# In[35]:


a=int(input("a="))
for i in range(1, a+1):
    for j in range(i):
        print("*", end=" ")
    print()


# In[52]:


a=int(input("a="))
for i in range(1, a+1):
    for j in range(10):
        print("#", end=" ")
    print()


# In[59]:


n=int(input("n="))
while n<=5:
    print(str(n)*n)
    n+=1


# In[64]:


n=int(input("n="))
while n<=5:
    print("# "*n)
    n+=1

