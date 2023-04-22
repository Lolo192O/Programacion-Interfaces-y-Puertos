int leds []= {5, 6,7};
///P_23 vectoresParaLeds.ino


void setup() {
  // put your setup code here, to run once:
   pinMode(leds[0],OUTPUT)
   pinMode(leds[2],OUTPUT)
   pinMode(leds[3],OUTPUT)


   Serial.begin(9600);
   Serial.setTimeout(10);
}

void loop() {
  // put your main code here, to run repeatedly:
  if (serial.available()>0){
    digitalWrite(leds[0], LOW)
    digitalWrite(leds[1], LOW)
    digitalWrite(leds[2], LOW)

   int v = Serial.readString().toInt()-1;
   digitalWrite(leds[v],HIGH);
  }
  
  delay(10);
}