import web
from readData import DataReader

urls = (
    '/getdata(.*)', 'getData'
)

app = web.application(urls, globals())

class getData:
    def GET(self, url_ext): #url_ext is any other data in the URL, probably not going to be used
        country = web.input(country='no country specified').country
        #startdate = web.input().startdate
        #enddate = web.input().enddate
        string = "<html><body><h2>Hello "
        string += country
        string += "</h2><br><p>"
        dr = DataReader()
        dr.getDeaths()
        string += dr.jsonOutput
        string += "</p><body></html>"
        return string 

        
          
if __name__ == "__main__":
    app.run()