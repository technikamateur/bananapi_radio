#!/bin/bash
version="1.0"
echo -e "Welcome to raspido v$version by Technikamateur!"
echo -e "Press 'enter' to continue setup."; read
echo -e "raspido Copyright (C) 2016 by Daniel Körsten aka TechnikAmateur
This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program.  If not, see <http://www.gnu.org/licenses/>."
echo -e "Press any key if you agree to the license. Press 'ctrl + c' if not."; read
clear
mkdir /etc/raspido
mv raspido /usr/local/bin
chmod a+x /usr/local/bin/raspido
mv main.py /etc/raspido
mv update.sh /etc/raspido
chmod a+x /etc/raspido/update.sh
echo -e "Setup done. You can remove all files in this folder now."
echo -e "Thanks for using raspido!"
