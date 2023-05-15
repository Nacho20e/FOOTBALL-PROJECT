import streamlit as st
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns
import plotly_express as px
from streamlit_option_menu import option_menu

import folium
from folium.plugins import FastMarkerCluster
import geopandas as gpd
from branca.colormap import LinearColormap

from wordcloud import WordCloud

from IPython.display import Image
import matplotlib.image as mpimg
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import plotly.io as pio
from datetime import datetime

def add_bg_from_url():
    st.markdown(
         f"""
         <style>
         .stApp {{
             background-image: url("https://assets.laliga.com/assets/logos/laliga-h/laliga-h-1200x1200.png");
             background-attachment: fixed;
             background-size: 1300px 700px;
         }}
         </style>
         """,
         unsafe_allow_html=True
     )

add_bg_from_url() 

add_bg_from_url() 

df=pd.read_csv("LIGAS\Output.csv", sep=",")


df["saves %"]=(df["shots on target against"]-df["GA"])*100/df["shots on target against"]
df["G+A"]=df["goals"]+df["assists"]
la_liga=df[df["league"] == "La Liga"]
la_liga_2017 = la_liga[la_liga["Season"]=="01/01/2017"]
la_liga_2018 = la_liga[la_liga["Season"]=="01/01/2018"]
la_liga_2019 = la_liga[la_liga["Season"]=="01/01/2019"]
mejores_jugadores_2017 = (la_liga_2017.groupby("player")["value"].sum().sort_values(ascending=False))
mejores_jugadores_2017.head(10)
gráfica_mej_jug_2017 = la_liga_2017.sort_values(by="value", ascending=False)
gráfica_mej_jug_2017 = gráfica_mej_jug_2017.head(10)
gráfica_mej_jug_2018 = la_liga_2018.sort_values(by="value", ascending=False)
gráfica_mej_jug_2018 = gráfica_mej_jug_2018.head(10)
gráfica_mej_jug_2019 = la_liga_2019.sort_values(by="value", ascending=False)
gráfica_mej_jug_2019 = gráfica_mej_jug_2019.head(10)
gráfica_gol_2017 = la_liga_2017.sort_values(by="goals", ascending=False)
gráfica_gol_2017 = gráfica_gol_2017.head(5)
gráfica_gol_2018 = la_liga_2018.sort_values(by="goals", ascending=False)
gráfica_gol_2018 = gráfica_gol_2018.head(5)
gráfica_gol_2019 = la_liga_2019.sort_values(by="goals", ascending=False)
gráfica_gol_2019 = gráfica_gol_2019.head(5)
total = la_liga.groupby("player").sum().reset_index()
gráfica_gol = total.sort_values(by="goals", ascending=False)
gráfica_gol = gráfica_gol.head(5)
gráfica_asist_2017 = la_liga_2017.sort_values(by="assists", ascending=False)
gráfica_asist_2017 = gráfica_asist_2017.head(5)
gráfica_asist_2018 = la_liga_2018.sort_values(by="assists", ascending=False)
gráfica_asist_2018 = gráfica_asist_2018.head(5)
gráfica_asist_2019 = la_liga_2019.sort_values(by="assists", ascending=False)
gráfica_asist_2019 = gráfica_asist_2019.head(5)
gráfica_asistencias = total.sort_values(by="assists", ascending=False)
gráfica_asistencias = gráfica_asistencias.head(5)
gráfica_gg_2017 = la_liga_2017.sort_values(by="G+A", ascending=False)
gráfica_gg_2017 = gráfica_gg_2017.head(5)
gráfica_gg_2018 = la_liga_2018.sort_values(by="G+A", ascending=False)
gráfica_gg_2018 = gráfica_gg_2018.head(5)
gráfica_gg_2019 = la_liga_2019.sort_values(by="G+A", ascending=False)
gráfica_gg_2019 = gráfica_gg_2019.head(5)
gráfica_gg = total.sort_values(by="G+A", ascending=False)
gráfica_gg = gráfica_gg.head(5)
gráfica_porteros_2017 = la_liga_2017.sort_values(by="saves %", ascending=False)
gráfica_porteros_2017 = gráfica_porteros_2017.head(5)
gráfica_porteros_2018 = la_liga_2018.sort_values(by="saves %", ascending=False)
gráfica_porteros_2018 = gráfica_porteros_2018.head(5)
gráfica_porteros_2019 = la_liga_2019.sort_values(by="saves %", ascending=False)
gráfica_porteros_2019 = gráfica_porteros_2019.head(5)
porteros=total
porteros["saves %"]=porteros["saves %"]/3
gráfica_paradas = porteros.sort_values(by="saves %", ascending=False)
gráfica_paradas = gráfica_paradas.head(5)






