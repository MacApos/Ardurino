#include <Servo.h> //Biblioteka odpowiedzialna za serwa
# define led 13
 
Servo servo;  //Tworzymy obiekt, dzięki któremu możemy odwołać się do serwa 
 
void setup() 
{ 
  servo.attach(9);  //Serwomechanizm podłączony do pinu 9
} 
 
void loop() 
{  

  for (int i = 0; i <= 180; i=i+5) {
    servo.write(i);
    delay(500);
  }                    
}
