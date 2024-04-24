#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#nested loops
'''
****
 ***
  **
   *
'''



# In[ ]:


num = 1
for i in range(0,4):
    for j in range(0,i):
        print(num,end=" ")
        num *=2
    print("")


# In[ ]:


num = 17
for i in range(0,4):
    for j in range(0,i):
        print(num,end=" ")
        num +=2
    print("")


# In[ ]:


num = 0
for i in range(0,4):
    for j in range(0,i):
        
        pro=2**num
        num=num+1
        print(pro,end=" ")
    print("")
        


# In[ ]:


for i in range(0,5):
    for j in range(0,i):
        
        print(" ",end=" ")
    for k in range(5,i,-1):
        print("*",end=" ")
    print("")
        


# In[ ]:


'''
i  j  k
1  0  5
2  1  4
3  2  3



'''


# In[ ]:


for i in range(1,5):
    num = 1
    for j in range(1,i):
        
        print(" ",end=" ")
    for k in range(i,5):
        print(num,end=" ")
        num+=1
        
        
    print("")


# In[ ]:


num = 1
for i in range(0,5):
    for j in range(0,i):
        
        print(" ",end="   ")
    for k in range(5,i,-1):
        
        print(num,end="   ")
        num+=1
    print("")


# In[ ]:


chr(40)


# In[ ]:


for i in range(0,5):
    if(i%2!=0):
    
        for j in range(0,i):

            print(" ",end=" ")
        for k in range(5,i,-1):

            print("#",end=" ")
        print("")
    else:
        for j in range(0,i):

            print(" ",end=" ")
        for k in range(5,i,-1):

            print("$",end=" ")
        print("")


# In[ ]:


num = 4
for i in range(0,4):
    for j in range(0,i):
        
        print("  ",end="")
    for k in range(4,i,-1):
        
        print(num,end="")
        num+=2
    print("")


# In[ ]:





# In[ ]:


for i in range(1,6):
    for j in range(1,6):
        if(i==j or i==5 or j==1):
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print("")


# In[1]:


ord("$")


# In[13]:


for i in range(0,4):
    num=1
    for j in range(0,i):
        
        print(" ",end=" ")
    for k in range(4,i,-1):
        
        print(chr(64+num),end=" ")
        num+=1
    print("")


# In[ ]:




