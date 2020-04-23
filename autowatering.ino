
#define BLYNK_PRINT Serial


#include <ESP8266WiFi.h>
#include <BlynkSimpleEsp8266.h>

#define motor D2
// You should get Auth Token in the Blynk App.
// Go to the Project Settings (nut icon).
char auth[] = "GZMPhm1lhqTGoXZ-AV2ZPj_RYonKohJT";

// Your WiFi credentials.
// Set password to "" for open networks.
char ssid[] = "TP-LINK_CF0DC6";
char pass[] = "88888888";
const int sensorPin= A0;
int value = 0;
BLYNK_WRITE_DEFAULT()
{
  int pin=request.pin;      //取得虛擬腳位
  value=param.asInt();  //取得參數值
  Serial.print(value);
}

void setup()
{
  // Debug console
  Serial.begin(9600);
  Blynk.begin(auth, ssid, pass);
  pinMode(motor,OUTPUT);
  pinMode(motor, OUTPUT);   
  pinMode(sensorPin,INPUT);
}

void loop()
{
  int moist;
  moist = analogRead(sensorPin);
  Serial.print(moist);
  moist = moist*100/1024;
  moist =100-moist;
  //代表數字越小越乾
  Serial.print("Humidity: ");
  Serial.print(moist);
  Serial.println("%");
  Blynk.virtualWrite(V2,moist);
  
  // 乾燥程度<27時，澆花
  if (moist < 27 || value == 1)
  {
    
    digitalWrite(motor, LOW); 
    if(value ==0)
    {
      delay(5000);
    }
  }
  else
  {
      digitalWrite(motor,HIGH);
      delay(5000);
  }
  Blynk.run();
}
