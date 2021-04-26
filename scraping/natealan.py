#natealan.py
#! /usr/bin/env python

"""
Project Name    : Project Technique web
File Name       : Projet final
Encoding        : UTF-8

Copyright (c) 2021 by Chinatsu KUROIWA

============================================
    usage :
    >>> pip3 install selenium

"""

import time
from selenium.webdriver import Chrome
from selenium import webdriver
import re
import csv


driver = "./chromedriver.exe"
browser = webdriver.Chrome(executable_path = driver)

browser.get("https://ntealan.net/dictionaries/content/fr-af/yb_fr_3031")
browser.implicitly_wait(10)

# click radio button
button = browser.find_elements_by_xpath("/html/body/app-root/div/div[1]/div/app-entete/div[3]/div/div/div[2]/button")[0]
button.click()
time.sleep(5)

# récuperer la balise qui conitiens des balises des articles 
listeUL = browser.find_elements_by_class_name('listeUL')
time.sleep(5)

# récuperer toute les balise li qui contines des articles 
list_article = listeUL[0].find_elements_by_tag_name('li')
time.sleep(5)

articles= []
# récuperer 1à artciles dans la liste 
for i in range(7):
	# on click cette balise pour afficher le contenu d'un article
	list_article[i].click()
	time.sleep(2)

	articl = []
	# récuperer des informations souhaitées
	article = browser.find_elements_by_class_name('article')
	time.sleep(2)

	radical = article[0].find_elements_by_class_name('radical')
	articl.append(radical[0].text)

	form = article[0].find_elements_by_class_name('forme')
	articl.append(form[0].text)

	typ =  article[0].find_elements_by_class_name('type')
	articl.append(typ[0].text)

	cat =  article[0].find_elements_by_class_name('cat_part')
	articl.append(cat[0].text)

	trans= article[0].find_elements_by_class_name('translation')
	trad = []
	# il peut y avoir plusieurs traductions donc on fait une boucle et récupere tous
	for elt in trans :
		span = elt.find_elements_by_class_name('group_equiv')
		for mot in span :
			# suprime "fr" car ce une informations que je ne veux pas 
			mot = re.sub("fr","",mot.text)
			trad.append(mot)
	articl.append(trad)

	articles.append(articl)
# on ferme le browser lorsque on a récupéré touts les infos souhaitées 
browser.quit();

# ouvre le fichier csv pour écrire des données extraites
f = open(".././data/output_natealan.csv", "w")
# écrire le header du fichier 
header = ["radical","form","type","cat","traduction"]
writer = csv.writer(f)
writer.writerow(header)
# écrire des infos de chaque articles à chaque ligne
for elts in articles : 
	writer.writerow(elts)
#fermer le fichier csv
f.close()
