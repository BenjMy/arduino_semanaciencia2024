import streamlit as st


def infiltration_test():
    st.header("Infiltration Test")

    # Create tabs for the different sections
    tab1, tab2, tab3 = st.tabs(["Objetivo", "Materiales", "Procedimiento"])

    with tab1:
        st.write("### Objetivo")
        st.write("To measure how irrigation affects soil moisture content.")

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
			    1. Insert soil moisture sensors into the test area.
			    2. Apply water to the soil.
			    3. Record soil moisture content (SMC) changes over time using Arduino.
			    4. Analyze how fast the soil absorbs water and how it affects SMC at different depths.
        """)

        # Add irrigation image with reduced size (e.g., 300 pixels wide)
        st.image("irrigation.png", caption="irrigation", width=300)

    # Initialize session state for showing results
    if 'show_results' not in st.session_state:
        st.session_state.show_results = False

    # Button to toggle expected results visibility
    button_color = "#FF4B4B"  # Custom color for the button
    if st.button("Descubrir/Ocultar Resultados Esperados", key='toggle_button'):
        st.session_state.show_results = not st.session_state.show_results

    # Show expected results if the state is True
    if st.session_state.show_results:
        st.write("""
        **Resultados Esperados**:
        -  Rapid increase in SMC during irrigation.
        - Gradual decrease as water infiltrates deeper layers.
        """)



# Call the function to display the test
infiltration_test()
