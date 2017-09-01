import csv
from collections import defaultdict
import matplotlib.pyplot as plt
from math import floor, ceil
from calendar import month_name

collection = defaultdict(list)
with open('IDCJCM0037_066062.csv') as f:
    reader = csv.reader(f)
    for row in reader:
        if len(row)!= 0:
            if row[0] == 'Mean maximum temperature (Degrees C) for years 1859 to 2016 ':
                for i in range(1,len(row) - 4):
                    collection['max'].append(float(row[i]))
            if row[0] == 'Mean minimum temperature (Degrees C) for years 1859 to 2016 ':
                for i in range(1,len(row) - 4):
                    collection['min'].append(float(row[i]))


min_temperature = floor(min(collection['min']))
max_temperature = ceil(max(collection['max']))

min_dec_jan = (collection['min'][0] + collection['min'][-1]) / 2
max_dec_jan = (collection['max'][0] + collection['max'][-1]) / 2

collection['min'] = [min_dec_jan] + collection['min'] + [min_dec_jan]
collection['max'] = [max_dec_jan] + collection['max'] + [max_dec_jan]

temperatures = plt.figure(dpi = 220, figsize = (5, 3.5))
plt.axis([0.5, 12.5, min_temperature - 1, max_temperature + 1])
plt.xticks(range(1, 13), [month_name[i] for i in range(1, 13)], fontsize = 8)
plt.yticks([i / 2 for i in range(min_temperature * 2, max_temperature * 2 + 1)], fontsize = 4)
xrange = [0.5] + list(range(1, 13)) + [12.5]
plt.plot(xrange, collection['max'], c = 'red')
plt.plot(xrange, collection['min'], c = 'blue')
plt.fill_between(xrange, collection['max'],collection['min'], facecolor = 'gray', alpha = 0.1)
plt.title('Mean min and max temperatures in Sydney', fontsize = 10)
plt.grid(True)
temperatures.autofmt_xdate()
plt.show()
##plt.figure(figsize=(5,3.5))
##plt.plot(collection['max'],color='red')
##plt.plot(collection['min'],color='blue')
##plt.title('Mean min and max temperatures in Sydney')
####plt.axis(['January','December'])
##plt.grid(True)
##
##x_value = ['January','February','March','April','May','June','July','August','September','October','November','December']
##x_axis = range(1,13,1)
##plt.xticks(x_axis,x_value)
##
##plt.yticks(range(8,26,1))
###plt.fill_between(x,y, facecolor = 'gray',transparency= True)
##plt.show()
