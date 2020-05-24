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
        cwd = os.getcwd()
        config_filename = cwd+'/Config/config.json'
        config = json.loads(fm.Read(config_filename))
        
        # Read CSVs into Dataframe
        csv_file = cwd + '/'+config["datapath"] + config["international deaths"]
        self.globalDeaths = pd.read_csv(csv_file)
        csv_file = cwd + '/'+config["datapath"] + config["us deaths"]
        self.usDeaths = pd.read_csv(csv_file)
        csv_file = cwd + '/'+config["datapath"] + config["international cases"]
        self.globalCases = pd.read_csv(csv_file)
        csv_file = cwd + '/'+config["datapath"] + config["us cases"]
        self.usCases = pd.read_csv(csv_file)

        # Set date subset - todo: make this dynamic and also set updaily refreshes
        self.startDate = "2/28/20"
        self.endDate = self.usCases.columns[-1]

    def getCountryList(self):
        df = self.globalDeaths
        return pd.Series(df['Country/Region'].unique()).to_json()

    def getStateList(self):
        df = self.usDeaths
        return pd.Series(df['Province_State'].unique()).to_json()
        
    def getData(self,country,state,datatype):
        
        if(('US' in country) & (datatype == "deaths")):
            data = self.getDeathsUS(state)
        if(('US' in country) & (datatype == "cases")):
            data = self.getCasesUS(state)
        if(('US' not in country) & (datatype == "deaths")):
            data = self.getDeathsGlobal(country)
        if(('US' not in country) & (datatype == "cases")):
            data = self.getCasesGlobal(country)

        # 7 day delta average (should add this to the class)
        deltaData = data.copy()
        deltaData[0] = 0
        for i in range(1,data.size):
            deltaData[i] = data[i] - data[i-1]
        delta7d = deltaData.copy()
        for i in range(7,data.size):
            total = 0
            for j in range(0,6):
                total += deltaData[i-j]
            delta7d[i] = total / 7
 
        return delta7d.to_json(orient='split')
        # the split orientation makes a fairly complicated json, but this
        # was what I got to work - complicated to manage objects/arrays
        # that pass over json. can probably find something
        # simpler later

    def getDeathsUS(self,state):
        return self.usDeaths.loc[(self.usDeaths['Province_State'] == state),self.startDate:self.endDate].sum(axis=0)

    def getCasesUS(self,state):
        return self.usCases.loc[(self.usDeaths['Province_State'] == state),self.startDate:self.endDate].sum(axis=0)
        
    def getDeathsGlobal(self,country):
        return self.globalDeaths.loc[(self.globalDeaths['Country/Region'] == country),self.startDate:self.endDate].sum(axis=0)
        
    def getCasesGlobal(self,country):
        return self.globalCases.loc[(self.globalCases['Country/Region'] == country),self.startDate:self.endDate].sum(axis=0)

## Notes
# NLDeaths is a series. This is a column of the dataframe
# NLDeaths.size is the length
# NLDeaths.index[x] is each index
# NLDeaths[x] is the value
# or NLDeaths[indexname]
# Iterate:  for items in NLDeaths.iteritems(): print(items)
# or items[0] for index and items[1] for value
