#!/bin/bash
sudo apt update
sudo apt install python3-pip cmake
sudo apt install python3-tk libnuma-dev clustershell
pip3 install numpy matplotlib
sudo bash alloc_hugepage.sh