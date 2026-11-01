#include <WiFi.h>
#include <PubSubClient.h>
#include <DHT.h>
const char* ssid="YOUR_WIFI";
const char* pass="YOUR_PASSWORD";
const char* broker="broker.hivemq.com";
const char* topic="iot/student/demo/dht22";
WiFiClient wifi; PubSubClient mqtt(wifi); DHT dht(4,DHT22);
void setup(){
 Serial.begin(115200); dht.begin(); WiFi.begin(ssid,pass);
 while(WiFi.status()!=WL_CONNECTED){delay(500); Serial.print(".");}
 mqtt.setServer(broker,1883);
}
void loop(){
 if(!mqtt.connected()){
  while(!mqtt.connected()){if(!mqtt.connect("ESP32StudentDemo"))delay(2000);}
 }
 mqtt.loop(); float t=dht.readTemperature(),h=dht.readHumidity();
 if(!isnan(t)&&!isnan(h)){
  String data=String("{\"temperature\":")+String(t)+",\"humidity\":"+String(h)+"}";
  mqtt.publish(topic,data.c_str());Serial.println(data);
 }
 delay(5000);
}
