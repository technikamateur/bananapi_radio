# Raspido by TechnikAmateur
***
##### Important information:
All releases, wich are marked with the tag *beta* are not stable and can damage your hardware.
The usage of raspido is your own risk! Please understand that this Software comes with NO WARRANTY! For more information read *license.txt*.
***
### About:
raspido is a free webradio, disgned for the Rasperry Pi and Banana Pi. It is extremly fast, easy to use and saves a lot of energy, wich leads in low energy consumption because raspido is based on python3, sqlite3, shell and mpg321.

### Installation:
Please make sure, that the following packages are installed. They are necessary to use raspido.
- mpg321
- curl
- python3
- sqlite3

To find out or install the missing packages run the following line in the terminal:

`apt-get install mpg321 curl python3 sqlite3`

On this website go to *releases*, copy the link adress of the latest version and download it:

`wget (copied link adress)`

Now make the setup executable:

`chmod +x setup_raspido.sh`

and run it via:

`./raspido.sh`

Follow the steps of the installation script.

### License:
This project is licensed under GPLv3! For more information see *license.txt*.
