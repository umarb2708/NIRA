#Set up file to run before running hira
#Update First
sudo apt update
sudo apt upgrade -y


sudo apt install apache2 -y
sudo apt install php libapache2-mod-php -y
sudo apt install mariadb-server php-mysql -y
sudo service apache2 restart

#Need to select Apache2 when installation prompt
sudo apt install phpmyadmin -y