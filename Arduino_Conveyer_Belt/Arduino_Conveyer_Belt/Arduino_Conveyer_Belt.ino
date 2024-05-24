int stepPin = 2;
int dirPin = 5;

void setup() {

pinMode(stepPin,OUTPUT);
pinMode(dirPin,OUTPUT);
digitalWrite(dirPin,LOW);
}

void loop() {
  int sensorValue = analogRead(A2);
  sensorValue = map(sensorValue,0,1023,250,5000);

  digitalWrite(stepPin,HIGH);
  delayMicroseconds(sensorValue);
  digitalWrite(stepPin,LOW);
  delayMicroseconds(sensorValue);


}
