import streamlit as st

from PIL import Image
st.set_page_config(
    page_title="Calamardo / MACHINE LEARNING",)
logo = Image.open('imagenes panda/Logo')
with st.sidebar:
    st.image(logo)
st.title("INVESTIGACIÓN FORMATIVA")
st.header(" PROYECTO/APLICACION EN IA")
st.markdown("# Grupo 1")
st.markdown("## Integrantes:")
st.markdown("Patrick Huaccharaqui Coila")
st.markdown("Alejandro Camargo Calatayud")
st.markdown("Alberth Chagua Acero")
st.markdown("Dilcia Quispe Checa")
st.markdown("Diego Banda Gutierrez")
st.markdown("Franklin Ramos Rodrigo")
