# Raspido by TechnikAmateur
***
#####Information: Raspido befindet sich momentan noch im Beta Status. Dies bedeutet, dass das Programm Fehler aufweisen kann und möglicherweise nicht ordnugsgemäß funktioniert. Da auf GPIO-Pins zugegriffen wird, kann kann keine Haftung für eventuell beschädigte oder zerstörte Hardware, sowie Software übernommen werden.
***
### Über:
Raspido ist ein Webradio, konzipiert für den Raspberry Pi und Banana Pi. Der Fokus liegt dabei auf Geschwindigkeit und einfache Bedienbarkeit.

Um dies zu gewährleisten, ist Raspido in python und shell programmiert, was eine ressourcenschonende Ausführung ermöglicht. Dazu kommt eine effiziente Datenspeicherung in Form von SQLite3 Datenbanken und als Player dient mpg321, ein effizienter decoder.

Im Moment werden von Raspido allerdings ausschließlich .m3u streams akzeptiert.

### Installation:
Bitte stellen sie sicher, dass folgende Pakete für einen ordnungsgemäßen Betrieb installiert sind:
- mpg321
- curl
- python3
- sqlite3

Dies lässt sich via Terminal nachholen bzw. überprüfen:

`apt-get install mpg321 curl python3 sqlite3`

Anschließend zu *releases* wechseln und die neuste Version downloaden:

`wget (kopierte Linkadresse)`

Nun die Datei ausführbar machen:

`chmod +x raspido.sh`

und ausführen mittels:

`./raspido.sh`

und den Anweisungen des Skripts folgen.

### Lizenz:
GPLv3 für mehr Informationen *"license.txt"* lesen.
