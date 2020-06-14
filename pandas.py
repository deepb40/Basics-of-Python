import pandas as pd

path = "C:/Users/Himanshu/Documents/R Class Exercises Per day/Datasets/dataset/glass.csv" 
# Wrong path it is ..please change 

# import dataset
df_glass = pd.read_csv(path)

# view dataset

print(df_glass)

#default : 5 (also you can specify records (10) means first 10 records)
df_glass.head()

#for bottom records default : 5, (specify number of records)
df_glass.tail()

#dimension of the dataset
df_glass.shape

#display the column names of dataset

cols = df_glass.columns
len(cols)

#datatypes of the columns

df_glass.dtypes

#describe the dataset

df_glass.describe()

#get unique values of a column

df_glass.columns
df_glass.Type.unique()

#accessing the dataframe
#selecting columns from dataset
#1 column
df_glass['RI']

#>1 columns
df_glass[['RI','Mg','Na',]]
#select RI, Mg, Na from df_glass

#with conditions
# select RI, Mg, Na from df_glass
#where Mg>20
# and Na > 13
#and RI > 1.53

#create a subset of the dataframe

df_filter1 = df_glass[['RI','Mg','Na']] [(df_glass.Mg > 2) & (df_glass.Na > 13) 
& (df_glass.RI > 1.52)]

print(df_filter1)
df_filter1.columns


#to drop unwanted columns from dataframe
df_glass = df_glass.drop(['id_number'],axis=1)

df_glass.columns

#check for anomalies
# 1) check for 0's

df_glass.RI[df_glass.RI == 0] #NO 0's for RI column

#condition for checking 0's
#len statement gives the number of zeros

if (len(df_glass.RI[df_glass.RI == 0]) > 0):
    print("column RI has 0")
else:
    print("column RI has no 0")
    
# 2) NULL check
    
if(len(df_glass.RI[df_glass.RI.isnull()]) > 0):
    print("nulls are present")
else:
    print("no nulls")

#generic script to check 0 for all columns

#check for 0's    
cols = df_glass.columns
print(cols)

for e in cols:
    if(len(df_glass[e][df_glass [e] == 0]) > 0):
        print("column {0} has zeroes".format(e))
    else:
        print("column {0} has no zeroes".format(e))

#check for nulls

    if(len(df_glass[e][df_glass[e].isnull()]) > 0):
        print("column {0} has NULLS".format(e))
    else:
        print("column {0} has no NULLS".format(e))
    
    print("\n")
    
#check for blanks
# NA values means there are no values
    
    if(len(df_glass[e][df_glass[e].isna()]) > 0):
        print("column {0} has NA values".format(e))
    else:
        print("column {0} has no NA values".format(e))

#assignment
#find the special characters in the dataset
#assignment single(=)
#        

#updating the dataset to fix anomalies

len(df_glass.Ba[df_glass.Ba == 0])

#update Ba with 9999, where Ba == (the statement in[] is where condition) 

df_glass.Ba[df_glass.Ba==0] = 9999        

#check if the updates have taken place        
        
len(df_glass.Ba[df_glass.Ba == 9999])

#format gives the output in the form of a string

mean_Ba = float(format(df_glass.Ba[df_glass.Ba!=9999].mean(),'.2f'))

print(mean_Ba)

df_glass.Ba[df_glass.Ba == 9999] = mean_Ba

df_glass.Ba[df_glass.Ba == mean_Ba]

#---------------------------------------------

#creating a panda dataframe from scratch
# 1) first create a dictionary
# 2) convert dictionary into pandas        
   
import random as r

age=[]; matches=[]; runs=[]; avg=[]
sno = list(range(1,21));print(sno)
name = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t']

for i in range(1,21):
    age.append(r.randint(18,38))
    matches.append(r.randint(1,400))
    runs.append(r.randint(1000,10000))
    avg.append(
            float(format(r.uniform(10.0,60.0),'.2f'))
            )    

#create to dictionary
    
d_players = {'sno':sno, 'playername':name, 'age':
    age, 'matches':matches, 'runs':runs, 'average':avg}

print(d_players)    

#convert dictionary to dataframe

df_players = pd.DataFrame(d_players)

print(df_players)

#rearranging the column sequence 
cols = ['sno','playername','age','matches','runs','average']

df_players = df_players[cols]

print(df_players)






