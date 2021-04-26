# hotel_eco.py
#! /usr/bin/env python

"""
Project Name    : Technique_web_scraping
Encoding        : UTF-8

Copyright (c) 2021 by Chinatsu KUROIWA

============================================
    usage :
    >>> pip3 install beautifulsoup4

"""

import requests
from bs4 import BeautifulSoup
import re
import csv


#ouvrire le fichier csv pour stocker les données que on va extraire
f = open(".././data/output_nhHotels.csv", "w")
# ecrire en avance les têtes du fichier
header = ["pays","hotel","etoile_hotel","eco_friendly","avis_client"]
writer = csv.writer(f)
writer.writerow(header)


# déclarer les infos de brouwser que on pourrait utiliser pour donner accès au page 
# j'ai declaré ici  les informations de browser que je utilise 
headers = {"User-Agent": "Mozilla/87.0 (Windows NT 10.0; Win64; x64) Chrome/90.0.4430.85 "}

# donner le lien de site et envoyer la requete 
url = "https://www.nh-hotels.fr/hotels"
res = requests.get(url,headers=headers)

soup = BeautifulSoup(res.text, "html.parser")

### listes de pays
lists_pays = soup.find_all('h3', class_ =re.compile('h6'))
urls_pays = [elt.contents[0].attrs['href'] for elt in lists_pays]


#### listes de hotel de chaque pays
# on va au chaque page de pays  
for pays in urls_pays :
    #récuperer juste des noms de pays qui commance à partir de la position 32 (en string) de chaque urls
    nom_pays = pays[32:]
    
    res = requests.get(pays, headers = headers)
    soup = BeautifulSoup(res.text, "html.parser")

    # récuperer des balises des hôtels
    lists_hotels = soup.find_all('a', href =  re.compile("/hotel/.+"))
    
    for elt in lists_hotels :
        infos_hotel = []
        infos_hotel.append(nom_pays)
    
        contenu = "https://www.nh-hotels.fr"+elt.attrs['href']
        res = requests.get(contenu,headers=headers)
        soup = BeautifulSoup(res.text, "html.parser")
        
        ##### nom du hotel
        nom_hotel = soup.find('h2', class_ =  re.compile("h3"))
        infos_hotel.append(nom_hotel.text)
        
        ##### count etoiles de hotel
        # etoiles de hôtels sont presntés avec des image d'étoile dans chaque balises donc on compte de ces nombre de balise
        stars = soup.find('div', class_ =  re.compile("stars"))
        count = 0
        for star in stars :
            if len(star) == 0 :
                count +=1
        infos_hotel.append(count)
        
        ###Eco-friendly
        lists_pays = soup.find_all('p', class_ =re.compile('color-primary'))
        rep = False
        for elt in lists_pays :
            if "Eco" in elt.text:
                rep = True
        infos_hotel.append(rep)
        
        ##### étoiles de trip Adviser
        l = soup.find('div', class_ =re.compile('comments'))
        et = l.contents[0].attrs['data-url-tripadvisor']
        res = requests.get(et,headers=headers)
        soup = BeautifulSoup(res.text, "html.parser")
        if len(soup.select('img')) > 1 :
            star_adviser = soup.select('img')[1].get('alt')[:3]
            infos_hotel.append(star_adviser)
        else : 
            infos_hotel.append("0")
        
        # ecrire des informations de chaque hôtel
        writer.writerow(infos_hotel)

# fermer la fichier
f.close()
