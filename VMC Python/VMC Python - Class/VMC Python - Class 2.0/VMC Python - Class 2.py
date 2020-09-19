#!/usr/bin/env python
# coding: utf-8

# In[1]:


print(2+3)
print(5-3)
print(2*3)
print(10/3)
#"+", "-", "*", and "/" are basic arithmetic operators.


# In[8]:


print(2**3)
#"**" represents power.


# In[9]:


print(10//3)
#"//' will give us quotient. 


# In[10]:


print(10%3)
#"%" represents mod.


# In[13]:


print(2==3)
#"==" represents equals to.


# In[14]:


print(3!=4)
#"!=" represents not equals to.


# In[18]:


print(5>10)
print(2>2)
#">" represents greater than.


# In[20]:


print(2>=2)
#">=" represents greater than or equal to.


# In[21]:


print(5<10)
print(2<2)
#"<" represents less than.


# In[23]:


print(2<=2)
#"=<" represents less than or equal to.


# In[31]:


print(2==3 and 5>3)
print(3==3 and 5>3)
print(2==3 and 5<3)


# In[34]:


print(5==3 or 2>1)
print(5==3 or 2<1)
print(5==5 or 2>1)


# In[35]:


print(not(3>2))


# In[54]:


marks=int(input("Enter your marks: "))
print(marks>=33)
if marks>33: 
    print("You have passed the test.")
    print("Congratulations! :)")
else:
    print("You have failed the test.")
    print("Try hard next time. :(")
    
print("What are you waiting for? Go home!")
    
#if else: conditional formatting


# In[58]:


marks=int(input("Enter your marks: "))
print(marks>=33)
if marks>33: 
    print("You have passed the test.")
    print("Congratulations! :)")
else:
    print("You have failed the test.")
    print("Try hard next time. :(")
    
print("What are you waiting for? Go home!")
    
#if else: conditional formatting


# In[4]:


marks=int(input("Enter your marks: "))
print(marks>=33)
if marks<33:
    print("You have not passed the test.")
elif marks>=33 and marks<=60:
    print("You have passed the test but did'nt did well.")
    print("Congratulations! :)")
elif marks>60:
    print("You have passed the test, excellent.")
    print("Congratulations! :)")

print("What are you waiting for? Go home!")
    
#if else: conditional formatting


# In[68]:


num=int(input("Enter a number: "))
if (num%2==0):
    print("Even")
else:
    print("Odd")


# In[78]:


num=int(input("Enter a number: "))
if (not(num%2==0 or num%5==0)):
    print("Multiple of 5")
else:
    print("Not a multiple of 5")


# In[83]:


a=int(input("a="))
b=int(input("b="))
c=int(input("c="))
if (a>=b and a>=c):
    print("a is largest")
elif (b>=a and b>=c):
    print("b is largest")
else:
    print("c is largest")


# In[93]:


a=int(input("a="))
b=int(input("b="))
c=int(input("c="))
largest=a
if b>=largest:
    largest=b
    print("inside b condition")
elif c>=largest:
    largest=c
    print("inside c condition")
print()
print(largest)

