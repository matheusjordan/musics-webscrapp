from CifraScrapper import scrapper

scrap = scrapper()

artists = scrap.get_artists_by_letter('A')

for art in artists.keys():
    print(art, artists[art])