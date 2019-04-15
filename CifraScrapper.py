import requests
from bs4 import BeautifulSoup
import lxml

class scrapper:
    url = "https://www.cifraclub.com.br"

    #Return a soup content from html or html5 page
    def make_request(self, url = "/"):
        url = "https://www.cifraclub.com.br" + url
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