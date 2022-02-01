#include <Servo.h>

Servo esc1; 
Servo esc2;

void setup() {
  // put your setup code here, to run once:
  esc1.attach(9);
  esc2.attach(10);
  delay(15); 
  Serial.begin(115200);
  esc1.write(0);
  esc2.write(0);
  delay(3000);
  esc1.write(70);
  esc2.write(70);
  delay(5);
}

float map(float x, float a, float b, float c, float d)
{
  return  c + (x - a) * (d - c) / (b - a) ;
}

void runMotor(float cmdl, float cmdr){
    esc1.write(cmdl);
    esc2.write(cmdr);
    
    Serial.print(" You sent me : " );
    Serial.print(" data 1 : " );
    Serial.print(cmdl );
    Serial.print(" data 2 " );
    Serial.println(cmdr ); 
  }


void loop() {
  // put your main code here, to run repeatedly:
  if( Serial.available()>0){
    String data = Serial.readStringUntil('\n');

    Serial.print(data.length());
    if ( data.length() > 2 ) {
      int index = data.indexOf('$');
      String data1 = data.substring(0,index);
      String data2 = data.substring(index+1);
      //float cmdl = data1.toFloat();
      //float cmdr = data2.toFloat();
      float cmdl = map ( data1.toFloat() , 0 , 100, 70, 80 );
      float cmdr = map ( data1.toFloat() , 0 , 100, 70, 80 );
      runMotor(cmdl, cmdr);
    }
    else {
      Serial.print(" les vitesses sont : es1 ") ;
      Serial.print(esc1.read());
      Serial.print(" esc 2 : " );
      Serial.println(esc2.read());
    }
}
}
