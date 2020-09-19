#!/usr/bin/env python
# coding: utf-8

# In[19]:


#Question 1
ilist=[[1, 2, 3], [4, 2, 6], [5, 6, 7], [67, 89]]
sum=0
for x in ilist:
    for y in x:
        sum+=y
print("Sum =", sum)


# In[39]:


#Question 2
ilist=[[1, 2, 3], [4, 2, 6], [5, 6, 7], [67, 89]]
sum=192
product=1
for x in ilist:
    for y in x:
        product*=y
print("Product =", product)

print("Difference between the sum and the product of the given list =", product-sum)


# In[9]:


#Question 3
a=[]
for i in range (1, 7):
    h=[]
    for j in range (1, i+1):
        h.append(j)
    a.append(h)
print(a)

