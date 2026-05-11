/*
 * Amphibious Robot - Bluetooth Serial Passthrough Sketch
 *
 * Purpose:
 *   Bridges the Arduino hardware Serial (USB) and the HC-05
 *   SoftwareSerial port, allowing you to:
 *     1. Test HC-05 connectivity via Serial Monitor
 *     2. Send AT commands to configure the HC-05 module
 *     3. Debug Bluetooth communication
 *
 * Wiring:
 *   HC-05 TX  →  Arduino pin 3  (SoftwareSerial RX)
 *   HC-05 RX  →  Arduino pin 2  (SoftwareSerial TX)
 *   HC-05 VCC →  Arduino 5V
 *   HC-05 GND →  Arduino GND
 *
 * Usage:
 *   Open Serial Monitor at 9600 baud.
 *   Type any character to forward to HC-05, or pair your phone
 *   and send commands — they will echo to Serial Monitor.
 *
 * Team: Akshay Raj B, Nandana Sunil, Sneha Alphonso Francis, Swaroop S
 * Guide: Mr. Sreedeep Krishnan
 * Adi Shankara Institute of Engineering and Technology, Kalady
 */

#include <SoftwareSerial.h>

// HC-05 TX → pin 3 (Arduino RX), HC-05 RX → pin 2 (Arduino TX)
SoftwareSerial mySerial(3, 2);

void setup() {
  // Begin serial communication with Arduino IDE (Serial Monitor)
  Serial.begin(9600);

  // Begin serial communication with HC-05
  mySerial.begin(9600);

  Serial.println("Initializing...");
  Serial.println("Device started — pair it with Bluetooth now!");
}

void loop() {
  // Forward data from USB Serial → HC-05
  if (Serial.available()) {
    mySerial.write(Serial.read());
  }

  // Forward data from HC-05 → USB Serial
  if (mySerial.available()) {
    Serial.write(mySerial.read());
  }

  delay(20);
}
