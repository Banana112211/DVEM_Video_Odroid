#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Thu Oct 12 13:34:01 2017

@author: odroid
"""
import serial
def find_gps(i):
    """Find the right ttyACM_Port. It should be normally ttyACM1 or ttyACM02 """
    try:
        gps=""
        gps=serial.Serial("/dev/ttyACM"+str(i),baudrate=9600) 
        return gps,"success"
    except:
        return gps,"false"
    
        
        
