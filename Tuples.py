# -*- coding: utf-8 -*-

# CONCEPT OF TUPLES

t1 = ()
type(t1)
len(t1)

t1=('news','movies','tv series','sports','game show','music')
print(t1)


#acessing a tuple
t1[0]
primary_channels = t1[0:3]
type(primary_channels)

for e in t1:
    print("tuple has " + e)
    
del t1[0]

t1 = list(t1)
type(t1)
t1[0] = 'technology news'

print(t1)

t1=tuple(t1)
type(t1)

print(t1)

t1.append('education')

t_t1 = ('education','healthcare','IT','farming')

#appending values to an existing tuple
#first create a new tuple
t_t1 = ('education','healthcare','IT','farming')

#append the tuple
t1=t1+t_t1

print(t1)

'IT' in t1

#index of an element
t1.index("movies")

#tuple of lists

#inventory data
item_code, item_name, itemq_qty, reorder_qty, item_flag, item_price

'IT/00910','steel wire', 1800, 100, 'Y', 20000

inventory = (
        ['IT/00910','steel wire', 1800, 100, 'Y', 20000],
        ['ABC001','blue pen',500,10,'Y',20],
        ['PR/189/1','papers',210,5,'N',1900])

print(inventory)

inventory[2]
inventory[2][1]

#tuple of numbers

t_num1 = tuple(range(1,51))
print(t_num1)

max(t_num1)
min(t_num1)

sum(t_num1)

avg = (sum(t_num1)/len(t_num1))
print(avg)

odds,evens,vowels = tuple(range(1,51,2)),tuple(range(1,51,2)),('a','e',
                         'i','o','u')

print(vowels)


#Assignment


import random as r

itemname = ['AFG','KJA','FIE','IEJ','YUE','IOP','QWE','JGI','KOP','MAN']
qty=[]
price=[]
total_price=[]

for i in range(10):
    qty.append(r.randint(2,16))
    price.append(r.randint(12,100))

gro=(itemname, qty, price)
gro

type(gro)

for i in range(10):
    total_price = qty[i]*price[i]
    print(total_price)
    
gro=(itemname, qty, price, total_price)

type(total_price)

gr1 = list(gro)

gr1.append(total_price)

