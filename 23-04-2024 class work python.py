#!/usr/bin/env python
# coding: utf-8

# In[1]:


#while loop

i=1
while(i<10):
    print(i)
    i+=1


# In[3]:


company="regex"

index =0
while(index<len(company)):
    print(index,company[index])
    index+=1


# In[4]:


#Using break

for i in range(1,5):
    if(i==3):
        break
    
    print(i)


# In[6]:


a = 50
b =20
while(a>=b):
    print(a)
    a-=1


# In[ ]:


a = 50
b =20
sum = 0
while(a>=b):
        
    sum += a
    a-=1
print(sum)


# In[12]:


# from 50, 10 numbers 5and 7 divisible
total =0
count = 50
while(total<10):
    if(count%5==0 and count%7==0):
        print(count)
        total+=1
    count +=1


# In[14]:


#nested loop
for i in range(1,6):
    print("hello")
    
    for k in range(1,4):
        print(k)
    


# In[16]:


for i in range(1,6):
    
    for k in range(1,4):
        print(k)
        
    print(" ")


# In[19]:


for i in range(0,5):
    for j in range(0,5):
        print("*",end=" ")
    print("")


# In[21]:


for i in range(0,5):
    for j in range(0,i):
        print("*",end=" ")
    print("")


# In[23]:


for i in range(0,5):
    for j in range(0,5):
        print("*",end=" ")
    print("")


# In[ ]:




