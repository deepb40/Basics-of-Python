# -*- coding: utf-8 -*-
"""
Created on Wed Feb  6 12:02:49 2019

@author: himanshu
"""

# DATE : 06.02.2019
# CONCEPT OF LAMBDA FUNCTIONS 

# add 2 numbers
def add (n1,n2):
    return(n1+n2)
add(20,25)

# lambada function
add = lambda n1,n2 : n1+n2
add(45,70)

add = lambda n1,n2,n3 : n1+n2+n3
add(45,70,10)

# multiply
mul = lambda n1,n2 : n1*n2
mul(45,70)

# bigger and smaller number
big = lambda n1,n2 : n1 if n1>n2 else n2
big(25,45)
small = lambda n1,n2 : n1 if n1<n2 else n2
small(38,101)

# iterations
num1 = [2,3,4,5,6,7]
for e in num1:
    print(e*e)
    
list(map(lambda x:x*x,num1))

# calculate area of rectangle
import random as r
l=[];b=[]
for i in range(10):
    l.append(r.randint(30,100))
    b.append(r.randint(1,20))

print(l)
print(b)

list(map(lambda l,b : l*b, l,b))

import random as r
temp=[]
for i in range(50):
    temp.append(float(format(r.uniform(98.0,105.0),'.2f')))
   
list(filter(lambda x:x>101, temp))

# using lambda function check if given list number is odd 

import random as r
l=[];
for i in range(15):
    l.append(r.randint(30,100))
    
list(filter(lambda x: x % 2 == 1 ,l)) #odd
list(filter(lambda x: x % 2 == 0 ,l)) #even
