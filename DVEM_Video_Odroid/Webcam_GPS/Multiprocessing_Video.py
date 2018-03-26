#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Thu Sep 28 08:12:55 2017

multiprocessing

prozesse werden nacheinander gestartet und abgearbeitet. am ende wartet
mit join das Programm auf den jeweiligen prozess und führt das programm dann weiter

Verschiedene machbare Aufloesungen der Cams:
(176, 144),(320,240),(352,288),(432,240),(544,288),(640,480),(800,448),(864,480) ,(960, 544),(960, 720),(1184, 656), (1280, 960)
"""


import os
import Video_Frame_recored as video
from multiprocessing import Process
import gps_sensor
import server
import obd_recorder

def multiprocessing_3cam_1gps():
    try:
        dir_path = os.path.dirname(os.path.realpath(__file__))
        proc_server=Process(target=server.server,args=('192.168.0.1',55606))
        proc_server.start()
        proc1 = Process(target=video.videoaufzeichnung, args=(320,240,1,dir_path,1000,20))#Fahrer
        proc1.start()
        proc2 = Process(target=video.videoaufzeichnung, args=(960, 544,0,dir_path,1000,80)) #Front
        proc2.start()
        proc3 = Process(target=video.videoaufzeichnung, args=(432,240,2,dir_path,1000,20)) #Heck
        proc3.start()
        proc4=Process(target=gps_sensor.gps_signal, args=())
        proc4.start()
        proc_OBP=Process(target=obd_recorder.startOBD,args=())
        proc_OBP.start()
        print "Please enter"
        userinput=input()
        while True:
            if userinput=="kill":
                proc1.terminate()
                proc2.terminate()
                proc3.terminate()
                proc4.terminate()
                proc_server.terminate()
                proc_OBP.terminate()
                return
            print "Please enter"
            userinput=input()
    except:
            proc1.terminate()
            proc2.terminate()
            proc3.terminate()
            proc4.terminate()
            proc_OBP.terminate()
            proc_server.terminate()
            print "everything is dead"
            return
    #proc_server.join()
if __name__=="__main__":
    multiprocessing_3cam_1gps()

#def One_Kamera():
#    
#    dir_path = os.path.dirname(os.path.realpath(__file__))#legt speicherort fuer frames und log-files fuer kameras im selben ordner an
#    
#    proc1=Process(target=video.videoaufzeichnung, args=(176,144,0,dir_path,1000,90))
#    proc1.start()
#    proc1.join()
#=========
#=Weitere Konfigurationen
#def multiprocessing_2cams():   #Funktionsdef.
#    #1.Step:
#    dir_path = os.path.dirname(os.path.realpath(__file__))
#    
#    #start Process1
#
#    proc1 = Process(target=video.videoaufzeichnung, args=(960,720,0,dir_path,1000))    #(bridth,width,cam_port1,path,frames)
#    proc1.start()
#    
#    #start Process2
#    proc2 = Process(target=video.videoaufzeichnung, args=(960,720,1,dir_path,1000))    #(bridth,width,cam_port2,path,frames)
#    proc2.start()
#    
#    #wait for Process1
#    proc1.join()
#    #wait for Process2
#    proc2.join()
#    
#def multiprocessing_3cams_server_gps(Fahrer_CAM,Heck_CAM,Front_CAM):   #Funktionsdef.
#    #1.Step:
#    dir_path = os.path.dirname(os.path.realpath(__file__))
#    
#    #start proc_server
##    proc_server = Process(target=video.videoaufzeichnung, args=(352,288,0,dir_path,"key",1000,"nein",20))    #(bridth,width,cam_port1,path,frames)
##    proc_server.start()
#    
#    #start proc_gps
#    proc_gps=Process(target=gps_sensor.gps_signal, args=())
#    proc_gps.start()
#    
#    #start proc_driver_camera
#    proc_driver_camera = Process(target=video.videoaufzeichnung, args=(352,288,Fahrer_CAM,dir_path,1000,20))    #(bridth,width,cam_port1,path,frames)
#    proc_driver_camera.start()
#    
#    #start proc_front_camera
#    proc_front_camera = Process(target=video.videoaufzeichnung, args=(352,288,Front_CAM,dir_path,1000,20))    #(bridth,width,cam_port2,path,frames)
#    proc_front_camera.start()
#    
#    #start proc_back_camera
#    proc_back_camera = Process(target=video.videoaufzeichnung, args=(352,288,Heck_CAM,dir_path,1000,20))
#    proc_back_camera.start()
#    #wait for proc_driver_camera,proc_front_camera,proc_back_camera
#    proc_driver_camera.join()
#    proc_front_camera.join()
#    proc_back_camera.join()
#    proc_gps.join()
#    return 
##==================== MAIN =================================
#def multiprocessing_1cam_server():
#        #1.Step:
#    dir_path = os.path.dirname(os.path.realpath(__file__))
#    
#    #start Process1
#    proc1 = Process(target=video.videoaufzeichnung, args=(352,288,0,dir_path,1000,20))    #(bridth,width,cam_port1,path,frames)
#    proc1.start()
#    
#    #start Process2
#    proc2=Process(target=server.server,args=('192.168.0.1',55605))
#    proc2.start()
#    
#    #wait for Proc1, Proc2def multiprocessing_3cams_server():
#    """Funktion fuer Simulatortest"""
#    #1.Step:
#    dir_path = os.path.dirname(os.path.realpath(__file__))
#    
#    #start proc_server
#    proc_server=Process(target=server.server,args=('192.168.0.1',55606))
#    proc_server.start()
#
#    #start proc_driver_camera
#    proc_driver_camera = Process(target=video.videoaufzeichnung, args=(352,288,0,dir_path,2000,20))    #(bridth,width,cam_port1,path,frames)
#    proc_driver_camera.start()
#    
#    #start proc_front_camera
#    proc_front_camera = Process(target=video.videoaufzeichnung, args=(352,288,1,dir_path,2000,20))    #(bridth,width,cam_port2,path,frames)
#    proc_front_camera.start()
#    
#    #start proc_back_camera
#    proc_back_camera = Process(target=video.videoaufzeichnung, args=(352,288,2,dir_path,2000,20))
#    proc_back_camera.start()
#    
#    #wait for proc_driver_camera,proc_front_camera,proc_back_camera
#    proc_driver_camera.join()
#    proc_front_camera.join()
#    proc_back_camera.join()
#    proc_server.join()
#    proc1.join()
#    proc2.join()
#    
#def multiprocessing_3cams_server():
#    """Funktion fuer Simulatortest"""
#    #1.Step:
#    dir_path = os.path.dirname(os.path.realpath(__file__))
#    
#    #start proc_server
##    proc_server=Process(target=server.server,args=('192.168.0.1',55606))
##    proc_server.start()
#
#    #start proc_driver_camera
#    proc_driver_camera = Process(target=video.videoaufzeichnung, args=(352,288,0,dir_path,2000,20))    #(bridth,width,cam_port1,path,frames)
#    proc_driver_camera.start()
#    
#    #start proc_front_camera
#    proc_front_camera = Process(target=video.videoaufzeichnung, args=(352,288,1,dir_path,2000,20))    #(bridth,width,cam_port2,path,frames)
#    proc_front_camera.start()
#    
#    #start proc_back_camera
#    proc_back_camera = Process(target=video.videoaufzeichnung, args=(352,288,2,dir_path,2000,20))
#    proc_back_camera.start()
#    
#    #wait for proc_driver_camera,proc_front_camera,proc_back_camera
#    proc_driver_camera.join()
#    proc_front_camera.join()
#    proc_back_camera.join()
