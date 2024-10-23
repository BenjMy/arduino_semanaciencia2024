# Semana Ciencia 2024 - 🌿 Measuring Plant Water Stress with Arduino 🌱

![Arduino](https://img.shields.io/badge/-Arduino-00979D?style=for-the-badge&logo=Arduino&logoColor=white)
[![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white)](YOUR_STREAMLIT_LINK)

## 🌟 Description
For the **Semana Ciencia** event, the goal is to demonstrate plant water stress by comparing two plants—one well-watered 💧 and one stressed 🌵—using soil moisture sensors and a thermal camera. Children will learn how soil moisture affects plant health and how technology can help monitor this. 

## 🛠 Materials

- 1 Arduino (with breadboard and jumper wires)
- 2 Pots with plants 🌱 (one well-watered, one water-stressed)
- 2 Capacitive soil moisture sensors 🌡 (one per pot)
- 2 Time Domain Reflectometry (TDR) sensors 🌍 (one per pot)
- 1 Thermal camera 📷 (to show leaf temperature differences)
- 1 LCD screen 📺 (optional, for live display of moisture levels)
- 1 Power source 🔋 (for Arduino)
- Laptop 💻 with Arduino IDE for data visualization

## 📏 Protocol of Measurement

1. **Setup:**
   - Place the two pots side by side 🪴🪴.
   - Label one pot "Well-Watered" 💧 and the other "Stressed" 🌵.
   - Insert 1 capacitive soil moisture sensor and 1 TDR sensor into each pot.

2. **Sensor Calibration:**
   - Explain to the children that the sensors measure soil moisture 💦.
   - Demonstrate sensor readings using Arduino:
     - **Capacitive sensor**: Lower voltage when soil is moist, higher when dry.
     - **TDR sensor**: Measures electrical pulse speed—faster in wet soil, slower in dry soil.

3. **Thermal Camera:**
   - Use the thermal camera 📷 to show temperature differences between the leaves 🍃 of the two plants.
   - Explain that water-stressed plants tend to have warmer leaves due to less transpiration 🌡️.

4. **Arduino Monitoring:**
   - Real-time soil moisture monitoring using Arduino.
   - Display live moisture readings 📊 from the sensors on the LCD screen (or serial output on the laptop 💻).
   - Allow children to compare the moisture content in both pots and observe the stressed plant’s lower moisture levels.

5. **Conclusion:**
   - Summarize how technology helps monitor plant health 🌿 and the importance of soil moisture in preventing plant stress 🌞.
   - Encourage children to think about applications of this knowledge in gardening and farming 🚜.

## 🌐 Streamlit Application

```bash
conda create -n semana_ciencia streamlit python=3.10
conda activate semana_ciencia
pip install streamlit pandas matplotlib
pip install pyserial
```

👩‍🏫 Authors and Acknowledgment
- Benjamin Mary
- Hector Nieto

📜 License: CC-BY

🚧 Project Status: In progress

🔗 Useful Links
Capacitive Sensors Performance: https://www.youtube.com/watch?v=IGP38bz-K48

