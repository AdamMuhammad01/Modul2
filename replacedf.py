import pandas as pd
import numpy as np


df = pd.read_csv('data1.csv')
# df = df.replace(['-','#'],np.NaN)
# df = df.fillna('XXX')
# df = df.replace({
# '-':'+',
# '#':np.NaN
# })

# df = df.replace({
#     'usia' :['-','#'],
#     'nama':'#'
# },np.NaN)
# df = df.replace({
#     'usia' :['-','#'],
#     'nama':'#'
# },{
#     'usia':np.NaN,
#     'nama':'Anonim'
# })
# df = df.replace(0, 'XXX')
df['usia']=df['usia'].replace(
    to_replace = '-',
    method = 'ffill'
)
print(df)