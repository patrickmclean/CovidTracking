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


# Start with the basics, some printing commands
myInt = 12
myString = "Hello"
myFloat = 1.2
myDate = datetime(2001, 2, 3, 4, 5)

#print('Dat {:%Y-%m-%d %H:%M}'.format(datetime(2001, 2, 3, 4, 5)))

print ("This is an int {:d}, a float {:.2f} a string: {} and a date {:%Y-%m-%d %H:%M}".format(myInt,myFloat,myString,myDate) )
# Details https://pyformat.info/
