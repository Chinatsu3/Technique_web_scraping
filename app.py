#app.py
#! /usr/bin/env python

"""
Project Name    : Technique_web_scraping
Encoding        : UTF-8

Copyright (c) 2021 by Chinatsu KUROIWA

============================================
	usage :
	>>> pip3 install streamlit

"""
from visualisation import app_hotel
from visualisation import app_accueil
from visualisation import app_ntealan
import streamlit as st

PAGES = {
    "Page d'accueil": app_accueil,
    "NH Hôtels": app_hotel,
    "NTeALan" : app_ntealan
}

st.sidebar.title('Projet Technique Web - TAL M2 Inalco')
st.sidebar.header('Navigation')
selection = st.sidebar.radio("Go to", list(PAGES.keys()))
page = PAGES[selection]

st.sidebar.subheader('Auteur')
st.sidebar.write('Chinatsu KUROIWA')

page.app()
