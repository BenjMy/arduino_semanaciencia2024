import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import time

def obtener_datos_sensor(sensor_number, num_readings=10):
    # Generate time values (e.g., 10 time steps)
    tiempo = pd.date_range(start="2024-10-01", periods=num_readings, freq="H")
    # Generate random soil moisture values for the selected sensor
    humedad_suelo = {
        f'Humedad del Suelo {sensor_number}': np.random.randint(0, 100, num_readings)
    }
    return tiempo, humedad_suelo

def mostrar_monitoreo_en_tiempo_real():
    st.header("Datos de Sensores en Tiempo Real")
    
    # Select sensor and plant number on the main page
    num_sensors = 4  # Number of sensors
    num_plants = 2   # Number of plants
    sensor_number = st.selectbox("Selecciona el Número de Sensor", 
                                  [f'Sensor {i + 1}' for i in range(num_sensors)])
    plant_number = st.selectbox("Selecciona el Número de Planta", 
                                 [f'Planta {i + 1}' for i in range(num_plants)])
    
    # Button to pause or resume the plot
    pause_button = st.button("Pausar/Continuar")

    # Number of readings to simulate
    num_readings = 10  
    max_readings = 50  # Max readings to display in the plot
    humedad_suelo_data = {f'Humedad del Suelo {sensor_number[-1]}': []}

    # Create a placeholder for the plot
    placeholder = st.empty()
    
    # Live update loop
    is_paused = False  # Track the pause state
    while True:
        if pause_button:
            is_paused = not is_paused  # Toggle pause state
            pause_button = st.button("Pausar/Continuar")  # Recreate button to get new state

        if not is_paused:
            tiempo, datos_sensor = obtener_datos_sensor(int(sensor_number[-1]), num_readings)
            humedad_suelo_data[f'Humedad del Suelo {sensor_number[-1]}'].extend(datos_sensor[f'Humedad del Suelo {sensor_number[-1]}'])

            # Limit to the last `max_readings`
            if len(humedad_suelo_data[f'Humedad del Suelo {sensor_number[-1]}']) > max_readings:
                humedad_suelo_data[f'Humedad del Suelo {sensor_number[-1]}'] = humedad_suelo_data[f'Humedad del Suelo {sensor_number[-1]}'][-max_readings:]

            # Create DataFrame for plotting
            df = pd.DataFrame(humedad_suelo_data)
            df.index = pd.date_range(start="2024-10-01", periods=len(df), freq="H")

            # Plotting
            plt.figure(figsize=(10, 5))
            plt.plot(df.index, df[f'Humedad del Suelo {sensor_number[-1]}'], marker='o', label=f'Humedad del Suelo {sensor_number[-1]}')
            
            plt.ylabel("Valores de Humedad (%)")
            plt.title(f"Evolución de la Humedad del Suelo en el Tiempo - {plant_number}")
            plt.ylim(0, 100)  # Limiting y-axis between 0 and 100%
            plt.legend()  # Show legend for the sensors
            plt.grid()

            # Display the plot in Streamlit
            placeholder.pyplot(plt)
        
        # Pause for a moment before the next update
        time.sleep(2)  # Update every 2 seconds

# Call the function to run the app
if __name__ == "__main__":
    mostrar_monitoreo_en_tiempo_real()
