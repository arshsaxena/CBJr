#!/usr/bin/env python
# coding: utf-8

# In[1]:


import turtle
window=turtle.Screen()
t=turtle.Turtle()
t.forward(200)
turtle.done()


# In[1]:


import turtle
wind=turtle.Screen()
pen=turtle.Turtle()
for i in range(4):
    pen.forward(200)
    pen.left(90)
turtle.done()


# In[1]:


import turtle
wind=turtle.Screen()
pen=turtle.Turtle()
for i in range(3):
    pen.forward(200)
    pen.left(120)
turtle.done()


# In[1]:


import turtle
wind=turtle.Screen()
pen=turtle.Turtle()
for i in range(3):
    pen.forward(200)
    if i!=2:
        pen.left(120)
turtle.done()


# In[1]:


import turtle
wind=turtle.Screen()
pen=turtle.Turtle()
for i in range(6):
    pen.forward(200)
    pen.left(60)
turtle.done()


# In[1]:


import turtle
wind=turtle.Screen()
pen=turtle.Turtle()
for i in range(0, 6):
    pen.forward(200)
    pen.left(144)
turtle.done()


# In[1]:


import turtle
wind=turtle.Screen()
pen=turtle.Turtle()
length=100
for i in range(40):
    pen.forward(length)
    pen.right(90)
    length-=5
turtle.done()


# In[1]:


import turtle
t=turtle.Turtle()
t.pensize(6)
firstRowColors=["blue", "black", "red"]
for i in range(3):
    t.penup()
    t.pencolor(firstRowColors[i])
    t.goto(i*110, 0)
    t.pendown()
    t.circle(50)
secondRowColors=["", "yellow", "", "green"]
for i in range(1, 4, 2):
    t.penup()
    t.pencolor(secondRowColors[i])
    t.goto(i*55, -50)
    t.pendown()
    t.circle(50)
turtle.done()


# In[7]:


ilist=[2, 10, 65, 23, 25]
largest=0
for x in ilist:
    if largest<x:
        largest=x
print("Largest =", largest)


# In[6]:


listoflist=[[21, 15, 32], [2, 7, 43, 100], [34, 99, 25]]
largest=0
for x in listoflist:
    for y in x:
        if largest<y:
            largest=y
print("Largest =", largest)

