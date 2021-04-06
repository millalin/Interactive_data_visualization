import os
import pandas as pd
import plotly.graph_objects as go



big_data = pd.read_csv("co2_emissions_to2019.csv")
big_data.drop('co2_growth_prct', inplace = True, axis=1)
big_data.drop('co2_growth_abs', inplace = True, axis=1)
big_data.drop('consumption_co2', inplace = True, axis=1)
big_data.drop('trade_co2', inplace = True, axis=1)
big_data.drop('trade_co2_share', inplace = True, axis=1)
big_data.drop('consumption_co2_per_capita', inplace = True, axis=1)
big_data.drop('share_global_co2', inplace = True, axis=1)
big_data.drop('share_global_cumulative_co2', inplace = True, axis=1)
big_data.drop('co2_per_gdp', inplace = True, axis=1)
big_data.drop('consumption_co2_per_gdp', inplace = True, axis=1)
big_data.drop('co2_per_unit_energy', inplace = True, axis=1)
big_data.drop('cement_co2', inplace = True, axis=1)
big_data.drop('coal_co2', inplace = True, axis=1)
big_data.drop('flaring_co2', inplace = True, axis=1)
big_data.drop('gas_co2', inplace = True, axis=1)
big_data.drop('oil_co2', inplace = True, axis=1)
big_data.drop('other_industry_co2', inplace = True, axis=1)
big_data.drop('cement_co2_per_capita', inplace = True, axis=1)
big_data.drop('coal_co2_per_capita', inplace = True, axis=1)
big_data.drop('flaring_co2_per_capita', inplace = True, axis=1)
big_data.drop('gas_co2_per_capita', inplace = True, axis=1)
big_data.drop('oil_co2_per_capita', inplace = True, axis=1)
big_data.drop('other_co2_per_capita', inplace = True, axis=1)
big_data.drop('share_global_coal_co2', inplace = True, axis=1)
big_data.drop('share_global_oil_co2', inplace = True, axis=1)
big_data.drop('share_global_gas_co2', inplace = True, axis=1)
big_data.drop('share_global_flaring_co2', inplace = True, axis=1)
big_data.drop('share_global_cement_co2', inplace = True, axis=1)
big_data.drop('cumulative_coal_co2', inplace = True, axis=1)
big_data.drop('cumulative_oil_co2', inplace = True, axis=1)
big_data.drop('cumulative_gas_co2', inplace = True, axis=1)
big_data.drop('cumulative_flaring_co2', inplace = True, axis=1)
big_data.drop('cumulative_cement_co2', inplace = True, axis=1)
big_data.drop('share_global_cumulative_coal_co2', inplace = True, axis=1)
big_data.drop('share_global_cumulative_oil_co2', inplace = True, axis=1)
big_data.drop('share_global_cumulative_gas_co2', inplace = True, axis=1)
big_data.drop('share_global_cumulative_flaring_co2', inplace = True, axis=1)
big_data.drop('share_global_cumulative_cement_co2', inplace = True, axis=1)
big_data.drop('methane', inplace = True, axis=1)
big_data.drop('methane_per_capita', inplace = True, axis=1)
big_data.drop('nitrous_oxide', inplace = True, axis=1)
big_data.drop('nitrous_oxide_per_capita', inplace = True, axis=1)
big_data.drop('primary_energy_consumption', inplace = True, axis=1)
big_data.drop('energy_per_capita', inplace = True, axis=1)
big_data.drop('energy_per_gdp', inplace = True, axis=1)
big_data.drop('total_ghg', inplace = True, axis=1)
big_data.drop('ghg_per_capita', inplace = True, axis=1)

big_data = big_data.fillna(0)

print(big_data.head())

big_data.columns = ['code', 'country', 'year', 'emission', 'per_capita', 'cumulative', 'pop', 'gdp']

big_data.to_csv('big_data.csv', index = True)

#data = pd.read_csv("co2_emission.csv")
#data.columns = ['country', 'code', 'year', 'emission']

# If testing using bigger data
data = big_data


