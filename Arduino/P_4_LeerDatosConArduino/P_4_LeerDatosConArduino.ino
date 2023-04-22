    //UART
    
    byte contador; //max de byte =255
    
    
    
    void setup() {
      // put your setup code here, to run once:
      Serial.begin(9600);//baudios
      Serial.setTimeout(10);//ms

    }

    void loop() {
      // put your main code here, to run repeatedly:

      //available retorna cuantos bytes existen en el buffer de entrada
      if(Serial.available()>0){
        
      //Arduino intentara leer todoslos bytes que le sean posible hasta que se llegue al tiempo limite(timeout)
      //por defecto, el timeout del arduino es de 1 segundo
      cadena = Serial.readString();

      Serial.println(cadena)
      }

    }
