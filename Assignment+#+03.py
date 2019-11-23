
# coding: utf-8

# In[1]:


def add(x, y):
   return x + y

def subtract(x, y):
   return x - y

def multiply(x, y):
   return x * y

def divide(x, y):
   return x / y

def power(x, y):
   return x ** y

choice = input('''Attention:
1. Addition
2. Subtract
3. Multiplication
4. Division
5. Power
Select Operation: ''')
print('\n')
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
print('\n')
if choice == '1':
   print(num1,"+",num2,"=", add(num1,num2))
elif choice == '2':
   print(num1,"-",num2,"=", subtract(num1,num2))
elif choice == '3':
   print(num1,"*",num2,"=", multiply(num1,num2))
elif choice == '4':
   print(num1,"/",num2,"=", divide(num1,num2))
elif choice == '5':
   print(num1,"^",num2,"=", power(num1,num2))
else:
    print("Invalid input")


# In[2]:


i_list = [1, 2, 5, 'hello', 'Hi']
count=0
for i in i_list:
    if type(i) == int:
        count = 1
        
if count == 1:
    print('There are integers in the list')
else:
    print('There are no integers in the list')


# In[3]:


dic = {0:10, 1:20}
print("Before Adding a new key " + str(dic))
dic.update({2:30})
print("After Adding a new key " + str(dic))


# In[4]:



i_sum=0
dic1 = {0:10, 1:20, 2:"Hello"}
for i in dic1:
    if type(i) == int:
        i_sum = i_sum+i
print(i_sum)


# In[5]:


def Repeat(x): 
    size = len(x) 
    repeated = [] 
    for i in range(size): 
        k = i + 1
        for j in range(k, size): 
            if x[i] == x[j] and x[i] not in repeated: 
                repeated.append(x[i]) 
    return repeated 
  

list1 = [10, 20, 30, 20, 10, 20, 30, 40,  50, -20, 60, 60, -20, -20] 
print (Repeat(list1))


# In[6]:



def checkKey(dict, key): 
      
    if key in dict.keys(): 
        print("Present, ", end =" ") 
        print("value =", dict[key]) 
    else: 
        print("Not present") 
  
dict = {'a': 100, 'b':200, 'c':300} 
  
  
key = 'w'
checkKey(dict, key)

