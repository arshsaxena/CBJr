#!/usr/bin/env python
# coding: utf-8

# In[8]:


s="Hello Arsh!"
type(s)


# In[9]:


isinstance(s, str)


# In[10]:


#Capitalize first alphabet of first word.
s.capitalize()


# In[11]:


s1="arsh saxena"
s1.capitalize()


# In[14]:


#Capitalize first alphabet of each word.
s1.title()


# In[16]:


s1


# In[26]:


s1="arsh saxena"
s1=s1.title()
s1


# In[7]:


#Capitalize all alphabets of each words.
s2="arsh saxena"
s2.upper()


# In[5]:


s2


# In[30]:


s2="arsh saxena"
s2=s2.upper()
s2


# In[11]:


#Convert each alphabet of each word in lowercase.
s3="ARSH SAXENA"
s3.lower()


# In[9]:


s3


# In[10]:


s3=s3.lower()
s3


# In[17]:


#Tells lentgh of the given string.
s4="Arsh Saxena"
len(s4)


# In[16]:


s5="Arsh Saxena"
l=0
for i in s5:
    l+=1
print(l)


# In[20]:


#Breaks the given string around spaces.
s6="Arsh Saxena"
s6.split()


# In[21]:


s6


# In[23]:


s6=s6.split()


# In[24]:


type(s6)


# In[28]:


s7="How are you?"
s7.split()


# In[30]:


s8=123456789
len(s8)


# In[31]:


len(str(s8))


# In[37]:


#Joins the elements of the given list.
s9=["Arsh", "Saxena"]
"_".join(s9)


# In[38]:


I="Arsh"
II="Saxena"
I+II


# In[39]:


s10="Arsh Saxena"
".".join(s10)


# In[40]:


"-".join(s10)


# In[1]:


"_".join(s10)


# In[13]:


s11="rahul Janghu"
new=""
for i in s11:
    if i=="r":
        new+="R"
    else:
        new+=i
print(new)


# In[10]:


#To replace any alphabet with other.
s16="ARsh Saxena"
s16.replace("R", "r")


# In[8]:


s16


# In[9]:


s16=s16.replace("R", "r")
s16


# In[54]:


#Count particular aplhabet.
s12="Arsh Saxena"
count=0
for i in s12:
    if i=="A":
        count+=1
count  


# In[55]:


s13="My name is Arsh."
s13


# In[56]:


name=input("What is your name? ")


# In[57]:


print("My name is", name)


# In[72]:


#Used for formatting.
naam=input("Name: ")
age=int(input("Age: "))
s14="Hey my name is %a and my age is %i."%(naam, age)
s14


# In[73]:


naam=input("Name: ")
age=int(input("Age: "))
s14="Hey my name is {} and my age is {}.".format(naam, age)
s14


# In[76]:


naam=input("Name: ")
age=int(input("Age: "))
s15=f"Hey my name is {name} and my age is {age}."
s15


# In[82]:


num=int(input("Number="))
sq=f"Hey, the square of the given number {num} is {num*num}."
sq

