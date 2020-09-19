#!/usr/bin/env python
# coding: utf-8

# In[4]:


def PrintMessage():
    for x in range(10):
        print("Hello Arsh!")
print("Greeting is about to come!")
PrintMessage()
print("Once again, greeting is about to come. Be ready! ")
PrintMessage()


# In[8]:


def PrintMessage(message, times):
    for x in range(times):
        print(message)
print("Greeting is about to come!")
message="Hello Arsh!"
PrintMessage(message, 10)
print("Once again, greeting is about to come. Be ready! ")
PrintMessage("Scared?", 5)


# In[11]:


def PrintMessage(message="Arsh is great!", times=10):
    for x in range(times):
        print(message)
print("Greeting is about to come!")
message="Hello Arsh!"
PrintMessage(message, 14)
print("Once again, greeting is about to come. Be ready! ")
PrintMessage("Scared?", 2)


# In[12]:


def PrintIntegers(*values):
    print(values)
    for x in values:
        print(x)
PrintIntegers(3, 4, 6, 10, 12)


# In[20]:


def PrintValues(a, b, c):
    print("a=", a)
    print("b=", b)
    print("c=", c)
print("Ordered")
PrintValues(2, 14, 16)
print("Unordered")
PrintValues(c="2", b="14", a="16")


# In[25]:


def add(a, b, c):
   return a+b+c 
sum=add(2, 14, 16)
print("Sum =", sum)


# In[4]:


def tinput():
    return int(input("Enter next number: "))
ilist=[]
while True:
    number=tinput()
    if number!=0:
        ilist.append(number)
    else:
        print("Program Ended!!")
        break 
print("List", ilist)


# In[1]:


def tinput():
    return int(input("Enter next number: "))
ilist=[]
def slist(ilist):
    ilist.sort()
    for x in ilist:
        print(x)
while True:
    number=tinput()
    if number!=0:
        ilist.append(number)
    else:
        print("Program Ended!!")
        break 
print("List:", ilist)


# In[15]:


def tinput(ilist):
    while True:
        number=int(input("Enter next number: "))
        if number!=0:
            ilist.append(number)
        else:
            break
def slist(ilist):
    ilist.sort()
    for x in ilist:
        print(x)
ilist=[]
tinput(ilist)
slist(ilist)


# In[9]:


def inum():
    return int(input("Enter a number: "))
def aoper():
    return int(input("Add=1, Sub=2, Mul=3, and Div=4.    Operator: "))
def Add(a, b):
    return a+b
def Sub(a, b):
    return a-b
def Mul(a, b):
    return a*b
def Div(a, b):
    return a/b
opt=aoper()
if opt==1:
    print("Sum =", Add(inum(), inum()))
elif opt==2:
    print("Difference =", Sub(inum(), inum()))
elif opt==3:
    print("Product =", Mul(inum(), inum()))
elif opt==4:
    print("Quotient =", Div(inum(), inum()))

