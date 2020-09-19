#!/usr/bin/env python
# coding: utf-8

# In[17]:


i_loop_count=2
j_loop_count=3
for i in range (1, i_loop_count+1):
    print("loop for i =", i, "started")
    for j in range(1, j_loop_count+1):
        print("|", "\t loop for j =", j)
    print()


# In[22]:


i_loop_count=2
j_loop_count=3
k_loop_count=4
for i in range (1, i_loop_count+1):
    print("loop for i =", i, "started")
    for j in range(1, j_loop_count+1):
        print("|", "\t loop for j =", j)
        for k in range(1, k_loop_count+1):
            print("|", "\t|", "\t\t""loop for k =", k)
    print()


# In[24]:


i_loop_count=4
j_loop_count=3
k_loop_count=2
l_loop_count=1
for i in range (1, i_loop_count+1):
    print("loop for i =", i, "started")
    for j in range(1, j_loop_count+1):
        print("|", "\t loop for j =", j)
        for k in range(1, k_loop_count+1):
            print("|", "\t|", "\t\t""loop for k =", k)
            for l in range(1, l_loop_count+1):
                print("|", "\t|", "\t\t\t\t""loop for l =", l)
    print()


# In[48]:


iloop=int(input("i="))
jloop=int(input("j="))
for i in range(1, iloop+1):
    for j in range(1,jloop+1):
        print(i, ",", j, end=" | ")
    print()


# In[49]:


count=int(input("count="))
for i in range(1, count+1):
    for j in range(1, i+1):
        print(i, end=" ")
    print()


# In[77]:


ilistolist=[[9, 5, 7], [0, 9, 5], [9, 7, 3], [9, 8, 1]]
sum=0
for x in ilistolist:
    print(x)
    for y in x:
        print(y, end=", ")
        sum+=y
    print()
    print(sum, end="")
    print()
print()
print("Sum of the elements =", sum)


# In[79]:


ilistolist=[[9, 5, 7], [0, 9, 5], [9, 7, 3], [9, 8, 1]]
sum=0
for i in range(0, len(ilistolist)):
    for j in range(0, len(ilistolist[i])):
        sum+=ilistolist[i][j]
print("Sum of the elements =", sum)


# In[89]:


ilist=[[9, 5, 7], [0, 9, 5], [9, 7, 3], [9, 8, 1]]
sum=0
print("ilist[0] =", ilist[0])
print("ilist[0][1] =", ilist[0][1])
print("ilist[3] =", ilist[3])
print("ilist[3][2] =", ilist[3][2])


# In[93]:


ilist=[[9, 5, 7], [0, 9, 5], [9, 7, 3], [9, 8, 1]]
sum=0
print(ilist[0])
index=len(ilist[2])-1
print(ilist[2][len(ilist[2])-1])

