import os, os.path
import random
import string

import cherrypy
from readData import DataReader

class DataLoader(object):
    @cherrypy.expose
    def index(self):
        return open('Client/index.html')

    @cherrypy.expose
    def test(self):
        return "Another place"

@cherrypy.expose
class DataLoaderWebService(object):

    @cherrypy.tools.accept(media='text/plain')
    def POST(self, country='Netherlands'):
        dr = DataReader()
        return dr.getDeaths(country)
    
@cherrypy.expose
class CountryLoaderWebService(object):

    @cherrypy.tools.accept(media='text/plain')
    def GET(self):
        dr = DataReader()
        return dr.getCountryList()

if __name__ == '__main__':
    conf = {
        '/': {
            'tools.sessions.on': True,
            'tools.staticdir.root': os.path.abspath(os.getcwd())
        },
        '/loaddata': {
            'request.dispatch': cherrypy.dispatch.MethodDispatcher(),
            'tools.response_headers.on': True,
            'tools.response_headers.headers': [('Content-Type', 'text/plain')],
        },
        '/loadus': {
            'request.dispatch': cherrypy.dispatch.MethodDispatcher(),
            'tools.response_headers.on': True,
            'tools.response_headers.headers': [('Content-Type', 'text/plain')],
        },
        '/loadcountry': {
            'request.dispatch': cherrypy.dispatch.MethodDispatcher(),
            'tools.response_headers.on': True,
            'tools.response_headers.headers': [('Content-Type', 'text/plain')],
        },
        '/static': {
            'tools.staticdir.on': True,
            'tools.staticdir.dir': 'Client'
        },
        #'log.access_file': 'access.log'
    }
    webapp = DataLoader()
    webapp.loaddata = DataLoaderWebService()
    webapp.loadcountry = CountryLoaderWebService()
    cherrypy.config.update({'server.socket_host': '0.0.0.0', #this makes it transmit through host
                            'server.socket_port':8080})
    cherrypy.quickstart(webapp, '/', conf)