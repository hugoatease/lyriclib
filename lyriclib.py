#!/usr/bin/python
'''TuneHub Lyrics Library.
    Copyright (C) 2011-2012  Hugo Caille
    
    Redistribution and use in source and binary forms, with or without modification, are permitted provided that the following conditions are met:
    1. Redistributions of source code must retain the above copyright notice, this list of conditions and the following disclaimer.
    2. Redistributions in binary form must reproduce the above copyright notice, this list of conditions and the following disclaimer
    in the documentation and/or other materials provided with the distribution.
    3. The name of the author may not be used to endorse or promote products derived from this software without specific prior written permission.
    
    THIS SOFTWARE IS PROVIDED BY THE AUTHOR ``AS IS'' AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED WARRANTIES
    OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE AUTHOR BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL,
    SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR
    PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE
    OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
    '''

__version__ = 2

import re, json, urllib2, urlparse

def escape(text):
    if text != None:
        text = text.replace('<br>', '\n').replace('<br />', '\n').replace('</br>', '\n')
        text = re.sub('<[^<]+?>', '', text)
    return text

def url(template, artist, title, escaping):
    artist = artist.lower().replace(' ', escaping['artist'])
    title = title.lower().replace(' ', escaping['title'])
    return template.replace(':artist', artist).replace(':title', title)

def parse(text, execsnippet):
    result = None
    toparse = text
    try:
        exec execsnippet
        return result
    except:
        return None

class Lyric():
    def __init__(self, sitesdic):
        self.sitesdic = sitesdic
        self.artist = self.title = ''
        self.lyric = None
    def get(self):
        for site in self.sitesdic:
            error = False
            self.url = url(template = site['url'], artist = self.artist, title = self.title, escaping = site['escaping'])
            try:
                p = urllib2.urlopen(self.url)
            except:
                error = True
            
            if error == False:
                self.page = p.read()
                p.close()
                
                self.execsnippet = site['exec']
                self.parsed = parse(self.page, self.execsnippet)
                self.lyric = escape(self.parsed)
                print self.lyric
                if self.lyric != None:
                    break
        if self.lyric != None:
            return self.lyric
    

def init(filename = 'sites.json'):
    f = open(filename, 'r')
    js = f.read()
    f.close()
    global sites
    sites = json.loads(js)
    return Lyric(sites)

if __name__ == '__main__':
    print 'Tunehub Lyriclib 2 Test'
    artist = raw_input('Artist: ')
    title = raw_input('Title: ')
    
    api = init()
    api.artist = artist
    api.title = title
    api.get()
    print api.url, api.lyric