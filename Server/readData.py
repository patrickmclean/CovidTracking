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

    def getStateList(self):
        df = self.usFrame
        return pd.Series(df['Province_State'].unique()).to_json()
        
    def getDeaths(self,country,state):
        df = self.globalFrame

        if('US' in country):
            deaths = self.getDeathsUS(country,state)
        else:
            deaths = df.loc[(df['Country/Region'] == country),self.startDate:self.endDate].sum(axis=0)
        
        # 7 day delta average (should add this to the class)
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

    def getDeathsUS(self,country,state):
        df = self.usFrame
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
