#include <Arduino.h>

void setup() {
  Serial.begin(115200);
  Serial.println("Xiao is awake ");
  pinMode(LED_BUILTIN, OUTPUT);
}

void loop() {
  Serial.println("Xiao is running 2 ");
  digitalWrite(LED_BUILTIN, HIGH); 
  delay(1000);                    
  digitalWrite(LED_BUILTIN, LOW);
  delay(1000);
  digitalWrite(LED_BUILTIN, HIGH); 
  delay(250);                    
  digitalWrite(LED_BUILTIN, LOW);
  delay(250);
  digitalWrite(LED_BUILTIN, HIGH); 
  delay(250);                    
  digitalWrite(LED_BUILTIN, LOW);
  delay(250);
}