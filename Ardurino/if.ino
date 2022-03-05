void setup() {
  pinMode(8, OUTPUT);
  pinMode(7, INPUT_PULLUP);
  digitalWrite(8, HIGH);
}
 
void loop() {
  if (digitalRead(7) == LOW) { //wciśnięty przycisk
    digitalWrite(8, HIGH);}
  else { //niewciśnięty przycisk
    digitalWrite(8, LOW);}
}