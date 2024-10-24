import streamlit as st
import serial
import time
import plotly.graph_objs as go
from collections import deque

# Configure serial connection (adjust to your Arduino's port and baud rate)
SERIAL_PORT = '/dev/ttyACM0'  # Adjust for your device
BAUD_RATE = 9600

def mostrar_monitoreo_en_tiempo_real():
    st.empty()  # Clear previous content

    # Function to read data from Arduino
    def read_arduino_data(ser):
        if ser.in_waiting > 0:
            try:
                # Read line from Arduino, decode to string, and remove newline
                line = ser.readline().decode('utf-8').rstrip()
                return float(line)  # Convert to float for plotting
            except Exception as e:
                st.error(f"Error reading data: {e}")
        return None

    # Open serial connection
    try:
        ser = serial.Serial(SERIAL_PORT, BAUD_RATE, timeout=1)
        time.sleep(2)  # Wait for connection to be established
    except Exception as e:
        st.error(f"Could not open serial port: {e}")
        ser = None

    # Real-time plotting setup
    if ser:
        # Deque to store time series data for plotting (max length of 100 points)
        sensor_data = deque(maxlen=100)
        time_data = deque(maxlen=100)
        start_time = time.time()

        # Plotting placeholder
        plot_placeholder = st.empty()

        while True:
            data = read_arduino_data(ser)
            if data is not None:
                current_time = time.time() - start_time  # Time elapsed in seconds
                sensor_data.append(data)
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

            time.sleep(1)  # Adjust delay to match your data frequency
