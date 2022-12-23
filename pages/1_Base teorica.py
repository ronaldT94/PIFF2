import streamlit as st

from PIL import Image
st.set_page_config(
    page_title="Calamardo / MACHINE LEARNING",)
logo = Image.open('imagenes panda/Logo')
with st.sidebar:
        st.image(logo)
st.title("Base teorica")
st.markdown("#### - Análisis de Correlación")
st.markdown("El análisis de correlación es el primer paso para construir modelos explicativos y predictivos más complejos.A menudo nos interesa observar y medir la relación entre 2 variables numéricas mediante el análisis de correlación.Se trata de una de las técnicas más habituales en análisis de datos y el primer paso necesario antes de construir cualquier modelo explicativo o predictivo más complejo. Para poder tener el  Datset hay que recolectar información a travez de encuentas")
st.markdown("#### -  ¿Qué es la correlación?")
st.markdown("La correlación es un tipo de asociación entre dos variables numéricas, específicamente evalúa la tendencia (creciente o decreciente) en los datos.Dos variables están asociadas cuando una variable nos da información acerca de la otra. Por el contrario, cuando no existe asociación, el aumento o disminución de una variable no nos dice nada sobre el comportamiento de la otra variable.Dos variables se correlacionan cuando muestran una tendencia creciente o decreciente.")
st.markdown("#### - ¿Cómo se mide la correlación?")
st.markdown("Tenemos el coeficiente de correlación lineal de Pearson que se sirve para cuantificar tendencias lineales, y el coeficiente de correlación de Spearman que se utiliza para tendencias de aumento o disminución, no necesariamente lineales pero sí monótonas. ")
st.markdown("#### - Correlación de Pearson")
st.markdown("El coeficiente de correlación lineal de Pearson mide una tendencia lineal entre dos variables numéricas.Es el método de correlación más utilizado, pero asume que:")
st.markdown("- La tendencia debe ser de tipo lineal.")
st.markdown("- No existen valores atípicos (outliers)")
st.markdown("- Las variables deben ser numéricas.")
st.markdown("- Tenemos suficientes datos (algunos autores recomiendan tener más de 30 puntos u observaciones).")
st.markdown("Los dos primeros supuestos se pueden evaluar simplemente con un diagrama de dispersión, mientras que para los últimos basta con mirar los datos y evaluar el diseño que tenemos.")
st.markdown("#### - Cómo se interpreta la correlación")
st.markdown("El signo nos indica la dirección de la relación, como hemos visto en el diagrama de dispersión.")
st.markdown("- Un valor positivo indica una relación directa o positiva")
st.markdown("- Un valor negativo indica relación indirecta, inversa o negativa")
st.markdown("- Un valor nulo indica que no existe una tendencia entre ambas variables (puede ocurrir que no exista relación o que la relación sea más compleja que una tendencia, por ejemplo, una relación en forma de U).")
st.markdown("La magnitud nos indica la fuerza de la relación, y toma valores entre −1 a 1. Cuanto más cercano sea el valor a los extremos del intervalo ($1$ o −1) más fuerte será la tendencia de las variables, o será menor la dispersión que existe en los puntos alrededor de dicha tendencia. Cuanto más cerca del cero esté el coeficiente de correlación, más débil será la tendencia, es decir, habrá más dispersión en la nube de puntos.")
st.markdown("- Si la correlación vale 1 o −1 diremos que la correlación es “perfecta”")
st.markdown("- Si la correlación vale 0 diremos que las variables no están correlacionadas.")
img3 = Image.open('imagenes panda/Correlacion')
st.image(img3, width=700)
st.markdown("#### - Fórmula Coeficiente de Correlación de Pearson")
st.markdown("$$ r(x,y)=\\frac{\\sum_{i=1}^{n}(x_{i}-\\overline{x})(y_{i}-\\overline{y})}{\\sqrt{\\sum_{i=1}^{n}(x_{i}-\\overline{x})^{2}}\\sqrt{\\sum_{i=1}^{n}(y_{i}-\\overline{y})^{2}}}$$.")
st.markdown("Regresión Lineal: La regresión lineal se usa para encontrar una relación lineal entre el objetivo y uno o más predictores.")
img3 = Image.open('imagenes panda/Regresion lineal')
st.image(img3, width=700)
st.markdown("#### - ¿Que es pandas?")
st.markdown("Pandas es una muy popular librería de código abierto dentro de los desarrolladores de Python, y sobre todo dentro del ámbito de Data Science y Machine Learning, ya que ofrece unas estructuras muy poderosas y flexibles que facilitan la manipulación y tratamiento de datos.Pandas surgió como necesidad de aunar en una única librería todo lo necesario para que un analista de datos pudiese tener en una misma herramienta todas las funcionalidades que necesitaba en su día a día, como son: cargar datos, modelar, analizar, manipular y prepararlos.")
img3 = Image.open('imagenes panda/pandas')
st.image(img3, width=700)
st.markdown("#### - ¿Que es numpy?")
st.markdown("NumPy es una librería de Python especializada en el cálculo numérico y el análisis de datos, especialmente para un gran volumen de datos.Incorpora una nueva clase de objetos llamados arrays que permite representar colecciones de datos de un mismo tipo en varias dimensiones, y funciones muy eficientes para su manipulación.La ventaja de Numpy frente a las listas predefinidas en Python es que el procesamiento de los arrays se realiza mucho más rápido (hasta 50 veces más) que las listas, lo cual la hace ideal para el procesamiento de vectores y matrices de grandes dimensiones.")
img3 = Image.open('imagenes panda/numpy')
st.image(img3, width=700)
st.markdown("# - ¿Que es la Covarianza?")
st.markdown("La covarianza es el valor a través del cual se refleja en qué cuantía don variables cualesquiera varían de forma conjunta respecto de sus medias aritméticas. Así, esta medida nos permite conocer cómo se comportan las variables en cuestión respecto de otras variables. Es decir, ¿qué hace la variable X cuando Y aumenta? ¿y cuándo Y disminuye? ¿y si Y se mantiene estable y constante?La covarianza puede adquirir valores negativos y positivos, y además puede adquirir valores iguales a 0. ¿Cómo se han de interpretar estos resultados? Veámoslo:")
st.markdown("1.- Cuando la covarianza es menor que 0: en este caso, hay una relación negativa, de forma que X e Y son dos variables inversamente proporcionales la una respecto de la otra. En palabras más sencillas: cuando la variable Y aumenta, la variable X disminuye.")
st.markdown("2.- Cuando la covarianza es mayor que 0: en este caso, hay una relación positiva, de forma que X e Y son dos variables directamente proporcionales la una respecto de la otra. En otras palabras más sencillas de entender: cuando la variable X aumenta, la variable Y también lo hace.")
st.markdown("3.- Cuando la covarianza adquiere un valor igual a 0: en este caso, la relación entre una variable y otra variable es inexistente, lo que quiere decir que la covarianza será igual que 0 independientemente de que cualquiera de las dos variables aumente o disminuya.")
st.markdown("# - PROPIEDADES QUE POSEE LA COVARIANZA")
st.markdown("A la hora de calcular la covarianza y de utilizar y trabajar con esta medida, es necesario tener en cuenta una serie de propiedades que nos harán más fácil su aplicación. Así, sus propiedades son las siguientes:")
st.markdown("1.- Cuando las dos variables cuya relación se calcula gracias a la covarianza están multiplicadas por dos constantes diferentes, ésta será igual a la covarianza de las dos variables multiplicada por la multiplicación de las dos constantes en cuestión. Sería de la siguiente manera à Cov (a x X, b x Y) = a x b x Cov (X, Y)")
st.markdown("2.- La covarianza adquirirá el mismo valor independientemente del orden de las dos variables X e Y.")
st.markdown("3.- Cuando la covarianza adquiere un valor igual a 0, significa que una de las variables es una constante.")
st.markdown("4.- La covarianza de una variable, por ejemplo, X, y de sí misma, es igual a la varianza de la variable. Sería de la siguiente manera à Cov (X, X) = Var (X)")
st.markdown("5.- Cuando se suman dos constantes cualesquiera a cada una de las variables X e Y, no se verá afectada la covarianza. Así à Cov (a + X, b + Y) = Cov (X, Y)")
st.markdown("6.- La covarianza es una medida igual a la esperanza de la multiplicación de las dos variables X e Y menos el producto de las dos esperanzas por separado. Quedaría de la siguiente manera à Cov (X, Y) = E(X x Y) – E(X) x (E(Y).")
st.markdown("Es importante tener en cuenta todas estas propiedades a la hora de calcular la covarianza")
