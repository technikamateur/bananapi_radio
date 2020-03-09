import subprocess

PH = "play3r@192.168.1.112"

mpc = {
    # Playlist leeren
    "clear": "mpc -h " + str(PH) + " clear",
    # Playlist update
    "update": "mpc -h " + str(PH) + " update",
    # Abspielen beginnen
    "play": "mpc -h " + str(PH) + " play ",
    # Abspielen stoppen
    "stop": "mpc -h " + str(PH) + " stop",
    # Sender aus Datei laden
    "loadlist": "mpc -h " + str(PH) + " load radio_sender",
    # Nächter Sender/Song
    "next": "mpc -h " + str(PH) + " next",
    # Vorheriger Sender/Song
    "prev": "mpc -h " + str(PH) + " prev",
    # Playlist zufällig zusammenstellen
    "shuffle": "mpc -h " + str(PH) + " shuffle",
    # Alle MP3 Songs aus diesem Verzeichnis einlesen
    "addmusic": "cd /home/pi/raspiradio/music && mpc -h " + str(PH) + " add *.*",
    # Aktuelle Songinfo/Radioinfo
    "songinfo": "mpc -h " + str(PH) + " current"
}


class Radio:
    _stations = None
    _station_pos = 1

    def init_app(self):
        self._stations = [line.rstrip() for line in open('stations.m3u', 'r')]

    def play_station(self):
        subprocess.run(
            ["mpc", "-h", PH, "play", str(self._station_pos)], shell=False)

    def next_station(self):
        subprocess.run(["mpc", "-h", PH, "next"], shell=False)


Raspido = Radio()
Raspido.init_app()
Raspido.next_station()
