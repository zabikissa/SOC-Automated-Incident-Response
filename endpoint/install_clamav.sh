#!/bin/bash
# Installation et configuration ClamAV sur Ubuntu

sudo apt update && sudo apt upgrade -y
sudo apt install clamav clamav-daemon -y
sudo freshclam
sudo systemctl enable clamav-daemon
sudo systemctl start clamav-daemon
sudo systemctl status clamav-daemon
chmod +x endpoint/install_clamav.sh

