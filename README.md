# bananapi_radio by TechnikAmateur

<img align="right" src="https://github.com/technikamateur/raspido/blob/master/logo/raspido_128px_transparent.png" alt="logo raspido">

### About:
bananapi_radio is a webradio software for the banana pi. It is simply a python3 software to control a mpd server via mpc, while you are using the hardware buttons of the selfbuild radio.

### Installation:
Please make sure, that the following packages are installed. They are necessary to use raspido.
- python3 python3-pip python3-dev
- libfreetype6-dev libjpeg-dev build-essential libopenjp2-7 libtiff5
- mpd
- mpc

In order to run, simply clone this repo and create a file called *"radio_stations.m3u"* in *"/var/lib/mpd/playlists"*, which contains all the mp3 streams of your favourite radio stations.
Now, you are ready to run the `radio.py`. It is helpfull to create a systemd service file to run the radio on startup. Maybe some time, I'll create a small installer script.

### License:
This project is licensed under GPLv3! For more information see *license.txt*.
