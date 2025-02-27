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
  st.write('Cuál es el mejor tipo para counter a Flygon?')
  answer = st.checkbox('Ice')
  answer2 = st.checkbox('Dragon')
  if answer:
    st.write('Correcto!')
  if answer2:
    st.write('Incorrecto!')

with col2: 
  st.subheader('Esta es la segunda columna')
  modo = st.radio('Cuál es tu tipo de pokémon favorito?', ('Electric', 'Dragon', 'Ground'))
  if modo == 'Electric':
    st.write('Cuídate de los tipo Ground.')
  if modo == 'Dragon':
    st.write('Cuidado con los tipo Ice, Dragon y Fairy.')
  if modo == 'Ground':
    st.write('Cuidado con los tipo Water, Grass o Ice.')

st.subheader('Uso de botones')
if st.button('Presiona el botón):
   st.write('Gracias por presionar')
else:
   st.write('No has presionado el botón')
