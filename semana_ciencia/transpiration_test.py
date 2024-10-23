import streamlit as st

def transpiration_test():
    st.header("Prueba de Transpiración")

    # Create tabs for the different sections
    tab1, tab2, tab3 = st.tabs(["Objetivo", "Materiales", "Procedimiento"])

    with tab1:
        st.write("### Objetivo")
        st.write("Observar el efecto de la transpiración de las plantas en el contenido de humedad del suelo y la evapotranspiración (ET).")

    with tab2:
        st.write("### Materiales")
        st.write("""
        - Dos plantas (una bien regada, una estresada)
        - Sensores de humedad del suelo (TDR, capacitivo)
        - Cámara térmica
        """)

    with tab3:
        st.write("### Procedimiento")
        st.write("""
        1. Colocar los sensores en ambas macetas con plantas bien regadas y estresadas.
        2. Monitorear la diferencia en el contenido de humedad del suelo (SMC) a lo largo del tiempo utilizando Arduino.
        3. Usar la cámara térmica para monitorear la temperatura de las hojas y las tasas de transpiración.
        4. Comparar el efecto de la transpiración de las plantas en el SMC y ET entre las dos plantas.
        """)

        # Add ET thermal image with reduced size (e.g., 300 pixels wide)
        st.image("ET_thermal_leaves_test.webp", caption="Imagen térmica que muestra las diferencias de evapotranspiración en las hojas de las plantas.", width=300)

    # Initialize session state for showing results
    if 'show_results' not in st.session_state:
        st.session_state.show_results = False

    # Button to toggle expected results visibility
    button_color = "#FF4B4B"  # Custom color for the button
    if st.button("Descubrir/Ocultar Resultados Esperados"):
        st.session_state.show_results = not st.session_state.show_results

    # Show expected results if the state is True
    if st.session_state.show_results:
        st.write("""
        **Resultados Esperados**:
        - Menor SMC y mayor ET en la planta bien regada.
        - Temperaturas de hojas más altas en la planta estresada, indicando menos transpiración.
        """)



# Call the function to display the test
transpiration_test()
