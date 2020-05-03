# Server code for reading covid files

# Read file into data frame

# Host web service calls

# Input: Country, Date Range. Output: Deaths

# system imports
import pandas as pd
import os
import json

#local imports
import FileManager as fm

# Read the config file
cwd = os.getcwd()
config_filename = cwd+'/Config/config.js'

config = json.loads(fm.Read(config_filename))

print(config["international deaths"])

