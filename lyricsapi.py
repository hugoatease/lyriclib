#!/usr/bin/python
if __name__ == '__main__':
    import metahub, sing365

class Fetcher:
#Parent-class for the site-specific fetching modules
    def __init__(self, artist, title):
        artist = artist.encode('utf-8')
        title = title.encode('utf-8')
        self.artist = artist
        self.title = title
        
    def get(self):
        return self.lyrics
 
class API:
    def __init__(self, artist, title, sources=None):
        if sources == None:
            self.sources = [metahub, sing365]
        self.artist = artist
        self.title = title

    def get(self):
        for source in self.sources:
            api = source.Fetch(self.artist, self.title)
            results = api.get()
            if results != None and results != 'Error':
                if len(results) > 1:
                    self.results = results
                    self.siteID = source.__siteID__
                    self.version = source.__version__
                    break
        return self.results

if __name__ == '__main__':
    artist = raw_input('Artist: ')
    title = raw_input('Title: ')
    api = API(artist, title)
    api.get()
    print api.results
    print 'SiteID: ', api.siteID
    print 'Version: ', api.version