import streamlit as st # Biblioteca de Dashboards.
import pandas as pd # Biblioteca de Manipulação de dados.
import plotly.express as px # Biblioteca de Grárficos.

imagem = 'logolong.jpg'
imagem2 = 'logo.jpg'
imagem3 = 'wwc-23-homepage-hero-med-bg-7x2-xl-jpg.jpg.adapt.crop5x2.145.jpg'
imagem4 = 'fifa23-logo.svg'
imagem5 = 'dataset-thumbnail.jpg'
link = 'https://www.kaggle.com/datasets/bryanb/fifa-player-stats-database'
anime = 'jogadores.gif'
anime2 = 'FIFA_23.mp4'
video = 'https://youtu.be/o3V-GvvzjE4'

st.set_page_config(layout="wide") #configurar wide
st.image(imagem)

# Layout de colunas
col1, col2 = st.columns(2)
col3 = st.columns(1)
col4, col5, col6 = st.columns(3)

# Agora você pode adicionar outros elementos, como texto
with col1:
    st.header('Base de dados baixada do :blue[Kaagle]', divider='rainbow')
    st.subheader('Objetivo Realizar analise de dados utilizando o :blue[PYTHON]'
    ' e outras bibliotecas como o :blue[Pandas], o :blue[Streamlit] entre outras.' )
    st.subheader('Link dos dados: ')
    st.subheader(link)


    # st.video(anime)
# Coluna central com a imagem

with col2:
    st.video(video)

