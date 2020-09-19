#!/usr/bin/env python
# coding: utf-8

# In[48]:


#I will be given an input and I have to check the number of times vowels came in my sentence.
s=input("Give me a sentence: ")
vowel=["A", "a", "E", "e", "I", "i", "O", "o", "U", "u"]
count=0
for i in s:
    if i in vowel:
        print(i)
        count+=1    
print("Number of vowels:", count)


# In[47]:


#I will be given an input and I have to check the number of times consonents came in my sentence.
s=input("Give me a sentence: ")
vowel=["A", "a", "E", "e", "I", "i", "O", "o", "U", "u"]
count=0
for i in s:
    if i not in vowel:
        print(i)
        count+=1
print("Number of consonents:", count)


# In[21]:


a="hey there"
a.split()


# In[24]:


id("arsh"+"_"+"saxena")==id("arsh_saxena")


# In[25]:


h=5
n=5
h==n


# In[32]:





# In[29]:


#== checks for value.
#is checks memory location.


# In[30]:


id(h)


# In[31]:


id(n)


# In[36]:


a=14214
b=14214


# In[37]:


id(a)


# In[38]:


id(b)


# In[39]:


a==b


# In[40]:


a is b

