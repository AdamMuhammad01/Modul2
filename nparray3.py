# numpy = array, dimensi, shape
# pandas = dataframe

import pandas as pd
import numpy as np

# series
# x = [8,5,7,8]
# y = pd.Series(np.array(x), index = ['a', 'b' , 'c', 'd'])
# print(y)
# type(y)


#dataframe
x =  [2,4,6,8,10]

df = pd.DataFrame(x, columns=['Nilai'])
print(df.shape)
print(df)



# x =  [2,4,6,8,10]
# y = [1,3,5,7,9]
# df = pd.DataFrame([x,y])
# baris, kolom = df.shape
# print(kolom)
# print(df)


# x = [[1,2], [3,4], [5,6], [7,8]]
# df = pd.DataFrame(x)
# print(df)



# x =  [2,4,6,8,10]
# y = [1,3,5,7,9]
# z = map(lambda a, b: [a, b], x, y)
# z = list(z)
# df = pd.DataFrame(z)
# baris, kolom = df.shape
# print(kolom)
# print(df)
# print(df[0])

# df.pd.DataFrame()




# x =  [2,4,6,8,10]
# y = [1,3,5,7,9]
# z = list('david')
# df = pd.DataFrame([x,y,z])
# print(df)

# x =  [2,4,6,8,10]
# y = [1,3,5,7,9]
# z = 'david'
# df = pd.DataFrame()
# df['X'] = x
# df['Y'] = y
# df['Z'] = z
# print(df)



# data = [
#     ['Andi', 'Jakarta', 'PNS'],
#     ['Budi', 'Palembang', 'Karyawan Swasta'],
#     ['Caca', 'Malang', 'HouseWives']
# ]

# dfData = pd.DataFrame(
#     data,
#     index = list('abc'),
#     columns = ['Nama', 'Kota', 'Pekerjaan']
# )
# print(dfData)
