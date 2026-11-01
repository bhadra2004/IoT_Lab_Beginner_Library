// Simple Wokwi ESP32 demonstration: 4 roads, green LEDs on GPIOs 16-19
// Emergency button on GPIO 4 (button to GND, internal pull-up)
const int greens[4]={16,17,18,19};
const int buttonPin=4;
void setup(){for(int i=0;i<4;i++)pinMode(greens[i],OUTPUT);pinMode(buttonPin,INPUT_PULLUP);}
void loop(){
 for(int road=0;road<4;road++){
  if(digitalRead(buttonPin)==LOW){road=0;}
  for(int i=0;i<4;i++)digitalWrite(greens[i],i==road?HIGH:LOW);
  int seconds=road==0?12:6;
  for(int t=0;t<seconds*10;t++){
   if(digitalRead(buttonPin)==LOW && road!=0)break;
   delay(100);
  }
 }
}
