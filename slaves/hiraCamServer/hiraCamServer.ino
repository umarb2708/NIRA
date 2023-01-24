
#include <Arduino.h>
#include <WiFi.h>
#include "soc/soc.h"
#include "soc/rtc_cntl_reg.h"
#include "esp_camera.h"
#include <PubSubClient.h>

const char* ssid = "Umar Jio";
const char* password = "Umar@JIO123#";
const char* mqtt_server = "192.168.15.2";
const char* mqtt_user="hiraAdmin";
const char* mqtt_pass="Admin@MQTT123#";
String camControl="sleep";
String serverName = "hira.innovize.in";   // OR REPLACE WITH YOUR DOMAIN NAME
String serverPath = "/FaceRecog/upload-face.php";     // The default serverPath should be upload.php
String httpStatus="";
const int serverPort = 80;
String newHostname="HIRA-CAM";

WiFiClient httpClient;
//WiFiClient mqttClient;
PubSubClient mqttClient(httpClient);
// CAMERA_MODEL_AI_THINKER
#define LED_BUILTIN 4
#define PWDN_GPIO_NUM     32
#define RESET_GPIO_NUM    -1
#define XCLK_GPIO_NUM      0
#define SIOD_GPIO_NUM     26
#define SIOC_GPIO_NUM     27

#define Y9_GPIO_NUM       35
#define Y8_GPIO_NUM       34
#define Y7_GPIO_NUM       39
#define Y6_GPIO_NUM       36
#define Y5_GPIO_NUM       21
#define Y4_GPIO_NUM       19
#define Y3_GPIO_NUM       18
#define Y2_GPIO_NUM        5
#define VSYNC_GPIO_NUM    25
#define HREF_GPIO_NUM     23
#define PCLK_GPIO_NUM     22

const int timerInterval = 30000;    // time between each HTTP POST image
unsigned long previousMillis = 0;   // last time image was sent


void callback(char* topic, byte* payload, unsigned int length) {
  Serial.print("Message arrived [");
  Serial.print(topic);
  Serial.print("] ");
  camControl="";
  for (int i = 0; i < length; i++) {
    Serial.print((char)payload[i]);
    camControl=camControl+(char)payload[i];
  }
  Serial.println();
  //eyeControl=String(payload);
  Serial.print("CamControll:");
  Serial.println(camControl);
  // Switch on the LED if an 1 was received as first character
  if (camControl == "capture") {
    Serial.println("Capturing and sending photo to server");
      digitalWrite(LED_BUILTIN,HIGH);
      sendPhoto();
      digitalWrite(LED_BUILTIN,LOW);
      
  }


}

void reconnect() {
  // Loop until we're reconnected
  while (!mqttClient.connected()) {
    Serial.print("Attempting MQTT connection...");
    // Create a random mqttClient ID
    String clientId = "ESP8266Client-";
    clientId += String(random(0xffff), HEX);
    // Attempt to connect
    if (mqttClient.connect(clientId.c_str(),mqtt_user, mqtt_pass)) {
      Serial.println("connected");
      // Once connected, publish an announcement...
      mqttClient.publish("hiraCam/connection", "1");
      // ... and resubscribe
      mqttClient.subscribe("hiraCam/camControl");
      if(httpStatus!=""){
        httpStatus.trim();
        Serial.println(httpStatus);
        mqttClient.publish("hiraCam/uploadStatus", httpStatus.c_str());
        httpStatus="";
      }
    } else {
      Serial.print("failed, rc=");
      Serial.print(mqttClient.state());
      Serial.println(" try again in 5 seconds");
      // Wait 5 seconds before retrying
      delay(5000);
    }
  }
}

