import os, os.path
import random
import string

import cherrypy
from readData import DataReader

class DataLoader(object):
    @cherrypy.expose
    def index(self):
        return open('./Client/index.html')


@cherrypy.expose
class DataLoaderWebService(object):

    @cherrypy.tools.accept(media='text/plain')
    def GET(self):
        return cherrypy.session['mystring']

    def POST(self, country='netherlands'):
        return_string = 'this is the data for the ' + country + '<br>'
        dr = DataReader()
        dr.getDeaths()
        return_string += dr.jsonOutput
        return return_string

    def PUT(self, another_string):
        cherrypy.session['mystring'] = another_string

    def DELETE(self):
        cherrypy.session.pop('mystring', None)


if __name__ == '__main__':
    conf = {
        '/': {
            'tools.sessions.on': True,
            'tools.staticdir.root': os.path.abspath(os.getcwd())
        },
        '/generator': {
            'request.dispatch': cherrypy.dispatch.MethodDispatcher(),
            'tools.response_headers.on': True,
            'tools.response_headers.headers': [('Content-Type', 'text/plain')], 
        },
        '/loaddata': {
            'request.dispatch': cherrypy.dispatch.MethodDispatcher(),
            'tools.response_headers.on': True,
            'tools.response_headers.headers': [('Content-Type', 'text/plain')],#move this to json next
        },
        '/static': {
            'tools.staticdir.on': True,
            'tools.staticdir.dir': './cherrypy'
        }
    }
    webapp = DataLoader()
    webapp.loaddata = DataLoaderWebService()
    cherrypy.quickstart(webapp, '/', conf)