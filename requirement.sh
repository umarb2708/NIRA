#--------------------------------------------------------------------------------------------------------------------------------
#				This file contains Library files need for HIRA to work perfectly 
#--------------------------------------------------------------------------------------------------------------------------------

#------------------Text to Speech--------------------
pip install gTTS

#-------------------Database------------------------
apt install mariadb-server 
pip3 install mysql-connector-python
# Steps to Create Local Database: https://raspberrytips.com/install-mariadb-raspberry-pi/

#------------------Wikipedia--------------------------
pip3 install wikipedia

#-------------------Node REd--------------------------
sudo apt-get install build-essential
bash <(curl -sL https://raw.githubusercontent.com/node-red/linux-installers/master/deb/update-nodejs-and-nodered)
#visit:https://iotdesignpro.com/projects/home-automation-with-node-red-and-raspberry-pi

#---------------MQTT Broker----------------------------
sudo apt install -y mosquitto mosquitto-clients
sudo systemctl enable mosquitto.service

#--------------Android-ADB tool----------------------------
sudo apt install snapd
#reboot
sudo snap install core
sudo snap install android-adb --edge --devmode
pip3 install pure-python-adb

#-------------Speech Recog Module--------------------------
pip3 install SpeechRecognition

#-------------Server Info Script---------------------------
#This script should run in every boot: follow https://www.dexterindustries.com/howto/auto-run-python-programs-on-the-raspberry-pi 

#-------------Internet Speed Test--------------------------
pip3 install speedtest-cli




