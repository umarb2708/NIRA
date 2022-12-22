#--------------------------------------------------------------------------------------------------------------------------------
#				This file contains Library files need for HIRA to work perfectly 
#--------------------------------------------------------------------------------------------------------------------------------

#------------------Text to Speech--------------------
pip install gTTS

#-------------------Database------------------------
apt install mariadb-server 
pip3 install mysql-connector-python==8.0.29
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
sudo apt-get install portaudio19-dev
pip3 install pyaudio

#-------------Server Info Script---------------------------
#This script should run in every boot: follow https://www.dexterindustries.com/howto/auto-run-python-programs-on-the-raspberry-pi 
#1. Type 'sudo crontab -e' in terminal
#2. Type '@reboot python3 /home/pi/HIRA/server_info.py' at last lane
#3. reboot your pi
#-------------Internet Speed Test--------------------------
pip3 install speedtest-cli

#-------------NGROK for remote DASH------------------------
pip3 install pyngrok

#------------Face Recog Tools---------------------------
# installing dlib 
pip3 install dlib
# installing face recognition
pip install face recognition
#OpenCV  --> Refer: https://mega.nz/file/1rZQQJTL#H_Dqhpi36_lJGMdzExpd2mTWcCucu8MMyhLnmQG__r4
sudo snap install cmake --classic #check gpuMemory not less than 256
wget -O opencv.zip https://github.com/opencv/opencv/archive/4.0.0.zip
wget -O opencv_contrib.zip https://github.com/opencv/opencv_contrib/archive/4.0.0.zip
unzip opencv.zip
unzip opencv_contrib.zip
pip3 install numpy
cd ~/opencv-4.0.0
mkdir build
cd build
cmake -D CMAKE_BUILD_TYPE=RELEASE \
    -D CMAKE_INSTALL_PREFIX=/usr/local \
    -D OPENCV_EXTRA_MODULES_PATH=~/opencv_contrib-4.0.0/modules \
    -D ENABLE_NEON=ON \
    -D ENABLE_VFPV3=ON \
    -D BUILD_TESTS=OFF \
    -D WITH_TBB=OFF \
    -D INSTALL_PYTHON_EXAMPLES=OFF \
    -D BUILD_EXAMPLES=OFF ..
make –j4 #if gives fatal error then give make –j1
sudo apt-get install libopencv-devpython-opencv



#--------------------Whatsapp-------------------
#create API with TWILIO and do the below
pip3 install twilio

#--------------------SFTP-------------------
pip3 install pysftp
