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
        
        # Read Covid CSVs into Dataframe
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

        # Read Population CSVs into Dataframe
        csv_file = cwd + '/'+config["populationspath"] + config["world populations"]
        self.worldPopulations = pd.read_csv(csv_file)
        csv_file = cwd + '/'+config["populationspath"] + config["us state populations"]
        self.usStatePopulations = pd.read_csv(csv_file)

        # Read country and state favorites
        self.countryfavorites = config["favorite countries"]
        self.statefavorites = config["favorite states"]
        

    def getCountryList(self):
        df = self.globalDeaths
        countries = pd.Series(df['Country/Region'].unique())
        favorites = pd.Series(self.countryfavorites.split(','))
        new_list = pd.concat([favorites,countries],ignore_index=True)
        return new_list.to_json()

    def getStateList(self):
        df = self.usDeaths
        states = pd.Series(df['Province_State'].unique())
        favorites = pd.Series(self.statefavorites.split(','))
        new_list = pd.concat([favorites,states],ignore_index=True)
        return new_list.to_json()

        #return pd.Series(df['Province_State'].unique()).to_json()
        
    def getData(self,country,state,datatype):
        
        # Get raw data
        if(('US' in country) & (datatype in ("deaths-abs","deaths-1m" ))):
            data = self.getDeathsUS(state)
        if(('US' in country) & (datatype in ("cases-abs","cases-1m"))):
            data = self.getCasesUS(state)
        if(('US' in country) & ('All' in state) & (datatype in ("deaths-abs","deaths-1m" ))):
            data = self.getDeathsGlobal(country)
        if(('US' in country) & ('All' in state) & (datatype in ("cases-abs","cases-1m"))):
            data = self.getCasesGlobal(country)
        if(('US' not in country) & (datatype in ("deaths-abs","deaths-1m"))):
            data = self.getDeathsGlobal(country)
        if(('US' not in country) & (datatype in ("cases-abs","cases-1m"))):
            data = self.getCasesGlobal(country)

        # Get population
        cp = self.worldPopulations.loc[self.worldPopulations['Country'] == country]['Population'].values
        if (cp.size == 1): countryPopulation = pd.Series((cp[0]/1000000),range(0,data.size)) 
        else: countryPopulation = 1 # trying to avoid an error state, no doubt a more elegant method available
        sp = self.usStatePopulations.loc[self.usStatePopulations['State'] == state]['Population'].values
        if (sp.size == 1): statePopulation = pd.Series((sp[0]/1000000),range(0,data.size)) 
        else: statePopulation = 1
        
        # Divide if 1m
        if(('US' in country) & ('All' not in state) & (datatype == "deaths-1m")):
            data = data / statePopulation.values
        if(('US' in country) & ('All' not in state) & (datatype == "cases-1m")):
            data = data / statePopulation.values
        if(('US' in country) & ('All' in state) & (datatype == "deaths-1m")):
            data = data / countryPopulation.values
        if(('US' in country) & ('All' in state) & (datatype == "cases-1m")):
            data = data / countryPopulation.values
        if(('US' not in country) & (datatype == "deaths-1m")):
            data = data / countryPopulation.values
        if(('US' not in country) & (datatype == "cases-1m")):
            data = data / countryPopulation.values
        
        # 7 day delta average (should add this to the class)
        deltaData = data.copy()
        deltaData[0] = 0
        for i in range(1,data.size):
            deltaData[i] = data[i] - data[i-1]
        delta7d = deltaData.copy().astype(float)
        for i in range(7,data.size):
            total = 0
            for j in range(0,7):
                total += deltaData[i-j]
            delta7d[i] = total / 7
 
        delta7d = delta7d.round(1)
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
