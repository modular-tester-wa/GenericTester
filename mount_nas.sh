#!/bin/sh
sudo mount -t cifs -o user=tester_00,password=StateCuba,sec=ntlm,rw,vers=1.0,file_mode=0777,dir_mode=0777 //192.168.201.81/tester_00/log /home/pi/Desktop/GenericTester/log/nas