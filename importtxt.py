import numpy as np  

id, usia =np.loadtxt('0.csv', skiprows=1, delimiter=',', unpack=True)
print(id)
print(usia)
data1 = np.array(list(map(lambda a,b:[a,b],id,usia)))
print(data1)
np.savetxt('1.csv',data1,fmt='%d', header='id,usia', comments='', delimiter=',')


# id, usia =np.loadtxt('0.csv', skiprows=1, delimiter=',', unpack=True)
# print(id)
# print(usia)

# np.savetxt('1.csv',usia,fmt='%d', header='usia', comments='')