#app_hotel.py
#! /usr/bin/env python
"""
Project Name    : Technique_web_scraping
Encoding        : UTF-8

Copyright (c) 2021 by Chinatsu KUROIWA

============================================
    usage :
    >>> pip3 install streamlit
    >>> pip3 install plotly
    >>> pip3 install pandas
"""

import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

def app():
    st.title('Analyses du site NH Hôtels')
    st.write("Dans cette page vous allez trouver des analyses sur le site NH Hôtels, via lequel on peut chercher 357 hôtels parmis 29 pays dans le monde entier.")
    
    st.header("Objectif des analyses")
    st.write("Récemment, le changement climatique, tel que le réchauffement de la planète, est devenu plus visible pour le public. "
    "Nous pensons qu'il est nécessaire que les entreprises de tous les domaines, y compris le tourisme, prennent plus sérieusement en compte l'environnement. "
    "Dans le site NH Hôtels, il y a des hôtels qui mettent en avant leur respect de l'environements. "
    "Dans cette page vous trouverez des analyses sur les hôtels en fonction de leur respect de l’environnement (Eco_Friendly).")
    
    # Lire la data scrapée 
    df = pd.read_csv("./data/output_nhHotels.csv")
    
    # présentation de donnée 
    st.subheader("Donées sur les hôtels du site NH Hôtels")
    st.write(df)
    st.markdown("Ce sont des données que nous avons extraites depuis le site NH hôtels. "
    "Elles contiennent les informations suivantes : " )
    st.markdown("- **Pays**")
    st.markdown("- **Nom de l'hôtel**")
    st.markdown("- **Nombre d'étoile de l'hôtel**")
    st.markdown("- **Eco Friendly** : *Présence ou non d'un signe indiquant que l'hôtel adopte une demarche spécifique de protection de l'environement*."
    " Plus d'information [ici](https://www.nh-hotels.fr/environnement/hotels-ecologiques-developpement-durable)")
    st.markdown("- **Nombre d'étoiles sur Trip Adviser**")
    
    
    # ====== Parie Analyes ===== #
    st.write("")
    st.header("Analyses")
    
    # doughnut chart
    st.subheader("Répartition des hôtels")
    labels = ['Non Eco Friendly', 'Eco friendly']
    vals = df['eco_friendly'].value_counts()
    values = [vals[0], vals[1]]
    fig = go.Figure(data=[go.Pie(labels=labels, values=values, hole=.3)])
    st.write(fig)
    st.markdown("**56%** des hôtels qui se trouvent dans ce site ont le signe de *Eco Friendly* et **44%** de les hôtels ne l'ont pas. "
    "Vous pouvez regarder les chiffres détaillés lorsque vous passer votre souris sur le graphe.")
    
    
    # Bar chart
    st.subheader("Note moyenne sur Trip Adviser")
    means = df.groupby('eco_friendly')['avis_client'].mean()
    colors = ['lightslategray',] * 2
    colors[1] = 'crimson'
    fig_bar = go.Figure(data=[go.Bar( x=labels, y=[means[0],means[1]],marker_color=colors)])
    st.write(fig_bar)
    st.markdown("Nous pouvons observer que la note des avis clients sur Trip Adviser pour les hôtels Eco Friendly est plus élevée à **4.12 étoiles** "
    "que ceux Non Eco Friendly à **3.9 étoiles**. Nous povons donc remarquer que les clients ont eu des expériences plus positives avec des hôtels Eco Friendly.")
    
    # ===== Conclusion ===== #
    st.write("")
    st.subheader("Conclusion")
    st.write("D'après ces résultats, nous povons observer que, parmi les hôtels répertoriés sur ce site, "
    "ceux qui sont plus respectueux de l'environnement offrent un meilleur service à leurs clients."
    " Afin de promouvoir des activités plus respectueuses de l'environnement de la part du secteur du tourisme, "
    "il est conseillé de mettre ces informations sur le site afin qu'elles soient plus clairement visibles pour les clients potentiels."
    " Par conséquent, nous pensons qu'un site web qui permet aux utilisateurs de rechercher des hôtels en fonction de leur respect de l'environnement est "
    "précieux pour offrir un service plus satisfaisant aux futurs clients.")
    
    
  
    
   
    