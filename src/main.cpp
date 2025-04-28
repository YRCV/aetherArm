#include <Arduino.h>

void setup() {
  Serial.begin(115200);
  Serial.println("Xiao is awake ");
  pinMode(LED_BUILTIN, OUTPUT);
}

void loop() {
  Serial.println("Xiao is running ");
  digitalWrite(LED_BUILTIN, HIGH);  // turn the LED on (HIGH is the voltage level)
  delay(1000);                      // wait for a second
  digitalWrite(LED_BUILTIN, LOW);   // turn the LED off by making the voltage LOW
  delay(1000);
}