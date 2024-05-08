import streamlit as st
import pandas as pd
import plotly_express as px

car_data = pd.read_csv("vehicles_us.csv") # leer los datos

st.header("Venta de carros")

# crear una casilla de verificación
build_histogram = st.checkbox('Construir un histograma')
build_dispersion = st.checkbox('Construir un diagrama de dispersion')

if build_histogram: # si la casilla de verificación está seleccionada
    st.write('Histograma para la columna odómetro')
    fig_check=px.histogram(car_data, x="odometer")
    # mostrar un gráfico Plotly interactivo
    st.plotly_chart(fig_check, use_container_width=True)

if build_dispersion: # si la casilla de verificación está seleccionada
    st.write('Diagrama de dispersion: odómetro VS price')
    fig_check=px.scatter(car_data, x="odometer", y="price")
    # mostrar un gráfico Plotly interactivo
    st.plotly_chart(fig_check, use_container_width=True)
