#include <Servo.h> //Biblioteka odpowiedzialna za serwa
# define led 13
 
Servo serwomechanizm;  //Tworzymy obiekt, dzięki któremu możemy odwołać się do serwa 
int pozycja = 0; //Aktualna pozycja serwa 0-180
int zmiana = 6; //Co ile ma się zmieniać pozycja serwa?
 
void setup() 
{ 
  serwomechanizm.attach(8);  //Serwomechanizm podłączony do pinu 9
  pinMode(led, OUTPUT);
} 
 
void loop() 
{  
  if (pozycja < 180) { //Jeśli pozycja mieści się w zakresie
    serwomechanizm.write(pozycja); //Wykonaj ruch
  } else { //Jeśli nie, to powrót na początek
    pozycja = 0;
  }    

  digitalWrite(led, HIGH);
  delay(1000); // Wait for 1000 millisecond(s)
  digitalWrite(led, LOW);
  delay(1000); // Wait for 1000 millisecond(s)
  
  pozycja = pozycja + zmiana; //Zwiększenie aktualnej pozycji serwa
  delay(200); //Opóźnienie dla lepszego efektu                        
}
