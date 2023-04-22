int led1 =5;


boolean estadoLED;

void setup(){
  pinMode(led1, OUTPUT);
  estadoLED = false;
 
  Serial.begin(9600); //baud
  Serial.setTimeout(10); //ms
}

void loop(){
  if(Serial.available()>0){//Si existe informacion en buffer que se pueda leer...

    int v = Serial.readString().toInt();
  if(v==1){
    estadoLED = !estadoLED;
    }

  digitalWrite(led1, estadoLED); 

 }

    delay(10);

}


