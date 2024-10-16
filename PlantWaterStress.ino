```cpp
int capacitivePin1 = A0;  // Capacitive sensor for well-watered pot
int capacitivePin2 = A1;  // Capacitive sensor for stressed pot
int tdrPin1 = A2;         // TDR sensor for well-watered pot
int tdrPin2 = A3;         // TDR sensor for stressed pot
int sensorValue1, sensorValue2, tdrValue1, tdrValue2;

void setup() {
  Serial.begin(9600);   // Start serial communication for monitoring
}

void loop() {
  // Read values from sensors
  sensorValue1 = analogRead(capacitivePin1);
  sensorValue2 = analogRead(capacitivePin2);
  tdrValue1 = analogRead(tdrPin1);
  tdrValue2 = analogRead(tdrPin2);

  // Display values on the serial monitor
  Serial.print("Well-Watered Pot Capacitive: ");
  Serial.println(sensorValue1);
  Serial.print("Stressed Pot Capacitive: ");
  Serial.println(sensorValue2);
  Serial.print("Well-Watered Pot TDR: ");
  Serial.println(tdrValue1);
  Serial.print("Stressed Pot TDR: ");
  Serial.println(tdrValue2);

  // Delay between readings
  delay(1000);
}
