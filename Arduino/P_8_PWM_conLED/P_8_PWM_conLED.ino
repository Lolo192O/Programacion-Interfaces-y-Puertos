
int led = 6;

int valorPWM;

int control = 1;

void setup(){
  valorPWM= 0;
}

void logo(){
  analogWrite(led, valorPWM);

  valor PWM +=control;

  if(valorPWM == 256 || valorPWM ==-1 ){
    control *=-1;
  }

  delay(100);
}