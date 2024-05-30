#!/usr/bin/env python
# coding: utf-8

# In[1]:


print('hello','world','a',sep='22',end='#')


# In[2]:


#syntax of print()
#print(*objects,sep='',end='\n',file=sys.stdout,flush=False) 


# In[3]:


outdata=open("C:/Users/CHIKKI/Desktop/mydocuments_PrathapTejaswi/requirements.txt","w")
print('hello',file=outdata)


# In[4]:


#creating an empty list
numlist1=[]
numlist2=list()
#Tuple
num2=()
num1=tuple()
#set
numSet=set()
#dictionary
numDict={}
numDict1=dict()

num={1} #it takes as set
print(type(num))


# In[5]:


numList=[21,78,'hello',87,76539]
print(numList[-2])


# In[6]:


numList1=list(input().split())
print(numList1)


# In[7]:


num1=list(map(int,input().split())) #mapping number into int of list
print(num1)


# # take 2 diff lists , merge them and print a new sorted list

# In[8]:



l1= list(map(int,input().split()))
l2= list(map(int,input().split()))
res= l1 + l2
print(sorted(res))
#print(res.sort())


# 

# In[9]:


l1=[1,2,3,6]
l2=[0,5,7]
l=l1+l2
print(sorted(l))


# In[2]:


data='hello'
dlist=list(data)
print(dlist)
print(sorted(dlist))


# # given an int n, return all numbers in range[1,n] sorted in lexicographical order

# In[1]:



data=int(input())
rList=[str(i) for i in range(1,data+1)]
rList.sort()
print(list(map(int,rList)))


# # read a list and swap first and last element in list

# In[2]:


l=list(input().split())
l[0],l[-1]=l[-1],l[0]
print(l)


# # stealing max values of houses without stealing 2 adjacent houses
# 

# In[3]:


house=list(map(int,input().split()))
emax=sum(house[0::2])
omax=sum(house[1::2])
tmax=0
while(max(house)!=0):
    tmax+=max(house)
    i=house.index(max(house))
    if i==0:
        house[0],house[1]=0,0
    elif i==len(house)-1:
        house[-2],house[-1]=0,0
    else:
        house[i],house[i+1],house[i-1]=0,0,0
print(max([omax,emax,tmax]))


# In[8]:


def max_steal(houses):
    n = len(houses)
    dp = [0] * n
    dp[0] = houses[0]
    dp[1] = max(houses[0], houses[1])
    
    for i in range(2, n):
        dp[i] = max(houses[i] + dp[i - 2], dp[i - 1])
    
    return dp[-1]
houses = list(map(int, input().split(',')))
print(max_steal(houses))


# # all 

# In[6]:


l=[9,2,1]
print(all(l))#if no false value is given, then it returns True


# In[7]:


l=[0,1,2]
print(all(l))#if false value is given, then it returns False


# # any

# In[8]:


l=[1,4,0,5]
print(any(l))#if any one true value is given it returns True


# In[9]:


l=['',[],(),False,0]
print(any(l))


# # repetition

# In[11]:


l=[1,2,3]
print(l*2)


# # cubes of 1-5 numbers in list

# In[12]:


cubes=[]
for i in range(1,6):
    cubes.append(i*i*i)
print(cubes)


# In[13]:


cubeList=[i*i*i for i in range(1,6)]
print(cubeList)


# In[15]:


cubeList=[i*i*i for i in range(1,6) if i%2==0]
print(cubeList)


# # print odd indexed elements in list

# In[25]:


data="Hello Everyone"
print([data[i] for i in range(len(data)) if i%2!=0])
#or
print([ch for ch in data[1::2]])


# In[26]:


data="Hello Everyone"
resList=[]
for i in range(len(data)):
    if i%2!=0:
        resList.append(data[i])
print(resList)
#or
oRes=[]
for ch in data[1::2]:
    oRes.append(ch)
print(oRes)


# In[27]:


l=[1,2,3,3,2]
print(max(l))


# 
# # find min no.potions required to compete with hurdles

# In[29]:


# sample input:
  #  5 4
   # 1 6 5 3 2 
# sample output:
   # 2                  '''max-k=output'''


# In[28]:


# n=hurdles k=units of magic potion hList=heigts of hurdles 
n,k=map(int,input().split())        
hList=list(map(int,input().split()))
print(max(hList)-k)


# # return max number of consecutive 1's in array

# In[30]:


biList=list(map(int,input().split(','))) #like [0,1,1,0,1,1,1]
count,maxVal=0,0
for i in biList:
    if i==1:
        count+=1
        if count>maxVal:
            maxVal=count
    else:
        count=0
print(maxVal)


# # 2 arrays of same size n find min value of A[0]*B[0]+...A[n-1]*B[n-1] if shuffling of elements is allowed

# In[31]:


#hint: keep A in asc and B in desc
a=list(map(int,input().split()))
b=list(map(int,input().split()))
a.sort()
b=sorted(b)[::-1]
res=0
for i in range(len(a)):
    res+=a[i]*b[i]
print(res)


# In[38]:


#another method
a=list(map(int,input().split()))
b=list(map(int,input().split()))
a.sort()
sorted(b).reverse()
'''b.sort()
b.reverse()'''
res=0
for i in range(len(a)):
    res += a[i]*b[i]
print(res)


# # given lists in  list,find max sum of elements of list in a list of lists and print its index

# In[40]:


n=int(input())
nestlist=[list(map(int,input().split())) for i in range(n)]
print(nestlist)
maxIn,tsum=0,0
for index,data in enumerate(nestlist):
    if tsum<sum(data):
        tsum=sum(data)
        maxIn=index
print(maxIn)


# # remove element from specified index

# In[42]:


'''input: read tuple and index
    output: remove element from specified index and print tuple'''
#program to remove element from specified index input:tuple,index
n=int(input())#index you want to remove
t=tuple(input())#give continuous values without space
l1=list(t)
l1.pop(n)
print(tuple(l1))
print(t[:n]+t[n+1:])


# # remove empty tuple(s) from list of tuples

# In[43]:


'''input: read list
output: print list after removing the empty tuples'''
myData=[(),(),('',),(1,2,3),(5,1)]
myData=[i for i in myData if i and all(i)]
print(myData)


# In[ ]:




