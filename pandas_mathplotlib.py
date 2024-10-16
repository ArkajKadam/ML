import numpy as np 
import pandas as pd 

data = {
         'PRN'  :  [1,2,3,4],
         's_name' : ["Arkaj","Rushi","Jay","sidd"]

}

df = pd.DataFrame(data,index = ['A','B','C','D'])

print(df)



import matplotlib.pyplot as plt
x=[1,2,3]
y=[10,20,30]
plt.plot(x,y,color='red',linestyle='--',marker='^',markerfacecolor='yellow',markersize=15,linewidth='1')

plt.title("Line plot",color='blue',fontsize=15)
plt.xlabel("x-axis")
plt.ylabel("y-axis")
plt.show()





x = [1, 2, 3, 4, 5]
y = [2, 4, 6, 8, 10]

plt.plot(x, y)

plt.title('Simple Graph')
plt.xlabel('X-axis')
plt.ylabel('Y-axis')

plt.show()


import matplotlib.pyplot as plt
import numpy as np

data = np.random.randn(1000)


plt.hist(data, bins=30, color='green', alpha=0.7, edgecolor='black')

plt.title('Histogram')
plt.xlabel('Value')
plt.ylabel('Frequency')

plt.show()
