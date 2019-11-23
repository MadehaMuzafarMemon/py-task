
# coding: utf-8

# In[1]:


import datetime
import platform


# In[2]:


print("""Twinkle, twinkle, little star,
      How I wonder what you are!
          Up above the world so high,
          Like a diamond in the sky.
  Twinkle, twinkle, little star,
      How I wonder what you are
      """)


# In[3]:


print("Current Python version is " + platform.python_version())


# In[4]:


now = datetime.datetime.now()


# In[5]:


print("Date is " + now.strftime("%Y-%m-%d"))
print("Time is " + now.strftime("%H:%M:%S"))


# In[6]:


rad = float(input("Radius = "))
comrad = rad*rad
pi=3.14
area = pi*rad**2
print(area)


# In[7]:


def reverse_slicing(s):
    return s[::-1]

fname = input("first name = ")
lname = input("last name = ")

full_name = fname + " "+ lname
print("Reverse = " + full_name[::-1])


# In[ ]:



str1 = input("First Input = ")
str2 = input("Second Input = ")
print(str1 + " " + str2)