opt=st.sidebar.radio("Elige:",options=("Jugadores destacados", "Competición"))
if opt=="Jugadores destacados":
    st.title("JUGADORES DESTACADOS")
    st.header("VALOR DE MERCADO")

    show_content = st.checkbox("Valor 2017")

    if show_content:
        valor2017 = px.bar(gráfica_mej_jug_2017, x="player", y="value", color="value")
        valor2017.update_layout(title=dict(text="TOP 10", x=0.5, xanchor="center"))
        st.plotly_chart(valor2017)
        st.text("Real Madrid(5): Cristiano Ronaldo, Bale, Kroos, Asensio e Isco")
        st.text("F.C. Barcelona(4): Messi, Coutinho, Dembélé y Busquets")
        st.text("Atlético de Madrid(1): Griezmann")

    show_content = st.checkbox("Valor 2018")

    if show_content:
        valor2018 = px.bar(gráfica_mej_jug_2018, x="player", y="value", color="value")
        valor2018.update_layout(title=dict(text="TOP 10", x=0.5, xanchor="center"))
        st.plotly_chart(valor2018)
        st.text("F.C. Barcelona(5): Messi, Griezmann, Dembélé, Coutinho y ter Stegen")
        st.text("Atlético de Madrid(4): Oblak, Saúl, Rodri y Koke")
        st.text("Real Madrid(1): Varane")
        
    show_content = st.checkbox("Valor 2019")

    if show_content:
        valor2019 = px.bar(gráfica_mej_jug_2019, x="player", y="value", color="value")
        valor2019.update_layout(title=dict(text="TOP 10", x=0.5, xanchor="center"))  
        st.plotly_chart(valor2019)
        st.text("F.C. Barcelona(5): Messi, Griezmann, Ansu Fati, ter Stegen y de Jong")
        st.text("Atlético de Madrid(4): Oblak, Joao Felix, Saúl y Gimenez")
        st.text("Real Madrid(1): Hazard")



    st.header("MÁXIMOS GOLEADORES")

    show_content = st.checkbox("Goles 2017")
    if show_content:
        gol1 = px.bar(gráfica_gol_2017, x="player", y="goals", color="goals",color_continuous_scale=px.colors.sequential.Reds)
        gol1.update_layout(title=dict(text="TOP 5", x=0.5, xanchor="center"))
        st.plotly_chart(gol1)
        
        

    show_content = st.checkbox("Goles 2018")
    if show_content:
        gol2 = px.bar(gráfica_gol_2018, x="player", y="goals", color="goals",color_continuous_scale=px.colors.sequential.Reds)
        gol2.update_layout(title=dict(text="Máximos goleadores 2018", x=0.5, xanchor="center"))
        st.plotly_chart(gol2)
        
        
    show_content = st.checkbox("Goles 2019")
    if show_content:
        gol3 = px.bar(gráfica_gol_2019, x="player", y="goals", color="goals",color_continuous_scale=px.colors.sequential.Reds)
        gol3.update_layout(title=dict(text="Máximos goleadores 2019", x=0.5, xanchor="center"))
        st.plotly_chart(gol3)

    show_content = st.checkbox("Goles totales")
    if show_content:
        goltotal = px.bar(gráfica_gol, x="player", y="goals", color="goals",color_continuous_scale=px.colors.sequential.Reds)
        goltotal.update_layout(title=dict(text="Máximos goleadores", x=0.5, xanchor="center"))
        st.plotly_chart(goltotal)
    

    st.header("MÁXIMOS ASISTENTES")

    show_content = st.checkbox("Asistencias 2017")

    if show_content:
        asist1 = px.bar(gráfica_asist_2017, x="player", y="assists", color="assists",color_continuous_scale=px.colors.sequential.Purples)
        asist1.update_layout(title=dict(text="Máximos asistentes 2017", x=0.5, xanchor="center"))
        st.plotly_chart(asist1)
        
        

    show_content = st.checkbox("Asistencias 2018")

    if show_content:
        asist2 = px.bar(gráfica_asist_2018, x="player", y="assists", color="assists",color_continuous_scale=px.colors.sequential.Purples)
        asist2.update_layout(title=dict(text="Máximos asistentes 2018", x=0.5, xanchor="center"))
        st.plotly_chart(asist2)
        
        
    show_content = st.checkbox("Asistencias 2019")

    if show_content:
        asist3 = px.bar(gráfica_asist_2019, x="player", y="assists", color="assists",color_continuous_scale=px.colors.sequential.Purples)
        asist3.update_layout(title=dict(text="Máximos asistentes 2019", x=0.5, xanchor="center"))
        st.plotly_chart(asist3)
        

    show_content = st.checkbox("Asistencias totales")

    if show_content:
        asisttotal = px.bar(gráfica_asistencias, x="player", y="assists", color="assists",color_continuous_scale=px.colors.sequential.Purples)
        asisttotal.update_layout(title=dict(text="Máximos asistentes", x=0.5, xanchor="center"))
        st.plotly_chart(asisttotal)
    



    st.header("GOLES GENERADOS")

    show_content = st.checkbox("Goles generados 2017")

    if show_content:
        gg1 = px.bar(gráfica_gg_2017, x="player", y="G+A", color="G+A",color_continuous_scale=px.colors.sequential.Greens)
        gg1.update_layout(title=dict(text="TOP 5", x=0.5, xanchor="center"))
        st.plotly_chart(gg1)
        
        

    show_content = st.checkbox("Goles generados 2018")

    if show_content:
        gg2 = px.bar(gráfica_gg_2018, x="player", y="G+A", color="G+A",color_continuous_scale=px.colors.sequential.Greens)
        gg2.update_layout(title=dict(text="TOP 5", x=0.5, xanchor="center"))
        st.plotly_chart(gg2)
        
        
    show_content = st.checkbox("Goles generados 2019")

    if show_content:
        gg3 = px.bar(gráfica_gg_2019, x="player", y="G+A", color="G+A",color_continuous_scale=px.colors.sequential.Greens)
        gg3.update_layout(title=dict(text="TOP 5", x=0.5, xanchor="center"))
        st.plotly_chart(gg3)
        

    show_content = st.checkbox("Goles generados totales")

    if show_content:
        ggtotal = px.bar(gráfica_gg, x="player", y="G+A", color="G+A",color_continuous_scale=px.colors.sequential.Greens)
        ggtotal.update_layout(title=dict(text="TOP 5", x=0.5, xanchor="center"))
        st.plotly_chart(ggtotal)

        show_content = st.checkbox("Iago Aspas")

        if show_content:
            Celta = la_liga[la_liga["squad"]=="Celta Vigo"]

            Resto_jugadores = Celta[Celta["G+A"] < 16]["G+A"].sum()
            Aspas = Celta[Celta["G+A"] > 16].append({"player": "Resto_jugadores", "G+A": Resto_jugadores}, ignore_index=True)
            Aspas = px.pie(Aspas, values="G+A", names="player", title="Goles generados por el Celta: 238", hole=0.5,)
            st.plotly_chart(Aspas)
    




    st.header("MEJORES PORTEROS")

    show_content = st.checkbox("% paradas 2017")

    if show_content:
        paradas1 = px.bar(gráfica_porteros_2017, x="player", y="saves %", color="saves %",color_continuous_scale=px.colors.sequential.Oranges)
        paradas1.update_layout(title=dict(text="% paradas 2017", x=0.5, xanchor="center"))
        st.plotly_chart(paradas1)
        
        

    show_content = st.checkbox("% paradas 2018")

    if show_content:
        paradas2 = px.bar(gráfica_porteros_2018, x="player", y="saves %", color="saves %",color_continuous_scale=px.colors.sequential.Oranges)
        paradas2.update_layout(title=dict(text="% paradas 2018", x=0.5, xanchor="center"))
        st.plotly_chart(paradas2)
        
        
    show_content = st.checkbox("% paradas 2019")

    if show_content:
        paradas3 = px.bar(gráfica_porteros_2019, x="player", y="saves %", color="saves %",color_continuous_scale=px.colors.sequential.Oranges)
        paradas3.update_layout(title=dict(text="% paradas 2019", x=0.5, xanchor="center"))
        st.plotly_chart(paradas3)
        

    show_content = st.checkbox("% paradas media")

    if show_content:
        paradasmedia = px.bar(gráfica_paradas, x="player", y="saves %", color="saves %",color_continuous_scale=px.colors.sequential.Oranges)
        paradasmedia.update_layout(title=dict(text="% paradas", x=0.5, xanchor="center"))
        st.plotly_chart(paradasmedia)

        
    
    
    
