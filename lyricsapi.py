#!/usr/bin/python

class Fetcher:
#Parent-class for the site-specific fetching modules
    def __init__(self, artist, title):
        artist = artist.encode('utf-8')
        title = title.encode('utf-8')
        self.artist = artist
        self.title = title
        
    def unicode(self, lyric):
        if lyric != None:
            ulyric = lyric.decode('utf-8')
            ulyric = unicode(ulyric)
            return ulyric
        else:
            return None
        
    def get(self):
        return self.lyrics
 
class API:
    def __init__(self, artist, title, sources=None):
        import metahub, sing365
        if sources == None:
            self.sources = [metahub, sing365]
        self.artist = artist
        self.title = title

    def get(self):
        for source in self.sources:
            api = source.Fetch(self.artist, self.title)
            results = api.get()
            if results != None:
                if len(results) > 1:
                    self.results = results
                    self.siteID = source.__siteID__
                    self.version = source.__version__
                    break
        try:
            return self.results
        except:
            self.results = None
            self.siteID = None
            self.version = None
            return None

if __name__ == '__main__':
    artist = raw_input('Artist: ')
    title = raw_input('Title: ')
    api = API(artist, title)
    api.get()
    print api.results
    print 'SiteID: ', api.siteID
    print 'Version: ', api.version
    print type(api.results)