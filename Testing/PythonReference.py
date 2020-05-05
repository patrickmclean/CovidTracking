# -*- coding: utf-8 -*-
"""
Created on Sun Jul 24 18:16:37 2016

@author: patrickmclean

This is my Python documentation
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from datetime import datetime
import os


# Start with the basics, some printing commands
myInt = 12
myString = "Hello"
myFloat = 1.2
myDate = datetime(2001, 2, 3, 4, 5)

print ("This is an int {:d}, a float {:.2f} a string: {} and a date {:%Y-%m-%d %H:%M}".format(myInt,myFloat,myString,myDate) )
# Details https://pyformat.info/

# A couple of loops
for i in range(0,5):
    print (i)
    
# Lists, Sets, Dictionaries
# Use a dictionary when you have a set of unique keys that map to values. Dict is {}
residents = {'Puffin' : 104, 'Sloth' : 105, 'Burmese Python' : 106}
print (residents['Puffin']) # Prints Puffin's room number
residents['Maynard'] = 108
print ("Number of residents {:d}".format(len(residents)))

# Use a list if you have an ordered collection of items. List is []
zoo_animals = ["pangolin", "cassowary", "sloth", "tiger"]
zoo_animals.append("crocodile")
print ("Length of list {:d} item in list {}".format(len(zoo_animals),zoo_animals[2]))
print ("First,middle and last 3 {} / {} / {}".format(zoo_animals[:3],zoo_animals[1:3],zoo_animals[1:]))

#Indices
animals = ["aardvark", "badger", "duck", "emu", "fennec fox"]
duck_index = animals.index("duck")
animals.insert(duck_index,"cobra")
print (animals) # Observe what prints after the insert operation
    
# Looping a list
myList = ['Apples','Bananas','Pears']
for i in myList:
    print (i)

#Dictionaries that include lists
inventory = {
    'gold' : 500,
    'pouch' : ['flint', 'twine', 'gemstone'], # Assigned a new list to 'pouch' key
    'backpack' : ['xylophone','dagger', 'bedroll','bread loaf']
}

# Adding a key 'burlap bag' and assigning a list to it
inventory['burlap bag'] = ['apple', 'small ruby', 'three-toed sloth']
inventory['pocket'] = ['seashell','strange berry','lint']

# Sorting the list found under the key 'pouch'
inventory['pouch'].sort() 
inventory['backpack'].sort()
inventory['backpack'].remove('dagger')
inventory['gold'] = 550
print (inventory)

# Use a set to store an unordered set of items.


# Onto the fun part - Dataframes
# Good details here: http://chrisalbon.com/python/pandas_indexing_selecting.html
print ('local path: '+os.getcwd())
myDataFrame = pd.read_csv("./Testing/city-of-chicago-salaries.csv")
myDataFrame.head(10)
myDataFrame.info()
myDataFrame.describe()


# Create an example dataframe about a fictional army
raw_data = {'regiment': ['Nighthawks', 'Nighthawks', 'Nighthawks', 'Nighthawks', 'Dragoons', 'Dragoons', 'Dragoons', 'Dragoons', 'Scouts', 'Scouts', 'Scouts', 'Scouts'],
            'company': ['1st', '1st', '2nd', '2nd', '1st', '1st', '2nd', '2nd','1st', '1st', '2nd', '2nd'],
            'deaths': [523, 52, 25, 616, 43, 234, 523, 62, 62, 73, 37, 35],
            'battles': [5, 42, 2, 2, 4, 7, 8, 3, 4, 7, 8, 9],
            'size': [1045, 957, 1099, 1400, 1592, 1006, 987, 849, 973, 1005, 1099, 1523],
            'veterans': [1, 5, 62, 26, 73, 37, 949, 48, 48, 435, 63, 345],
            'readiness': [1, 2, 3, 3, 2, 1, 2, 3, 2, 1, 2, 3],
            'armored': [1, 0, 1, 1, 0, 1, 0, 1, 0, 0, 1, 1],
            'deserters': [4, 24, 31, 2, 3, 4, 24, 31, 2, 3, 2, 3],
            'origin': ['Arizona', 'California', 'Texas', 'Florida', 'Maine', 'Iowa', 'Alaska', 'Washington', 'Oregon', 'Wyoming', 'Louisana', 'Georgia']}
df = pd.DataFrame(raw_data, columns = ['regiment', 'company', 'deaths', 'battles', 'size', 'veterans', 'readiness', 'armored', 'deserters', 'origin'])
df = df.set_index('origin')
df.head()

# Select one or more column - single [] for one, double [[]] for multiple
df[['size', 'veterans']]

# Select one or more rows
df.loc[:'Arizona']
# Select every row up to 3
df.iloc[:2]
# Select the second and third row
df.iloc[1:2]
# Select every row after the third row
df.iloc[2:]
# Select the first 2 columns
df.iloc[:,:2]
# Select rows where df.deaths is greater than 50
df[df['deaths'] > 50]
# Select rows where df.deaths is greater than 500 or less than 50
df[(df['deaths'] > 500) | (df['deaths'] < 50)]
# Select all the regiments not named "Dragoons"
df[~(df['regiment'] == 'Dragoons')]



# Join and merge : http://chrisalbon.com/python/pandas_join_merge_dataframe.html

# Another excellent dataframes resource: http://www.gregreda.com/2013/10/26/working-with-pandas-dataframes/

# more on basics
# New frame with just columns of another
#interactions = calls[['participantID.A', 'participantID.B']]


# Working on my csv data frames
# Need to show journey from array to series to dataframe

# First extract a series from a dataframe, and create a new series with the deltas between
startDate = "2/28/20"
endDate = "5/2/20"
df = pd.read_csv("CovidData/COVID-19/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_deaths_global.csv")
countryRow = df[(df['Country/Region'] == 'Netherlands') & (df['Province/State'].isnull())].index[0]
deaths = df.loc[countryRow,startDate:endDate]
deltaDeaths = deaths.Series.copy()
deltaDeaths[0] = 0;
for i in range(1,deaths.size):
    deltaDeaths[i] = deaths[i] - deaths[i-1]


print('placeholder')    