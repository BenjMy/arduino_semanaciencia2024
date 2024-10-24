import streamlit as st

def transpiration_test():
    st.header("Prueba de Transpiración")

    # Create tabs for the different sections
    tab1, tab2, tab3 = st.tabs(["Objetivo", "Materiales", "Procedimiento"])

    with tab1:
        st.write("### Objetivo")
        st.write("""
        En esta prueba, vamos a investigar cómo las plantas "respiran" a través de un proceso llamado transpiración. 
        """)

    with tab2:
        st.write("### Materiales")
        st.write("""
        Para nuestra emocionante aventura, necesitaremos:
        - **Dos plantas**: una que ha recibido mucho agua (bien regada) y otra que no ha recibido suficiente (estresada).
        - **Cámara térmica**: esta herramienta nos permitirá ver cómo están de calientes las hojas de las plantas y cuánto agua están perdiendo.
        """)

    with tab3:
        st.write("### Procedimiento")
        st.write("""
        ¡Listos para comenzar! Sigue estos pasos:
        3. **Usa la cámara térmica** para ver la temperatura de las hojas. ¿Están calientes? Eso puede significar que están perdiendo agua.
        4. **Compara los resultados**: Observa cómo la transpiración de las plantas afecta la temperatura de las hojas!
        """)

        # Add ET thermal image with reduced size (e.g., 300 pixels wide)
        st.image("ET_thermal_leaves_test.png", caption="Imagen térmica que muestra las diferencias de evapotranspiración en las hojas de las plantas.", width=300)

    # Initialize session state for showing results
    if 'show_results' not in st.session_state:
        st.session_state.show_results = False

    # Button to toggle expected results visibility
    button_color = "#FF4B4B"  # Custom color for the button
    if st.button("Descubrir/Ocultar Resultados Esperados", key='b_transpiration'):
        st.session_state.show_results = not st.session_state.show_results

    # Show expected results if the state is True
    if st.session_state.show_results:
        st.write("""
        **Resultados Esperados**:
        - Las hojas de la planta estresada estarán más calientes, lo que indica que está transpirando menos agua.
        - Aprenderemos cómo las plantas utilizan el agua y cómo eso afecta su salud.
        """)

# Call the function to display the test
transpiration_test()
