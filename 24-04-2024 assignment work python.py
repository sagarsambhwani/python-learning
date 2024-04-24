#!/usr/bin/env python
# coding: utf-8

# In[5]:


#1
for i in range(1,5):
    for j in range(1,i):
        print(" ",end=" ")
    for k in range(i,5):
        print(chr(64+i),end=" ")
        i+=1
    print("")


# In[6]:


#2
for i in range(1,5):
    num =1
    for j in range(1,i):
        print(" ",end=" ")
    for k in range(i,5):
        print(chr(64+num),end=" ")
        num+=1
    print("")


# In[20]:


#3
for i in range(1,5):
    for j in range(1,i):
        print(" ",end=" ")
    for k in range(i,5):
        print(chr(64+i),end=" ")
        i+=1
    print("")


# In[66]:


#4
temp =0
sum = 0
for i in range(1,5):
    num =10
    
    if(i%2!=0):
        
        for j in range(1,i):
            print(" ",end=" ")
        for k in range(i,5):
            print(chr(64+i-sum),end=" ")
            i+=1
        print("")
        sum+=1
        
    elif(i%2==0):
        
        for j in range(1,i):
            print(" ",end=" ")
        for k in range(i,5):
            print(num + temp,end=" ")
            num*=10
        print("")
        temp+=90
            
    print("")  


# In[29]:


#5
num =0

for i in range(1,4):
    
    for j in range(1,i):
        print(" ",end=" ")
    for k in range(i,4):
        print(chr(90-num),end=" ")
        num+=1
    print("")


# In[26]:


ord("Y")


# In[43]:


#6
for i in range(0,5):
    for j in range(0,5):
        if(i==j or i==0 or j==4):
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print("")
             


# In[47]:


#7
for i in range(0,5):
    for j in range(0,5):
        if(i+j==4 or i==0 or j==0):
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print("")
             


# In[ ]:




