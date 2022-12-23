import streamlit as st

from PIL import Image
st.set_page_config(
    page_title="Calamardo / MACHINE LEARNING",)
logo = Image.open('imagenes panda/Logo')
with st.sidebar:
        st.image(logo)
st.markdown("# Referencias")
st.markdown("https://aprendeconalf.es/docencia/python/manual/numpy/")
st.markdown("https://profile.es/blog/pandas-python/")
st.markdown("https://www.genbeta.com/guia-de-inicio/que-es-markdown-para-que-sirve-y-como-usarlo")
st.markdown(".https://www.sdelsol.com/glosario/covarianza/#:~:text=La%20covarianza%20es%20el%20valor,cuesti%C3%B3n%20respecto%20de%20otras%20variables.")
st.markdown("https://www.sdelsol.com/glosario/varianza/#:~:text=La%20Varianza%20es%20una%20medida,entre%20el%20total%20de%20observaciones.")
st.markdown("https://www.zendesk.com.mx/blog/que-es-escala-de-likert/#:~:text=La%20escala%20de%20likert%20es,s%C3%AD%E2%80%9D%20o%20%E2%80%9Cno%E2%80%9D.")
st.markdown("https://aws.amazon.com/es/what-is/linear-regression/#:~:text=La%20regresi%C3%B3n%20lineal%20es%20una,independiente%20como%20una%20ecuaci%C3%B3n%20lineal.")
st.markdown("https://www.youtube.com/watch?v=bY7OIJvTMrE")
