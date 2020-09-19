#!/usr/bin/env python
# coding: utf-8

# In[5]:


#Average=sum/(len("LIST NAME"))
ilist=[10, 23, 45, 60, 15]
sum=0
for x in ilist:
    sum+=x
print("Average =", sum/(len(ilist)))


# In[5]:


ilist=[10, 23, 45, 60, 15]
sum=0
count=0
for x in ilist:
    if x%2==0:
        sum+=x
        count+=1
average=sum/count
print(count)
print("Average =", average)


# In[32]:


count=20
i=1;
j=1
print("1 :", i)
print("2 :", j)
for x in range(3, count+1):
    print(x, ":", i+j)
    i, j=j, i+j


# In[2]:


limit=1000
i=1;
j=1
count=2
print("1 :", i)
print("2 :", j)
while i+j<1000:
    count+=1
    print(count, ":", i+j)
    i, j=j, i+j


# In[22]:


num=int(input("Enter a number: "))
for x in range (2, num):
#x=2, x=3, x=4,....,x=num
    if num%x==0:
        print(num, "is not a prime number.")
        break
else:
    print(num, "is a prime number.")


# In[27]:


num=int(input("Enter a number: "))
x=2
while x<num:
    if num%x==0:
        print(num, "is not a prime number.")
        break
    x+=1
else:
    print(num, "is a prime number.")


# In[58]:


xcount=5
ycount=5
for x in range(1, xcount+1):  
    for y in range (1, ycount+1): #Start a for loop and run it ycount times.
        print(x, ",", y, end=" | ") #Print x and y in same line.
    print() #Move pointer to next line.
    print() #Leave a blank line.

