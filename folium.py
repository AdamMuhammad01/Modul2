import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import mpl_toolkits.mplot3d.axes3d
import folium



fig = plt.figure()
p = plt.subplot(111,projection = '3d')


x = np.arange(10)   #data x
y = np.arange(10)    #data y
z = np.ones(10)

dx = np.ones(10)
dy = np.ones(10)
dz = np.arange(10)   # data dz


p.bar3d(x, y, z, dx, dy, dz,
        color = ['r','pink','g','orange','r','pink','g','orange','k','b'])
p.set_xlabel('sumbu X')
p.set_ylabel('sumbu Y')
p.set_zlabel('sumbu Z')

p.set_yticks([1,5])

plt.show()
