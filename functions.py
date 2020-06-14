# -*- coding: utf-8 -*-
"""
Created on Wed Feb  6 09:42:33 2019

@author: himanshu
"""
# DATE : 06.02.2019
# CONCEPT OF FUNCTIONS 

# Writing Functions 

def calnetsal(base,al,hs,t):
    if(base==0):
        msg = "Base Amount cannot be 0"
        return(msg)
        
    gross = base + al + hs
    net = gross - (t/100)*gross
    return(net)
        
netsalary = calnetsal(0.0,1100,800,10)
print(netsalary)

bonus = 10000
netsalary + bonus

# ASSIGNMENT : base != 0 , a != 0
            #gross -> <=20,000 <- tax = 10%
            #gross -> <=20,001 to 50,000 <- tax = 15%
            #gross -> <=51,000 to 1,00,000 <- tax = 20%
            #gross -> >= 1,00,000 <- tax = 30%
# Calculate Net Salary with the following conditions..
            

# Creation of Function with OPTIONAL PARAMETERs...
            
def calnetsal(base,al,t=25): # t=25 is an OPTIONAL PARAMETER 
    print('BASE = ' + str(base))
    print('ALLOWANCES = ' + str(al))
    print('TAX = ' + str(t))
    return(1)          

calnetsal(20000,2100) # Here , tax variable being an optional parameters...it 
                        #is not compulsory to specify the tax pararmeter while 
                        #calling the function... As you see in the example...
                        
# Another Example for OPTIONAL PARAMETER
def calnetsal(base,al,t=25):
    if((base==0) | (al==0)):
        msg = "Base Amount + Allowances cannot be 0"
        return(msg)
        
    gross = base + al
    net = gross - (t/100)*gross
    return(net)

calnetsal(1000000,10000,10)

# Concept of NAMED PARAMETERS

calnetsal(t = 10,base = 1000000,al = 10000)

#ASSIGNMENT : Create function namely "Calitemprice" which takes 4 parameter -
            # 1. Itemcost , 2. Overhead cost , 3. Tax(IN %) , 4.discount(IN %) 
            # overhead,Tax and discount are optional parameters ..
            # Item cost is mandatory and greater than 0..
            # discount can be 0..
            # Tax cant be 0..
            # Overall price calculations - First apply discount on total price
            #(itemcost + overhead cost) 
            #then, apply tax on discounted price 
            # Finally , return the FINAL PRice ....

def cal_item_price(item_cost,overhead_cost=1500,tax=18,discount=5):
    if(item_cost == 0):
        msg = "Item_Cost cannot be 0"
        return(msg)
        
    total_price = item_cost + overhead_cost 
    total_price = total_price - ((discount/100)*total_price)
    total_price = total_price + ((tax/100) * total_price)
    return(total_price)
   
cal_item_price(5000)

# Passing a list as a parameter

def multiply(*mylist):
    x=1
    for e in mylist:
        x = x * e
    
    return(x)
mylist = [2,4,6,8,10]
multiply(*mylist)

#ASSIGNMENT : Create and execute an function to calculate HCF between the given 
                #numbers..
                
def computeHCF(x, y):

# choose the smaller number
    if x > y:
        smaller = y
    else:
        smaller = x
    for i in range(1, smaller+1):
        if((x % i == 0) and (y % i == 0)):
            hcf = i    
    return hcf

num1 = 54 
num2 = 24

print("The H.C.F. of", num1,"and", num2,"is", computeHCF(num1, num2))

# Using while Loop ..

x,y = input("Enter two integer").split()
x,y = [int(x), int(y)] #convert input string to integers


a = x
b = y

while(b != 0 ):
	t = b
	b = a % 
	a = t

hcf = a
lcm = (x*y)/hcf

print("HCF of %d and %d is %d\n" %(x,y,hcf))
print("LCM of %d and %d is %d\n" %(x,y,lcm))




