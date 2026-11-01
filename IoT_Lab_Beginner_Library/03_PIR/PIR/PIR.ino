#define PIR_PIN 27
void setup(){Serial.begin(115200); pinMode(PIR_PIN,INPUT);}
void loop(){
 if(digitalRead(PIR_PIN)==HIGH) Serial.println("Motion detected");
 else Serial.println("No motion");
 delay(1000);
}
