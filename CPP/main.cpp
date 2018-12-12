#include <Arduino.h>
String distances_to_station;   // for incoming serial data

void setup() {
        Serial.begin(9600);     // opens serial port, sets data rate to 9600 bps
}

void loop() {

        // send data only when you receive data:
        if (Serial.available() > 0) {
                // read the incoming byte:
                distances_to_station = Serial.readString();

                // say what you got:
                Serial.print("Distances to source: ");
                Serial.println(distances_to_station);
        }
}
