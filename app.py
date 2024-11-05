import pandas as pd
import plotly.express as px
import streamlit as st
        
car_data = pd.read_csv('vehicles_us.csv') # leer los datos
st.header('Análisis de datos de vehículos en EE.UU.')
hist_button = st.button('Construir histograma') # crear un botón
scatter_button = st.button('Construir gráfico de dispersión') ## Botón para construir un gráfico de dispersión
        
if hist_button: # al hacer clic en el botón
    st.write('Creación de un histograma para el conjunto de datos de anuncios de venta de coches') # escribir un mensaje
    fig = px.histogram(car_data, x="odometer", title='Distribución del odómetro')     # crear un histograma
    st.plotly_chart(fig, use_container_width=True) # mostrar un gráfico Plotly interactivo

#st.header('Lanzar una moneda') AGREGAR
#Esto se tiene que agregar depsues
#car_data = pd.read_csv('vehicles_us.csv') # leer los datos
#fig1 = px.scatter(car_data, x="odometer", y="price") # crear un gráfico de dispersión
#fig1.show() # crear gráfico de dispersión

if scatter_button:  # Al hacer clic en el botón
    st.write('Creación de un gráfico de dispersión entre el precio y el año del coche')
    fig = px.scatter(car_data, x="model_year", y="price", 
                     title='Gráfico de dispersión: Precio vs Año del Modelo', 
                     labels={'model_year': 'Año del Modelo', 'price': 'Precio (USD)'})
    st.plotly_chart(fig, use_container_width=True)
