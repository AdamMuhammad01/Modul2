# import numpy as np
# import pandas as pd


# df = pd.read_excel('bps.xlsx', skiprows = 1 , skipfooter = 1)
# print(df)




import pymongo
myclient = pymongo.MongoClient("mongodb://localhost:27017")
mydb = myclient["py_mongo"]
mycol = mydb['kampus']
print(myclient.list_database_names())
# print(mydb.list_collection_names())

print(list(mycol.find()))


for x in mycol.find():
    print(x)
