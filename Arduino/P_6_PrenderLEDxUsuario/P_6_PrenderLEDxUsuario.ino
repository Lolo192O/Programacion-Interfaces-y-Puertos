    //Los pines digitales en arduino uno, van del 0 al 13 y en arduino mega del 0 al 54



    //un led, es un dispositivo que funciona con una señal digital...
    int led = 13;    
    
    
    void setup() {
      //PARA QUE UN PIN DIGITAL FUNCIONE CON NORMALIDAD, ES NECESARIO ESTABLECER EL MODO DE TRABAJO DEL PIN
      //ES DECIR, SEÑALAR SI SERA DE ENTRAD O SALIDA

      pinMode(led, OUTPUTP);
      
      Serial.begin(9600);//baudios
      Serial.setTimeout(10);//ms

    }

    int op;
    void loop() {

      if(Serial.available()>0){
        op = Serial.readString().toInt(); //op = (0,1) puede ser 0 o 1
        digitalWrite(led, op);
      }
      // put your main code here, to run repeatedly:
      delay(10);

    }
