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
        self.csv_file = cwd + '/'+config["datapath"] + config["international deaths"]

        
    def getDeaths(self):
        # Read CSV into Dataframe
        myDataFrame = pd.read_csv(self.csv_file)

        # Get country & Date subset
        startDate = "2/28/20"
        endDate = "5/2/20"
        json_file = "output.json"

        NLDeaths = myDataFrame.loc[
            (myDataFrame['Country/Region'] == 'Netherlands') 
            & (myDataFrame['Province/State'].isnull()),
            startDate:endDate]
        self.jsonOutput = NLDeaths.to_json()


## Main ##

# Instantiate a DataReader object 

#dr = DataReader()
#dr.getDeaths()
#print (dr.jsonOutput)
