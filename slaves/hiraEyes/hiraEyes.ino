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
#include "eyesdata.h"

#define SCREEN_WIDTH 128
#define SCREEN_HEIGHT 64

Adafruit_SSD1306 display(SCREEN_WIDTH, SCREEN_HEIGHT, &Wire, LED_BUILTIN);


void setup() {
  Serial.begin(9600);
   if(!display.begin(SSD1306_SWITCHCAPVCC, 0x3C)) {
    Serial.println(F("SSD1306 allocation failed"));
    for(;;);
}
 
  delay(2000); // Pause for 2 seconds

  display.clearDisplay();  // Clear the buffer
  display.invertDisplay(1);
// Displays DISTRESSED_EYES on the screen
  //display.drawBitmap(0, 0, epd_bitmap_left_sleep, 128, 64, 1);
  //display.display();
  fullClose();
  display.clearDisplay();  // Clear the buffer
  quaterOpen();
  display.clearDisplay();  // Clear the buffer
  halfOpen();

}

void loop() {
// Use Void Loop to display multipule images
/*
  display.drawBitmap(0, 0, epd_bitmap_left_sleep, 128, 64, 1);
  display.display();
  delay(500); // Pause for half second
  display.clearDisplay();  // Clear the buffer

// Displays EYES_FRONT on the screen
  display.drawBitmap(0, 0, epd_bitmap_Left_Lid_open, 128, 64, 1);
  display.display();

  delay(1500); // Pause for 1.5 seconds
  display.clearDisplay();  // Clear the buffer

// Displays EYES_RIGHT on the screen
  display.drawBitmap(0, 0, epd_bitmap_Left_Middle, 128, 64, 1);
  display.display();
  delay(1500); // Pause for 1.5 seconds*/
  fullOpen();
   display.clearDisplay();  // Clear the buffer
  happy();
   display.clearDisplay();  // Clear the buffer
  sad();
   display.clearDisplay();  // Clear the buffer
  love();
   display.clearDisplay();  // Clear the buffer
  surprized();
   display.clearDisplay();  // Clear the buffer
  deny();
   display.clearDisplay();  // Clear the buffer
  angry();
   display.clearDisplay();  // Clear the buffer
}
void fullClose()
{
  display.drawBitmap(0, 0, epd_bitmap_FullClose, 128, 64, 1);
  display.display();
  delay(1000); // Pause for 1.0 seconds
}
void quaterOpen()
{
  display.drawBitmap(0, 0, epd_bitmap_quaterOpen, 128, 64, 1);
  display.display();
  delay(1000); // Pause for 1.0 seconds
}
void halfOpen()
{
  display.drawBitmap(0, 0, epd_bitmap_HalfOpen, 128, 64, 1);
  display.display();
  delay(1000); // Pause for 1.0 seconds
}
void fullOpen()
{
  display.drawBitmap(0, 0, epd_bitmap_Fullopen, 128, 64, 1);
  display.display();
  delay(1000); // Pause for 1.0 seconds
}
void happy()
{
  display.drawBitmap(0, 0, epd_bitmap_Happy, 128, 64, 1);
  display.display();
  delay(1000); // Pause for 1.0 seconds
}
void sad()
{
  display.drawBitmap(0, 0, epd_bitmap_Sad, 128, 64, 1);
  display.display();
  delay(1000); // Pause for 1.0 seconds
}
void love()
{
  display.drawBitmap(0, 0, epd_bitmap_Love, 128, 64, 1);
  display.display();
  delay(1000); // Pause for 1.0 seconds
}
void surprized()
{
  display.drawBitmap(0, 0, epd_bitmap_Surprised, 128, 64, 1);
  display.display();
  delay(1000); // Pause for 1.0 seconds
}
void deny()
{
  display.drawBitmap(0, 0, epd_bitmap_Deny, 128, 64, 1);
  display.display();
  delay(1000); // Pause for 1.0 seconds
}
void angry()
{
  display.drawBitmap(0, 0, epd_bitmap_AngryRight, 128, 64, 1);
  display.display();
  delay(1000); // Pause for 1.0 seconds
}
// End of Arduino Sketch  