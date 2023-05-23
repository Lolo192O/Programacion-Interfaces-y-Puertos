

//On / OFF
int led1 = 10;
int led2 = 11;
int led3 = 12;
int led4 = 13;


//PWM
int led5 = 3;
int led6 = 5;
int led7 = 6;


//POTENCIOMETROS (SENSORES)
int pot1 = A0;
int pot2 = A1;
int pot3 = A2;


 void setup() {
  // put your setup code here, to run once:
  
  pinMode(led1, OUTPUT); //Solo los pines digitales que sean usados como ON / off, requieren se estableza
  pinMode(led2, OUTPUT); //El modo de trabajo del pin .. en este caso, como output, debido a que se
  pinMode(led3, OUTPUT); //prenderan o apagaran los leds
  pinMode(led4, OUTPUT);

  Serial.begin(9600);
  Serial.setTimeout(100);//

}
char *c;
char *token;


int vPot1, vPot2, vPot3;
String cadenaSensores;

String respuesta;
void loop() {
  // put your main code here, to run repeatedly:
  vPot1 = analogRead(pot1); // cada uno de ellos simula un sensor
  vPot2 = analogRead(pot2); //0-1023
  vPot3 = analogRead(pot3);
//ahora mandaremos estos valores a comunicacion serial, creamos linea 36 y continuamos

cadenaSensores = String(vPot1) + "-" + String(vPot2) + "-" + String(vPot3);

Serial.println(cadenaSensores);



//ENTRADA QUE ESPERA EL ARDUINO : 1111111

if(Serial.available()>0){ //si hay informacion en el buffer para ser leido.. entonces se leera

    respuesta= Serial.readString(); //esto leera la cadena recibida por el usuario(comunicacion serial...)
    respuesta.respuesta.replace("\n", "");
    respuesta.respuesta.replace("\r", "");
    c = cadena.c_str();

    token = stroke(c,"-"); //tokeniza la cadena

    String temp;
    int contador = 0;
    while(token !=NULL){
      temp = String(token);
      //Serial.println("Tokens: " + temp+ "Contador: " + String(contador));
      
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
        digitalWrite(led5, temp.toInt());
        break;

        case 5:
        digitalWrite(led6, temp.toInt());
        break;

        case 6:
        digitalWrite(led7, temp.toInt());
        break;
      }

      contador++;
      token = strtok(Null, "-";)


    }

    }



delay(100);

}