continent_data = pd.read_csv("continent.csv")
continent_data.columns = ['continent', 'cc', 'country_name', 'two', 'code', 'num']
continent_data.drop('two', inplace = True, axis=1)
continent_data.drop('num', inplace = True, axis=1)

data_with_continent_info = pd.merge(data, continent_data, on= ['code'], how='left')
data_with_continent_info.to_csv('data_with_continent_info.csv', index = True)


data_clean = data[data.country != 'Statistical differences']
data_clean = data_clean[data_clean.country != 'World']
data_clean = data_clean[data_clean.year >1950]
data_clean.to_csv('data_clean.csv', index = True)


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
data2 = data2[data2.country != 'Asia']
data2 = data2[data2.country != 'Asia (excl. China & India)']
data2 = data2[data2.country != 'EU-27']
data2 = data2[data2.country != 'Europe']
data2 = data2[data2.country != 'Europe (excl. EU-27)']
data2 = data2[data2.country != 'Europe (excl. EU-28)']
data2 = data2[data2.country != 'Macao']
data2 = data2[data2.country != 'Micronesia']
data2 = data2[data2.country != 'North America']
data2 = data2[data2.country != 'North America (excl. USA)']
data2 = data2[data2.country != 'Oceania']
data2 = data2[data2.country != 'Panama Canal Zone']
data2 = data2[data2.country != 'South America']
data2 = data2[data2.country != 'St. Kitts-Nevis-Anguilla']
data2 = data2[data2.country != 'French Equatorial Africa']
data2 = data2[data2.country != 'French West Africa']
data2 = data2[data2.country != 'Kuwaiti Oil Fires']
data2 = data2[data2.country != 'Kosovo']
data2 = data2[data2.country != 'Leeward Islands']



data2.to_csv("testest.csv", index = True)

# Bigger data to remove
# Asia, Asia (excl. China & India), EU-27, EU-28, Europe, Europe (excl. EU-27), Europe (excl. EU-28), 
# Macao, Micronesia, North America, North America (excl. USA), Oceania, Panama Canal Zone, South America, St. Kitts-Nevis-Anguilla


df2 = data2.set_index(['code', 'year']).emission.unstack()
#df2.drop(df.iloc[:, 0:149], inplace = True, axis = 1)

df2.drop(df.iloc[:, 0:69], inplace = True, axis = 1)
df2 = df2.fillna(0)



# drop 149 first years
df.drop(df.iloc[:, 0:149], inplace = True, axis = 1)
df.drop('World',inplace = True, axis=0)

df = df.fillna(0)
without_continent = df



country_code = data2
country_code.drop('year', inplace = True, axis=1)
country_code.drop('emission', inplace = True, axis=1)
country_code.drop_duplicates(subset ="country",
                     keep = 'first', inplace = True)

clean_with_continent = pd.merge(df2, continent_data, on= ['code'], how='left')
clean_with_continent = pd.merge(clean_with_continent, country_code, on= ['code'], how='left')

df.to_csv('clean.csv', index = True)
clean_with_continent.to_csv('clean_with_continent.csv', index = True)


# used with smaller data 
#without_continent.drop('EU-28',inplace = True, axis=0)
#without_continent.drop('Asia and Pacific (other)',inplace = True, axis=0)
#without_continent.drop('Europe (other)',inplace = True, axis=0)
#without_continent.drop('Americas (other)',inplace = True, axis=0)
#without_continent.drop('Africa',inplace = True, axis=0)
#without_continent.drop('International transport',inplace = True, axis=0)
#without_continent.drop('Middle East',inplace = True, axis=0)
#without_continent.drop('Statistical differences',inplace = True, axis=0)

#without_continent.to_csv('only_countries.csv', index = True) 


world = pd.read_csv("co2_emission.csv", delimiter = ",")
world.columns = ['country', 'code', 'year', 'emission']

world = world.loc[world['country'] == 'World']
world = world.astype(int, errors='ignore')

world.to_csv('world.csv', index = True)


world = world.set_index(['country', 'year']).emission.unstack()
world.drop(world.iloc[:, 0:149], inplace = True, axis = 1)

world.to_csv('world2.csv', index = True)
