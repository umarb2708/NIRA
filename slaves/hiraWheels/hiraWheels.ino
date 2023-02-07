#ifdef ESP8266
#include <ESP8266WiFi.h>
#elif defined(ESP32)
#include <WiFi.h>
#else
#error "Board not found"
#endif
#include <PubSubClient.h>

//Relays for switching appliances
/*

 * Appliance       +    NodeMCU    +    ESP-01  
 * ----------------+   pin + gpio  +  pin + gpio-------------
 * Light           |    
 */
#define IN1            14
#define IN2            12
#define IN3            13
#define IN4            15
#define BATT           A0
#define led            16

int sensorValue;          // Analog Output of Sensor
float calibration = 0.20; // Check Battery voltage using multimeter & add/subtract the value
String bat_percentage;
char mqttVal[10];
unsigned long lastMsg = 0;
#define MSG_BUFFER_SIZE  (50)
char msg[MSG_BUFFER_SIZE];
int value = 0;

String newHostname="HIRA-WHEELS";
const char* ssid = "Umar Jio";
const char* password = "Umar@JIO123#";
const char* serverHostname = "hira.local";
const char* username = "hiraWheels";
const char* pass = "Esp@HIRA123#";

//Public Topics
#define pub0 "hiraWheels/battery"
// Subscribed Topics
#define sub1 "hiraWheels/roboControl"

//#define sub2 "hiraWheels/control/right"
//#define sub3 "hiraWheels/control/forward"
//#define sub4 "hiraWheels/control/backward"



WiFiClient espClient;
PubSubClient client(espClient);


// Connecting to WiFi Router

void setup_wifi()
{

  delay(10);
  // We start by connecting to a WiFi network
  Serial.println();
  Serial.print("Connecting to ");
  Serial.println(ssid);

  WiFi.mode(WIFI_STA);
  WiFi.hostname(newHostname.c_str());
  WiFi.begin(ssid, password);


  while (WiFi.status() != WL_CONNECTED) 

  {
    delay(500);
    Serial.print(".");

  }

  randomSeed(micros());

  Serial.println("");
  Serial.println("WiFi connected");
  Serial.print("IP address: ");
  Serial.println(WiFi.localIP());
}


float mapfloat(float x, float in_min, float in_max, float out_min, float out_max)
{
  return (x - in_min) * (out_max - out_min) / (in_max - in_min) + out_min;
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
void callback(char* topic, byte* payload, unsigned int length)
{
  digitalWrite(led, LOW);
  Serial.print("Message arrived [");
  Serial.print(topic);
  Serial.print("] ");
  delay(10);
  digitalWrite(led, HIGH);
  if (strstr(topic, sub1))
  {
    for (int i = 0; i < length; i++)
    {
      Serial.print((char)payload[i]);
    }
    Serial.println();
    if ((char)payload[0] == '0'){
      moveForward();
    } else if ((char)payload[0] == '1'){
      moveBack();
    }else if ((char)payload[0] =='2'){
      moveLeft();
    }else if ((char)payload[0] == '3'){
      moveRight();
    } else {
      stopmov();
    }
  }
}

// Connecting to MQTT broker

void reconnect()
{
  // Loop until we're reconnected
  while (!client.connected()) {
    Serial.print("Attempting MQTT connection...");
    // Create a random client ID

    String clientId = "ESP8266Client-";
    clientId += String(random(0xffff), HEX);
    // Attempt to connect
    if (client.connect(clientId.c_str() , username, pass)) {
      Serial.println("connected");
      // Once connected, publish an announcement...

      client.publish("HIRA-WHEELS", "Connected");

      // ... and resubscribe
      client.subscribe(sub1);
     //client.subscribe(sub4);
    }
    else
    {
      Serial.print("failed, rc=");
      Serial.print(client.state());
      Serial.println(" try again in 5 seconds");
      // Wait 5 seconds before retrying
      digitalWrite(led, LOW);
      delay(1000);
      digitalWrite(led, HIGH);
      delay(1000);
      digitalWrite(led, LOW);
      delay(1000);
      digitalWrite(led, HIGH);
      delay(2000);
    }
  }
}



void setup()
{


  pinMode(IN1, OUTPUT);
  pinMode(IN2, OUTPUT);
  pinMode(IN3, OUTPUT);
  pinMode(IN4, OUTPUT);
  pinMode(led, OUTPUT);
  
  digitalWrite(led, LOW);
  Serial.begin(115200);
  setup_wifi();
  client.setServer(serverHostname, 1883);
  Serial.println("Connected to MQTT server");

 client.setCallback(callback);
 digitalWrite(led, HIGH);
}

void loop()
{


  if (!client.connected())
  {
    reconnect();
  }
      sensorValue = analogRead(BATT);
      float voltage = (((sensorValue * 3.3) / 1024)*2 - calibration);
      bat_percentage = 100-((5.5-voltage)*100);//mapfloat(voltage,5.5 , 4.5, 0, 100);
      bat_percentage.toCharArray(mqttVal, 10);
      Serial.print("voltage  >");
      Serial.println(voltage);
      Serial.print("Battry  >");
      Serial.println(mqttVal);
      client.publish(pub0, mqttVal);
      Serial.println("publishing.....");
      delay(1000);
  client.loop();

}
