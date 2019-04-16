from CifraScrapper import scrapper

scrap = scrapper()

musics = scrap.get_musics_by_artist('/racionais-mcs')

for music in musics.keys():
    print(music, musics[music])