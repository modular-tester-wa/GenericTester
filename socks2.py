#!/usr/bin/env python

__author__ = "Marta Escolar"
__version__ = "0.3"

import socket
import getopt
import sys, string
import time
# import settings
#import RPi.GPIO as GPIO


def SocketConnect(remote_ip, count):
    port=9221
    try:
        c = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    except socket.error:
        print ('Failed to create socket.')
        c.shutdown(1)
        c.close()
        return -1
        # GPIO.cleanup()
        sys.exit()
    try:
        c.connect((remote_ip , port))
    except socket.error as e:
        print("ERROR: ", e)
        print ('failed to connect to ip ' + remote_ip)
        count=count+1
        try:
            SocketClose(c)
        except:
            pass
        if count==5:
            return -1
            # GPIO.cleanup()
            sys.exit()
        time.sleep(1)
        c = SocketConnect(remote_ip, count)
    return c


def SocketQuery(Sock, cmd, who):
    try :
        Sock.sendall(cmd.encode())
    except socket.error:
        print ('Send failed')
    if who=="Multi":
        try:
            reply = Sock.recv(4096)
        except:
            pass
        try:
            Sock.sendall(b'READ?\n')
            reply = Sock.recv(4096)
        except:
            reply=-1
    elif who=="Signal":
        reply = 0
    return reply


def SocketMain(cmd, remote_ip, who):
    count=0
    s = SocketConnect(remote_ip, 0)
    if s==(-1):
        return -1
    qStr = SocketQuery(s, cmd, who)
    SocketClose(s)
    if str(qStr)=="-1":
        return -1
    if who=="Multi":
        qStr = str(qStr)
        if qStr.find("OVLOAD") == -1:
            lon = len(qStr)
            qStr = qStr[2:(lon-5)]
            qStr = qStr[:qStr.find("e")].strip()  # remove all after letter e
        else:
            qStr = "OVLOAD"
    return qStr
    
def SocketClose(Sock):
    Sock.shutdown(1)
    Sock.close()
