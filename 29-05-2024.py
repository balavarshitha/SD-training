#!/usr/bin/env python
# coding: utf-8

# In[3]:


class Student:
  def __init__(self,roll,name,phone,address):
    self.roll=roll
    self.name=name
    self.phone=phone
    self.address=address
  def displayInfo(self):
    print('roll:',self.roll,'name: ',self.name,'phone:',self.phone,'address:',self.address)
st1=Student(2007,'Anvitha',9876543210,'Warangal')
st1.displayInfo()


# In[5]:


class test:
  def __init__(self,a="Hello World"):
    self.a=a
  def display(self):
    print(self.a)
t1=test() #obj creation
t1.display()


# In[6]:


#to get a list, sorted in increasing order by last element in each tuple from given list of non-empty tuples
#input:  [(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)]
#output: [(2, 1), (1, 2), (2, 3), (4, 4), (2, 5)]
def end(data):
  return data[-1]
n=int(input())
l=[]
for i in range(n):
  l.append(tuple(map(int,input().split())))
l.sort(key=end)
print(l)


# In[9]:


class Test:
  def __init__(self):
    self.x=0
class Derived_Test(Test):
  def __init__(self):
    Test.__init__(self)
    self.y=1
def main():
  d=Derived_Test()
  print(d.x,d.y)
main()


# In[11]:


class A:
  n=10
  def __init__(self,z,y=5):
    self.zee=z
    self.yee=y
  def disp(self):
    print(self.zee,self.n)
class B(A):
  def __init__(self,m,x,p):
    self.my=m
    A.__init__(self,x,p)
obj=B(10,15,21)
obj.disp()


# In[13]:


class A:
  def __init__(self,z):
    self.zee=z
class B(A):
  def __init__(self,z,x):
    super().__init__(x)
    self.zee=z
  def p(self):
    print(self.zee,A(12).zee)
obj=B(10,15)
obj.p()


# In[14]:


class A:
  def __init__(self,x=3):
    self._x=x
class B(A):
  def __init__(self):
    super().__init__(5)
  def display(self):
    print(self._x)
def main():
  obj=B()
  obj.display()
main()


# In[15]:


# to remove dulicates from a list
#input: 1 4 2 5 5 3 4 7
#output: [1,4,2,5,3,7]
numList=list(map(int,input().split()))
resList=[]
for i in numList:
   if i not in resList:
    resList.append(i)
print(resList)


# # overriding

# In[16]:


class Product:
    def disp(self):
        print("This is a product info")
class Cal(Product):
    def disp(self):
        print("This is a calculation info")
        super().disp()
p1=Cal()
p1.disp()


# # Overload

# In[18]:


class Product:
    def disp(self):
        print("this is a product info")
    def disp(self,name):
        print("name is",name)
p1=Product()
p1.disp()
p1.disp("hello")


# In[20]:


class A:
    def __str__(self):
        return '1'
class B(A):
    def __init__(self):
        super().__init__()
class C(B):
    def __init__(self):
        super().__init__()
def main():
    o1=B()
    o2=A()
    o3=C()
    print(o1,o2,o3)
main()


# In[22]:


class A:
    def __init__(self):
        self.m='Hi'
    def __str__(self):
        return 'Hello'
objA=A()
print(objA.m)
print(objA)


# In[23]:


class A:
    def __init__(self,x,y):
        self.x=x
        self.y=y
    def __str__(self):
        return 1
    def __eq__(self,other):
        return self.x*self.y==other.x*other.y
o1=A(5,2)
o2=A(2,5)
print(o1==o2)


# In[26]:


# some prime no.s can be expressed as sum of other consecutive prime no.s
#5=2+3
#17=2+3+5+7
def isPrime(num):
    if num==0 or num==1:
        return False
    for deno in range(2,int(num**0.5)+1):
        if num%deno==0:
            return False
    return True
num=int(input())#20
primeList=[i for i in range(2,num+1) if isPrime(i)]
count,pSum=0,primeList[0]
for p in primeList[1:]:
    pSum+=p
    if pSum>num:
        break
    if isPrime(pSum):
        count+=1
print(count)


# In[ ]:




