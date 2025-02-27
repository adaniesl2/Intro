import streamlit as st
from PIL import Image

st.title("Buenas")

st.header("En este espacio comienzo a desarrollar mis aplicaciones para interfaces multimodales")
st.write("Este es mi Pokémon favorito")
image = Image.open('Flygon.jpg')

st.image(image, caption = 'Flygon')

text = st.text_input('Cuál es tu favorito?', 'Mi pokémon favorito es...')
st.write(text+'?', 'Que buen gusto.')

st.subheader(' ')
