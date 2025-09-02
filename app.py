import pandas as pd
import plotly.graph_objects as go
import streamlit as st

# Configurar la página
st.set_page_config(page_title="Panel de anuncios de coches", layout="wide")

# Encabezado
st.header("Panel de anuncios de venta de coches")

# Cargar dataset
df = pd.read_csv("vehicles_us.csv")  # cambia el nombre si tu CSV es distinto

# Mostrar número de filas
st.write(f"Cantidad de registros: {len(df)}")

# Checkbox para mostrar histograma
if st.checkbox("Mostrar histograma"):
    fig = go.Figure(data=[go.Histogram(x=df['odometer'])])  # columna ejemplo: odometer
    fig.update_layout(title="Histograma del odómetro")
    st.plotly_chart(fig, use_container_width=True)

# Checkbox para mostrar gráfico de dispersión
if st.checkbox("Mostrar gráfico de dispersión"):
    fig2 = go.Figure(data=[go.Scatter(
        x=df['odometer'],      # eje X
        y=df['price'],         # eje Y
        mode='markers',
        marker=dict(opacity=0.5)
    )])
    fig2.update_layout(title="Dispersión: odómetro vs precio", xaxis_title="odometer", yaxis_title="price")
    st.plotly_chart(fig2, use_container_width=True)
