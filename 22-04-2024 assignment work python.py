#!/usr/bin/env python
# coding: utf-8

# In[1]:


#1 Run for loop and find the total sum of first 20 natural numbers
sum = 0
for i in range(0,21):
    sum += i
print(sum)
    


# In[2]:


#2 Run for loop and find the total sum of last 20  3 digit natural numbers
sum =0
for i in range(999,978,-1):
    sum += i
print(sum)


# In[4]:


#3 Run for loop and find the product & average of any 20 natural numbers
a = int(input("enter the number: "))
b = a + 20
Product = 1
sum = 0
for i in range(a,b):
    Product *= i
    sum += i
average = sum/20
print(average)
print(Product)


# In[7]:


#4 print a multiplication table of a number given by a user
a = int(input("enter the number: "))

for i in range(1,11):
    table = a * i
    print(table)


# In[9]:


#5 find out the sum of the power of starting 6 number
a = int(input("enter the number: "))
sum = 0
for i in range(1,7):
    sum += a**i
print(sum)


# In[15]:


#6take a string from the user and find out the total consonant which are available
# in a string
consonants = "bcdfghjklmnpqrstvwxyz"
string= input("Enter a string: ")
count = 0

for i in string:
    if i in consonants:
        count += 1

print(count)


# In[27]:


# 7  take a int number from the user and find out the total sum, average and the product of that numbers from 1 to the input provided only for odd values
number=int(input("enter the number: "))
sum = 0
product = 1
count = 0

for i in range(1,number+1):
    if i%2!=0:
        sum+=i
        product*=i
        count +=1
average = sum/count
print(sum,product,average)


# In[ ]:





# In[ ]:




