# -*- coding: utf-8 -*-
# DATE : 12.02.2019
# CONCEPT OF object-oriented [OOP's] IN PYTHON...

# CLASSES

class cCompany():
    #variables
    def __init__(self):
        self.name = "Bhatt Corporation"
        self.address = "Pune Wagholi"
        self.total = 0
    #methods    
    def print(self):
        print("Name of the company is = " + self.name)
        print("Adress of the company is = " + self.address)
        
    def calculate_total(self,c1,c2):
        self.total = c1 + c2 
        print("Total Cost is {0}".format(self.total))
        
        if ((c1 <= 0) | (c2 <= 0)):
            print("Costs cant be ZERO !!")
            return
        else:
            self.total = c1+c2
            print("Total Cost is = {0}" .format(self.total))
        
        self.print()
# To create instance ..

#c1 = cCompany()
#c1.print()
c3 = cCompany()
c3.calculate_total(10,0)

# Creating parent and child classes in python...






