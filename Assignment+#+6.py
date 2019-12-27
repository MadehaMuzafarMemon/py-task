
# coding: utf-8

# In[1]:


#Q U E S T I O N _ 5

class car:
    def __init__(self,color,price,name,engine,model):
        self.color=color
        self.price=price
        self.name=name
        self.engine=engine
        self.model=model
    def changename(self):
        self.name=input('enter name')
    def changemodel(self):
        self.model=input('enter model')
    def print(self):
        print(self.color,self.price,self.name,self.engine,self.model)
        
a=car('gray','1','abc','auto','111xcx')
a.changename()
a.print()

b=car('gray','2','abcd','auto','222xcx')
b.changemodel()
b.print()

c=car('gray','3','abce','auto','333xcx')
c.print()
d=car('gray','4','abcf','auto','444xcx')
d.print()

e=car('gray','5','abcf','auto','555xcx')
e.print()


# In[ ]:


# Q U E S T I O N _ 1

Object-oriented programming  refers to a type of computer programming  in which programmers define the
data type of a data structure and also the types of operations  that can be applied to the data structure.

# Q U E S T I O N _ 2

1. Re-usability
2. Data Redundancy
3. Code Maintenance
4. Security
5. Design Benefits
7. Easy troubleshooting
8. Polymorphism Flexibility


# Q U E S T I O N _ 3

Unlike a function, methods are called on an object. Like in our example above we call our method .i.e. my_method on the
object cat whereas the function sum is called without any object. Also, because the method is called on an object,
it can access that data within it.
# Q U E S T I O N _ 4


CLASS:
A class is a user defined blueprint or prototype from which objects are created. It represents the set of properties or methods
that are common to all objects of one type.
OBJECT: 
Object is simply a collection of data and methods that act on those data. And, class is a blueprint
for the object.
ATTRIBUTE:
Everything in Python is an object, and almost everything has attributes and methods. In python, functions too are objects.
So they have attributes like other objects. 
BEHAVIOUR:
Objects in Python are generally classified according to their behaviors and the features that they implement.