if opt=="Competición":
    st.title("COMPETICIÓN")
    st.header("VALOR DE LAS PLANTILLAS")

    show_content = st.checkbox("Valor total")

    if show_content:
        valor = la_liga.groupby("squad").sum().reset_index()
        valor= valor.sort_values(by="value",ascending=False)
        valortotal = px.bar(valor, x="squad", y="value", color="value")
        st.plotly_chart(valortotal)

        
        value_counts = la_liga_2019["value"]
        valorpie = go.Figure(data=[go.Pie(labels=la_liga["squad"], values=value_counts,hovertext=value_counts.index)],)
        
        st.plotly_chart(valorpie)

    st.header("ASPECTOS DEL JUEGO")
    
    show_content = st.checkbox("Goles marcados")
    if show_content:
        goles = la_liga.groupby("squad").sum().reset_index()
        goles= goles.sort_values(by="goals",ascending=False)
        fig = px.bar(goles, x="squad", y="goals", color="goals",color_continuous_scale=px.colors.sequential.Reds)
        fig.update_layout(title=dict(text="goles por club", x=0.5, xanchor="center"))
    
        st.plotly_chart(fig)





    show_content = st.checkbox("Faltas cometidas")
    
    if show_content:
        faltas = la_liga.groupby("squad").sum().reset_index()
        faltas= faltas.sort_values(by="fouls",ascending=False)
        fig = px.bar(faltas, x="squad", y="fouls", color="fouls",color_continuous_scale=px.colors.sequential.YlGnBu_r)
        fig.update_layout(title=dict(text="faltas cometidas", x=0.5, xanchor="center"))

        st.plotly_chart(fig)
    
    
    
    
    
    
    
    
    
    
    
    


