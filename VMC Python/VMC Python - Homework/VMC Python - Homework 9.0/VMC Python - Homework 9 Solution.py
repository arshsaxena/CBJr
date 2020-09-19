#!/usr/bin/env python
# coding: utf-8

# In[11]:


#Question 1
def iint(a, b, c):
    if a>b and a>c:
        highest=a
    elif b>a and b>c:
        highest=b
    else:
        highest=c
    return highest
iint(2, 16, 14)


# In[30]:


#Question 2
def iint2(a):
    a=str(a)
    b=a[::-1]
    return int(b)
iint2(21416)


# In[31]:


#Question 3
def replace_0(a):
    a=str(a)
    b=""
    for i in a:
        if i=="0":
            b+="5"
        else:
            b+=i
    return int(b)
replace_0(102920083)

