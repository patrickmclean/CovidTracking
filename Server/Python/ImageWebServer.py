# -*- coding: utf-8 -*-
"""
Created on Sun Sep 18 18:32:19 2016

@author: patrickmclean
"""

#!/usr/bin/env python
import web
import xml.etree.ElementTree as ET
from PIL import Image

tree = ET.parse('user_data.xml')
root = tree.getroot()

urls = (
    '/users', 'list_users',
    '/users/(.*)', 'get_user',
    '/image', 'load_image'
)

app = web.application(urls, globals())

class list_users:        
    def GET(self):
        output = 'users:[';
        for child in root:
            print 'child', child.tag, child.attrib
            output += str(child.attrib) + ','
            output += ']';
        return output

class get_user:
    def GET(self, user):
        for child in root:
            if child.attrib['id'] == user:
                return str(child.attrib)

class load_image:
    def GET(self):
        #image = Image.open("/Users/patrickmclean/Documents/Web/AppleScript/capture.png")
        #buffer = image.load()
        myFile = open("/Users/patrickmclean/Documents/Web/AppleScript/capture.png","r")
        buffer = myFile.read()
        return buffer
        
if __name__ == "__main__":
    app.run()
