#include <Servo.h>

Servo servo0;
Servo servo1;
Servo servo2;

void setup() {
  servo0.attach(3);
  servo1.attach(5);
  servo2.attach(9);
}

void loop() {
  servo0.writeMicroseconds(800);

    servo0.write(180);
    servo1.write(0);
    servo2.write(0);
    delay(1500);

    servo0.write(0);
    servo1.write(180);
    servo2.write(180);
    delay(1500);
  
}
