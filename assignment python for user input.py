#!/usr/bin/env python
# coding: utf-8

# In[2]:


x=int(input("enter the number for day of the week: "))

if(x==1):
    print("Sunday")
elif(x==2):
    print("Monday")
elif(x==3):
    print("Tuesday")
elif(x==4):
    print("Wednesday")
elif(x==5):
    print("Thursday")
elif(x==6):
    print("Friday")
elif(x==7):
    print("Saturday")
else:
    print("not valid")


# In[4]:


x=int(input("enter the number for month of the year: "))

if(x==1):
    print("January")
elif(x==2):
    print("Febuary")
elif(x==3):
    print("March")
elif(x==4):
    print("April")
elif(x==5):
    print("May")
elif(x==6):
    print("June")
elif(x==7):
    print("July")
elif(x==8):
    print("August")
elif(x==9):
    print("September")
elif(x==10):
    print("October")
elif(x==11):
    print("November")
elif(x==12):
    print("December")
else:
    print("not valid")


# In[5]:


x=int(input("enter the marks of the student: "))

if(x<=60):
    print("Fail")
elif(x>60 and x<=80):
    print("Average")
elif(x>80 and x<=90):
    print("Good")
elif(x>90 and x<=100):
    print("Excellent")
else:
    print("not valid")


# In[ ]:




