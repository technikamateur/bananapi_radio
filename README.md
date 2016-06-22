# Raspido by TechnikAmateur

<img align="right" src="https://github.com/technikamateur/raspido/blob/master/logo/raspido_128px_transparent.png" alt="logo raspido">
***
[![License](https://img.shields.io/badge/License-GPLv3-green.svg)](http://www.gnu.org/licenses/gpl.html)
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

`chmod +x setup-raspido.sh`

and run it via:

`./setup-raspido.sh`

Follow the steps of the installation script.

### License:
This project is licensed under GPLv3! For more information see *license.txt*.
