import streamlit as st

def infiltration_test():
    st.header("Prueba de Infiltración")

    # Create tabs for the different sections
    tab1, tab2, tab3 = st.tabs(["Objetivo", "Materiales", "Procedimiento"])

    with tab1:
        st.write("### Objetivo")
        st.write("""
        ¡Bienvenidos a nuestra aventura científica! En esta prueba, vamos a descubrir cómo el riego afecta la cantidad de agua en el suelo. 
        Aprenderemos cómo el agua se mueve en la tierra y cómo esto puede ayudar a que nuestras plantas crezcan sanas. 
        Al final, podremos ver cómo la planta bien regada se siente más feliz que la planta estresada.
        """)

    with tab2:
        st.write("### Materiales")
        st.write("""
        Para nuestra prueba, necesitaremos:
        - **Dos plantas**: una bien regada (sana) y otra que no ha recibido suficiente agua (estresada).
        - **Sensores de humedad del suelo**: estos nos ayudarán a medir cuánta agua hay en la tierra.
        - **Arduino**: una pequeña computadora que nos ayudará a registrar los datos que recogemos.
        """)

    with tab3:
        st.write("### Procedimiento")
        st.write("""
        ¡Ahora, pongámonos manos a la obra! Sigue estos pasos:
        1. **Coloca los sensores** de humedad en el suelo donde están las plantas. Asegúrate de que estén bien enterrados.
        2. **Riega la planta sana** con suficiente agua y observa cómo cambia la tierra alrededor de ella.
        3. **Registra los cambios en la humedad del suelo** a lo largo del tiempo usando el Arduino. ¡Recuerda que es como un diario de agua!
        4. **Analiza los resultados**: ¿Cómo cambia la cantidad de agua en el suelo? ¿Cuánto tiempo tarda en absorber el agua y cómo afecta a la planta? 
        Es divertido ver cómo el agua se mueve en la tierra y cómo nuestras plantas responden a ello.
        """)

        # Add irrigation image with reduced size (e.g., 300 pixels wide)
        st.image("irrigation.png", caption="Irrigación", width=300)

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
        - Aumento rápido en la humedad del suelo durante el riego.
        - Disminución gradual a medida que el agua se infiltra en capas más profundas.
        - Las plantas bien regadas se verán más saludables y felices.
        """)

# Call the function to display the test
st.empty()  # Clear previous content
infiltration_test()
