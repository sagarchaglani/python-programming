#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#program to find grading
num = int(input('enter the obtain marks  = '))
if num >=90 and num <=100:
    print('grade = ' , 'A' , "OH! vey")
if num >=80 and num <=89:
    print('grade  =', 'B')
if num >=70and num <=79:
    print ("Grade =", "C")
if num >=60 and num <=69:
    print('Grade =','D')
else:
    if num<=59:
        print("grade  =",'fail')
        print('Better luck Next Time')
       

    


# In[13]:


#A company decided to give bonus of 5% to employee if his/her year of service is more than 5 years.
#Ask user for their salary and year of service and print the net bonus amount.
salary = int(input('enter the salary  = '))

service = int(input('year of service = '))

if service >5:

    print('bonus', 0.5*salary)
else:

    print('No Bonus = ')


# In[5]:


#Take values of length and breadth of a rectangle from user and check if it is square or not.
length,breadth = int(input('enter the lenth of rectangle = ')), int(input('enter the breadth of rectangle = '))
if length == breadth:
    print ('yes it is square')
else:
    print('no', '\n It is only rectangle')


# In[11]:


#Take two int values from user and print greatest among them.

value1,value2 = int(input('enter first value = ')),int(input('enter second value = '))
if value1>value2:
    print('value1 is greatest')
elif value1<value2:
        print('value2 is greatest')
else:
    if value1==value2:
        print('values are equal')


# In[ ]:


'''A shop will give discount of 10% if the cost of purchased quantity is more than 1000.
Ask user for quantity
Suppose, one unit will cost 100.
Judge and print total cost for user.'''


# In[ ]:


cost = int(input('enter the cost of purchased quantity = '))
if cost*100=1000
    print('discount', 


# In[ ]:


print "Enter quantity"
quantity = input()
if quantity*100 > 1000:
  print "Cost is",((quantity*100)-(.1*quantity*100))
else:
  print "Cost is",quantity*100


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




