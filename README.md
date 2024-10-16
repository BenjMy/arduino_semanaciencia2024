# Arduino project Semana Ciencia 2024

![Arduino](https://img.shields.io/badge/-Arduino-00979D?style=for-the-badge&logo=Arduino&logoColor=white)

## TECH4Agro tailer 

## Description

For the "Semana Ciencia" event, the goal is to demonstrate plant water stress by comparing two plants—one well-watered and one stressed—using soil moisture sensors and a thermal camera. Children will learn how soil moisture affects plant health and how technology helps monitor this.

## Materials

- 1 Arduino (with breadboard and jumper wires)
- 2 Pots with plants (one well-watered, one water-stressed)
- 2 Capacitive soil moisture sensors (one per pot)
- 2 Time Domain Reflectometry (TDR) sensors (one per pot)
- 1 Thermal camera (to show leaf temperature differences)
- 1 LCD screen (optional, for live display of moisture levels)
- 1 Power source (for Arduino)
- Laptop with Arduino IDE for data visualization

## Protocol of Measurement

1. **Setup:**
   - Place the two pots side by side.
   - Label one pot "Well-Watered" and the other "Stressed."
   - Insert 1 capacitive soil moisture sensor and 1 TDR sensor into each pot.

2. **Sensor Calibration:**
   - Explain to the children that the sensors measure soil moisture.
   - Demonstrate sensor readings using Arduino, showing the range:
     - **Capacitive sensor**: Lower voltage when soil is moist, higher when dry.
     - **TDR sensor**: Measures electrical pulse speed—faster in wet soil, slower in dry soil.

3. **Thermal Camera:**
   - Use the thermal camera to show temperature differences between the leaves of the two plants.
   - Explain that water-stressed plants tend to have warmer leaves due to less transpiration.

4. **Arduino Monitoring:**
   - Real-time soil moisture monitoring with Arduino.
   - Display live moisture readings from the sensors on the LCD screen (or serial output on the laptop).
   - Allow children to compare the moisture content in both pots and see the stressed plant’s lower moisture levels.

5. **Conclusion:**
   - Summarize how technology helps monitor plant health and the importance of soil moisture in preventing plant stress.
   - Encourage children to think about applications of this knowledge in gardening and farming.

## Authors and acknowledgment
Benjamin Mary

## License
CC-BY

## Project status
In progress
