import streamlit as st

from PIL import Image
import numpy as np
import pandas as pd
st.set_page_config(
    page_title="Calamardo / MACHINE LEARNING",)
logo = Image.open('imagenes panda/Logo')
with st.sidebar:
        st.image(logo)
st.markdown("# 3.1.- BASE DE DATOS:")
music = pd.read_csv('musica.csv')

music
music.shape
music.dtypes
music.isnull().sum()
musica1 = music.fillna(music.mean())
musica1

musica1.isnull().sum()
st.markdown("# 3.2- Correlación de Pearson  (Pandas)")
n = musica1[musica1.columns[1:]].to_numpy()
m = musica1[musica1.columns[0]].to_numpy()
z = pd.DataFrame(n).T


print(n)
print(m)
st.markdown("# -Trampuesta")
n.T
df = pd.DataFrame(n.T, columns = m)
df
m_corr_pandas = df.corr()
st.markdown("# -Correlacion de Pandas")
m_corr_pandas
