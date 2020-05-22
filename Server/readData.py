# Server code for reading covid files

# Read file into data frame

# Host web service calls

# Input: Country, Date Range. Output: Deaths

# system imports
import os
import json
import pandas as pd 

#local imports
import FileManager as fm



class DataReader:
    def __init__(self):

        # Read the config file
        # Future - turn this into a service - get key/value pair
        cwd = os.getcwd()
        config_filename = cwd+'/Config/config.json'
        config = json.loads(fm.Read(config_filename))
        # Read CSV into Dataframe
        csv_file = cwd + '/'+config["datapath"] + config["international deaths"]
        self.globalFrame = pd.read_csv(csv_file)
        csv_file = cwd + '/'+config["datapath"] + config["us deaths"]
        self.usFrame = pd.read_csv(csv_file)

        # Set date subset - todo: make this dynamic and also set updaily refreshes
        self.startDate = "2/28/20"
        self.endDate = "5/19/20"

    def getCountryList(self):
        df = self.globalFrame
        return pd.Series(df['Country/Region'].unique()).to_json()
    
    def getCountryRow(self,country):
        df = self.globalFrame
        return df[(df['Country/Region'] == country) & (df['Province/State'].isnull())].index[0]
        # separating this out is a way to get the array to format well.
        # no doubt could be done better
        # Todo: error handling. If the country name is misformated (capitals)
        # or doesn't exist, this will fail. Need a graceful method.

        
    def getDeaths(self,country):
        df = self.globalFrame

        if('US' in country):
            deaths = self.getDeathsUS(country)
        else:
            deaths = df.loc[self.getCountryRow(country),self.startDate:self.endDate]
        
        deltaDeaths = deaths.copy()
        deltaDeaths[0] = 0
        for i in range(1,deaths.size):
            deltaDeaths[i] = deaths[i] - deaths[i-1]
        delta7d = deltaDeaths.copy()
        for i in range(7,deaths.size):
            total = 0
            for j in range(0,6):
                total += deltaDeaths[i-j]
            delta7d[i] = total / 7
 
        return delta7d.to_json(orient='split')
        # the split orientation makes a fairly complicated json, but this
        # was what I got to work - complicated to manage objects/arrays
        # that pass over json. can probably find something
        # simpler later

    def getDeathsUS(self,country):
        df = self.usFrame
        state = country.replace('USA - ','') # strict for now, to improve later 
        sf = df.loc[(df['Province_State'] == state),self.startDate:self.endDate]
        return sf.sum(axis=0)
        
        
## Notes
# NLDeaths is a series. This is a column of the dataframe
# NLDeaths.size is the length
# NLDeaths.index[x] is each index
# NLDeaths[x] is the value
# or NLDeaths[indexname]
# Iterate:  for items in NLDeaths.iteritems(): print(items)
# or items[0] for index and items[1] for value
