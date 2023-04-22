//los POTENCIOMETROS son dispositivos analogicos de entrada, porque tienen mas de dos estados



//en el caso de arduino, se cuenta con algunos pines analogicos para estos acutadores
//los pines analogicos se representan por la letra A y un numero..
//ejemplo A0


    //un led, es un dispositivo que funciona con una señal digital...
    int potenciometro = A0;
    
    
    void setup() {
      //no se requiere establecer el modo de trabajo de un pin analogico
      
      Serial.begin(9600);//baudios
      Serial.setTimeout(10);//ms

    }

    int v;
    void loop() {

      v = analogRead(potenciometro);
      //un acutador analogico en arduino nos puede proporcionar 1024 valores... que van
      // que van del 0 al 1023... esto DEBIDO A QUE ARDUINO CUENTA CON UN ADC DE 10 BITS...
      //ASI MISMO, ARDUINO TRABAJA EN EL ADC CON 5 VOTS..

      //ESTO SIGNIFICA QUE 1023= 5V     Y           0 =0V

      //APROXIMADAMENTE, SE TIENE UN CAMBIO DE VALOR CADA 4.8mv

      Serial.println(v);            
      delay(10);

      //el potenciometro tiene 3 patitas.. de las cuales la de enmedio debe conectar al A0, y uno de los extremos a
      //a 5V, mientras que el otro extremo a GND

    }
