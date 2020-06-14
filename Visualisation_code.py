import matplotlib.pyplot as plt 
import numpy as np 

x = np.random.randint(1,100,25)
y = np.random.randint(10,20,25)

# Line graph Example 

plt.plot(x,y)
plt.xlabel("X Random")
plt.label("Y Random ")
plt.title("LINE GRAPH")
plt.show()

# Scatter Plot Example

actual =  np.round(np.random.uniform(10,100,25),decimals = 2)
predicted =  np.round(np.random.uniform(10,100,25),decimals = 2)

plt.scatter(actual,predicted,color = ['red','blue'])
plt.show()

# Bar Chart Example 

names = ['a','b','c','d','e']
avg_1 = np.round(np.random.uniform(1,100,5),decimals = 2)
avg_2 = np.round(np.random.uniform(1,100,5),decimals = 2)

plt.bar(names,avg_1,label="Average 1",color="r")
plt.bar(names,avg_2,label="Average 2",color="y")

plt.xlabel("NAMES")
plt.label("AVERAGE OF 1 AND 2")

plt.legend()
plt.show()

# Histogram Example 


# Pie Chart Example 





