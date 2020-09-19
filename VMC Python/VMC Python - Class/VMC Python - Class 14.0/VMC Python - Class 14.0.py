#!/usr/bin/env python
# coding: utf-8

# In[1]:


f=open("abc.txt", "wt")
content="Hey there!"
f.write(content)
f.close()


# In[5]:


f1=open("abc.txt", "wt")
contentt="Hi there!"*100
f1.write(contentt)
f1.flush()
f1.close()


# In[7]:


f2=open("abc.txt", "wt")
contenttt="Hi flushed! "*100
f2.write(contenttt)
f2.flush()
f2.closed


# In[9]:


o=open("abc.txt", "rt")
o.read()


# In[10]:


o.close()


# In[11]:


o.closed


# In[13]:


with open ("arsh.txt", "wt") as f3:
    f3.write("This is a better way to write.")


# In[16]:


f3.closed


# In[17]:


import json


# In[20]:


d={"Arsh": "aVlogger",
  "Arshu": "Good boy!",
  "Arsh Saxena": ["aVlogger", "Topper", "Good boy!", "Indian"]}
d


# In[21]:


with open ("intro.json", "w") as f4:
    json.dump(d, f4)


# In[22]:


with open ("intro.json", "r") as o1:
    print(json.load(o1 ))


# In[24]:


import requests


# In[26]:


url="https://www.google.com"
data=requests.get(url)
data.content


# In[27]:


type(data)


# In[28]:


with open("google.html", "wb") as h:
    h.write(data.content)


# In[29]:


url2="https://www.google.com/search?q=panda&rlz=1C1CHBD_enIN916IN916&source=lnms&tbm=isch&sa=X&ved=2ahUKEwicq-jc7NTrAhXHzTgGHcX8C1EQ_AUoAXoECB8QAw&cshid=1599406370106374&biw=796&bih=625#imgrc=WlIqe3ZPkgqVbM"
img=requests.get(url2)
with open ("scrap.jpeg", "wb") as f6:
    f6.write (img.content)

