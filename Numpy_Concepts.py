# -*- coding: utf-8 -*-
"""
Created on Thu Feb  7 11:21:31 2019

@author: himanshu
"""

# DATE : 07.02.2019
# CONCEPT OF numpy IN PYTHON...


import numpy as np
import math

#Creating a python list ...

list1 = [1,2,3,4,5,6]
list2 = [7,8,9,10,11,12]

# Creating an NUMPY array..

list1 = np.array([1,2,3,4,5,6])
list2 = np.array([7,8,9,10,11,12])

type(list1)

list1 + list2

list1 * math.pi   

list1.shape # to see what dimensional array is list ..!

#Creating an Multi Dimensional Array ..

list3 = np.array([[10,15,20],[18,19,81],[19,67,71]])
print(list3)

list3 * 5 # To mulitply by 5 thorugh every element of matrix..

# To extract first row of the matrix

list3[0] * 5

# To create a Range of values ...

seq_no = np.arange(1,51)
print(seq_no)

#Reshaping the Matrix ..FISRT use of RESHAPE - convert 1D matrix to "N"d Matri

seq_no = seq_no.reshape(5,10)
print(seq_no)

# To Transpose a matrix..

seq_no.T

#USE of RESHAPE - Second 
result = seq_no.reshape(2,5,5)
print(result)

# To store 2 matrixes into different different one NUMPY array ... 

line1=result[0]
line2=result[1]

print(line2)

# CONCEPT OF FANCY INDEXING ..
#------------------------------------

#To create random Numbers ...

random_numbers = np.random.randint(1,101,50)
print(random_numbers)

# To create a mask ..

mask = (random_numbers%3 == 0)
 
print(mask)

random_numbers[mask]

# Random Number Generation Using NUMPY...!
#-----------------------------------------------

# Random FLoat numbers 




















