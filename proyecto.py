import streamlit as st

def descripcion_proyecto():
	st.empty()  # Clear previous content
	st.header("Descripción del Proyecto 📊")
	st.write("""
	Este proyecto muestra cómo se puede medir el estrés hídrico de las plantas en tiempo real usando sensores como TDR y sensores de humedad del suelo. 
	- **Sensor de Humedad del Suelo**: Mide la cantidad de agua en el suelo. 🌱
	- **Cámara Térmica**: Mide diferencias de temperatura para detectar estrés hídrico. 🌡️
	""")

	# Nueva sección para explicar que los niños liderarán el experimento
	st.header("¡Tú Serás el Científico! 👩‍🔬👨‍🔬")
	st.write("""
	¡Tú liderarás el experimento! Aquí hay algunas preguntas que podrás responder:
	1. ¿Cómo de húmedo está el suelo de las plantas? 🌾
	2. ¿Cómo afecta el agua en el suelo a la temperatura de la planta? 🔥
	3. ¿Qué diferencias ves entre las plantas que tienen mucha y poca agua? 🤔
	""")

	# Agregar enlaces a las pruebas
	st.header("Selecciona un Experimento 🔍")
	st.write("Haz clic en uno de los siguientes enlaces para comenzar:")
	st.markdown("""
	- [Experimento de Infiltración 🌊](#prueba-de-infiltracion)
	- [Experimento de Transpiración 🌬️](#prueba-de-transpiracion)
	""") 

