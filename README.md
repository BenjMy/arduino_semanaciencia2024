# 🌱 Arduino Monitoring App for Semana de la Ciencia

[![Arduino](https://img.shields.io/badge/-Arduino-00979D?style=for-the-badge&logo=Arduino&logoColor=white)](https://git.csic.es/tech4agro/arduino_semanaciencia2024)
[![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white)](https://tech4agro-csic-semanaciencia2024.streamlit.app/)


This project is a **real-time monitoring application** for Arduino-based soil moisture sensors, built using Streamlit. It aims to help students visualize and understand how plants respond to changes in water availability, focusing on two experiments: **Infiltration** and **Transpiration**.

The app can be run **locally** or deployed **online** (e.g., via Heroku or Streamlit Cloud). Note that due to hardware access limitations, Arduino data may not be accessible in the online version without additional configurations.

---

## Table of Contents
- [Getting Started](#getting-started)
- [Installation](#installation)
- [Files and Directory Structure](#files-and-directory-structure)
- [App Sections](#app-sections)
- [Running the App](#running-the-app)
  - [Locally](#locally)
  - [Online](#online)
- [Current Limitations](#current-limitations)

---

## 🚀 Getting Started

This app is designed for interactive education on soil moisture, temperature monitoring, and plant water response. It's set up to interface with an Arduino through serial communication to display live data for soil moisture and temperature readings. Currently, local setups with USB-connected Arduinos are supported.

---

## 🛠 Installation

Before running the app, ensure all dependencies are installed. We recommend using Conda for managing dependencies.

1. **Clone the repository**:
   ```bash
   git clone https://git.csic.es/tech4agro/arduino_semanaciencia2024
   cd arduino_semanaciencia2024

2. Set up Conda environment:
  ```
   conda create -n arduino_app_env python=3.10
   conda activate arduino_app_env
  ```

3. Install dependencies:
  ```
  conda install --file requirements.txt
  ```

Note: Ensure the serial package is installed to handle Arduino communication:
  ```bash
  conda install pyserial
  ```

## 📂 Files and Directory Structure
- `app.py`: Main file that runs the Streamlit application.
- `run_server.py`: Optional Tornado server script to handle serial data and make it accessible online.
- `find_port_arduino.py`: Script to dynamically detect Arduino’s serial port on your machine.
- `infiltration_test.py`: A component of the app displaying the infiltration experiment.
- `transpiration_test.py`: A component of the app showing the transpiration experiment.

  
## 🌿 App Sections
- Infiltration Test:
  - Demonstrates the effect of water infiltration on soil moisture levels.
  - Uses two pots with different watering conditions to track changes in soil moisture over time.
- Transpiration Test:
  - Illustrates plant water loss through leaf transpiration.
  - Uses thermal imaging and soil moisture sensors to display temperature differences and transpiration rates between well-watered and stressed plants.


## ▶️ Running the App

### 💻 Locally
You can run the app locally with a USB-connected Arduino.

```bash
  streamlit run app.py
```

### 🌐 Online
For online deployment, this app is compatible with Streamlit Cloud or Heroku. 

## ⚠️ Current Limitations

While the app functions smoothly in a local setup, the online version may face challenges due to serial port access restrictions. To investigate possible solutions:

1. Use `run_server.py` to serve serial data through an HTTP endpoint.
2. Update `app.py` to fetch data from this server instead of the direct serial port.

We’re continuing to explore solutions to make this project fully accessible online.


