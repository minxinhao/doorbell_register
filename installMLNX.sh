#!/bin/bash

if [ ! -d "tmp" ]; then
	mkdir tmp
fi


cd tmp
# wget https://content.mellanox.com/ofed/MLNX_OFED-4.9-5.1.0.0/MLNX_OFED_LINUX-4.9-5.1.0.0-ubuntu18.04-x86_64.tgz
# tar -xvf MLNX_OFED_LINUX-4.9-5.1.0.0-ubuntu18.04-x86_64.tgz
# cd MLNX_OFED_LINUX-4.9-5.1.0.0-ubuntu18.04-x86_64

wget https://content.mellanox.com/ofed/MLNX_OFED-23.10-1.1.9.0/MLNX_OFED_LINUX-23.10-1.1.9.0-ubuntu20.04-x86_64.tgz
tar -xvf MLNX_OFED_LINUX-23.10-1.1.9.0-ubuntu20.04-x86_64.tgz
cd MLNX_OFED_LINUX-23.10-1.1.9.0-ubuntu20.04-x86_64

sudo ./mlnxofedinstall  --force
sudo /etc/init.d/openibd restart
sudo /etc/init.d/opensmd restart

# cd ..
# rm -rf tmp