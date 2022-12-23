import streamlit as st

from PIL import Image
import numpy as np
import pandas as pd
st.set_page_config(
    page_title="Calamardo / MACHINE LEARNING",)
logo = Image.open('imagenes panda/Logo')
with st.sidebar:
        st.image(logo)
st.markdown("# - Formulario de Google (Preguntas):")
st.markdown("https://docs.google.com/forms/d/e/1FAIpQLSehtEDAXbt4R-3dtWXF_jaUbclcAFjthWnrfRS_Jj2y1hyemg/viewform")
st.markdown("# - Formulario de Google (Imagenes):")
img3 = Image.open('imagenes panda/encuesta')
st.image(img3, width=700)
