#define diode 5

int load = 0;
int change = 5;

void setup()
{
  Serial.begin(9600);
  pinMode(diode, OUTPUT);
}

void loop()
{
  analogWrite(diode, load);
  
  if (load < 255) {
  	load = load + change;
    Serial.println(load);
  }
  else {
  	load = 0;
    Serial.println(load);
  }
  delay(150);
  
}