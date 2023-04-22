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

    void loop() {
      // put your main code here, to run repeatedly:
      digitalWrite(led, HIGH);
      delay(1000);

      digitalWrite(led, LOW);
      delay(1000);

    }
