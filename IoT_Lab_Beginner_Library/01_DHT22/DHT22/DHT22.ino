#include <DHT.h>
#define PIN 4
DHT dht(PIN, DHT22);
void setup() { Serial.begin(115200); dht.begin(); }
void loop() {
  float t = dht.readTemperature(), h = dht.readHumidity();
  if (isnan(t) || isnan(h)) Serial.println("Sensor error");
  else { Serial.print("Temperature: "); Serial.print(t); Serial.print(" C, Humidity: "); Serial.println(h); }
  delay(2000);
}
