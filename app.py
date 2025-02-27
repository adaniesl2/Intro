import streamlit as st
from PIL import Image

st.title("Buenas")

st.header("En este espacio comienzo a desarrollar mis aplicaciones para interfaces multimodales")
st.write("Este es mi Pokémon favorito")
image = Image.open('Flygon.jpg')

st.image(image, caption = 'Flygon')

text = st.text_input('Escribe algo', 'Este es mi texto')
st.write('El texto escrito es', text)

st.subheader(' ')
