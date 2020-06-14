# -*- coding: utf-8 -*-
"""
Created on Mon Feb  4 12:47:48 2019

@author: himanshu
"""

# DATE : 04.02.2019
# CONCEPT OF SETS

# Creating Sets with SET keyword ...

set1 = set(['violet' , 'indigo' , 'blue' , 'green' , 'orange' , 'red'])

set2 = set(['cyan' , 'yellow' , 'blue' , 'pink' , 'black' , 'red' , 'white'])

print(set1)


# To know the length of the set ...

len(set2)

# OPERATIONS ON SETS....

# OPERATION 1 : UUNION

set1.union(set2)
union_sets = set1.union(set2)

print(union_sets)

# OPERATION 2 : INTERSECTION OF SETS 

set1.intersection(set2)

# OPERATION 3 : MINUS OF SETS

    # A - B

a_b = set1.difference(set2)
print(a_b)

    # B - A

b_a = set2.difference(set1)
print(b_a)

# OPERATION 4 : SYMENTRIC DIFFERENCE OF SETS - will print unique elements of 
                                        #the set ...

set1.symmetric_difference(set2)


# Removing DUPLICATES in SETS ...

lov =  [1,2,3,3,3,3,5,7,65,65,65,9,9,9,8,7,34,87]
print(set(lov))

lov = list(set(lov))
print(lov)

# ASSIGNMENTS : Create ...in pic 




































