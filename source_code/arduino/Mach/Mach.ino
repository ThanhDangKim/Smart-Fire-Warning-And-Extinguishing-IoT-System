
#include <ArduinoWiFiServer.h>
#include <BearSSLHelpers.h>
#include <CertStoreBearSSL.h>
#include <ESP8266WiFi.h>
#include <ESP8266WiFiAP.h>
#include <ESP8266WiFiGeneric.h>
#include <ESP8266WiFiGratuitous.h>
#include <ESP8266WiFiMulti.h>
#include <ESP8266WiFiSTA.h>
#include <ESP8266WiFiScan.h>
#include <ESP8266WiFiType.h>
#include <WiFiClient.h>
#include <WiFiClientSecure.h>
#include <WiFiClientSecureBearSSL.h>
#include <WiFiServer.h>
#include <WiFiServerSecure.h>
#include <WiFiServerSecureBearSSL.h>
#include <WiFiUdp.h>

#include <ThingSpeak.h>
#include <time.h>
int buzzerPin = D2;
int motorPinPos = D3;
int motorPinNeg = D4;
int smokePin = D5;
int tempSenPin = A0;
#define mySSID "LanQ"
#define myPassword "$$$$$$$$"
// #define mySSID "Quoc Lan"
// #define myPassword "79797979"
WiFiClient client;
#define myAPIWriteKey "7800TDWI1BFQIL1A"
#define myAPIReadKey "RWYBJM9DZJFD14UQ"
int IDChannel = 2475438;

void checkFire() {
  int is_fire = ThingSpeak.readIntField(IDChannel, 1, myAPIReadKey);
  int smoke = digitalRead(smokePin);
  // LM35
  int temp = ((12.0*analogRead(tempSenPin)*100.0)/1024.0)-170;
  // Serial.printf("Dien the chan A0: %d\n", analogRead(tempSenPin));
  Serial.printf("Nhiet do: %d\n", temp);
  Serial.printf("Khoi: %d\n", smoke);
  if(is_fire == 0) {
    digitalWrite(buzzerPin, LOW);
    digitalWrite(motorPinPos, LOW);
    digitalWrite(motorPinNeg, LOW);
    Serial.println("KHONG CHAY");
    return;
  } 
  if (temp < 100) {
    return;
  }
  if (smoke == 0) {
    return;
  }
  digitalWrite(buzzerPin, HIGH);
  digitalWrite(motorPinPos, HIGH);
  digitalWrite(motorPinNeg, LOW);
  Serial.println("DANG CHAY");
}

void setup() {
  Serial.begin(115200);
  Serial.print(".");

  pinMode(buzzerPin, OUTPUT);
  pinMode(motorPinPos, OUTPUT);
  pinMode(motorPinNeg, OUTPUT);
  pinMode(smokePin, INPUT);

  WiFi.begin(mySSID, myPassword);
  ThingSpeak.begin(client);
  while(WiFi.status() != WL_CONNECTED) {
    Serial.print(".");
    delay(500);
  }

}

void loop() {
  checkFire();
  delay(500);
}

