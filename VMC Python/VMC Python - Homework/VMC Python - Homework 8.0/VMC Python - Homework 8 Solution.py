#!/usr/bin/env python
# coding: utf-8

# In[5]:


#Question 1
def power():
    """
    This function is to calcute x to the power y.
    x: It should be an interger.
    y: It should be an interger.
    """
    x=int(input("x="))
    y=int(input("y="))
    return x**y
print("x^y or x**y =", power())


# In[3]:


#Question 2
s2=str(input("Please enter a string: "))
def count_words(s2):
    li = s2.split()
    return len(li)
print("Number of words:", count_words(s2))       


# In[36]:


def cal():
    a=int(input("a="))
    b=int(input("b="))
    choice=input("Which operation do you want to perform? ")
    if choice=="Addition":
        return a+b
    elif choice=="Subtraction":
        return a-b
    elif choice=="Multiplication":
        return a*b
    elif choice=="Division":
        return a/b
    elif choice=="Exponent":
        return a**b
    else:
        return("Please enter a valid choice.")
print("Answer", "=", cal())

