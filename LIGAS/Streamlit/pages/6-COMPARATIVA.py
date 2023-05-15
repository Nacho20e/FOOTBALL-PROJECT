import streamlit as st
import streamlit.components.v1 as components
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
             background-size: 1300px 700px;
         }}
         </style>
         """,
         unsafe_allow_html=True
     )

add_bg_from_url() 

df=pd.read_csv("LIGAS\Output.csv", sep=",")

la_liga=df[df["league"] == "La Liga"]
la_liga_2017 = la_liga[la_liga["Season"]=="01/01/2017"]
la_liga_2018 = la_liga[la_liga["Season"]=="01/01/2018"]
la_liga_2019 = la_liga[la_liga["Season"]=="01/01/2019"]
mejores_jugadores_2017 = (la_liga_2017.groupby("player")["value"].sum().sort_values(ascending=False))
mejores_jugadores_2017.head(10)
gráfica_mej_jug_2017 = la_liga_2017.sort_values(by="value", ascending=False)
gráfica_mej_jug_2017 = gráfica_mej_jug_2017.head(3)
gráfica_mej_jug_2018 = la_liga_2018.sort_values(by="value", ascending=False)
gráfica_mej_jug_2018 = gráfica_mej_jug_2018.head(3)
gráfica_mej_jug_2019 = la_liga_2019.sort_values(by="value", ascending=False)
gráfica_mej_jug_2019 = gráfica_mej_jug_2019.head(3)
equipos = df.groupby("squad").sum().reset_index()

x1 = equipos["fouls"]
y1 = equipos["Pts"]
coefficients1 = np.polyfit(x1, y1, 1)
line_x1 = np.array([x1.min(), x1.max()])
line_y1 = coefficients1[0] * line_x1 + coefficients1[1]


x3 = equipos["passes completed"]
y3 = equipos["Pts"]
coefficients3 = np.polyfit(x3, y3, 1)
line_x3 = np.array([x3.min(), x3.max()])
line_y3 = coefficients3[0] * line_x3 + coefficients3[1]


x4 = equipos["pressures"]
y4 = equipos["Pts"]
coefficients4 = np.polyfit(x4, y4, 1)
line_x4 = np.array([x4.min(), x4.max()])
line_y4 = coefficients4[0] * line_x4 + coefficients4[1]

x5 = equipos["value"]
y5 = equipos["Pts"]
coefficients5 = np.polyfit(x5, y5, 1)
line_x5 = np.array([x5.min(), x5.max()])
line_y5 = coefficients5[0] * line_x5 + coefficients5[1]


with st.sidebar:
    st.write("5 grandes ligas europeas:")
with st.sidebar:
    st.write("La Liga  (España)")
    st.write("Premier League (Inglaterra)")
    st.write("Serie A (Italia)")
    st.write("Bundesliga (Alemania)")
    st.write("Ligue 1 (Francia)")


st.title("¿Dónde hay mejores jugadores?")
if st.button("Valor ligas"):
    valor_liga = df.groupby("league").sum().reset_index()
    valor_liga= valor_liga.sort_values(by="value",ascending=False)

    valorligas = px.bar(valor_liga, x="league", y="value", color="value")
    valorligas.update_layout(title=dict(text="Valor de cada liga", x=0.5, xanchor="center"))
    st.plotly_chart(valorligas)




    valor_ligas = df.groupby("squad").sum().reset_index()
    valor_ligas= valor_ligas.sort_values(by="value",ascending=False)
    valor_ligas=valor_ligas.head(10)

    equipos= px.bar(valor_ligas, x="squad", y="value", color="value")
    equipos.update_layout(title=dict(text="Top 10 clubes", x=0.5, xanchor="center"))
    st.plotly_chart(equipos)


    st.title("¿Dónde están ubicados?")
    html = open("map.html", "r", encoding='utf-8').read()
    st.components.v1.html(html,height=500)


    st.title("DIFERENCIA ENTRE PLANTILLAS")

    col1, col2 = st.columns(2)


    value_counts = la_liga_2019["value"]
    fig1 = go.Figure(data=[go.Pie(labels=la_liga["squad"], values=value_counts,hovertext=value_counts.index)])
    fig1.update_layout(title_text= "LA LIGA",width=350, height=340)

    with col1:
        st.plotly_chart(fig1)


    df_2019 = df[df["Season"]=="01/01/2019"]
    premier_2019=df_2019[df["league"] == "Premier League"]
    values = premier_2019["value"]
    fig2 = go.Figure(data=[go.Pie(labels=premier_2019["squad"], values=values,hovertext=value_counts.index)])
    fig2.update_layout(title_text= "PREMIER LEAGUE",width=350, height=340)
    
    with col2:
        st.plotly_chart(fig2)


    

st.title("¿Dónde se marcan más goles?")
if st.button("Goles"):
    goles_ligas = df.groupby("league").sum().reset_index()
    goles_ligas= goles_ligas.sort_values(by="goals",ascending=False)
    fig = px.bar(goles_ligas, x="league", y="goals", color="goals",color_continuous_scale=px.colors.sequential.Reds)
    fig.update_layout(title=dict(text="goles marcados", x=0.5, xanchor="center"))
    st.plotly_chart(fig)


st.title("¿Dónde se interrumpe más el juego?")
if st.button("Interrupciones"):
    col1, col2 = st.columns(2)
    
    faltas_ligas = df.groupby("league").sum().reset_index()
    faltas_ligas= faltas_ligas.sort_values(by="fouls",ascending=False)
    fig = px.bar(faltas_ligas, x="league", y="fouls", color="fouls",width=450, height=400,color_continuous_scale=px.colors.sequential.YlGnBu_r)
    fig.update_layout(title=dict(text="faltas cometidas", x=0.5, xanchor="center"))
    
    with col1:
        st.plotly_chart(fig)

    tarjetas_ligas = df.groupby("cards yellow").sum().reset_index()
    tarjetas_ligas= faltas_ligas.sort_values(by="cards yellow",ascending=False)
    fig = px.bar(tarjetas_ligas, x="league", y="cards yellow", color="cards yellow",width=450, height=400,color_continuous_scale=px.colors.sequential.YlGnBu_r)
    fig.update_layout(title=dict(text="tarjetas amarillas", x=0.5, xanchor="center"))

    with col2:
        st.plotly_chart(fig)





st.title("¿Cuál es la mejor forma de competir?")
if st.button("Veámoslo"):
    
    graf1 = go.Figure()
    graf1.add_trace(go.Scatter(x=line_x3, y=line_y3, mode="lines", name= "Regresión lineal"))
    graf1.add_trace(go.Scatter(x=equipos["passes completed"], y=equipos["Pts"], mode="markers",marker=dict(color="red"),text=equipos["squad"]))
    graf1.update_layout(title="Pases Completados|Puntos",
                  xaxis_title="Pases completados",
                  yaxis_title="Puntos",
                  xaxis=dict(showticklabels=False),
                  yaxis=dict(showticklabels=False))

    graf2 = go.Figure()
    graf2.add_trace(go.Scatter(x=line_x1, y=line_y1, mode="lines", name= "Regresión lineal"))
    graf2.add_trace(go.Scatter(x=equipos["fouls"], y=equipos["Pts"], mode="markers",marker=dict(color="yellow"),text=equipos["squad"]))
    graf2.update_layout(title="Faltas|Puntos",
                  xaxis_title="Faltas",
                  yaxis_title="Puntos",
                  xaxis=dict(showticklabels=False),
                  yaxis=dict(showticklabels=False))

    
    st.plotly_chart(graf1)
    st.plotly_chart(graf2)

    




    graf4 = go.Figure()
    graf4.add_trace(go.Scatter(x=line_x5, y=line_y5, mode="lines", name= "Regresión lineal"))
    graf4.add_trace(go.Scatter(x=equipos["value"], y=equipos["Pts"], mode="markers",marker=dict(color="green"),text=equipos["squad"]))
    graf4.update_layout(title="Valor de la plantilla|Puntos",
                  xaxis_title="Valor",
                  yaxis_title="Puntos",
                  xaxis=dict(showticklabels=False),
                  yaxis=dict(showticklabels=False))

    
    
    st.plotly_chart(graf4)
