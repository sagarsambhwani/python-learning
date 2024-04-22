#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# nested if

# for eg
age =18
city='Jaipur'
if(age>=18):
    print("age is eligible")
    if(city=="Jaipur"):
        print("eligilbe gor voting")
    else:
        print("not")
else:
    print("not eligible")
    


# In[2]:


#for loop
#using range
#0 upto 5 (5 is exclusive)
#range (start, end, Step[1])
for i in range(0,5):
    print(i)


# In[10]:


sum =0
for count in range(1,11):
    sum = sum + count
print(sum)


# In[12]:


sum = 0
for i in range(1,31):
    if(i%2==0):
        sum =sum+i
print(sum)


# In[14]:


#product of all number from 8 to 1

fact = 1
for i in range(8,0,-1):
    fact = fact *i
print(fact)


# In[15]:


data="jaipur"
for x in data:
    print(x)


# In[16]:


city="jaipur"
for index in range(0,len(city)):
    print(index,city[index])


# In[17]:


#from string total no. of char
#total no. of a

city="Jaipaura"
sum = 0
for index in range(0,len(city)):
    sum +=index
    print(index)
print(sum)
    


# In[24]:


count=0
for index in city:
    if(index=='a' or index=='e' or index=='i' or index=='o' or index=='u'):
        count= count+1
print(count)


# In[25]:


sum =0
for i in range(0,101):
    i+=1
    sum+=1
    print(i,sum)


# In[ ]:


#total 1 to 20
#last 20, 3 digit natural no.
#product and average of 1-20
#print table by user input
#sum of power of 1 no. by user input
#consonant count in string by user input

