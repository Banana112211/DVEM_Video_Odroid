


#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Wed Oct  4 14:34:56 2017

@author: odroid
"""

import cv2
import time

def identify_Cam():
    list_webcams=[]
    for j in range(0,10):
      webcam = cv2.VideoCapture(j)
      success,image = webcam.read()
      time.sleep(1 )
      if success==True:
         list_webcams.append(j)
      j += 1
    return list_webcams
 
    