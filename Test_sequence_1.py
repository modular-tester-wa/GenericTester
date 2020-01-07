from time import strftime, gmtime

import time
##import RPi.GPIO as GPIO
import settings
import logging
from pymodbus.client.sync import ModbusSerialClient as ModbusClient
from socks2 import SocketMain


__author__ = "Marta Escolar"
__version__ = "1.0"

###############
# Description #
###############
# this file contains every test to create a test squence.
# This file is run as many times as number of test there was in a test sequence.
# Firstly, turn off all relays, just in case.
# It loads all parameter of a single test in test_array.
# Then, it looks for the setup of that test, when it is found, the commands for signal generator, multimeter and relays are saved in variables.
# After that, the relays, signal generator are running and the program jumps to the specific test to know what to do.
# The last thing is to turn off all and to determinate if the test wass PASS or FAIL
###############

# ------------------------------------------------------
# Socket
# ------------------------------------------------------
remote_ip_Signal="192.168.1.100" # Signal generator
remote_ip_Multi="192.168.1.101" # Multimeter
#remote_ip_Signal="169.254.3.206" # Signal generator
#remote_ip_Multi="169.254.3.106" # Multimeter
##remote_ip_Signal="192.168.1.31" # Signal generator
##remote_ip_Multi="192.168.1.32" # Multimeter
#remote_ip_Signal="192.168.3.201"  # Signal generator
#remote_ip_Multi="192.168.3.15" # Multimeter
#remote_ip_Multi="169.254.39.130" # Multimeter
#remote_ip_Multi="169.254.154.156" # Multimeter
#remote_ip_Signal="169.254.63.206" # Signal generator
##remote_ip_Signal="169.254.126.194" # Signal generator
#remote_ip_Multi="169.254.3.106" # Multimeter
#remote_ip_Signal="169.254.252.87" # Signal generator
#remote_ip_Signal="169.254.126.194" # Signal generator
# ------------------------------------------------------


class SGen_parameter ():
    setup=''

def restart_sgen():
    cmd=b'SYNCOUT OFF\nOUTPUT OFF\nZLOAD OPEN\nOUTPUT NORMAL\nBST OFF\nAMPUNIT VRMS\nHILVL 10\nLOLVL 0\n'
    dat=SocketMain(cmd, remote_ip_Signal, "Signal")
    return dat

def ALL_Relays_OFF(tests_arrayX):
    
    log=settings.log
    # Turn OFF relays in every board
    elem=0
    for key, value in zip(addressesName,addressesNumber):
        relay=tests_arrayX.Board[elem]
        if not relay=='':
            relay=relay[::-1]
            for coil in relay:
                coil=(bin(int(coil, 16))[2:])
                coil=coil[::-1]
                for letter in coil:
                    send.append(False)
                for zero in range(4-len(coil)):
                    send.append(False)
            try:
                req = settings.mod.write_coils(0, send, unit=value) 
                assert (not req.isError())
            except Exception as e:
                print("No communication with board: " + key)
                log.debug(e)
                log.debug("No response from board: " + key)
        elem=elem+1


