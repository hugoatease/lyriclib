#!/usr/bin/python
import lyricsapi
import urllib2

__siteID__ = 'MetaHub'
__version__ = 1
__author__ = 'Hugo Caille'

class Fetch(lyricsapi.Fetcher):
       
    def makeURL(self):
        artist = urllib2.quote(self.artist)
        title = urllib2.quote(self.title)
        url = 'https://tunehubmeta.appspot.com/get?artist=' + artist + '&title=' + title
        self.url = url
        return url

    def getLyric(self):
        url = self.makeURL()
        try:
            page = urllib2.urlopen(url)
            lyrics = page.read()
            if len(lyrics) < 6:
                lyrics = None
        except:
            lyrics = None
        
        self.lyrics = lyrics
        return lyrics
    
    def get(self):
        self.getLyric()
        if self.lyrics == None:
            return None
        else:
            lyrics = self.unicode(self.lyrics)
            return lyrics
    
if __name__ == '__main__':
    artist = raw_input('Artist: ')
    title = raw_input('Title: ')
    api = Fetch(artist, title)
    print api.get()
    print type(api.lyrics)