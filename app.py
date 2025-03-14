import streamlit as st
import serial
import time
from infiltration_test import infiltration_test
from transpiration_test import transpiration_test
from monitoreo_en_tiempo_real import mostrar_monitoreo_en_tiempo_real
from proyecto import descripcion_proyecto


st.title("Midiendo el Estrés Hídrico de las Plantas 🌿🔍")
st.subheader("Semana de la Ciencia 2024")


# Button to return to project description
if st.sidebar.button("Volver a la Descripción del Proyecto"):
    st.empty()  # Clear previous content
    descripcion_proyecto()  # Call the project description function
    st.empty()  # Clear previous content

def main():
    # Title and event details (Only in app.py)
    st.title("Midiendo el Estrés Hídrico de las Plantas 🌿🔍")
    st.subheader("Semana de la Ciencia 2024")

    # Button to display real-time monitoring
    if st.sidebar.button("Mostrar Monitoreo en Tiempo Real", key="show_real_time"):
        st.empty()  # Clear previous content
        mostrar_monitoreo_en_tiempo_real()  # Call the real-time monitoring function

    # Sidebar radio selection without a default option
    st.session_state.prueba = st.sidebar.radio("Selecciona la Prueba",
                                                ["Prueba de Infiltración",
                                                "Prueba de Transpiración"],
                                                #index=None,
                                                on_change=show_prueba
                                                )
def show_prueba():
    st.write(st.session_state.prueba)
    st.empty()  # Clear previous content
    # Only display content based on selected tab
    if st.session_state.prueba == "Prueba de Infiltración":
        infiltration_test()      # Function to display infiltration test content
    elif st.session_state.prueba == "Prueba de Transpiración":
        transpiration_test()     # Function to display transpiration test content



# Call the main function to run the app
#if __name__ == "__main__":
    # Title and event details

main()
    #descripcion_proyecto()

# Add header image
st.sidebar.image("semana_ciencia_header.png", use_column_width=True)


# Sidebar logo
st.sidebar.image("Logo_CSIC-ICA_100cm_blanco-stroke-and-fill.svg", width=100)

    # Sidebar logo
    col1, col2 = st.sidebar.columns([0.45, 0.55], vertical_alignment="center")
    with col1:
        st.image("1-CSIC-Logotipo--SVG-Vectorial--COLOR--CSIC.svg",
                 use_column_width=True)
    with col2:
        st.image("Logo_CSIC-ICA_100cm_blanco-stroke-and-fill.svg", width=100)
    st.logo("LogoTech4Agro_primary.png")


    # Sidebar navigation
    st.sidebar.subheader("Grupo TECH4Agro del ICA-CSIC")
    st.sidebar.write("**Fecha**: 7 Noviembre 2024 📅")
    st.sidebar.write("**Ubicación**: Madrid, España 🇪🇸")
    st.sidebar.write("**Colaboradores**: Benjamin Mary, "
                     "Irene Borra Serrano, "
                     "Vicente Burchard Levine, "
                     "Gustavo Mesías Ruiz, "
                     "Héctor Nieto")

    # Add reproducibility section
    st.sidebar.subheader("Proyecto Reproducible")
    st.sidebar.write("Este proyecto es reproducible. "
                     "Los datos y códigos están disponibles de forma gratuita "
                     "en GitLab.")
    if st.sidebar.button("Visitar GitLab"):
        st.markdown(
            '<a href="https://git.csic.es/tech4agro/arduino_semanaciencia2024" '
            'target="_blank">GitLab - Proyecto Reproducible</a>',
            unsafe_allow_html=True)
