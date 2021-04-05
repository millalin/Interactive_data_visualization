import os
import pandas as pd
import plotly.graph_objects as go


data = pd.read_csv("co2_emission.csv")
data.columns = ['country', 'code', 'year', 'emission']


continent_data = pd.read_csv("continent.csv")
continent_data.columns = ['continent', 'cc', 'country_name', 'two', 'code', 'num']
#continent_data.drop('co', inplace = True, axis=1)
continent_data.drop('two', inplace = True, axis=1)
continent_data.drop('num', inplace = True, axis=1)
#continent_data.drop('co', inplace = True, axis=1)

data_with_continent_info = pd.merge(data, continent_data, on= ['code'], how='left')
data_with_continent_info.to_csv('data_with_continent_info.csv', index = True)

print(data.head())
#data['year']= data['year'].apply(str)

data_clean = data[data.country != 'Statistical differences']
data_clean = data_clean[data_clean.country != 'World']
data_clean = data_clean[data_clean.year >1950]
data_clean.to_csv('data_clean.csv', index = True)

print(data.head())

df = data.set_index(['country', 'year']).emission.unstack()


data2 = data
data2 = data2[data2.country != 'EU-28']
data2 = data2[data2.country != 'Asia and Pacific (other)']
data2 = data2[data2.country != 'Europe (other)']
data2 = data2[data2.country != 'Americas (other)']
data2 = data2[data2.country != 'Africa']
data2 = data2[data2.country != 'International transport']
data2 = data2[data2.country != 'Middle East']
data2 = data2[data2.country != 'Antarctic Fisheries']
data2 = data2[data2.country != 'World']
data2 = data2[data2.country != 'Kyrgysztan']
data2 = data2[data2.country != 'Statistical differences']


df2 = data2.set_index(['code', 'year']).emission.unstack()
df2.drop(df.iloc[:, 0:149], inplace = True, axis = 1)
df2 = df2.fillna(0)



# drop 149 first years
df.drop(df.iloc[:, 0:149], inplace = True, axis = 1)
df.drop('World',inplace = True, axis=0)

df = df.fillna(0)
#df = df.astype(int, errors='ignore')
without_continent = df


print(df.head(10))

country_code = data2
country_code.drop('year', inplace = True, axis=1)
country_code.drop('emission', inplace = True, axis=1)
country_code.drop_duplicates(subset ="country",
                     keep = 'first', inplace = True)
print(country_code.head())

clean_with_continent = pd.merge(df2, continent_data, on= ['code'], how='left')
clean_with_continent = pd.merge(clean_with_continent, country_code, on= ['code'], how='left')

df.to_csv('clean.csv', index = True)
clean_with_continent.to_csv('clean_with_continent.csv', index = True)


without_continent.drop('EU-28',inplace = True, axis=0)
print(without_continent.head())
without_continent.drop('Asia and Pacific (other)',inplace = True, axis=0)
without_continent.drop('Europe (other)',inplace = True, axis=0)
without_continent.drop('Americas (other)',inplace = True, axis=0)
without_continent.drop('Africa',inplace = True, axis=0)
without_continent.drop('International transport',inplace = True, axis=0)
without_continent.drop('Middle East',inplace = True, axis=0)
without_continent.drop('Statistical differences',inplace = True, axis=0)

without_continent.to_csv('only_countries.csv', index = True) 


world = pd.read_csv("co2_emission.csv", delimiter = ",")
world.columns = ['country', 'code', 'year', 'emission']

world = world.loc[world['country'] == 'World']
world = world.astype(int, errors='ignore')
#world.drop(world.iloc[0:149, :], inplace = True, axis = 0)

world.to_csv('world.csv', index = True)


world = world.set_index(['country', 'year']).emission.unstack()
world.drop(world.iloc[:, 0:149], inplace = True, axis = 1)

world.to_csv('world2.csv', index = True)
