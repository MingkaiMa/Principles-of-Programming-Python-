# Uses National Data on the relative frequency of given names in the population of U.S. births,
# stored in a directory "names", in files named "yobxxxx.txt with xxxx (the year of birth)
# ranging from 1880 to2013.
# Prompts the user for a female first name, and finds out the years when this name was most popular
# in terms of ranking. Displays the ranking, and the years in decreasing order of frequency.

from collections import defaultdict
import sys
import os

targeted_first_name = input('Enter a female first name: ')
rank = float('inf')
directory = 'names'

best_years = []
total_number = 0
year_number = 0
Fname_total_number_in_a_year = {}
current_rank = float('inf')
name_in_year = defaultdict(list)



for filename in os.listdir(directory):
    if not filename.endswith('.txt'):
        continue
    year = int(filename[3:7])
    with open(directory + '/' + filename) as file:
        for(num, value) in enumerate(file):
            name,gender,count = value.split(',')
            if gender == 'F':
                total_number = total_number + int(count)
    Fname_total_number_in_a_year[year] = total_number
    total_number = 0

for filename in os.listdir(directory):
    if not filename.endswith('.txt'):
        continue
    year = int(filename[3: 7])
    with open(directory + '/' + filename) as file:
        for(num, value) in enumerate(file):
            name,gender,count = value.split(',')
            if gender == 'F' and name == targeted_first_name:
                if num <= rank:
                    rank = num
                    name_in_year[rank].append([year,int(count)/Fname_total_number_in_a_year[year]])

most_popular_year = []

if len(name_in_year) == 0:
    best_years = []
else:
    rank = min(name_in_year)+1
    most_popular_year = name_in_year[min(name_in_year)]
    sort_most_popular_year = sorted(most_popular_year, key = lambda x:x[1], reverse = True)
    for i in range(0,len(sort_most_popular_year)):
        best_years.append(sort_most_popular_year[i][0])

            
        

if not best_years:
    print('{} is not a female first name in my records.'.format(targeted_first_name))
else:
    print('By decreasing order of frequency, {} was most popular in the years: '.format(targeted_first_name), end = '')
    for year in best_years:
        print(year, end = ' ')
    print('\nIts rank was {} then.'.format(rank))


