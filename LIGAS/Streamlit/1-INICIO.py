#-----------------------------LIBRERIAS-----------------------------
import streamlit as st
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns
import plotly_express as px
from streamlit_option_menu import option_menu
import base64

#background-image: url("https://images.sports.gracenote.com/images/lib/basic/sport/football/competition/logo/300/67.png");
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

#background-image: url("https://assets.laliga.com/assets/logos/laliga-h/laliga-h-1200x1200.png"
#background-size: 1300px 700px;


#----------------------COSAS QUE PODEMOS USAR EN TODA NUESTRA APP -------------------
df=pd.read_csv("LIGAS\Output.csv", sep=",")
#----------------------EMPIEZA NUESTRA APP------------------------------------------
st.title("ANÁLISIS DE LA LIGA")
st.write("Top 5 ligas europeas | Temporadas 17/18, 18/19, 19/20")

st.write("BASE DE DATOS:", df)

#st.image("https://assets.laliga.com/assets/logos/laliga-v/laliga-v-1200x1200.png")




if st.button("MAPA DE CORRELACIONES"):
    corr = df.corr(method='pearson')
    cmap = sns.color_palette("coolwarm", as_cmap=True)
    center = 0
    mask=np.zeros_like(corr)
    mask[np.triu_indices_from(mask)]=True
    with sns.axes_style("white"):
        f, ax=plt.subplots(figsize=(18,10))
        ax=sns.heatmap(corr,mask=mask, vmax=1, cmap=cmap, center=center, square=True,fmt=".2f",annot_kws={"size": 35 / np.sqrt(len(corr.iloc[0:37,0:37]))},linewidths=1,cbar_kws={"shrink": 1})
        plt.xticks(rotation=45)
        ax.set_yticklabels(ax.get_yticklabels(), fontsize=12, rotation=0)
        ax.set_xticklabels(ax.get_xticklabels(), fontsize=12, rotation=90)
    st.pyplot(f)







    


