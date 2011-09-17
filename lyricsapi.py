from tunehubcore.sites.sing365 import *
from tunehubcore import datastruct

class Lyrics:
    
    def __init__(self, cacheObject, artist, title, album=None, year=None):
        self.artist = artist
        self.title = title
        self.name = artist + ' - ' + title
        self.album = album
        self.year = year
        
        self.sing365 = Sing365(artist, title)
        self.cache = cacheObject
        self.cache.setMeta(self.artist, self.title)
        
    def getLyric(self):
        Cache = self.cache
        Cache.openFile()
        cached_data = Cache.read()
        if cached_data == None:
            self.provider = 'Sing365'
            sing365 = self.sing365
            lyric = sing365.getLyric()
            self.cached = False
            '''if lyric == None:
                self.provider = 'MLDB'
                mldb = self.mldb
                lyric = mldb.getLyric()
                if lyric == None:
                    self.provider = 'ChartLyrics'
                    chartlyrics = self.chartlyrics
                    lyric = chartlyrics.getLyric()
                    if lyric == None:
                        self.provider = None'''
            if lyric == None:
                self.provider = None
                    
            self.lyric = lyric
            Cache.add(self.lyric, self.provider)
            return lyric
        else:
            self.cached = True
            self.provider = cached_data['Provider']
            self.lyric = cached_data['Lyric']
            
    
    def get(self):
        self.getLyric()
        data = datastruct.Structure()
        data.Artist(self.artist)
        data.Title(self.title)
        data.Album(self.album)
        data.Year(self.year)
        data.Provider(self.provider)
        data.Lyric(self.lyric)
        data.Cached(self.cached)
        
        return data.get()
