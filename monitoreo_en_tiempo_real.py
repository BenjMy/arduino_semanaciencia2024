import streamlit as st
import requests
import plotly.graph_objs as go
from collections import deque
import time

def mostrar_monitoreo_en_tiempo_real():
    st.empty()  # Clear previous content

    # Real-time plotting setup
    sensor_data = deque(maxlen=100)
    time_data = deque(maxlen=100)
    start_time = time.time()

    # Plotting placeholder
    plot_placeholder = st.empty()

    while True:
        # Fetch data from the Flask server
        try:
            response = requests.get('http://localhost:5000/data')
            response.raise_for_status()  # Raise an error for bad responses
            data = response.json()
            if 'value' in data:
                sensor_value = data['value']
                current_time = time.time() - start_time  # Time elapsed in seconds
                sensor_data.append(sensor_value)
                time_data.append(current_time)

                # Create the plot
                fig = go.Figure()
                fig.add_trace(go.Scatter(x=list(time_data), y=list(sensor_data), mode='lines+markers', name='Sensor Value'))
                fig.update_layout(
                    title="Real-Time Sensor Data",
                    xaxis_title="Time (seconds)",
                    yaxis_title="Sensor Value",
                    xaxis_range=[max(0, current_time - 30), current_time],  # 30-second sliding window
                    yaxis_range=[min(sensor_data) - 5, max(sensor_data) + 5]
                )

                # Display the plot
                plot_placeholder.plotly_chart(fig, use_container_width=True)

        except Exception as e:
            st.error(f"Error fetching data: {e}")
        
        time.sleep(1)  # Adjust delay to match your data frequency
