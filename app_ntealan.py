#app_ntealan.py
#! /usr/bin/env python
"""
Project Name    : Project Technique web
File Name       : Projet final
Encoding        : UTF-8

Copyright (c) 2021 by Chinatsu KUROIWA

============================================
    usage :
    >>> pip3 install streamlit
    >>> pip3 install pandas

"""
import streamlit as st
import pandas as pd
import re

def app():
    st.title('NTeALan')
    st.markdown("Dans cette page, vous allez trouver une présentation d'un très beaux projet de [**NTeALan**](https://ntealan.org/) "
    	"(New Technologies for African Languages) qui travaille à la mise en œuvre d’outils technologiques intelligents pour la promotion,"
    	" le développement et l’enseignement des langues nationales africaines.")

    st.header("Objectif de ce projet")
    st.markdown("Le but du projet de NTeALan est d'eliminer efficacement les barrières linguistique et culturelles."
    	" Pour cet objectif, NTeALan crée plusieurs produits en utilisant les nouvelles téchnologies."
    	" Nous allons présenter ci-dessous un de leur projet **le dictionnaire collaboratif**.")

    st.header("Dictionnaire collaboratif")
    st.markdown("Le dictionnaire collaboratif est un des projet phar de NTeLan. "
    	" C'est un dictionnaire numérique et accesible sur internet. Ce site présente *Le Petit Dictionnaire yémba-français* en ultilisant une nouvelle tecnologie intelligente afin de faciliter l'accès à "
    	"la langue [**yɛmba**](https://fr.wikipedia.org/wiki/Yemba) pour tout le monde et à des fins très variées (e.g. apprentissage, recherche)."
    	" Ci-dessous, des exemples de vocabulaire que vous pouvez trouver dans ce dictionnaire collaboratif.")

     # Lire la data scrapée 
    df = pd.read_csv(".././data/output_natealan.csv")

     # présentation des artices extarit
    st.subheader("Exeples de dicitionnaire colaboratif")

    # présenter en format tabule qui a deux colones
    cols = st.beta_columns(2)

    #les éléments de 1er colonne
    rad = df['radical'][0]
    form = df['form'][0]
    _type = df['type'][0]
    cat = df['cat'][0]

    cols[0].title(rad)
    cols[0].markdown(f'Form : **{form}**     Type : **{_type}**')
    cols[0].markdown(f'Catégories grammaticales : **{cat}**')

    traduction = re.sub("(\[|\]|\')","",df['traduction'][0])
    traduction = traduction.split(',')
    trad_string = ""
    for trad in traduction :
    	trad_string += trad
    cols[0].markdown(f"Traduction en français : **{trad_string}** ")

    #les éléments de 2éme colonne
    rad2 = df['radical'][6]
    form2 = df['form'][6]
    _type2 = df['type'][6]
    cat2 = df['cat'][6]
    cols[1].title(rad2)
    cols[1].markdown(f'Form : **{form2}**     Type : **{_type2}**')
    cols[1].markdown(f'Catégories grammaticales : **{cat2}**')
    traduction = re.sub("(\[|\]|\')","",df['traduction'][6])
    traduction = traduction.split(',')
    trad_string2 = ""
    for trad in traduction :
    	trad_string2 += trad
    cols[1].markdown(f"Traduction en français : **{trad_string2}** ")

    st.markdown("Ce site est vraiment riche en termes d'informations pour chaque mots et propose une strucutre très pratique."
    	" On peut trouuver des infrmations linguistiques comme presenté ci-dessus et il y a aussi des images, des sons ou encore des exemple d'utilisation pour certains mots."
    	" Le site est [ici](https://ntealan.net/dictionaries/content/fr-af/yb_fr_3031)")

    st.header("Pour notre et votre Future ! ")
    st.write("La langue est un point d'entrée essentiel pour la communication et la compréhension d'une culture."
    	" Ce site qui est riche en informations linguistique peut être très utile non seulement pour les apprenants de cette langue, mais aussi pour les personnes qui viennent de différents domaines "
    	" afin d'approfondir les langues africaines ou la culture africaine.")
    st.write("Ce dictionnaire est développé également grâce à la communauté des bénévoles travaillant sur les langues peu-dotées "
    	" dans l’objectif de créer un marché de la donnée autour de ces langues.")
    st.write("Souhaitez vous soutenir cette gemme cachée pour notre et votre future ? ")

   
    st.balloons()
