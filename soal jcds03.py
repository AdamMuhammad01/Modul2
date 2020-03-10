
import mysql.connector

#
# db = mysql.connector.connect(
#     host = 'localhost',
#     port = 3306,
#     user = 'root',
#     passwd = '363636',
#     auth_plugin = 'mysql_native_password',
#     database = 'mydatabase'
#     # database = 'mydatabase'
# )
# c = db.cursor()
# # sql = 'create database'
# c.execute('describe karyawan')
# print (db)
# print(c.fetchall())
# print(x)
# c.execute(sql)
# sql =

# for i in x:
#     print(i)



#
#
# '''
# import numpy as np
# import matplotlib.pyplot as plt
# from mpl_toolkits.mplot3d import axes3d
# from matplotlib import style
#
# ############################No.1#################################
# A=np.array([[1, -2, 1],[3, 1, -2],[7, -6, -1]])
# B=np.array([6,4,10])
# X2 = np.linalg.solve(A,B)
# print(X2)
#
# '''
#
# '''
#
# import numpy as np
# import matplotlib.pyplot as plt
# from mpl_toolkits.mplot3d import axes3d
# from mpl_toolkits.mplot3d.art3d import Poly3DCollection  # appropriate import to draw 3d polygons
# from matplotlib import style
#
# plt.figure('SPLTV',figsize=(10,5))
# custom=plt.subplot(121,projection='3d')
# #x-2y+z=6
# x1=np.array([1, -2, 1])
# # y1=np.array([5, 3, 7])
# z1=np.array([6])  # z1 should have 3 coordinates, right?
# custom.scatter(x1,z1)
#
# # 1. create vertices from points
# verts = [list(zip(x1,z1))]
# # 2. create 3d polygons and specify parameters
# srf = Poly3DCollection(verts, alpha=.25, facecolor='#800000')
# # 3. add polygon to the figure (current axes)
# plt.gca().add_collection3d(srf)
#
# custom.set_xlabel('X')
# # custom.set_ylabel('Y')
# custom.set_zlabel('Z')
# plt.show()
#
# '''
#
# ##################################no.2################################
#
# import numpy as np
# import matplotlib.pyplot as plt
# from mpl_toolkits.mplot3d import axes3d
# from mpl_toolkits.mplot3d.art3d import Poly3DCollection  # appropriate import to draw 3d polygons
# from matplotlib import style
#
#
# plt.figure('SPLTV',figsize=(10,5))
#
# custom1=plt.subplot(1,2,1,projection='3d')
# #x-2y+z=6
# x1=np.array([6, 0, 0])
# y1=np.array([0, -3, 0])
# z1=np.array([0, 0, 6])  # z1 should have 3 coordinates, right?
# custom1.scatter(x1,y1,z1)
# # 1. create vertices from points
# verts1 = [list(zip(x1, y1, z1))]
# # 2. create 3d polygons and specify parameters
# srf1 = Poly3DCollection(verts1, alpha=.25, facecolor='#800000')
# # 3. add polygon to the figure (current axes)
# plt.gca().add_collection3d(srf1)
#
# custom2=plt.subplot(121,projection='3d')
# x2=np.array([1.33, 0, 0])
# y2=np.array([0, 4, 0])
# z2=np.array([0, 0, -2])  # z1 should have 3 coordinates, right?
# custom2.scatter(x2,y2,z2)
# # 1. create vertices from points
# verts2 = [list(zip(x2, y2, z2))]
# # 2. create 3d polygons and specify parameters
# srf2= Poly3DCollection(verts2, alpha=.25, facecolor='#800000')
# # 3. add polygon to the figure (current axes)
# plt.gca().add_collection3d(srf2)
#
# custom3=plt.subplot(121,projection='3d')
# x3=np.array([3, 1, 2])
# y3=np.array([5, 3, 7])
# z3=np.array([0, 0, 4])  # z1 should have 3 coordinates, right?
# custom3.scatter(x3,y3,z3)
# # 1. create vertices from points
# verts3 = [list(zip(x3, y3, z3))]
# # 2. create 3d polygons and specify parameters
# srf3 = Poly3DCollection(verts3, alpha=.25, facecolor='#800000')
# # 3. add polygon to the figure (current axes)
# plt.gca().add_collection3d(srf3)
#
#
#
# custom1.set_xlabel('X');custom2.set_xlabel('X');custom3.set_xlabel('X')
# custom1.set_ylabel('Y');custom2.set_ylabel('Y');custom3.set_ylabel('Y')
# custom1.set_zlabel('Z');custom2.set_zlabel('Z');custom3.set_zlabel('Z')
# plt.show()
