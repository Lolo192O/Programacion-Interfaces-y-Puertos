int potenciometro =A0;
int led = 6;
int valorPWM;

void setup(){
  valorPWM= 0;
}

void logo(){
    valorPWM = analogRead(potenciometro); // 0 1023

    valorPWM = valorPWM/4;
    
    analogWrite(led, valorPWM); //PWM = Pulse width modulation = Modulacion por ancho de pulso

    
    delay(10);
}