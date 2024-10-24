import streamlit as st
import requests
import time
import plotly.graph_objs as go
from collections import deque

def mostrar_monitoreo_en_tiempo_real():
    st.empty()  # Clear previous content

    # Real-time plotting setup
    sensor_data = deque(maxlen=100)
    time_data = deque(maxlen=100)
    start_time = time.time()
    
    # Plotting placeholder
    plot_placeholder = st.empty()

    while True:
        # Fetch data from the Tornado server
        try:
            response = requests.get('http://localhost:5000/data')  # Change to your Tornado server URL when deployed
            data = response.json()

            if 'value' in data:
                current_time = time.time() - start_time  # Time elapsed in seconds
                sensor_data.append(data['value'])
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
            else:
                st.error("Error fetching data: {}".format(data.get('error', 'Unknown error')))

        except Exception as e:
            st.error(f"Error fetching data: {e}")

        time.sleep(1)  # Adjust delay to match your data frequency

# Call the function to start monitoring
mostrar_monitoreo_en_tiempo_real()
