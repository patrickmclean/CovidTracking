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

# Read the config file
# Future - turn this into a service - get key/value pair
cwd = os.getcwd()
config_filename = cwd+'/Config/config.json'

config = json.loads(fm.Read(config_filename))

csv_file = cwd + '/'+config["datapath"] + config["international deaths"]
print(csv_file)


# Read CSV into Dataframe

myDataFrame = pd.read_csv(csv_file)
myDataFrame.head(10)
myDataFrame.info()
myDataFrame.describe()
