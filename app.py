import streamlit as st
from PIL import Image

st.title("Buenas")

st.header("En este espacio comienzo a desarrollar mis aplicaciones para interfaces multimodales")
st.write("Este es mi Pokémon favorito")
image = Image.open('Flygon.jpg')

st.image(image, caption = 'Flygon')

text = st.text_input('Cuál es tu favorito?', 'Mi pokémon favorito es...')
st.write(text+'?', 'Que buen gusto.')

st.subheader('Ahora usemos 2 columnas')

col1, col2 = st.columns(2)

with col1: 
  st.subheader('Esta es la primera columna')
  st.write('Cuál es el peor tipo para counter a Flygon?')
  answer = st.checkbox('Hielo')
  answer2 = st.checkbox('Dragón')
  if answer:
    st.write('Correcto!')
  if answer2:
    st.write('Incorrecto!')

with col2: 
  st.subheader('Esta es la segunda columna')
  modo = st.radio('Qué es la modalidad principal en tu interfaz?', ('Visual', 'Auditiva', 'Táctil'))
  if modo == 'Visual':
    st.write('La vista es fundamental para tu interfaz')
  if modo == 'Auditiva':
    st.write('La audición es fundamental para tu interfaz')
  if modo == 'Táctil':
    st.write('El tacto es fundamental para tu interfaz')
