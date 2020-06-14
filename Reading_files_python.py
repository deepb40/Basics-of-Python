# -*- coding: utf-8 -*-
"""
Created on Thu Feb  7 09:03:38 2019

@author: himanshu
"""

# DATE : 07.02.2019
# CONCEPT OF FILE HANDLING IN PYTHON...

import os
from datetime import datetime as dt 
import pandas as pd


#  CWD - CURRENT WORKING DIRECTORY

os.getcwd()

# Reading a file 

file = "C:\\Users\\himanshu\\Desktop\\shivaji.txt" 

# Open the file 

myfile = open(file,"r")

print("File Name is " + myfile.name) # To get the file path and the 
                                            # name of the file..

# To print the contents of the file 
                                            
myfile.readlines()

# To Reset the file pointer to the start , follow below ..

position = myfile.seek(0,0)

# To read "n" number of characters in the file ..

print(myfile.read(20))

# To read 1 line in the file ..

sentence = myfile.readline()

print(sentence)

# To convert to words from sentence .. (USE OF SPLIT() Function)

sentence.split()

#To close the file handle ...

myfile.close()


# How to write a file??
#------------------------

file = "C:\\Users\\himanshu\\Desktop\\writefile.txt" 

# Opening the file for writing in Write and append mode (W+)..

myfile = open(file,"w+")

today = str(dt.now()) # to egt current date and time..
print(today)

myfile.write(today)
myfile.write("I am writing the second line ")
myfile.write("\n\n")
myfile.write("I am writing the third line ")

myfile.write(sentence)
myfile.close()

# How to open a .CSV file ?

file = "C:\\Users\\himanshu\\Documents\\titanic.csv" 

# To read a .CSV file ...

titanic = pd.read_csv(file)
print(titanic)










































