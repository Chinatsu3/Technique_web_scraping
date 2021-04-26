#app_accueil.py
#! /usr/bin/env python

"""
Project Name    : Project Technique web
File Name       : Project final
Encoding        : UTF-8

Copyright (c) 2021 by Chinatsu KUROIWA

============================================
    usage :
    >>> pip3 install streamlit

"""

import streamlit as st
from PIL import Image

def app():
    st.title('Bienvenue ! ')
    st.write("Dans ce site web, nous allons vous présenter deux sites dans lesquels nous pensons que vous devriez investir dans le futur."
    " L'un est un site de recherche et de réservation d'hôtels et l'autre est un site sur la langue peu-dotée yɛmba.")
    
    st.text(" ")

    cols = st.beta_columns(2) 

    # explication pour le site NH hôtels
    cols[0].header("NH Hôtels")
    image = Image.open('./images/nh_hotels.jpg')
    cols[0].image(image)
    cols[1].text(" ")
    cols[1].write("NH Hôtels est un site qui permet de chercher des logements y compris des logements écologiques."
    	" Nous allons analyser des données que nous avons extraites de ce site afin d'étudier la valeur de "
    	"la mise en place d’un système de recherche des logements écologiques."
    	" Vous pouvez accéder à ces analyses en appuyant le bouton **NH Hôtels** à gauche " )

    cols[0].text(" ")
    cols[1].text(" ")

     # explication pour le dictionnaire
    cols[1].header("NTeALan")
    image = Image.open('./images/dict.PNG')
    cols[1].image(image)
    cols[0].text(" ")
    cols[0].write(" NTeALan est une organisation qui édite un dictioanniere en ligne pour la langue africaine *yɛmba*. Aujourd'hui le yɛmba est considéré comme une langue peu-dotée."
    "C'esr-à-dire qu'il y a peu de ressources disponibles sur cette langue."
    " Nous allons vous presenter ce dictionanire dans la page **NTeALan**." 
    " Vous pouvez y accéder en appuyant le bouton à gauche.")