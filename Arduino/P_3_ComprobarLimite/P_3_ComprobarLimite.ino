    //UART
    
    byte contador; //max de byte =255
    
    
    
    void setup() {
      // put your setup code here, to run once:
      contador = 0 ;
      Serial.begin(9600);

    }

    void loop() {
      // put your main code here, to run repeatedly:
      Serial.println(contador++)
      delay(1000); //ms

    }
