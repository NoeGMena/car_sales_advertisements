import streamlit as st
import pandas as pd
import plotly_express as px

car_data = pd.read_csv("C:/Users/noego/Documents/TripleTen/Sprint_5/Proyecto_de_sprint/car_sales_advertisements/vehicles_us.csv") # leer los datos

st.header("Venta de carros")

hist_button = st.button('Construir Histograma')

if hist_button:
    st.write('Creación de un histograma para el conjunto de datos de anuncios de venta de coches')

    #Creación del histograma
    fig = px.historgam(car_data, x="odometer")

    # mostrar un gráfico Plotly interactivo
    st.plotly_chart(fig, use_container_width=True)


# crear una casilla de verificación
build_histogram = st.checkbox('Construir un histograma')

if build_histogram: # si la casilla de verificación está seleccionada
    st.write('Construir un histograma para la columna odómetro')
    fig_check=px.historgam(car_data, x="odometer")
    # mostrar un gráfico Plotly interactivo
    st.plotly_chart(fig, use_container_width=True)
