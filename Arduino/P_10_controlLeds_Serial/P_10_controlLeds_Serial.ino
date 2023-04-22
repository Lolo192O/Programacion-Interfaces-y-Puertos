int led1 =5;
int led2=6;
int led3=7;

void setup(){
  pinMode(led1, OUTPUT);
  pinMode(led2, OUTPUT);
  pinMode(led3, OUTPUT);
  Serial.begin(9600);
  Serial.setTimeout(10);
}

void loop(){
  if(Serial.available()>0){//Si existe informacion en buffer que se pueda leer...

    //Apagamos todos los leds
    digitalWrite(led1, LOW);
    digitalWrite(led2, LOW);
    digitalWrite(led3, LOW);

  int v = Serial.readString().toInt(); // 1 2 3...

  switch(v){
    case 1:
      digitalWrite(led1,HIGH);
    break;
    case 2:
      digitalWrite(led2,HIGH);
    break;
    case 3:
      digitalWrite(led3,HIGH);
    break;
  }
  }
  delay(10);

}


