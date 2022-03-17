#include <Servo.h>
#define pin 5

Servo servo0;
Servo servo1;
Servo servo2;

void setup()
{
  servo0.attach(3);
  servo1.attach(5);
  servo2.attach(9);
}

void loop()
{
  servo0.write(0);
  delay(500);

  servo0.write(180);
  delay(500);
}
