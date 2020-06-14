# -*- coding: utf-8 -*-
import string
 
# DATE : 04.02.2019
# CONCEPT OF DICTIONARY

#Empty Dictionary
d1 = {}
type(d1)

# Add K-V pairs in the dictionary

d1[1]= 'NewsChannel'
d1[2]= 'Sports'
d1[3]= 'Movies'
d1[4]= 'Entertainment'

print(d1)

d1['a']= 'NewsChannel'
d1['b']= 'Sports'
d1['c']= 'Movies'
d1['d']= 'Entertainment'

print(d1)

# Accesing the dict. using key

d1[1]
d1[0] # This will give an ERROR

#Ways to access dict. - 3 ways

# WAY 1 : KEYS + VALUES

d1.items() # This will give results in TUPLE FORMAT 

for k,v in d1.items():
    print("key={0},value={1}".format(k,v))#Printing KEY VALUE in different 
                                            #format 

# WAY 2 : Only KEYS
                                            
print(d1.keys())                            

                                            
# WAY 3 : Only VALUES

print(d1.values())

# Exisistence KEY CHECK 

1 in d1
# So ... Programmatically , it looks like ...
if(1 in d1):
    print("KEY PRESENT")
else:
    print("KEY ABSENT")

# MERGING DICTIONARIES
    
d2 = {}
d2['name'] = 'deep bhatt'
d2['Proffession'] = 'Data Analyst and Programming'
d2['Age'] = 24
d2['Domain'] = 'Computer Science and Information Technology' 
print(d2)   

# To merge d2 with d1 and store it in d3 dictionary, we have to ...

d3 = dict(list(d1.items()) + list(d2.items()))
print(d3)

# Practice 

d4 = {}
d4['ItemCode'] = 1001
d4['ItemName'] = 'Apples'
d4['ItemDesc'] = 'This is an Fruit'
d4['ItemQty'] = 10
d4['ItemRate'] = 100
d4['ItemReOrder'] = 50
d4['ItemFlag'] = 101

print(d4)

print(d4.keys())

# To DELETE Dictionaries - K - V Pair

del d3['Domain']

'Domain' in d3.keys()

# Create a Dictionary with 1 KEY and MULTIPLE VALUES

# Names of Players

import random as r
ages =[];matches=[]; runs=[];avg=[]
sno = list(range(1,21)); print(sno)
names = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q',
         'r','s','t']
for i in range(1,21):
    ages.append(r.randint(18,38))
    matches.append(r.randint(1,400))
    runs.append(r.randint(1000,10000))
    avg.append(
            float(format(r.uniform(10.0,60.0),'.2f'))
            )

print(names)
print(ages)
print(matches)
print(runs)
print(avg)

# Here below , within single quotes is the key....so 

d_players = {
        'sno':sno,
        'playername':names,
        'age':ages,
        'matches':matches,
        'runs':runs,
        'average':avg
        }

print(d_players)

# Accessing the Dictionaries 

d_players['runs']

d_players['runs'][0:4]

d_players['playername'][0:3]


# ASSIGNMENT : Print out the names, matches , runs and average of the first 5

for i in range(5):
    print(d_players['playername'][i])
for i in range(5):
    print(d_players['runs'][i])
for i in range(5):
    print(d_players['matches'][i])
for i in range(5):
    print(d_players['average'][i])
    
# ASSIGNMENT : Find out the highest Scorer & Lowest Scorer 

# Dctionary in Dictionary - concept of NESTED DICTIONARY
    
services = {}

services['svc1'] = {'serviceid':1464,
        'servicename':'acrobatarservice',
        'status':'running',
        'group': 'acrobat update service'
        }

services['svc2'] = {'serviceid':13948,
        'servicename':'onesynsvc',
        'status':'running',
        'group': 'unistack service'
        }

# Accessing the NESTED DICTIONARY

print(services['svc1']['servicename'])

# To add one more key in nested dictionary 

services['svc1']['starttype'] ='automatic'






































































