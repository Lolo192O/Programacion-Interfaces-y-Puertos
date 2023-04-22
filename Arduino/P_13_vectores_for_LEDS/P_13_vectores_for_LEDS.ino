int leds[] = {5,6,7,8,9,10};

void setup(){
  for(int i=0; i <6; i++){
    pinMode(leds[i], OUTPUT);
  }

  Serial.begin(9600);
  Serial.setTimeout(10);
}

void loop(){
  if (Serial.available()>0){

    for(int i=0; i<6, i++){
      digitalWrite(leds[i],LOW);

    }
    int v = Serial.readString().toInt()-1;

    digitalWrite(leds[v], HIGH);

  }

  delay(10);
}