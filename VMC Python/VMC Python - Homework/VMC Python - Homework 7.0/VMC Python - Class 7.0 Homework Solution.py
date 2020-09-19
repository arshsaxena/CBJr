#!/usr/bin/env python
# coding: utf-8

# In[1]:


#Question 1
s=input("Give me a string: ")
print(s.upper())


# In[3]:


#Question 2
a=input("Give me a string: ")
h=""
for i in a:
    h+=i.upper()
print(h)


# In[13]:


#Question 3
s1=("Hey there! My name is Arsh.")
s2=input("What to check? ")
if s2 in s1:
    print("It is a substring of s1.")
else:
    print("It is not a substring of s1.")

