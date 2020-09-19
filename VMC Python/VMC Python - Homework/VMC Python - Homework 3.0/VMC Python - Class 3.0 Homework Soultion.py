#!/usr/bin/env python
# coding: utf-8

# In[4]:


#Question 1
n=int(input("Please enter a number: "))
for i in range (1, n+1):
    print(i)
for i in range (5, 0):
    print(i)


# In[6]:


#Question 1
for i in range (10, 0, -1):
    print(i)


# In[11]:


#Question 2
for x in range(2000, 3201):
    if (x%7==0) and (x%5!=0):
        print (x)


# In[13]:


#Question 3
addsq=0
sqsum=0
for i in range (1, 101):
    addsq+=i
    sqsum+=i**2
result=addsq-(addsq**2)
print(result)


# In[21]:


#Question 4
li=[]
for i in range(11):
    li.append(i)
print(li)


# In[32]:


#Question 5
li=[]
for i in range(1, 21):
    if i%2==0:
        li.append(i)
print(li)

