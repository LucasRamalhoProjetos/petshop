import streamlit as st
from PIL import Image
import requests
from io import BytesIO

# Configuração da página
st.set_page_config(page_title="PetShop Agro", layout="wide")

# Cabeçalho
st.image("logo.png", width=800)  # Substitua pelo logo da loja
st.title("Bem-vindo ao PetShop Agro!")

# Menu Principal
opcao = st.sidebar.radio("Menu", ["Início", "Produtos", "Serviços", "Contato"])

if opcao == "Início":
    st.header("🐶 Seu PetShop e Agropecuária de Confiança! 🌾")

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

elif opcao == "Produtos":
    st.subheader("🛍️ Nossos Produtos")
    st.write("Ração, brinquedos, acessórios e produtos agropecuários.")

elif opcao == "Serviços":
    st.subheader("🛠️ Nossos Serviços")
    st.write("Banho, tosa, consultas veterinárias e muito mais!")

elif opcao == "Contato":
    st.subheader("📞 Entre em Contato")
    st.write("Telefone: (XX) XXXX-XXXX")
    st.write("Endereço: Rua Tal, Nº 123")
    st.write("WhatsApp: [Clique Aqui](https://wa.me/seu_numero)")

# Rodapé
st.markdown("---")
st.write("📍 **PetShop Agro - Cuidando do seu pet e da sua fazenda!**")
