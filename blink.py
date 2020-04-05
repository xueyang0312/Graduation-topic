from pyfirmata import Arduino
import time
import serial

#arduino的 setup()

s=serial.Serial("com4",9600) #Serial.begin(9600)
sensorPin=2
motor = 8
led =13

#arduino的loop()
while True:
    #arduino的感測器讀取數據到python
    moist = s.readline()
    print(moist)
    if moist>500:
        s.digital[led].write(0)
        s.digital[motor].write(0)
    else:
        s.digital[led].write(1)
        s.digital[motor].write(1)
    time.sleep(5)
    """
    s.digital[13].write(1)
    time.sleep(0.2)
    s.digital[13].write(0)
    time.sleep(0.2)
    """

"""
const int sensorPin=2;
int motor = 8;
int led =13;
void setup()
{
  pinMode(motor, OUTPUT);
  pinMode(led,OUTPUT);    
  pinMode(sensorPin,INPUT);
  Serial.begin(9600);
}
 
void loop()
{
  int moist;
  moist = analogRead(sensorPin);
  Serial.println(moist);
  
  // 乾燥程度大於 550 時，關燈
  if (moist > 500)
  {
       digitalWrite(led,LOW);
       digitalWrite(motor, LOW); 
  }
  else
  {
      digitalWrite(led,HIGH);
      digitalWrite(motor,HIGH);
  }
  delay(5000);
}
"""