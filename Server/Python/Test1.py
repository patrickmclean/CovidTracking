from os import path
#import numpy as np
import pandas as pd
#from matplotlib.pyplot import figure, show, rc
#import matplotlib.pyplot as plt
#import matplotlib.mlab as mlab

df = pd.DataFrame({'A' : ['foo', 'bar', 'foo', 'bar','foo', 'bar', 'foo', 'foo'],
                   'B' : ['one', 'one', 'two', 'three','two', 'two', 'one', 'three'],
                   'C' : np.random.randn(8),
                   'D' : np.random.randn(8)})
