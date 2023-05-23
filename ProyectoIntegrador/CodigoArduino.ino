//ON / OFF
int led1 = 10;
int led2 = 11;
int led3 = 12;
int led4 = 13;

//PWM
int led5 = 3;
int led6 = 5;
int led7 = 6;

//Potenciometros (sensores)
int pot1 = A0;
int pot2 = A1;
int pot3 = A2;

void setup() {
  // put your setup code here, to run once:

  pinMode(led1, OUTPUT); //SOLO LOS PINDES DIGITALES QUE SERAN USADOS COMO ON/OFF, REQUIEREN SE ESTABLEZCA
  pinMode(led2, OUTPUT); //EL MODO DE TRABAJO DEL PIN... EN ESTE CASO , COMO OUTPUT, DEBIDO A QUE SE 
  pinMode(led3, OUTPUT); // PRENDERAN O APAGARAN LOS LEDS
  pinMode(led4, OUTPUT);

  Serial.begin(9600);
  Serial.setTimeout(100);
}

char *c;
char *token;

int vPot1, vPot2, vPot3;
String cadenaSensores; 

String respuesta; 
void loop() {
  // put your main code here, to run repeatedly:

  //OBTIENE EL VALOR DE LOS POTENCIOMETROS
  vPot1 = analogRead(pot1) * 1;  //0 - 1023
  vPot2 = analogRead(pot2) * 2;  //* 1  ... * 2  y * 3 --- solo solo valores para hacer prueba, en la practica real no deben ir 
  vPot3 = analogRead(pot3) * 3;

  //CONCATENA LOS VALORES DE LOS POTENCIOMETROS EN UNA UNICA CADENA PARA FACILITAR EL ENVIO DE LA INFORMACION
  cadenaSensores = String(vPot1) + "-" + String(vPot2) + "-" + String(vPot3);

  //ENVIA LA INFORMACION DE LOS POTENCIOMETROS A PYTHON A TRAVES DE COMUNICACION SERIAL
  Serial.println(cadenaSensores);

  //ENTRADA QUE ESPERA ARDUINO: 1-1-0-1-100-240-50

  // /dev/cu.usbmodem101

  if(Serial.available()>0){ //si hay informacion en el buffer para ser leida... entonces se leera

    respuesta = Serial.readString(); //leera la cadena recibida por el usuario (comunicacion serial...)    
    respuesta.replace("\n","");
    respuesta.replace("\r","");
    c = respuesta.c_str();
                
    token = strtok(c,"-"); //Tokeniza la cadena    

    String temp;
    int contador  = 0;
    while(token != NULL){
      temp = String(token);
    //Serial.println("Token: " + temp + " Contador: " + String(contador));

      switch(contador){
        case 0:
          digitalWrite(led1, temp.toInt());
        break;
        case 1:
          digitalWrite(led2, temp.toInt());
        break;
        case 2:
          digitalWrite(led3, temp.toInt());
        break;
        case 3:
          digitalWrite(led4, temp.toInt());
        break;
        case 4:
          analogWrite(led5, temp.toInt());
        break;
        case 5:
          analogWrite(led6, temp.toInt());
        break;
        case 6:
          analogWrite(led7, temp.toInt());
        break;
      }


      contador++;
      token = strtok(NULL,"-");
    }

  }

  delay(100); //milisegundos - por lo que se utilizo e python QTimer, el temporizador

}
