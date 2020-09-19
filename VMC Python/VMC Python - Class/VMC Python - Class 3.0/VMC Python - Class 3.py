#!/usr/bin/env python
# coding: utf-8

# In[10]:


#list, append
list=["Maths", "Physics", "Chemistry", "Computer"]
print(list)
list.append("History")
print(list)
print(list[0])
print(list[1])
print(list[-1])


# In[16]:


#insert, reverse, clear
list=["Maths", "Physics", "Chemistry", "Computer"]
print(list)
list.insert(3,"Geography")
print(list)
list.reverse()
print(list)
list.clear()
print(list)


# In[19]:


#sort
list=["Maths", "Physics", "Chemistry", "Computer"]
print(list)
list.insert(3,"Geography")
print(list)
list.sort()
print(list)


# In[43]:


#pop
list=["Maths", "Physics", "Chemistry", "Computer"]
print(list)
sub=list.pop(2)
print(sub)
print(list)


# In[41]:


#len (length)
list=["Maths", "Physics", "Chemistry", "Computer"]
print(len(list))


# In[39]:


#count
list=["Maths", "Physics", "Chemistry", "Computer"]
print(list)
print(list.count("Maths"))
list.append("Maths")
print(list)
print("Maths",list.count("Maths"))


# In[1]:


i=1
while i<=25:
    print(i, "Arsh")
    if i==10:
        break
    i+=1


# In[1]:


i=1
while i<=25:
    if i==10:
        i+=1
        continue
    print(i, "Arsh")
    i+=1


# In[52]:


#for loop
for i in range (1,26):
    print(i, "Arsh")


# In[59]:


#break
for i in range (1,26):
    print(i, "Arsh")
    if i==14:
        print("Inside if, break is about to come.")
        break
print("Out of the loop.")


# In[63]:


#continue
for i in range (1,26):
    print(i, "Arsh")
    if i==14:
          print("Inside if, continue is about to come.")  
    continue
    print(i, "Arsh")
    
print("Out of the loop.")


# In[55]:


sublist=["Maths", "Physics", "Chemistry", "Computer"]
print(sublist)
for x in sublist:
    print(x)
print(sublist)


# In[7]:


for i in range(0, 101):
    if i%2==0:
        print(i)


# In[21]:


ilist=[21, 101, 10, 34, 150, 5, 40, 80]
largest=ilist[0]
slargest=ilist[0]
print(largest)
for x in ilist:
    print(x, largest)
    if x>largest:
        slargest=largest
        largest=x
        print("INSIDE IF")
        print(x, largest)
print(largest, slargest)


# In[23]:


i=10
while i>0:
    print(i)
    i-=1

