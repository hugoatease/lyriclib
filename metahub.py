#!/usr/bin/python
import lyricsapi
import urllib2

class Metahub(lyricsapi.Fetcher):
       
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
        except:
            lyrics = 'Error'
        
        self.lyrics = lyrics
        return lyrics
    
    def get(self):
        self.getLyric()
        return self.lyrics
    
if __name__ == '__main__':
    artist = raw_input('Artist: ')
    title = raw_input('Title: ')
    api = Metahub(artist, title)
    print api.get()