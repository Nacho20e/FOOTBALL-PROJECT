#-----------------------------LIBRERIAS-----------------------------
import streamlit as st
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns
import plotly_express as px
from streamlit_option_menu import option_menu
import base64

#-----------------CONFIGURACION DE PAGINA--------------------------
st.set_page_config(page_title="" , layout="centered", page_icon="")

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


#----------------------COSAS QUE PODEMOS USAR EN TODA NUESTRA APP -------------------
df=pd.read_csv("LIGAS\Output.csv", sep=",")
df_2018 = df[df["Season"]=="01/01/2018"]
#----------------------EMPIEZA NUESTRA APP------------------------------------------
st.title("BASE DE DATOS 18/19")



selected_value = st.sidebar.selectbox("LIGA",df_2018["league"].unique())
filtered_data = df_2018[df_2018["league"] == selected_value]
st.header("Filtrado por liga")
st.write(filtered_data)


selected_value = st.sidebar.selectbox("EQUIPO",df_2018["squad"].unique())
filtered_data = df_2018[df_2018["squad"] == selected_value]
st.header("Filtrado por equipo")
st.write(filtered_data)


selected_value = st.sidebar.selectbox("NACIONALIDAD",df_2018["nationality"].unique())
filtered_data = df_2018[df_2018["nationality"] == selected_value]
st.header("Filtrado por nacionalidad")
st.write(filtered_data)