import streamlit as st
import requests
from PIL import Image
from io import BytesIO

# Cabeçalho
st.image("logo.png", width=800)  # Substitua pelo logo da loja
st.title("Bem-vindo a Casa de ração família animal!")

st.header("🐶 Tudo para seu pet em um só lugar!")

# Carregar imagem da internet corretamente
url_imagem = "https://img.irroba.com.br/filters:fill(fff):quality(80)/kreative/catalog/pizzaria/petshop/banner-petshop-30x100-kradesivos-mod-1-bps7-02.JPG"
response = requests.get(url_imagem)

if response.status_code == 200:
    img = Image.open(BytesIO(response.content))
    img_resized = img.resize((500, 300))  # Ajustar tamanho
    st.image(img_resized, use_container_width=False)
else:
    st.error("Erro ao carregar a imagem promocional.")

st.write("Temos produtos para pets, animais de fazenda e muito mais!")
