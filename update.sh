#!/bin/bash
version = "1.0"
internet = true
if [ $1 == "check" ]
then
  if [ -f /etc/raspido/raspido.tar.gz ]
  then
    rm raspido.tar.gz
  fi
  echo -e "Checking for Updates..."
  wget --spider --quiet http://technikamateur.bplaced.net
  if [ "$?" != 0 ]
  then
    internet = false
  fi
  if [ $internet == true ]
  then
    update=$(curl --silent --get http://technikamateur.bplaced.net/raspido/raspido_update.php?userversion=$version)
    if [ "$update" == "latest-version" ]
    then
      echo -e "You have got the latest-version!"
    else
      wget --quiet $update
    fi
  else
    echo "Connection to server failed! Are you online?"
  fi
fi
if [ $1 == "update" ] && [ -f /etc/raspido/raspido.tar.gz ]
then
#alle elemente in diesem ordner müssenweg sein
  tar xzf raspido.tar.gz -C /etc/raspido
fi
