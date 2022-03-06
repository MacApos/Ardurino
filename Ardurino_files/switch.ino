int servo1 = 0;
int servo2 = 0;
int servo3 = 0;

void setup() {
  Serial.begin(9600);
  for (int thisPin = 2; thisPin < 7; thisPin++) {
    pinMode(thisPin, OUTPUT);
  }
}
 
void loop() {
  if (Serial.available() > 0) {
    int inByte = Serial.read();
    //inByte = inByte.isLowerCase();
    
    switch (inByte) {
      case 'a':
        digitalWrite(2, HIGH);
      	servo1 = servo1 + 1;
       	break;

      case 'd':
        digitalWrite(3, HIGH);
      	servo1 = servo1 - 1;
       	break;

      case 'w':
        digitalWrite(4, HIGH);
      	servo2 = servo2 + 1;
       	break;

      case 's':
        digitalWrite(5, HIGH);
      	servo2 = servo2 - 1;
       	break;

      case '8':
        digitalWrite(6, HIGH);
      	servo3 = servo3 + 1;
       	break;
      
      default:
      	for (int thisPin = 2; thisPin < 7; thisPin++) {
          digitalWrite(thisPin, LOW);
      	}

    }
  
  }

}