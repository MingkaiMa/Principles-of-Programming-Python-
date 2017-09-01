from collections import defaultdict
import sys
import os

targeted_first_name = input('Enter a first name: ')
##targeted_male_first_name = input('Enter a male first name: ')
directory = 'names'

if not os.path.exists(directory):
    print(f'There is no directory named {directory}, giving up...')
    sys.exit()


Mname_total_number = {}
Fname_total_number = {}
total_male = 0
total_female = 0

max_male_f = 0
max_male_name = ''
max_female_f = 0
max_female_name = ''
male_name_in_year = defaultdict(list)
female_name_in_year = defaultdict(list)

for filename in os.listdir(directory):
    if not filename.endswith('.txt'):
        continue
    year = int(filename[3:7])
    with open(directory + '/' + filename) as file:
        for line in file:
            name, gender, count = line.split(',')
            if gender == 'M':
                total_male = total_male + int(count)
            if gender == 'F':
                total_female = total_female + int(count)
    Mname_total_number[year] = total_male
    Fname_total_number[year] = total_female
    total_male = 0
    total_female = 0



for filename in os.listdir(directory):
    if not filename.endswith('.txt'):
        continue
    year = int(filename[3:7])
    with open(directory + '/' + filename) as file:
        for line in file:
            name,gender,count = line.split(',')
            if gender == 'F' and name == targeted_first_name:
                female_name_in_year[name].append([year,int(count)/Fname_total_number[year]])

            if gender == 'M' and name == targeted_first_name:
                male_name_in_year[name].append([year, int(count)/Mname_total_number[year]])
                       

malelist = sorted(male_name_in_year[targeted_first_name], key = lambda x:x[1], reverse = True)
femalelist = sorted(female_name_in_year[targeted_first_name], key = lambda x:x[1], reverse = True)

if len(femalelist) == 0:
    print(f'In all years, {targeted_first_name} was never given as a female name.')
else:
    print(f'In terms of frequency, {targeted_first_name} was the most popular as a female name first in the year {femalelist[0][0]}.\
            It then accounted for {round(femalelist[0][1]*100,2)}% of all female names')

if len(malelist) == 0:
    print(f'In all years, {targeted_first_name} was never given as a male name.')
else:
    print(f'In terms of frequency, {targeted_first_name} was the most popular as a male name first in the year {malelist[0][0]}.\
             It then accounted for {round(malelist[0][1]*100,2):.2f}% of all male names')



##print(male_name_in_year['Zed'])
##    int(count)/Mname_total_number[year]
##
##
##               male_name_in_year[year].append([name,int(count)/Mname_total_number[year]])
##        
##

##
##for filename in os.listdir(directory):
##    if not filename.endswith('.txt'):
##        continue
##    year = int(filename[3:7])
##    with open(directory + '/' + filename) as file:
##        for line in file:
##            name,gender,count = line.split(',')
##            if gender == 'F':
##                a = int(count)/Fname_total_number[year]
##                if a > max_female_f:
##                    max_female_f = a
##                    max_female_name = name
##            if gender == 'M':
##                b = int(count)/Mname_total_number[year]
##                if b > max_male_f:
##                    max_male_f = b
##                    max_male_name = name
##                    
##    most_popular_female_name_in_year[year].append([max_female_name, max_female_f])
##    most_popular_male_name_in_year[year].append([max_male_name, max_male_f])
## 
    
