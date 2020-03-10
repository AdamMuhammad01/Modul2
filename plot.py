import matplotlib.pyplot as plt


x=[1,2,3,4,5,6,7,8,9]
y=[1,3,5,7,8,9,3,5,2]
z=[2,3,4,5,6,7,9,9,0]
plt.plot(x, y)
plt.plot(x, z)
plt.title('testing')
plt.xlabel('Nilai X')
plt.ylabel('Nilai Y/Z')
plt.grid(True)
plt.legend(['Garis XY','garis XZ'])
plt.show()