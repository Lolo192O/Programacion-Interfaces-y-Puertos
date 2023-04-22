    //UART 
    void setup() {
      // put your setup code here, to run once:
      Serial.begin(9600); //baudios, unidad de medidad por la cual se transmiten en los dispositivos

    }

    void loop() {
      // put your main code here, to run repeatedly:
      Serial.println("Esto es mensaje");

    }
