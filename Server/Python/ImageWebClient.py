# -*- coding: utf-8 -*-
"""
Created on Sun Sep 18 18:19:10 2016

@author: patrickmclean
"""

import urllib
import json

serviceurl = 'http://0.0.0.0:8080/image'


url = serviceurl 
print 'Retrieving', url
uh = urllib.urlopen(url)
data = uh.read()
print 'Retrieved',len(data),'characters'
myFile = open("/Users/patrickmclean/Documents/Web/AppleScript/test.png","wb")
myFile.write(data)
myFile.close()

