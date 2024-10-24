# find_port_arduino.py
import serial.tools.list_ports
import streamlit as st

def get_serial_port():
    # Function to list available serial ports
    def list_serial_ports():
        ports = serial.tools.list_ports.comports()
        return [port.device for port in ports]

    # Show available ports in local development
    if st.session_state.get('is_local', False):  # Check if running locally
        available_ports = list_serial_ports()
        st.write("Available ports:", available_ports)
        
        # Allow user to select a port
        selected_port = st.selectbox("Select the Arduino Port:", available_ports)
    else:
        selected_port = st.text_input("Enter the Arduino Port:", "/dev/ttyACM0")  # Default port

    return selected_port
