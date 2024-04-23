#!/usr/bin/env python
# coding: utf-8

# In[5]:


#1
for i in range(1,5):
    for j in range(4,i-1,-1):
        print("*",end=(" "))
    print("")


# In[8]:


#2
a=10
for i in range(1,4):
    for j in range(1,i+1):
        print(a,end=(" "))
        a+=1
    print("")
        


# In[10]:


#3
for i in range(10,15):
    for j in range(10,i):
        print(j,end=(" "))
    print("")


# In[14]:


#4
for i in range(1,5):
    for j in range(1,i+1):
        print(chr(64+j),end=" ")
    print("")


# In[17]:


#5
for i in range(0,5):
    for j in range(0,i):
        print(chr(68-j),end=(" "))
    print("")


# In[20]:


#6
for i in range(1,5):
    for j in range(4,i-1,-1):
        print(chr(64+j),end=(" "))
    print("")


# In[23]:


#7
for i in range(0,5):
    for j in range(0,i):
        if(j%2!=0):
            print(2,end=(" "))
        else:
            print(1,end=(" "))
    print("")


# In[34]:


#8
a=0
for i in range(0,5):
    for j in range(0,i):
        print(chr(70+a),end=(" "))
        a+=2
    print("")


# In[56]:


#9
for i in range(1,5):
    for s in range(2,i+1):
        print(" ",end=" ")
    for j in range(4,i-1,-1):
        print("*",end=(" "))
    print("")


# In[ ]:




