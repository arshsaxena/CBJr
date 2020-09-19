#!/usr/bin/env python
# coding: utf-8

# In[1]:


def arsh():
    pass
arsh()


# In[8]:


def abc():
    print("Hi!")
    return("Hi! How are you?")
abc()


# In[9]:


v=abc()


# In[10]:


v


# In[12]:


def efg():
    print("This print is before return.")
    return "I will retun this first."
    print("This print is after return.")
efg()


# In[14]:


#Parameters
def add():
    a=2
    h=14
    return str(a+h)
add()


# In[18]:


def add2():
    a=int(input("a="))
    h=int(input("h="))
    return str(a+h)
add2()


# In[30]:


def add3(a, h):
    return a+h
add3(2, 14)


# In[32]:


add3("Arsh", "Saxena")


# In[46]:


def add4(a, h):
    """
    This function helps us to add datatype.
    a: Give same datatype values for a and b.
    b: Give same datatype values for a and b.
    """
    print("Value of a:", a)
    print("Value of h:", h)
    return a+h
get_ipython().run_line_magic('pinfo', 'add4')


# In[45]:


add4(2, 14)


# In[47]:


add4(h=2, a=14)


# In[56]:


def super_add(*args):
    print (type(args))
    add=0
    for i in args:
        add+=i
    return add


# In[57]:


super_add(2, 14, 16, 9, 30, 13, 15, 14, 3)


# In[59]:


def arsh(a=2, h=14):
    return a+h
arsh()


# In[60]:


arsh(a=2004, h=1996)


# In[65]:


def interesting(a, b, c=30, d=40):
    return a+b+c+d
interesting(10, 20)


# In[67]:


def totte(a=30, b=40):
    return a, b
totte()


# In[70]:


d={"keys": "values"}


# In[74]:


def totte(**kwargs):
    print (type(kwargs))
    return kwargs
totte(a=2, h=14)


# In[75]:


def totte(**arsh):
    print (type(arsh))
    return arsh
totte(a=2, h=14)


# In[76]:


len("Hi! I am Arsh Saxena.")


# In[80]:


def new_len(s):
    """
    This is our personal length function.
    s: It is should be iterable and I will tell the length.
    """
    l=0
    for i in s:
        l+=1
    return l
new_len("Hi! I am Arsh Saxena.")


# In[79]:


get_ipython().run_line_magic('pinfo', 'new_len')


# In[90]:


def sum_prod(a, b):
    choice=input()
    if choice=="sum":
        return a+b
    elif choice=="prod":
        return a*b
    else:
        return "Please enter a valid choice."
sum_prod(14, 2)

