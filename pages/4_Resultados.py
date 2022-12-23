import streamlit as st

from PIL import Image
st.set_page_config(
    page_title="Calamardo / MACHINE LEARNING",)
logo = Image.open('imagenes panda/Logo')
with st.sidebar:
        st.image(logo)
st.markdown("# Resultados")
st.markdown("Los 2 mayores son:Dirección de correo electrónico")
st.markdown("dquispeche@unsa.edu.pe           suzymissa2010@gmail.com            0.773628")
st.markdown("dquispeche@unsa.edu.pe           andreacheca44@gmail.com            0.749020")
st.markdown("# Conclusiones")
st.markdown("- ¿Se valido o no los resultados? Si, se logro validar los resultados obtenidos usando algoritmos de correlaciones.")
st.markdown("- Los resultados Validados son:La compatibilidad mas alta entre 2 personas y el primer lugar fue del 100%.")
st.markdown("- ¿Es efectivo el metodo de correlación de pearson?")
st.markdown("SI, ya que logramos medir la relacion estadistica entra 2 valores continuas.")
st.markdown("- Correlación de Pearson y Regresión Lineal, ¿cual es su relación?")
st.markdown("De alguna manera se complementan, por ejemplo si en una variable (X,Y) existe una correlación fuerte entre las variables X e Y, el análisis de la regresión permite encontrar la ecuación de la función matemática que mejor se ajusta a la nube de puntos. Esta puede ser una recta, una parábola, una exponencial, una cúbica, etc.")
