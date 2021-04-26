#app.py
#! /usr/bin/env python

"""
Project Name    : Project Technique web
File Name       : Projet final
Encoding        : UTF-8

Copyright (c) 2021 by Chinatsu KUROIWA

============================================
	usage :
	>>> pip3 install streamlit

"""
import app_hotel
import app_accueil
import app_ntealan
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