# Here the tests start!!!!.
# 'start_tests' function is called as much as the number of tests the sequence has.
# --------------------------------------------------------
def start_tests(i, NumTest, NumVar, numDUTs, tests_array, x):
    # x is the DUT position in the Nest
    log=settings.log

    print("***********************************************************************")
    print("***********************************************************************")
    print("Test n." + str(tests_array[0].test) + " of " + str(NumTest))
    print("***********************************************************************")
    print("***********************************************************************")

    if str(tests_array[0].status)=="SKIP":
        return ["SKIP","SKIP","SKIP","SKIP"], ["SKIP","SKIP","SKIP","SKIP"]

    # Cheking Signal generator is going to have all its rigth parameters

    # In case of test 32 (DC ramp) the parameters for signal generator have different format
    if tests_array[0].setup == "32":
        if "'s"+tests_array[0].setup+"'" in settings.setups:
            position=settings.setups["'s"+tests_array[0].setup+"'"]
        else:
            settings.setups["'s"+tests_array[0].setup+"'"]=0
            position=settings.setups["'s"+tests_array[0].setup+"'"]
        try:
            aux=getattr(settings, 's'+tests_array[0].setup)
        except:
            return [-4,-4,-4,-4], [-1,-1,-1,-1]
        try:
            arg=(aux[0],aux[position+1])
        except:
            return [-4,-4,-4,-4], [-1,-1,-1,-1]
    else:
        if "'s"+tests_array[0].setup+"'" in settings.setups:
            position=settings.setups["'s"+tests_array[0].setup+"'"]
        else:
            settings.setups["'s"+tests_array[0].setup+"'"]=0
            position=settings.setups["'s"+tests_array[0].setup+"'"]
        try:
            aux=getattr(settings, 's'+tests_array[0].setup)
        except:
            return [-4,-4,-4,-4], [-1,-1,-1,-1]
        
        try:
            arg=(aux[position])
        except:
            return [-4,-4,-4,-4], [-1,-1,-1,-1]
        
    # Detect the setup of the particular test and make the setting of the relays & Signal generator
    if tests_array[0].setup == "21":   # AC signal, Trip Time
        print("AC signal, Trip Time")
        cycles=str(round(2*float(tests_array[0].duration)*float(tests_array[0].freq)/1000)).encode('UTF-8')
        cmd=b'WAVE SINE\nFREQ ' + tests_array[0].freq.encode('UTF-8') + b'\nAMPUNIT VRMS\nAMPL ' + str(arg).encode('UTF-8') + b'\nDCOFFS 0\nBST NCYC\nBSTCOUNT ' + cycles + b'\nSYNCOUT ON\nSYNCTYPE BURST\nTRGSRC MAN\nOUTPUT ON\n*TRG\n'
        cpd = b'IAC;READ?\n'
        settings.setups["'s"+tests_array[0].setup+"'"] += 1

    elif tests_array[0].setup == '22': # AC half wave, Trip Time
        print("AC half wave, Trip Time")
        cycles=str(round(2*float(tests_array[0].duration)*float(tests_array[0].freq)/1000)).encode('UTF-8')
        cmd=b'ARBLOAD ARB1\nDCOFFS 0\nFREQ ' + tests_array[0].freq.encode('UTF-8') + b'\nAMPUNIT VRMS\nAMPL ' + str(arg).encode('UTF-8') + b'\nBST NCYC\nBSTCOUNT ' + cycles + b'\nSYNCOUT ON\nSYNCTYPE BURST\nTRGSRC MAN\nOUTPUT ON\n*TRG\n'
        cpd = b'IACDC;READ?\n'
        settings.setups["'s"+tests_array[0].setup+"'"] += 1
        
    elif tests_array[0].setup == '23': # DC signal (10A), Trip Time
        print("DC signal (10A), Trip Time")
        cmd=b'WAVE PULSE\nDCOFFS ' + str(aux[3]).encode('UTF-8') + b'\nAMPUNIT VRMS\nAMPL ' + str(aux[2]).encode('UTF-8') + b'\nPULSEDGE ' + str(aux[5]).encode('UTF-8') + b'\nPULSWID ' + str(aux[4]).encode('UTF-8') + b'\nPULSFREQ ' + str(aux[1]).encode('UTF-8') + b'\nBST NCYC\nBSTCOUNT 1\nSYNCOUT ON\nSYNCTYPE BURST\nTRGSRC MAN\nOUTPUT ON\n*TRG\n'
        cpd = b'IDC 10A;READ?\n'
        
    elif tests_array[0].setup == '24': # AC signal, Trip/No trip
        print("AC signal, Trip/No trip")            
        cycles=str(round(float(tests_array[0].duration)*float(tests_array[0].freq)/1000)).encode('UTF-8')
        cmd=b'WAVE SINE\nFREQ ' + tests_array[0].freq.encode('UTF-8') + b'\nDCOFFS 0\nAMPUNIT VRMS\nAMPL ' + str(arg).encode('UTF-8') + b'\nBST NCYC\nBSTCOUNT ' + cycles + b'\nSYNCOUT ON\nSYNCTYPE BURST\nTRGSRC MAN\nOUTPUT ON\n*TRG\n'
        cpd = b'IAC 1000MA;READ?\n'
        settings.setups["'s"+tests_array[0].setup+"'"] += 1

    elif tests_array[0].setup == '25': # DC signal, Trip/no trip
        print("DC signal, Trip/no trip")
        if tests_array[0].AFmin[0] == '-':
            cmd=b'WAVE PULSE\nDCOFFS -' + str(float(arg)-0.01).encode('UTF-8') + b'\nAMPUNIT VRMS\nAMPL ' + str(arg).encode('UTF-8') + b'\nPULSFREQ 0.9\nPULSSYMM 95\nPULSEDGE 0.00000001\nBST NCYC\nBSTCOUNT 1\nSYNCOUT ON\nSYNCTYPE BURST\nTRGSRC MAN\nOUTPUT INVERT\nOUTPUT ON\n*TRG\n'
        else:
            cmd=b'WAVE PULSE\nDCOFFS ' + str(float(arg)-0.01).encode('UTF-8') + b'\nAMPUNIT VRMS\nAMPL ' + str(arg).encode('UTF-8') + b'\nPULSFREQ 0.9\nPULSSYMM 95\nPULSEDGE 0.00000001\nBST NCYC\nBSTCOUNT 1\nSYNCOUT ON\nSYNCTYPE BURST\nTRGSRC MAN\nOUTPUT ON\n*TRG\n'
        cpd = b'IDC;READ?\n'
        settings.setups["'s"+tests_array[0].setup+"'"] += 1

    elif tests_array[0].setup == '26': # AC 1kHz, Trip Time
        print("AC 1kHz, Trip Time")
        cycles=str(round(2*float(tests_array[0].duration)*float(tests_array[0].freq)/1000)).encode('UTF-8')
        cmd=b'WAVE SINE\nFREQ ' + tests_array[0].freq.encode('UTF-8') + b'\nAMPUNIT VRMS\nAMPL ' + str(arg).encode('UTF-8') + b'\nDCOFFS 0\nBST NCYC\nBSTCOUNT ' + cycles + b'\nSYNCOUT ON\nSYNCTYPE BURST\nTRGSRC MAN\nOUTPUT ON\n*TRG\n'
        cpd = b'IAC;READ?\n'
        settings.setups["'s"+tests_array[0].setup+"'"] += 1
        
    elif tests_array[0].setup == '27': # Current comsuption
        print("Current comsuption")
        if tests_array[0].PCunit=='mAdc':
            cpd = b'IDC 100MA;READ?\n'
        elif tests_array[0].PCunit=='Adc':
            cpd = b'IDC 1000MA;READ?\n'
        elif tests_array[0].PCunit=='mAac' or tests_array[0].PCunit=='mA':
            cpd = b'IAC 100MA;READ?\n'
        elif tests_array[0].PCunit=='Aac' or tests_array[0].PCunit=='A':    
            cpd = b'IAC 1000MA;READ?\n'
        # If the measurement is by a resistor, we need to look at voltage
        elif tests_array[0].PCunit=='mV' or tests_array[0].PCunit=='mVdc':
            if float(tests_array[0].PCmax)<100:
                cpd = b'VDC 100MV;READ?\n'
            else:
                cpd = b'VDC 1000MV;READ?\n'
        elif tests_array[0].PCunit=='V' or tests_array[0].PCunit=='Vdc':
            if float(tests_array[0].PCmax)<100:
                cpd = b'VDC 1000MV;READ?\n'
            else:
                cpd = b'VDC 100V;READ?\n'
        elif tests_array[0].PCunit=='mVac':
            if float(tests_array[0].PCmax)<100:
                cpd = b'VAC 100MV;READ?\n'
            else:
                cpd = b'VAC 1000MV;READ?\n'
        else:
            if float(tests_array[0].PCmax)<100:
                cpd = b'VAC 1000MV;READ?\n'
            else:
                cpd = b'VAC 100V;READ?\n'
        
    elif tests_array[0].setup == '28': # Measure Voltage
        print("Measure Voltage")
        if tests_array[0].PCunit=='mV' or tests_array[0].PCunit=='mVdc':
            if float(tests_array[0].PCmax)<100:
                cpd = b'VDC 100MV;READ?\n'
            else:
                cpd = b'VDC 1000MV;READ?\n'
        elif tests_array[0].PCunit=='V' or tests_array[0].PCunit=='Vdc':
            if float(tests_array[0].PCmax)<100:
                cpd = b'VDC 1000MV;READ?\n'
            else:
                cpd = b'VDC 100V;READ?\n'
        elif tests_array[0].PCunit=='mVac':
            if float(tests_array[0].PCmax)<100:
                cpd = b'VAC 100MV;READ?\n'
            else:
                cpd = b'VAC 1000MV;READ?\n'
        else:
            if float(tests_array[0].PCmax)<100:
                cpd = b'VAC 1000MV;READ?\n'
            else:
                cpd = b'VAC 100V;READ?\n'
        
    elif tests_array[0].setup == '29': # 1 full half cycle (inrush test), trip/No trip
        print("1 full half cycle (inrush test), trip/No trip")
        cycles=str(round(float(tests_array[0].duration)*float(tests_array[0].freq)/1000)).encode('UTF-8')
        cmd=b'ARBLOAD ARB1\nDCOFFS 0\nAMPUNIT VRMS\nAMPL ' + str(arg).encode('UTF-8') + b'\nFREQ ' + str(tests_array[0].freq).encode('UTF-8') + b'\nBSTPHASE 0\nBST NCYC\nBSTCOUNT 1\nSYNCTYPE BURST\nSYNCOUT ON\nTRGSRC MAN\nOUTPUT ON\n*TRG\n'
        cpd = b'IAC;READ?\n'
        settings.setups["'s"+tests_array[0].setup+"'"]+=1
        
    elif tests_array[0].setup == '30': # Test winding. Trip/No Trip
        print("Test winding. Trip/No Trip")
        rele=tests_array.RelayWord[x]
        cmd=b'AMPUNIT VRMS\nHILVL 10\nLOLVL 0\nWAVE SINE\nFREQ 0.25\nBSTPHASE 0\nBST NCYC\nBSTCOUNT 1\nSYNCTYPE BURST\nSYNCOUT ON\nTRGSRC MAN\nOUTPUT OFF\n*TRG\n'
        #cmd=b'WAVE SINE\nFREQ 0.25\nBSTPHASE 0\nBST NCYC\nBSTCOUNT 1\nSYNCTYPE BURST\nSYNCOUT ON\nTRGSRC MAN\nOUTPUT ON\n*TRG\n'
        cpd = b'IDC 1000MA;READ?\n'
        settings.setups["'s"+tests_array[0].setup+"'"]+=1
        
    elif tests_array[0].setup == "31": # DC signal, Trip Time
        print("DC signal, Trip Time")
        print(arg)
        if settings.setups["'s"+tests_array[0].setup+"'"] == 0 or settings.setups["'s"+tests_array[0].setup+"'"] % 2 == 0:
            cmd=b'AMPUNIT VRMS\nHILVL 10\nLOLVL 0\nWAVE PULSE\nDCOFFS ' + str(float(arg)).encode('UTF-8') + b'\nAMPUNIT VRMS\nAMPL 0.01\nPULSFREQ 0.9\nPULSSYMM 95\nPULSEDGE 0.00000001\nBST NCYC\nBSTCOUNT 1\nSYNCOUT ON\nSYNCTYPE BURST\nTRGSRC MAN\nOUTPUT ON\n*TRG\n' 
        else:
            cmd=b'AMPUNIT VRMS\nHILVL 10\nLOLVL 0\nWAVE PULSE\nDCOFFS -' + str(float(arg)).encode('UTF-8') + b'\nAMPUNIT VRMS\nAMPL 0.01\nPULSFREQ 0.9\nPULSSYMM 95\nPULSEDGE 0.00000001\nBST NCYC\nBSTCOUNT 1\nSYNCOUT ON\nSYNCTYPE BURST\nTRGSRC MAN\nOUTPUT INVERT\nOUTPUT ON\n*TRG\n'
        cpd = b'IDC 100MA;READ?\n'
        settings.setups["'s"+tests_array[0].setup+"'"] += 1
            
    elif tests_array[0].setup == "32": # DC ramp. Trip Level
        print("DC ramp. Trip Level")
        rele=tests_array[i].RelayWord[x]
        newvalue=(arg[1][0])
        period=float(tests_array[0].PCmax)-float(tests_array[0].PCmin)
        if period<0:
            period=period*(-1)
        dur_period=(period*(1-(2/(arg[0])))+2)+arg[0]*0.3
        if tests_array[0].PCmin[0]  == '-': # To know if the ramp is positive or negative
            cmd=b'WAVE PULSE\nAMPUNIT VRMS\nLOLVL 0\nHILVL 0.02\nDCOFFS -' + str(newvalue).encode('UTF-8') + b'\nPULSPER ' + str(dur_period).encode('UTF-8') + b'\nPULSSYMM 99\nPULSEDGE 0.00000001\nBST NCYC\nBSTCOUNT 1\nSYNCOUT ON\nSYNCTYPE BURST\nTRGSRC MAN\nOUTPUT INVERT\nOUTPUT ON\n*TRG\n'
            #cmd=b'WAVE PULSE\nAMPUNIT VRMS\n\nLOLVL 0\nDCOFFS -' + str(newvalue).encode('UTF-8') + b'\nAMPL ' + str(newvalue).encode('UTF-8') + b'\nPULSFREQ 0.1\nPULSSYMM 95\nPULSEDGE 0.00000001\nBST NCYC\nBSTCOUNT 1\nSYNCOUT ON\nSYNCTYPE BURST\nTRGSRC MAN\nOUTPUT INVERT\nOUTPUT ON\n*TRG\n'
            
            #cmd=b'SYNCOUT OFF\nOUTPUT OFF\nZLOAD OPEN\nOUTPUT NORMAL\nBST OFF\n\nHILVL 10\nLOLVL 0\nZLOAD OPEN\nWAVE PULSE\nAMPUNIT VRMS\nDCOFFS -' + str(newvalue).encode('UTF-8') + b'\nAMPL ' + str(newvalue).encode('UTF-8') + b'\nPULSFREQ 0.1\nPULSSYMM 95\nPULSEDGE 0.00000001\nBST NCYC\nBSTCOUNT 1\nSYNCOUT ON\nSYNCTYPE BURST\nTRGSRC MAN\nOUTPUT INVERT\nOUTPUT ON\n*TRG\n'
        else: # OK, it-s positive
            cmd=b'WAVE PULSE\nAMPUNIT VRMS\nLOLVL 0\nHILVL ' + str(newvalue).encode('UTF-8') + b'\nPULSPER ' + str(dur_period).encode('UTF-8') + b'\nPULSSYMM 99\nPULSEDGE 0.00000001\nBST NCYC\nBSTCOUNT 1\nSYNCOUT ON\nSYNCTYPE BURST\nTRGSRC MAN\nOUTPUT ON\n*TRG\n'
            #cmd=b'WAVE PULSE\nAMPUNIT VRMS\nLOLVL 0\nHILVL ' + str(newvalue).encode('UTF-8') + b'\nPULSPER ' + str(float(tests_array.duration)/1000).encode('UTF-8') + b'\nPULSSYMM 95\nPULSEDGE 0.00000001\nBST NCYC\nBSTCOUNT 1\nSYNCOUT ON\nSYNCTYPE BURST\nTRGSRC MAN\nOUTPUT ON\n*TRG\n'
        cpd = b'IDC 100MA;READ?\n'
        settings.setups["'s"+tests_array[0].setup+"'"] += 1

        
    elif tests_array[0].setup == "33": # DC signal. Trip Time
        print("DC signal. Trip Time")
        if settings.setups["'s"+tests_array[0].setup+"'"] == 0:
            cmd=b'WAVE PULSE\nDCOFFS ' + str(float(arg)-0.01).encode('UTF-8') + b'\nAMPUNIT VRMS\nAMPL ' + str(arg).encode('UTF-8') + b'\nPULSFREQ 0.9\nPULSSYMM 95\nPULSEDGE 0.00000001\nBST NCYC\nBSTCOUNT 1\nSYNCOUT ON\nSYNCTYPE BURST\nTRGSRC MAN\nOUTPUT ON\n*TRG\n'
        else:
            cmd=b'WAVE PULSE\nDCOFFS -' + str(float(arg)-0.01).encode('UTF-8') + b'\nAMPUNIT VRMS\nAMPL ' + str(arg).encode('UTF-8') + b'\nPULSFREQ 0.9\nPULSSYMM 95\nPULSEDGE 0.00000001\nBST NCYC\nBSTCOUNT 1\nSYNCOUT ON\nSYNCTYPE BURST\nTRGSRC MAN\nOUTPUT INVERT\nOUTPUT ON\n*TRG\n'
        cpd = b'IDC 1000MA;READ?\n'
        settings.setups["'s"+tests_array[0].setup+"'"]+=1

    elif tests_array[0].setup == "34": # AC 135 wave, Trip Level
        print("AC 135 wave, Trip Time")
        cycles=str(round(2*float(tests_array[0].duration)*float(tests_array[0].freq)/1000)).encode('UTF-8')
        cmd=b'ARBLOAD ARB2\nDCOFFS 0\nFREQ ' + tests_array[0].freq.encode('UTF-8') + b'\nAMPUNIT VRMS\nAMPL ' + str(arg).encode('UTF-8') + b'\nBST NCYC\nBSTCOUNT ' + cycles + b'\nSYNCOUT ON\nSYNCTYPE BURST\nTRGSRC MAN\nOUTPUT ON\n*TRG\n'
        cpd = b'IACDC;READ?\n'
        settings.setups["'s"+tests_array[0].setup+"'"]+=1
        
    elif tests_array[0].setup == "35": # AC ramp. Trip Level
        print("AC ramp. Trip Level")
        rele=tests_array[i].RelayWord[x]
        newvalue=(arg)
        cycles=str(round(2*float(tests_array[0].duration)*float(tests_array[0].freq)/1000)).encode('UTF-8')
        cmd=b'WAVE SINE\nFREQ ' + tests_array[0].freq.encode('UTF-8') + b'\nAMPUNIT VRMS\nDCOFFS 0\nAMPL ' + str(newvalue).encode('UTF-8') + b'\nBST NCYC\nBSTCOUNT ' + cycles + b'\nSYNCOUT ON\nSYNCTYPE BURST\nTRGSRC MAN\nOUTPUT ON\n*TRG\n'
        cpd = b'IAC 100MA;READ?\n'
        settings.setups["'s"+tests_array[0].setup+"'"]+=1

    elif tests_array[0].setup == "36": # Measure Freq.
        print("Measure Freq.")
        rele=tests_array[i].RelayWord[x]
        newvalue=(arg)
        cmd=b'BSTCOUNT 1\nSYNCOUT ON\nSYNCTYPE BURST\nTRGSRC MAN\nOUTPUT ON\n*TRG\n'
        cpd = b'FREQ 1000HZ;READ?\n'
        
    elif tests_array[0].setup == "37": # Continuity.
        print("Continuity")
        rele=tests_array[i].RelayWord[x]
        newvalue=(arg)
        cmd=b'BSTCOUNT 1\nSYNCOUT ON\nSYNCTYPE BURST\nTRGSRC MAN\nOUTPUT ON\n*TRG\n'
        cpd = b'CONT;READ?\n'

    elif tests_array[0].setup == "39":   # Programming ST microcontroller
        rele=tests_array[i].RelayWord[x]
        print("Programming ST microcontroller")
        flash_cmd="/home/pi/stm8flash/stm8flash -c stlink -p stm8s003f3 -w "+str(os.getcwd().split()[-1])+"/HEX/" + tests_array[0].AFmin #04836FIRMB.HEX

    else:
        rele='0x000000'
        print("ERROR: wrong Setup Number")
        cmd=b'SYNCOUT OFF\nOUTPUT OFF\nZLOAD OPEN\nOUTPUT NORMAL\nBST OFF\nAMPUNIT VRMS\nHILVL 10\nLOLVL 0\n'

    #---------------------------------------------------------------------------------------------------   
    dur=(float(tests_array[0].duration))/1000 # Dur= duration of a test
    count=0

    print("Turn relays for test")
    elem=0
    # Turn relays in every board
    for key,value in zip(settings.addressesName,settings.addressesNumber):
        send=[]
        relay=tests_array[x].Board[elem] # x is DUT to test
        try:
            relay=int(relay)
            if relay>0:

                relay=relay[::-1]
                for coil in relay:
                    coil=(bin(int(coil, 16))[2:])
                    coil=coil[::-1]
                    for letter in coil:
                        if letter=="1":
                            send.append(True)
                        else:
                            send.append(False)
                    for zero in range(4-len(coil)):
                        send.append(False)

                try:
                    req = settings.mod.write_coils(0, send, unit=value) 
                    assert (not req.isError())
                except Exception as e:
                    print("No communication with board: " + key)
                    log.debug(e)
                    log.debug("No response from board: " + key)
        except:
            pass
        elem=elem+1
                    
   ################### SETUP 21, 22, 23, 24, 25, 26, 29, 31, 33, 34 ##################
    if tests_array[0].setup=="21" or tests_array[0].setup=="22" or tests_array[0].setup=="23" or tests_array[0].setup=="26" or tests_array[0].setup =="31" or tests_array[0].setup =="33" or tests_array[0].setup =="34":
        # Active s.generator
        dat=SocketMain(cmd, remote_ip_Signal, "Signal")
        if dat==-1: # It's any problem with communitacion, turn off relays and exit!!
            print("Communication Error, parallel test")
            return [-1,-1,-1,-1], [-1,-1,-1,-1]   # Communication => fail
        TTime=[0,0,0,0]
        dut_read=[0,0,0,0]

        #If the interlock is close, wait here for the sync signal
        while (not(GPIO.input(16)) and settings.interlock==0 and count<1000000):
               count=count+1 # Count is the timeout, just in case
        if count>=1000000:  # In case the sync signal never arrives
            restart_sgen()
            print("Trigger Error")
            return [-3,-3,-3,-3], [-1,-1,-1,-1]   # Trigger => fail

        start=time.time()
        while ((dur)>(time.time()-start)):
            pass

        for key , value in zip(settings.addressesName,settings.addressesNumber):
            if 'ndb' in key:
                nDUT=0
                try:
                    req = settings.mod.read_holding_registers(0, 1, unit=value) 
                    assert (not req.isError())
                    TTime[nDUT] = req.registers[0] / 10
                    str_trip_time = str(trip_time) 
                except Exception as e:
                    TTime[nDUT]=0
                    print("No communication with board: " + key)
                    log.debug(e)
                    log.debug("No response from board: " + key)
                nDUT=nDUT+1
            
        settings.flag=0
        #---------------------------------------------------------------------------------------------------
        # Send to Signal generator to turn OFF
        restart_sgen()

        # Turn OFF relays in every board
        ALL_Relays_OFF(tests_array[x])
        if dat==-1:
            return [-1,-1,-1,-1], [-1,-1,-1,-1]   # Communication => fail
                                                                
        # Compare the measured time with pass criteria
        # TRIP TIME                                                        
        if tests_array[0].setup=="21" or tests_array[0].setup=="22" or tests_array[0].setup=="23" or tests_array[0].setup=="26" or tests_array[0].setup =="31" or tests_array[0].setup =="33":
            print("Which time we recieved: ", TTime)
            for count_dut in range(4):                
                if (float(tests_array[0].PCmax)/1000)>float(TTime[count_dut]) and ((float(tests_array[0].PCmin))/1000)<float(TTime[count_dut]):
                    result[count_dut]="PASS"
                    result1[count_dut]=TTime[count_dut]
                else:
                    result[count_dut]="FAIL"
                    if dur==float(TTime[count_dut]):
                        result1[count_dut]="NO TRIP"
                    else:
                        result1[count_dut]=TTime[count_dut]
            return result, result1

        # TRIP/NOT TRIP
        else:
            for count_dut in range(4):
                if TTime[count_dut]==0:
                    result[count_dut]="FAIL"
                    result1[count_dut]=0
                else:
                    if dur>float(TTime[count_dut]):
                        if tests_array[0].PCmin=="NO TRIP":
                            result[count_dut]="FAIL"
                            result1[count_dut]=TTime[count_dut]
                        else:
                            result[count_dut]="PASS"
                            result1[count_dut]=TTime[count_dut]
                    else:
                        if tests_array[0].PCmin=="TRIP":
                            result[count_dut]="FAIL"
                            result1[count_dut]='NO TRIP'
                        else:
                            result[count_dut]="PASS"
                            result1[count_dut]="NO TRIP"
            return result, result1
                                                                
            
   ################### SETUP 27 ##################
    if tests_array[0].setup=="27":
        # Taking measurement            
        result1=1
        result1=SocketMain(cpd, remote_ip_Multi, 'Multi')   #Read multimeter
        if result1=="OVLOAD":
            if 'Adc' in tests_array[0].PCunit:
                cpd = b'IDC;READ?\n'
            elif 'Aac' in tests_array[0].PCunit:
                cpd = b'IAC;READ?\n'
            # If the measurement is by a resistor, we need to look at voltage
            elif 'Vdc' in tests_array[0].PCunit:
                cpd = b'VDC;READ?\n'
            else:
                cpd = b'VAC;READ?\n'
            result1=SocketMain(cpd, remote_ip_Multi, 'Multi')   #Read multimeter
        if result1==-1: # It's any problem with communitacion, exit!!
            print("Communication Error, serial test")
            return [-1,-1,-1,-1], [-1,-1,-1,-1]   # Communication => fail 
        lon=len(result1)
        if lon<6:
            result1=0
        else:
            result1=float(result1[1:(lon-5)])   # Take only a part of the string
        print("Current comsuption is: ",result1)
        # Compare the result with pass criteria
        if (float(tests_array[0].PCmax)/1000)>result1 and ((float(tests_array[0].PCmin))/1000)<result1:
            print(" Result : PASS")
            result="PASS"
        else:
            print("Result : FAIL")
            result="FAIL"
        # Turn off dut board
        elem=0
        for key , value in zip(settings.addressesName,settings.addressesNumber):
            if 'ndb' in key:
                send=[]
                relay=tests_array[x].Board[elem]
                if not relay=='':
                    relay=relay[::-1]
                    for coil in relay:
                        coil=(bin(int(coil, 16))[2:])
                        coil=coil[::-1]
                        for letter in coil:
                            send.append(False)
                        for zero in range(4-len(coil)):
                            send.append(False)
                    try:
                        req = settings.mod.write_coils(0, send, unit=value) 
                        assert (not req.isError())
                    except Exception as e:
                        print("No communication with board: " + key)
                        log.debug(e)
                        log.debug("No response from board: " + key)
            elem=elem+1
                        
        return result, result1
    
        ################### SETUP 28 ##################
    if tests_array[0].setup=="28":
        print("Taking measurement")
        # Taking measurement
        result1=1
        result1=SocketMain(cpd, remote_ip_Multi, 'Multi') #Read multimeter
        if result1=="OVLOAD":
            if 'Vdc' in tests_array[0].PCunit:
                cpd = b'VDC;READ?\n'
            else:
                cpd = b'VAC;READ?\n'
            result1=SocketMain(cpd, remote_ip_Multi, 'Multi')   #Read multimeter
        if result1==-1: # It's any problem with communitacion, turn off relays and exit!!
            print("Communication Error, serial test")
            return [-1,-1,-1,-1], [-1,-1,-1,-1]   # Communication => fail
        lon=len(result1)
        if lon<6:
            result1=0
        else:
            result1=float(result1[1:(lon-5)]) # Take only a part of the string
        
        if tests_array[0].PCunit=='mV':
            change_unit=1000
        else:
            change_unit=1

        print("Compare the result with pass criteria")
        # Compare the result with pass criteria
        if (float(tests_array[0].PCmax)/change_unit)>result1 and ((float(tests_array[0].PCmin))/change_unit)<result1:
            print("Result : PASS")
            result="PASS"
        else:
            print("Result : FAIL")
            result="FAIL"
##            result1=5.0
        print(" Turn off dut board")
        # Turn off dut board
        elem=0
        for key , value in zip(settings.addressesName,settings.addressesNumber):
            if 'ndb' in key:
                send=[]
                relay=tests_array[x].Board[elem]
                if not relay=='':
                    relay=relay[::-1]
                    for coil in relay:
                        coil=(bin(int(coil, 16))[2:])
                        coil=coil[::-1]
                        for letter in coil:
                            send.append(False)
                        for zero in range(4-len(coil)):
                            send.append(False)
                    try:
                        req = settings.mod.write_coils(0, send, unit=value) 
                        assert (not req.isError())
                    except Exception as e:
                        print("No communication with board: " + key)
                        log.debug(e)
                        log.debug("No response from board: " + key)
            elem=elem+1
            
        return result, result1                
