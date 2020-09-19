#!/usr/bin/env python
# coding: utf-8

# In[3]:


#Question 1
num=int(input("Please enter a number: "))
if num>0:
    print("The given number is +ve.")
else:
    print("The given number is -ve.")


# In[10]:


#Question 2
num=int(input("Please enter a number: "))
if num>5:
    print("Hi! I'm above 5.")
else:
    print("Hi! I'm below 5.")


# In[1]:


#Question 3
marks=int(input("Please enter your marks: "))
if marks<33:
    print("You have failed the test.")
elif marks>=33 and marks<60:
    print("You have passed the test but score is not good.")
elif marks>60 and marks<80:
    print("You have scored well in the test.")
else:
    print("You have got some good skills in this subject!")


# In[2]:


#Question 4
temprature=float(input("Please enter the outside temperature: "))
if temprature<5:
    print("It's super cold out there.")
elif temprature>5 and temprature<15:
    print("It's little bit cold outside.")
elif temprature>15 and temprature<25:
    print("Weather is nice outside.")
elif temprature>25 and temprature<35:
    print("Weather is a bit hot out there.")
else:
    print("It's super hot!")


# In[22]:


#Question 5
num=int(input("Please enter a number: "))
if num%5==0:
    print("I'm a multiple of 5.")
else:
    print("I'm not a multiple of 5.")


# In[20]:


#Question 6
num=int(input("Please enter a number: "))
mod=num%2
if mod>0:
    print("No")
else:
    print("Yes")
#Yes=Even
#No=Odd


# In[25]:


#Question 7
num=int(input("Please enter a number: "))
if num%5==0 and num%7==0:
    print("I'm divisible by both 5 and 7.")
else:
    print("I'm not divisible by both 5 and 7.")


# In[16]:


#Question 8
a=int(input("a="))
b=int(input("b="))
c=int(input("c="))
largest=a
if b>largest:
    largest=b
if c>largest:
    largest=c
print(largest, "is the largest number.")


# In[12]:


#Question 9
num=int(input("Enter a number: "))
if num%5==0 and num%7==0:
    print("The number is divisible by both 5 and 7.")
else:
    print("The number is divisible by 5 but not by 7.")


# In[17]:


#Question 10
num=int(input("Enter a number: "))
if num%5==0 or num%7==0:
    print("The number is divisible either by 5 or by 7.")
else:
    print("The number is not divisible either by 5 or by 7 or both.")


# In[7]:


#Question 11
light=str(input("What is color of light? "))
if light=="Red":
    print("Please turn off your engine.")
elif light=="Yellow":
    print("Hey, please be ready to go.")
elif light=="Green":
    print("You are clear to go ahead.")
else:
    print("The given information is irrelevant.")


# In[4]:


#Question 12
a=int(input("Cofficient of a="))
b=int(input("Cofficient of b="))
c=int(input("Cofficient of c="))

#Finding discriminant
d=(b**2)-(4*a*c)

#Finding roots
root1=(-b+d**(1/2))/(2*a)
root2=(-b-d**(1/2))/(2*a)

print(root1,"and", root2)


# In[11]:


#Question 13
weather=str(input("Please enter outside weather: "))
if weather=="Rainy":
    print("Let's not go outside today.")
elif weather=="Sunny":
    print("Hey, let's go for swimming.")
elif weather=="Cloudy":
    print("Hey! Let's play outside, weather is cool.")
else:
    print("The given information is irrelevant.")


# In[2]:


#Question 14
True or True and False


# In[4]:


#Question 15
True and False or True


# In[5]:


#Question 16
not False and False


# In[6]:


#Question 17
True and True and (not False)


# In[7]:


#Question 18
True and True or (not False)


# In[8]:


#Question 19
(True and False) and (not False) or True


# In[9]:


#Question 20
(True and False) and ((not False) or True)

