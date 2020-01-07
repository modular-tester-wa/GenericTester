# -*- coding: utf-8 -*-
import sys
from PyQt5.QtCore import QObject, pyqtSignal, QIODevice
from PyQt5.QtSerialPort import QSerialPort


class Com_port(QObject):
    ser = None
    packet_received = pyqtSignal()
    rx_packet = ""

    def __init__(self, *args, **kwds):
        super(Com_port, self).__init__(kwds.pop('parent'))
        self.ser = QSerialPort(kwds.pop('port'))
        self.ser.open(QIODevice.ReadWrite)
        self.ser.setBaudRate(kwds.pop('baudrate'))
        self.ser.readyRead.connect(self.on_serial_read)
        print("Com port " + self.ser.portName() + ' ready.')

    def process_bytes(self, bs):
        for b in bs:
            self.rx_packet += chr(b)
            if b == 10:
                self.packet_received.emit()

    def on_serial_read(self):
        self.process_bytes(bytes(self.ser.readAll()))

# end of class Com_port


