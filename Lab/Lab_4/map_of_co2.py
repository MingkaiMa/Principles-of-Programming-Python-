import pygal

import csv
from collections import defaultdict
import pandas


import pygal.maps.world

worldmap_chart = pygal.maps.world.World()

a = pygal.maps.world.COUNTRIES
a['ly'] = 'Libya'
a['kg'] = 'Kyrgyz Republic'
country_list = []
for i in a:
    country_list.append(a[i].split(',')[0])



with open('API_EN.ATM.CO2E.KT_DS2_en_csv_v2.csv') as f:
    reader = csv.reader(f)
    rows = [row for row in reader]

R = rows
dic = {}

for i in range(5,253):
    if R[i][0].split(',')[0] in country_list:
        dic[R[i][0].split(',')[0]] = R[i][55]
    else:
        print(f'Leaving out {R[i][0]}')
       
known_data_country_list = []

for i in dic:
    known_data_country_list.append(i)


dic_country_code_with_no_data = {}
dic_country_code_with_data = {}

for i in a:
    if a[i].split(',')[0] in known_data_country_list:
        if len(dic[a[i].split(',')[0]]) != 0:
            dic_country_code_with_data[i] = float(dic[a[i].split(',')[0]])
        else:
            dic_country_code_with_no_data[i] = '?'
            
        
import pygal.maps.world
from pygal.style import Style
custom_style = Style(
    colors = ('#B22222', '#A9A9A9')

    )
custom_style.legend_font_size = 10
custom_style.tooltip_font_size = 8
worldmap_chart = pygal.maps.world.World(style = custom_style)
worldmap_chart.title = 'CO2 emissions in 2011'

worldmap_chart.add('Known data', dic_country_code_with_data)
worldmap_chart.add('No data', dic_country_code_with_no_data)
worldmap_chart.render_to_file('CO2_emissions.svg')

