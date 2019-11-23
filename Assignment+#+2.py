
# coding: utf-8

# In[1]:


i1 = int(input('Marks of Subject No.1 = '))
i2 = int(input('Marks of Subject No.2 = '))
i3 = int(input('Marks of Subject No.3 = '))
i4 = int(input('Marks of Subject No.4 = '))
i5 = int(input('Marks of Subject No.5 = '))
i_total = i1 + i2 + i3 + i4 + i5
print('Total Marks = ' + str(i_total))
i_max = int(input('Maximum Marks = '))
i_perc = (i_total*100) / i_max
print('Percentage = ' + str(i_perc))
if i_perc < 50:
    print('Grade = F')
elif i_perc <60:
    print('Grade = D')
elif i_perc <70:
    print('Grade = C')
elif i_perc <80:
    print('Grade = B')
elif i_perc <90:
    print('Grade = A')
elif i_perc <=100:
    print('Grade = A1') 
else:
    print('Invalid Input')


# In[2]:


i = int(input('Enter Your Number = '))
i_mod = i%2
if i_mod == 0:
    print('Even')
else:
    print('Odd')


# In[3]:


cities = ["Atlanta", "Baltimore", "Chicago", "Denver", "Los Angeles", "Seattle"]
i_length = print("The length of the list is = " + str(len(cities)))
i_length


# In[4]:



i_list = [2, 4, 5, 6, 7, 7, 8, 9]
i_sum = 0
for i in i_list:
    i_sum += i
    
print(i_sum)


# In[5]:


i_list2 = [2, 4, 5, 6, 7, 7, 10, 9]
i_list2.sort(key=None, reverse = True)
i_list2.pop(0)


# In[6]:



i_list = [2, 4, 5, 6, 7, 7, 8, 9]
for i in i_list:
    if i<5:
        print(i)