void setup() {
  WRITE_PERI_REG(RTC_CNTL_BROWN_OUT_REG, 0); 
  Serial.begin(115200);
  pinMode (LED_BUILTIN, OUTPUT);
  WiFi.mode(WIFI_STA);
  WiFi.hostname(newHostname.c_str());
  Serial.println();
  Serial.print("Connecting to ");
  Serial.println(ssid);
  WiFi.begin(ssid, password);  
  while (WiFi.status() != WL_CONNECTED) {
    Serial.print(".");
    delay(500);
  }
  Serial.println();
  Serial.print("ESP32-CAM IP Address: ");
  Serial.println(WiFi.localIP());

  camera_config_t config;
  config.ledc_channel = LEDC_CHANNEL_0;
  config.ledc_timer = LEDC_TIMER_0;
  config.pin_d0 = Y2_GPIO_NUM;
  config.pin_d1 = Y3_GPIO_NUM;
  config.pin_d2 = Y4_GPIO_NUM;
  config.pin_d3 = Y5_GPIO_NUM;
  config.pin_d4 = Y6_GPIO_NUM;
  config.pin_d5 = Y7_GPIO_NUM;
  config.pin_d6 = Y8_GPIO_NUM;
  config.pin_d7 = Y9_GPIO_NUM;
  config.pin_xclk = XCLK_GPIO_NUM;
  config.pin_pclk = PCLK_GPIO_NUM;
  config.pin_vsync = VSYNC_GPIO_NUM;
  config.pin_href = HREF_GPIO_NUM;
  config.pin_sscb_sda = SIOD_GPIO_NUM;
  config.pin_sscb_scl = SIOC_GPIO_NUM;
  config.pin_pwdn = PWDN_GPIO_NUM;
  config.pin_reset = RESET_GPIO_NUM;
  config.xclk_freq_hz = 20000000;
  config.pixel_format = PIXFORMAT_JPEG;

  // init with high specs to pre-allocate larger buffers
  if(psramFound()){
    config.frame_size = FRAMESIZE_SVGA;
    config.jpeg_quality = 10;  //0-63 lower number means higher quality
    config.fb_count = 2;
  } else {
    config.frame_size = FRAMESIZE_CIF;
    config.jpeg_quality = 12;  //0-63 lower number means higher quality
    config.fb_count = 1;
  }
  
  // camera init
  esp_err_t err = esp_camera_init(&config);
  if (err != ESP_OK) {
    Serial.printf("Camera init failed with error 0x%x", err);
    delay(1000);
    ESP.restart();
  }
  mqttClient.setServer(mqtt_server, 1883);
  mqttClient.setCallback(callback); 
}

void loop() {
  if (!mqttClient.connected()) 
  {
    reconnect();
  }
  mqttClient.loop();
}

String sendPhoto() {
  String getAll;
  String getBody;

  httpStatus="";
  camera_fb_t * fb = NULL;
  fb = esp_camera_fb_get();
  if(!fb) {
    Serial.println("Camera capture failed");
    delay(1000);
    ESP.restart();
  }
  
  Serial.println("Connecting to server: " + serverName);

  if (httpClient.connect(serverName.c_str(), serverPort)) {
    Serial.println("Connection successful!");    
    String head = "--HiraCam\r\nContent-Disposition: form-data; name=\"imageFile\"; filename=\"esp32-cam.jpg\"\r\nContent-Type: image/jpeg\r\n\r\n";
    String tail = "\r\n--HiraCam--\r\n";

    uint32_t imageLen = fb->len;
    uint32_t extraLen = head.length() + tail.length();
    uint32_t totalLen = imageLen + extraLen;
  
    httpClient.println("POST " + serverPath + " HTTP/1.1");
    httpClient.println("Host: " + serverName);
    httpClient.println("Content-Length: " + String(totalLen));
    httpClient.println("Content-Type: multipart/form-data; boundary=HiraCam");
    httpClient.println();
    httpClient.print(head);
  
    uint8_t *fbBuf = fb->buf;
    size_t fbLen = fb->len;
    for (size_t n=0; n<fbLen; n=n+1024) {
      if (n+1024 < fbLen) {
        httpClient.write(fbBuf, 1024);
        fbBuf += 1024;
      }
      else if (fbLen%1024>0) {
        size_t remainder = fbLen%1024;
        httpClient.write(fbBuf, remainder);
      }
    }   
    httpClient.print(tail);
    
    esp_camera_fb_return(fb);
    
    int timoutTimer = 10000;
    long startTimer = millis();
    boolean state = false;
    
    while ((startTimer + timoutTimer) > millis()) {
      Serial.print(".");
      delay(100);      
      while (httpClient.available()) {
        char c = httpClient.read();
        if (c == '\n') {
          if (getAll.length()==0) { state=true; }
          getAll = "";
        }
        else if (c != '\r') { getAll += String(c); }
        if (state==true) { getBody += String(c); }
        startTimer = millis();
      }
      if (getBody.length()>0) { break; }
    }
    Serial.println();
    httpClient.stop();
    //Serial.println(getBody);
    httpStatus=getBody;

  }
  else {
    getBody = "Connection to " + serverName +  " failed.";
    Serial.println(getBody);
    httpStatus="ERR:CONN";
  }
  return getBody;
}