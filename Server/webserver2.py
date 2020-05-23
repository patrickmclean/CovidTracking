import os, os.path
import random
import string

import cherrypy
from readData import DataReader

# Return index page (plus test page)
class DataLoader(object):
    @cherrypy.expose
    def index(self):
        return open('Client/index.html')

    @cherrypy.expose
    def test(self):
        return "Another place"

# Get deaths service
@cherrypy.expose
class DataLoaderWebService(object):

    @cherrypy.tools.accept(media='text/plain')
    def POST(self, country, state, datatype):
        return DataReader().getData(country,state, datatype)
    
# Get list of countries service    
@cherrypy.expose
class CountryLoaderWebService(object):

    @cherrypy.tools.accept(media='text/plain')
    def GET(self):
        return DataReader().getCountryList()

# Get list of states service    
@cherrypy.expose
class StatesLoaderWebService(object):

    @cherrypy.tools.accept(media='text/plain')
    def GET(self):
        return DataReader().getStateList()

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
        '/loadcountries': {
            'request.dispatch': cherrypy.dispatch.MethodDispatcher(),
            'tools.response_headers.on': True,
            'tools.response_headers.headers': [('Content-Type', 'text/plain')],
        },
        '/loadusstates': {
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
    webapp.loadcountries = CountryLoaderWebService()
    webapp.loadusstates = StatesLoaderWebService()
    cherrypy.config.update({'server.socket_host': '0.0.0.0', #this makes it transmit through host
                            'server.socket_port':8080})
    cherrypy.quickstart(webapp, '/', conf)