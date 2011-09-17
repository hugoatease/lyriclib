import urllib2

class Metahub:
    def __init__(self, artist, title):
        artist = artist.encode('utf-8')
        title = title.encode('utf-8')
        self.artist = artist
        self.title = title
        
    def makeURL(self):
        artist = urllib2.quote(self.artist)
        title = urllib2.quote(self.title)
        url = 'https://tunehubmeta.appspot.com/get?artist=' + artist + '&title=' + title
        self.url = url
        return url
    
    def unicode(self, lyric):
        ulyric = lyric.decode('utf-8')
        ulyric = unicode(ulyric)
        return ulyric

    def getLyric(self):
        url = self.makeURL()
        try:
            page = urllib2.urlopen(url)
            lyrics = page.read()
        except:
            lyrics = 'Error'