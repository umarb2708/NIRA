/******************************************************************************
  OLED Eyeballs for 128x64 OLED by Vin.X.Mod 
  Online Image to C Array Converter at https://lvgl.io/tools/imageconverter
  Adafruit 128x64 OLED Graphic Display https://www.adafruit.com/product/326
  For more information see the wonderful tutorial by Rui Santos
  https://randomnerdtutorials.com/guide-for-oled-display-with-arduino/
******************************************************************************/

#include <Wire.h>
#include <Adafruit_GFX.h>
#include <Adafruit_SSD1306.h>
#include <ESP8266WiFi.h>
#include <PubSubClient.h>

#include "eyesdata.h"

#define SCREEN_WIDTH 128
#define SCREEN_HEIGHT 64

const char* ssid = "Umar Jio";//Wifi SSID
const char* password = "Umar@JIO123#";//WIFI Password
const char* mqtt_server = "192.168.15.2";
const char* mqtt_user="hiraAdmin";
const char* mqtt_pass="Admin@MQTT123#";
String eyeControl="sleep";
String newHostname="HIRA-EYES";

Adafruit_SSD1306 display(SCREEN_WIDTH, SCREEN_HEIGHT, &Wire, LED_BUILTIN);
WiFiClient espClient;
PubSubClient client(espClient);

//Function to set up wifi
void setup_wifi() {
  delay(10);
  // We start by connecting to a WiFi network
  Serial.println();
  Serial.print("Connecting to ");
  Serial.println(ssid);
  WiFi.hostname(newHostname.c_str());
  WiFi.begin(ssid, password);
  while (WiFi.status() != WL_CONNECTED) {
    delay(500);
    Serial.print(".");
  }
  Serial.println("");
  Serial.print("WiFi connected - ESP IP address: ");
  Serial.println(WiFi.localIP());
}

void callback(char* topic, byte* payload, unsigned int length) {
  Serial.print("Message arrived [");
  Serial.print(topic);
  Serial.print("] ");
  eyeControl="";
  for (int i = 0; i < length; i++) {
    Serial.print((char)payload[i]);
    eyeControl=eyeControl+(char)payload[i];
  }
  Serial.println();
  //eyeControl=String(payload);
  Serial.print("EyesControll:");
  Serial.println(eyeControl);
  // Switch on the LED if an 1 was received as first character
  if (eyeControl == "sleep") {
    fullClose();
  }
  else if (eyeControl == "wakeup") {
    quaterOpen();
    delay(900);
    fullClose();
    delay(1900);
    halfOpen();
    delay(1900);
    fullOpen();

  }
  else if (eyeControl == "happy") {
    happy();
  }
  else if (eyeControl == "surprized") {
    surprized();
  }
  else if (eyeControl == "sad") {
    sad();
  }
  else if (eyeControl == "love") {
    love();
  }
  else if (eyeControl == "deny") {
    deny();
  }
  else if (eyeControl == "angry") {
    angry();
  }

}

void reconnect() {
  // Loop until we're reconnected
  while (!client.connected()) {
    Serial.print("Attempting MQTT connection...");
    // Create a random client ID
    String clientId = "ESP8266Client-";
    clientId += String(random(0xffff), HEX);
    // Attempt to connect
    if (client.connect(clientId.c_str(),mqtt_user, mqtt_pass)) {
      Serial.println("connected");
      // Once connected, publish an announcement...
      client.publish("hiraEyes/connection", "1");
      // ... and resubscribe
      client.subscribe("hiraEyes/eyesControl");
    } else {
      Serial.print("failed, rc=");
      Serial.print(client.state());
      Serial.println(" try again in 5 seconds");
      // Wait 5 seconds before retrying
      delay(5000);
    }
  }
}


void setup() {
  Serial.begin(115200);
  setup_wifi();
  client.setServer(mqtt_server, 1883);
  client.setCallback(callback);

  if(!display.begin(SSD1306_SWITCHCAPVCC, 0x3C)) 
  {
    Serial.println(F("SSD1306 allocation failed"));
    for(;;);
  }
  display.clearDisplay();  // Clear the buffer
  display.invertDisplay(1);
  fullClose();
  display.clearDisplay();  // Clear the buffer
  quaterOpen();
  display.clearDisplay();  // Clear the buffer
  halfOpen();

}

void loop() {
// Use Void Loop to display multipule images

  if (!client.connected()) 
  {
    reconnect();
  }
  client.loop();
  

}
void fullClose()
{
  display.clearDisplay();
  display.drawBitmap(0, 0, epd_bitmap_FullClose, 128, 64, 1);
  display.display();
  delay(100); // Pause for 1.0 seconds
}
void quaterOpen()
{
  display.clearDisplay();
  display.drawBitmap(0, 0, epd_bitmap_quaterOpen, 128, 64, 1);
  display.display();
  delay(100); // Pause for 1.0 seconds
}
void halfOpen()
{
  display.clearDisplay();
  display.drawBitmap(0, 0, epd_bitmap_HalfOpen, 128, 64, 1);
  display.display();
  delay(100); // Pause for 1.0 seconds
}
void fullOpen()
{
  display.clearDisplay();
  display.drawBitmap(0, 0, epd_bitmap_Fullopen, 128, 64, 1);
  display.display();
  delay(100); // Pause for 1.0 seconds
}
void happy()
{
  display.clearDisplay();
  display.drawBitmap(0, 0, epd_bitmap_Happy, 128, 64, 1);
  display.display();
  delay(100); // Pause for 1.0 seconds
}
void sad()
{
  display.clearDisplay();
  display.drawBitmap(0, 0, epd_bitmap_Sad, 128, 64, 1);
  display.display();
  delay(100); // Pause for 1.0 seconds
}
void love()
{
  display.clearDisplay();
  display.drawBitmap(0, 0, epd_bitmap_Love, 128, 64, 1);
  display.display();
  delay(100); // Pause for 1.0 seconds
}
void surprized()
{
  display.clearDisplay();
  display.drawBitmap(0, 0, epd_bitmap_Surprised, 128, 64, 1);
  display.display();
  delay(100); // Pause for 1.0 seconds
}
void deny()
{
  display.clearDisplay();
  display.drawBitmap(0, 0, epd_bitmap_Deny, 128, 64, 1);
  display.display();
  delay(100); // Pause for 1.0 seconds
}
void angry()
{
  display.clearDisplay();
  display.drawBitmap(0, 0, epd_bitmap_AngryRight, 128, 64, 1);
  display.display();
  delay(100); // Pause for 1.0 seconds
}
// End of Arduino Sketch  