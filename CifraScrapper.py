import requests
from bs4 import BeautifulSoup
import lxml

class scrapper:
    url = "https://www.cifraclub.com.br"

    #Return a soup content from html or html5 page
    def make_request(self, url = "/"):
        url = self.url + url
        req = requests.get(url)
        soap = BeautifulSoup(req.content, 'lxml')
        return soap
    
    #Return a dictionary of artits
    def get_artists_by_letter(self, letter = None):
        if(letter == None): return "Letter is mandatory!"
        
        url = "/letra/" + letter + "/lista.html"
        soap = self.make_request(url)
        
        body = soap.find('body')
        tbl = body.find('div', attrs={'class' : 'g-1 g-fix g-sb'})
        arts = tbl.find('ul').find_all('li')
        
        artists = {}
        for artist in arts:
            data = artist.find('a')
            name = data.get_text()
            link = data['href']
            
            if(name[0] != letter):
                pass
            else:
                artists[name] = link

        return artists

    #Return a dictionary of musics
    def get_musics_by_artist(self, artist = None):
        if(artist == None): return "Artist is mandatory!"

        url = artist + "/#instrument=lyrics"
        soap = self.make_request(url)

        body = soap.find('body')
        tbl = body.find('div', attrs={'id':'js-a-s-box'})
        mscs = tbl.find('ol').find_all('li')
        
        musics = {}
        for music in mscs:
            data = music.find('a')
            nome = data.get_text().strip()
            link = data['href']
            musics[nome] = link

        return musics

    #Return a dict with music info
    def get_musics_lyrics(self, link = None):
        if(link == None): return "artist and music link is mandatory!"
        
        url = link + '/letra/'
        soap = self.make_request(url)

        body = soap.find('body')
        tbl = body.find('div', attrs={'class':'g-1 g-fix cifra'})
        
        music = tbl.find('h1').get_text()
        artist = tbl.find('h2').find('a').get_text()

        lrcs = tbl.find('div', attrs={'class':'letra'}).find_all('p')

        lyrics = ""
        music_info = {}
        for lyric in lrcs:

            #Replace the tags br
            lyric = str(lyric).replace('<br/>', ' ')
            lyrics += lyric

        
        #Added a paragraph
        lyrics = lyrics.replace('</p><p>', '.\n\n')

        #Remove <p> and </p> from the final of lyrics
        lyrics = lyrics.replace('<p>', '')
        lyrics = lyrics.replace('</p>', '.')

        music_info['music name'] = music
        music_info['music artist'] = artist
        music_info['music lyrics'] = lyrics

        return music_info        

