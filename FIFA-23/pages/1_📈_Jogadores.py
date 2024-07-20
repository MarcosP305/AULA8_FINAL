import streamlit as st
import pandas as pd
import plotly.express as px
import matplotlib.pyplot as plt
import numpy as np

st.set_page_config(layout="wide", page_title="Jogadores", page_icon="📈")

df = pd.read_csv('fifa23.csv', sep=",", decimal=",")

imagem = 'logolong.jpg'
imagem2 = 'logo.jpg'
imagem3 = 'wwc-23-homepage-hero-med-bg-7x2-xl-jpg.jpg.adapt.crop5x2.145.jpg'
imagem4 = 'fifa23-logo.svg'
imagem5 = 'dataset-thumbnail.jpg'
link = 'https://www.kaggle.com/datasets/bryanb/fifa-player-stats-database'
anime = 'jogadores.gif'
anime2 = 'FIFA_23.mp4'
video = 'https://youtu.be/o3V-GvvzjE4'

st.image(imagem)

st.sidebar.title("Filtros")

# Crida uma caixa de seleção para o clube
club1 = st.sidebar.selectbox("Selecione o Clube 1", df["Club"].unique())
club2 = st.sidebar.selectbox("Selecione o Clube 2", df["Club"].unique())

# Filtrar dados com base no clube escolhido
df_filtered_club1 = df[df["Club"] == club1]
df_filtered_club2 = df[df["Club"] == club2]

# Caixas de seleção para os jogadores
player1 = st.sidebar.selectbox("Selecione o Jogador 1", df_filtered_club1["Name"].unique())
player2 = st.sidebar.selectbox("Selecione o Jogador 2", df_filtered_club2["Name"].unique())

# Filtrar novamente com base no jogador escolhido
df_filtered_player1 = df_filtered_club1[df_filtered_club1["Name"] == player1]
df_filtered_player2 = df_filtered_club2[df_filtered_club2["Name"] == player2]

# Definição das colunas / Layout.
col1, col2, col3, col4 = st.columns(4)
col5, col6, col7 = st.columns(3) 

# Crie um DataFrame com as estatísticas médias
stats_columns = ["Overall", "Potential", "Age"]
# stats_columns1 = ["Overall", "Potential", "Age"]
stats_data = {
    "Statistic": stats_columns,
    # "Statistic1": stats_columns,
    "Player 1": df_filtered_player1[stats_columns].mean(),
    "Player 2": df_filtered_player2[stats_columns].mean(),
}
df_stats = pd.DataFrame(stats_data)

# Crie o gráfico
# fig = px.bar(df_stats, y="Statistic", x=["Player 1", "Player 2"], title="Comparativo")
fig = px.bar(df_stats, x="Statistic", y=["Player 1", "Player 2"], title="")
# st.plotly_chart(fig)

#----
# #Passos para elaboração do 4º Gráfico!
# fig_kind = px.pie(df_filtered_player1, values="Overall", names="Overall",
#                    title="Faturamento por tipo de pagamento")
# with col4:
#     st.plotly_chart(fig_kind, use_container_width=True)

with col1:
    st.title("Clube")
    st.subheader(df_filtered_player1["Club"].values[0])
    st.image(df_filtered_player1["Club Logo"].values[0])            
    st.write('Altura: ', df_filtered_player1["Height"].values[0]) 
    st.write('Peso: ', df_filtered_player1["Weight"].values[0]) 
    st.write('Contrato: ', df_filtered_player1["Contract Valid Until"].values[0])


with col2:
    st.title("Player 1")
    st.image(df_filtered_player1["Photo"].values[0]) # Exibe a imagem do jogador 1
    st.write(df_filtered_player1["Name"].values[0]) 
    st.write(df_filtered_player1["Nationality"].values[0])
    st.image(df_filtered_player1["Flag"].values[0])            
    st.write('Idade: ', df_filtered_player1["Age"].values[0]) 
    st.write('Salário: ', df_filtered_player1["Wage"].values[0]) 
    st.write('Cláusula de Liberação: ', df_filtered_player1["Release Clause"].values[0])

with col3:
    st.title("Player 2")
    st.image(df_filtered_player2["Photo"].values[0]) 
    st.write(df_filtered_player2["Name"].values[0]) 
    st.write(df_filtered_player2["Nationality"].values[0]) 
    st.image(df_filtered_player2["Flag"].values[0])          
    st.write('Idade: ', df_filtered_player2["Age"].values[0]) 
    st.write('Salário: ', df_filtered_player2["Wage"].values[0]) 
    st.write('Cláusula de Liberação: ', df_filtered_player2["Release Clause"].values[0])    

with col4:
    st.title("Clube")
    st.subheader(df_filtered_player2["Club"].values[0])
    st.image(df_filtered_player2["Club Logo"].values[0])           
    st.write('Altura: ', df_filtered_player2["Height"].values[0]) 
    st.write('Peso: ', df_filtered_player2["Weight"].values[0]) 
    st.write('Contrato: ', df_filtered_player2["Contract Valid Until"].values[0])   

# with col5:    
    # st.header("abilidades")
st.header('Comparativo :blue[Habilidades]', divider='rainbow')
st.subheader(':blue[Player 1 x Player 2]')
 
st.plotly_chart(fig)
