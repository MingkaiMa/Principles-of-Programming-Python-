import csv
from collections import defaultdict
import sys
import os
filename = 'HNP_Data.csv'
if not os.path.exists(filename):
    print(f'There is no file named {filename} in the working directory, giving up...')
    sys.exit()

Indicator_Name = input('Enter an Indicator Name: ')

country_year_dic = defaultdict(list)

with open(filename) as file:
    reader = csv.reader(file)
    for row in reader:
        if row[2] == Indicator_Name:
            L = [float(i) if len(i)!=0 else 0 for i in row[4:]]
            country_year_dic[Indicator_Name].append([row[0],max(L),[(i+1960) for i,j in enumerate(L) if j == max(L)]])


result_list = sorted(country_year_dic[Indicator_Name], key = lambda x:x[1], reverse = True)

if len(result_list) == 0:
    print('Sorry, either the indicator of interest does not exist or it has no data.')
    sys.exit()
    

max_value = result_list[0][1]
value_by_year = defaultdict(list)

max_value_1 = str(max_value).strip('.0')


for i in range(0,len(result_list)):
    if result_list[i][1] == max_value:
        for k in result_list[i][2]:
            value_by_year[k].append(result_list[i][0])
    else:
        break


print('The maximum value is: ',max_value_1)
for i in value_by_year:
    print(i,': ',value_by_year[i])



                



