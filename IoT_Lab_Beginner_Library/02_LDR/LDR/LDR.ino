#define LDR_PIN 34
void setup(){Serial.begin(115200);}
void loop(){
 int value=analogRead(LDR_PIN);
 Serial.print("Light sensor: "); Serial.print(value);
 if(value<1200) Serial.println(" LOW");
 else if(value<2500) Serial.println(" MEDIUM");
 else Serial.println(" HIGH");
 delay(1000);
}
