import streamlit as st
import serial
import time
from infiltration_test import infiltration_test
from transpiration_test import transpiration_test
from monitoreo_en_tiempo_real import mostrar_monitoreo_en_tiempo_real
from proyecto import descripcion_proyecto

# Add header image
st.sidebar.image("semana_ciencia_header.png", use_column_width=True)

# Title and event details
st.title("Midiendo el Estrés Hídrico de las Plantas 🌿🔍")
st.subheader("Semana de la Ciencia 2024")

# Button to return to project description
if st.sidebar.button("Volver a la Descripción del Proyecto"):
    st.empty()  # Clear previous content
    descripcion_proyecto()  # Call the project description function

def main():
    # Button to display real-time monitoring with a green color using HTML
    if st.sidebar.button("Mostrar Monitoreo en Tiempo Real", key="show_real_time"):
        mostrar_monitoreo_en_tiempo_real()  # Call the real-time monitoring function

    # Sidebar radio selection without a default option
    tab = st.sidebar.radio("Selecciona la Prueba", 
                            ["Prueba de Infiltración", "Prueba de Transpiración"],
                            index=None)
    # Only display content based on selected tab
    if tab:
        if tab == "Prueba de Infiltración":
            infiltration_test()      # Function to display infiltration test content
        elif tab == "Prueba de Transpiración":
            transpiration_test()     # Function to display transpiration test content


# Call the main function to run the app
if __name__ == "__main__":
    main()
    descripcion_proyecto()
    
# Sidebar logo
st.sidebar.image("Logo_CSIC-ICA_100cm_blanco-stroke-and-fill.svg", width=100)

# Sidebar navigation
st.sidebar.subheader("Grupo TECH4Agro del ICA-CSIC")
st.sidebar.write("**Fecha**: 7 Noviembre 2024 📅")
st.sidebar.write("**Ubicación**: Madrid, España 🇪🇸")
st.sidebar.write("**Colaboradores**: Benjamin Mary")

# Add reproducibility section
st.sidebar.subheader("Proyecto Reproducible")
st.sidebar.write("Este proyecto es reproducible. Los datos y códigos están disponibles de forma gratuita en GitLab.")
if st.sidebar.button("Visitar GitLab"):
    st.markdown("[GitLab - Proyecto Reproducible](https://gitlab.com/cscic/your_project_link)")  # Replace with your actual GitLab link
