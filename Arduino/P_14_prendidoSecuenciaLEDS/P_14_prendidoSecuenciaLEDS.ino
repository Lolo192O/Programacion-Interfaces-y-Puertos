//On //Off
int led1 = 13;
int led2 = 12;
int led3 = 11;
int led4 = 10;

/PWM
int led5 = 3;
int led6 = 5;
int led7 = 6;

//Potenciomentros
int pot1 = A0;
int pot2 = A1;
int pot3 = A2;

void setup(){

  pinMode(led1, OUTPUT); //SOLO LOS PINDES DIGITALES QUE SERAN USADOS COMO ON/OFF, REQUIEREN SE ESTABLEZCA
  pinMode(led2, OUTPUT); //EL MODO DE TRABAJO DEL PIN,,, EN ESTE CADO, COMO UTPUT, DEBIDO A QUE SE
  pinMode(led3, OUTPUT); //PRENDERAN O APAGARAN LOS LEDS
  pinMode(led4, OUTPUT);
  
  Serial.begin(9600);
  Serial.setTimeout(100);
}

int vPot1, vPot2, vPot3;
void loop(){
  vPot1 analogRead(pot1);
  vPot2 analogRead(pot2);
  vPot3 analogRead(pot3);
  cadenaSensores = String(vPot1)+ "-" + String(vPot2) + "-" + String(vPot3);

  Serial.println(cadenaSensores);

  delay(1000);
}
