import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as im
import mpl_toolkits.mplot3d.axes3d


fig = plt.figure()
p = plt.subplot(111, projection='3d')
# data = range(10)
# x = np.array(data)
data = [1,5,3,6,3,5,6,3,2]
x = np.array(data)



p.plot_wireframe(x,x, x.reshape(1,-1), color='r', linestyle=':')
p.scatter(x, x, x, marker = 'o', color = 'black', s = 150)
p.set_xlabel('sumbu X')
p.set_ylabel('sumbu Y')
p.set_zlabel('sumbu Z')
plt.show()
