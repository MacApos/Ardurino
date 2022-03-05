#define red 8

void setup() {
  pinMode(red, OUTPUT);
  pinMode(7, INPUT_PULLUP);

}
 
void loop() {
  while (digitalRead(7) == LOW) {
    digitalWrite(red, HIGH);
    delay(500);
    digitalWrite(red, LOW);
    delay(500); 
  }
}