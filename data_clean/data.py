import os
import pandas as pd
import plotly.graph_objects as go


data = pd.read_csv("co2_emission.csv")
data.columns = ['country', 'code', 'year', 'emission']

#data['year']= data['year'].apply(str)

data_clean = data[data.country != 'Statistical differences']
data_clean = data_clean[data_clean.country != 'World']
data_clean = data_clean[data_clean.year >1950]
data_clean.to_csv('data_clean.csv', index = True)

print(data.head())

df = data.set_index(['country', 'year']).emission.unstack()

# drop 149 first years
df.drop(df.iloc[:, 0:149], inplace = True, axis = 1)
df.drop('World',inplace = True, axis=0)
df = df.fillna(0)
#df = df.astype(int, errors='ignore')

print(df.head(10))

df.to_csv('clean.csv', index = True)

world = pd.read_csv("co2_emission.csv", delimiter = ",")
world.columns = ['country', 'code', 'year', 'emission']

world = world.loc[world['country'] == 'World']
world = world.astype(int, errors='ignore')
#world.drop(world.iloc[0:149, :], inplace = True, axis = 0)

world.to_csv('world.csv', index = True)


world = world.set_index(['country', 'year']).emission.unstack()
world.drop(world.iloc[:, 0:149], inplace = True, axis = 1)

world.to_csv('world2.csv', index = True)
