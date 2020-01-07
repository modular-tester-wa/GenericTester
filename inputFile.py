#!/usr/bin/env python

__author__ = "Marta Escolar"
__version__ = "0.0"

from time import strftime, gmtime
import numpy as np
import os, shutil
import os.path as path

def InitLogFile(title, file, data, num):
##    date = strftime("%Y%m%d", gmtime())
##    name = date + title
    name = title
    if not path.isfile(name):
        with open(file, 'r') as fil:
            with open(name, 'a') as f:
    ##            f.write("\n-------------------------------------------------------------------\n")
    ##            f.write(strftime("Test Sequence Init Time: %Y-%m-%d %H:%M:%S", gmtime()) + '\n')
    ##            f.write("Configuration Parameters\n")
    ##            f.write(fil.read())
    ##            f.write("-------------------------------------------------------------------\n")
                f.write("Date,Time,Station,Product,Batch,IDUser,Board,")
                for i in range(num):
                    f.write("Test" + str(i+1) + ",")
                f.write("Result,Comments\n")
    return name
    
        
def read_words(filename):
    file=open(filename, 'r')
    f=[]
    line='0,'
    while len(line)>1:
        line=np.array(file.readline().rstrip('\n').split(',')).astype(str)
        if len(line)>1 and (not line.dtype=='<U1'):
            f.append(line)
        else:
            break
    file.close()
    return np.array(f)


def extrac_data_file(file, title):
    data=read_words(file)
    try:
        row, col= data.shape
    except:
        return "ERROR", -4,-4,-4
    name=InitLogFile(title, file, data, row-2)
    data=np.delete(data, 0,0)
    data=np.delete(data, 0,0)
    row, col = data.shape
    column=[]
    for i in range(col):
        column.append(data[:,i])
    return name, column, row, col

    
