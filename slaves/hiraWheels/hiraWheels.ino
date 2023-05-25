#include <ESP8266WiFi.h>
#include <PubSubClient.h>

#define IN1            14
#define IN2            12
#define IN3            13
#define IN4            15
#define led            16

const char* ssid = "Umar Jio";//Wifi SSID
const char* password = "Umar@JIO123#";//WIFI Password
const char* mqtt_server = "192.168.15.2";
const char* mqtt_user="hiraWheels";
const char* mqtt_pass="Esp@HIRA123#";
String wheelsControl="stop";
String newHostname="hira-wheels";

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
  wheelsControl="";
  for (int i = 0; i < length; i++) {
    Serial.print((char)payload[i]);
    wheelsControl=wheelsControl+(char)payload[i];
  }
  Serial.println();
  //wheelsControl=String(payload);
  Serial.print("WheelsControll:");
  Serial.println(wheelsControl);
  // Switch on the LED if an 1 was received as first character
  if (wheelsControl == "stop") {
    stopmov();
  }
  else if (wheelsControl == "front") {
    moveForward();
    delay(200);
    stopmov();
  }
  else if (wheelsControl == "back") {
    moveBack();
    delay(200);
    stopmov();
  }
  else if (wheelsControl == "left") {
    moveLeft();
    delay(200);
    stopmov();
  }
  else if (wheelsControl == "right") {
    moveRight();
    delay(200);
    stopmov();
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
      //client.publish("hiraEyes/connection", "1");
      // ... and resubscribe
      client.subscribe("hiraEyes/roboControl");
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
  pinMode(IN1, OUTPUT);
  pinMode(IN2, OUTPUT);
  pinMode(IN3, OUTPUT);
  pinMode(IN4, OUTPUT);
  pinMode(led, OUTPUT);
  setup_wifi();
  client.setServer(mqtt_server, 1883);
  client.setCallback(callback);


}

void loop() {
// Use Void Loop to display multipule images

  if (!client.connected()) 
  {
    reconnect();
  }
  client.loop();
  

}
void moveForward()
{
  Serial.println("Front");
  digitalWrite(IN1,HIGH);
  digitalWrite(IN2,LOW);
  digitalWrite(IN3,HIGH);
  digitalWrite(IN4,LOW);
}
void moveBack()
{
  Serial.println("Back");
  digitalWrite(IN1,LOW);
  digitalWrite(IN2,HIGH);
  digitalWrite(IN3,LOW);
  digitalWrite(IN4,HIGH);
}
void moveLeft()
{
  Serial.println("Left");
  digitalWrite(IN1,LOW);
  digitalWrite(IN2,HIGH);
  digitalWrite(IN3,HIGH);
  digitalWrite(IN4,LOW);
}
void moveRight()
{
  Serial.println("Right");
  digitalWrite(IN1,HIGH);
  digitalWrite(IN2,LOW);
  digitalWrite(IN3,LOW);
  digitalWrite(IN4,HIGH);
}
void stopmov()
{
  Serial.println("Stopping....");
  digitalWrite(IN1,LOW);
  digitalWrite(IN2,LOW);
  digitalWrite(IN3,LOW);
  digitalWrite(IN4,LOW);
}
