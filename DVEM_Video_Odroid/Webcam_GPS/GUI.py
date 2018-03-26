# -*- coding: utf-8 -*-
"""
Created on Mon Dec 11 17:05:36 2017

@author: odroid
"""
import Tkinter 
from Tkinter import Tk, Label, Button,Text, END, Listbox,BROWSE,MULTIPLE,LEFT
import identify_Cam
import showWebcam
#======0for multiprocessing
import os

import Video_Frame_recored as video
#Import Multiprocessing
from multiprocessing import Process,Queue
import multiprocessing
import gps_sensor
import server
import pexpect
import time
#======
#todo: Änderung von WebcamShow, das ein Parameter übergeben werden kann
       #Änderung von WebcamStart, das Parameter übergeben werden kann

#====Globale Variablen

row_default=0

with_lamp="     "
#====
class MainWindow:
    
    cam_1=None;
    cam_2=None;
    cam_3=None;
    gps_sensor_1=None;
    humansensor=None;
    #humansensor=pexpect.spawn("echo online")#nc -v 192.168.0.2 4444")
    proc_server=None;
    def __init__(self, master):

        self.master = master
        self.master.geometry("700x500")
        master.title("DVEM")
        self.label_Webcams=Label(text="Configuration of webcams",fg = "#E0E0E0",bg = "#18384e",font = "Verdana 15 bold").grid(row=row_default, column=1,columnspan=6, sticky=Tkinter.W)    

        
        List_Cams=identify_Cam.identify_Cam() #Wieder einkommentieren
        #List_Cams=[0]
        self.label_found_Webcams= Label(master, justify=LEFT, text=str(len(List_Cams))+" webcams have been found.\nWebcam input channel (see below).")
        self.label_found_Webcams.grid(row=row_default+1, column=1,columnspan=3,sticky=Tkinter.W)
        self.listbox_webcam = Listbox(master,width=10, height=5, exportselection=1)
        for item in List_Cams:
            self.listbox_webcam.insert(END, item)

        self.Fahrer=Label(text=" Fahrerkamera: ",fg = "black",font = "Verdana 10 bold")
        self.Fahrer.grid(row=row_default+1, column=4,sticky=Tkinter.W)
        self.listbox_Fahrer = Listbox(master,exportselection=False,width=12, height=4)
        for item in List_Cams:
            self.listbox_Fahrer.insert(END, item)
        self.listbox_Fahrer.grid(row=row_default+2, column=4,rowspan=4,sticky=Tkinter.W)

        self.Front=Label(text="Frontkamera: ",fg = "black",font = "Verdana 10 bold")
        self.Front.grid(row=row_default+1, column=5,sticky=Tkinter.W)
        self.listbox_Front = Listbox(master,exportselection=False,width=10, height=4)
        for item in List_Cams:
            self.listbox_Front.insert(END, item)
        self.listbox_Front.grid(row=row_default+2, column=5, rowspan=4,sticky=Tkinter.W)

        self.Heck=Label(text="Heckkamera: ",fg = "black",font = "Verdana 10 bold")
        self.Heck.grid(row=row_default+1, column=6,sticky=Tkinter.W)
        self.listbox_Heck =Listbox(master,exportselection=False,width=10, height=4)
        for item in List_Cams:
            self.listbox_Heck.insert(END, item)
        self.listbox_Heck.grid(row=row_default+2, column=6, rowspan=4,sticky=Tkinter.W)


        
        self.listbox_webcam.grid(row=row_default+2, column=1, rowspan=4,sticky=Tkinter.W)
        self.showWebcam = Button(master, text="ShowWebcam",command=self.show_Webcam).grid(row=row_default+6, column=1,sticky=Tkinter.W)

        self.label_Recording=Label(text="Start recording",fg = "#E0E0E0",bg = "#18384e",font = "Verdana 15 bold").grid(row=row_default+7, column=1)

        self.Label_Status_Web=Label(text="Status Webcams: ",font = "Verdana 10 bold").grid(row=row_default+8, column=1, sticky=Tkinter.W)
        self.Label_Status_Web_2=Label(text=with_lamp,bg = "snow4").grid(row=row_default+8, column=2, sticky=Tkinter.W)
        self.Label_Status_GPS=Label(text="Status GPS: ",font = "Verdana 10 bold").grid(row=row_default+9, column=1, sticky=Tkinter.W)
        self.Label_Status_GPS_2=Label(text=with_lamp,bg = "snow4").grid(row=row_default+9, column=2, sticky=Tkinter.W)
        self.Label_Status_OBD=Label(text="Status OBDBlueth: ",font = "Verdana 10 bold").grid(row=row_default+10, column=1, sticky=Tkinter.W)
        self.Label_Status_OBD_2=Label(text=with_lamp,bg = "snow4").grid(row=row_default+10, column=2, sticky=Tkinter.W)
        self.Label_Status_Human_Sensors=Label(text="Status Human_Sensors: ",font = "Verdana 10 bold").grid(row=row_default+11, column=1, sticky=Tkinter.W)
        self.Label_Status_Human_Sensors_2=Label(text=with_lamp,bg = "snow4",).grid(row=row_default+11, column=2, sticky=Tkinter.W)

        self.button_Start_WEBCAMS_GPS_OBD = Button(master,bg = "#356312",fg="white", text="Start: Webcams, GPS",command=self.StartWEBCAMSGPSOBD).grid(row=row_default+12, column=1,sticky=Tkinter.W)
        self.kill_webcam_gps_button = Button(master,text="Terminate_Webcam_GPS_sensor", command=self.determinate_webcam_gps_sensor).grid(row=row_default+13, column=1,sticky=Tkinter.W)
        self.button_Start_Human_Sensors = Button(master,bg = "#356312",fg="white", text="Start: Human_Sensors,OBD",command=self.StartHumanSensor).grid(row=row_default+15, column=1, sticky=Tkinter.W)
        self.kill_humansensor_button = Button(master,text="Terminate_Human_sensor", command=self.determinate_human_sensor).grid(row=row_default+16, column=1, sticky=Tkinter.W)
        self.close_button = Button(master,text="Close", command=self.close_window).grid(row=row_default+17, column=1, sticky=Tkinter.W)

        self.label_Recording=Label(text="Information",fg = "#E0E0E0",bg = "#18384e",font = "Verdana 15 bold").grid(row=row_default+18, column=1,sticky=Tkinter.W)
        self.gps_data = Button(master,text="Show_GPS_Data", command=self.gps_data).grid(row=row_default+19, column=1, sticky=Tkinter.W)
#Nachfolgende Button noch einbauen       
#        self.close_button = Button(master, text="Close", command=self.close_window).grid(row=3, column=2)  
#        self.textbox=Text(root, height=2, width=30).grid(row=2, column=1)

     
    def show_Webcam(self):
        try:
            self.label_Webcams=Label(text="Please select item",fg = "snow2",bg="snow2",font = "Verdana 15 bold").grid(row=row_default+1, column=2, sticky=Tkinter.W)
            selected_input_channel = self.listbox_webcam.get(self.listbox_webcam.curselection())#Somit bekomt man das Iteam das gerade ausgewählt ist in der Listbox
            showWebcam.showWebcam(selected_input_channel)
            
            
        except:
            self.label_Webcams=Label(text="Please select item",fg = "red",font = "Verdana 15 bold").grid(row=row_default+1, column=2, sticky=Tkinter.W)
        #showWebcam.showWebcam()
    def close_window(self):
         root.destroy()
    
    def determinate_human_sensor(self):
            print "hallochen"
            self.proc_server.terminate()
            i=0
            humansensor2=pexpect.spawn('nc -v 192.168.0.2 4445')
            humansensor2.sendline("killall mate-terminal")            
            self.Label_Status_Human_Sensors_2=Label(text=with_lamp,bg = "snow4",).grid(row=row_default+11, column=2, sticky=Tkinter.W)
    def determinate_webcam_gps_sensor(self):
        self.cam_1.terminate()
        self.cam_2.terminate()
        self.cam_3.terminate()
        self.gps_sensor_1.terminate()

        #Change lamp color
        self.Label_Status_Human_Sensors_2=Label(text=with_lamp,bg = "snow4",).grid(row=row_default+10, column=2, sticky=Tkinter.W)
        self.Label_Status_Web_2=Label(text=with_lamp,bg = "snow4").grid(row=row_default+7, column=2, sticky=Tkinter.W)
        self.Label_Status_GPS_2=Label(text=with_lamp,bg = "snow4").grid(row=row_default+8, column=2, sticky=Tkinter.W)
        self.Label_Status_OBD_2=Label(text=with_lamp,bg = "snow4").grid(row=row_default+9, column=2, sticky=Tkinter.W)
    def StartWEBCAMSGPSOBD(self):
        try:
            self.label_Webcams=Label(text="Please select item",fg = "snow2",bg="snow2",font = "Verdana 15 bold").grid(row=row_default+1, column=2, sticky=Tkinter.W)
            self.Label_Status_Human_Sensors_2=Label(text=with_lamp,bg = "green",).grid(row=row_default+10, column=2, sticky=Tkinter.W)
            self.Label_Status_Web_2=Label(text=with_lamp,bg = "green").grid(row=row_default+7, column=2, sticky=Tkinter.W)
            self.Label_Status_GPS_2=Label(text=with_lamp,bg = "green").grid(row=row_default+8, column=2, sticky=Tkinter.W)
            self.Label_Status_OBD_2=Label(text=with_lamp,bg = "green").grid(row=row_default+9, column=2, sticky=Tkinter.W)
            selected_listbox_Fahrer = self.listbox_Fahrer.get(self.listbox_Fahrer.curselection())
            selected_listbox_Front = self.listbox_Front.get(self.listbox_Front.curselection())
            selected_listbox_Heck = self.listbox_Heck.get(self.listbox_Heck.curselection())
            

            dir_path = os.path.dirname(os.path.realpath(__file__))
            
            

            self.gps_sensor_1=Process(target=gps_sensor.gps_signal, args=(dir_path,))
            self.gps_sensor_1.start()
            self.cam_1 = Process(target=video.videoaufzeichnung, args=(320,240,selected_listbox_Fahrer,40000,20))#Fahrer
            self.cam_1.start()
            self.cam_2 = Process(target=video.videoaufzeichnung, args=(960, 544,selected_listbox_Front,40000,80)) #Front
            self.cam_2.start()
            self.cam_3 = Process(target=video.videoaufzeichnung, args=(432,240,selected_listbox_Heck,40000,20)) #Heck
            self.cam_3.start()
            
        except:
                self.cam_1.terminate()
                self.cam_2.terminate()
                self.cam_3.terminate()
                self.gps_sensor_1.terminate()
                
                print "everything is dead"
    def gps_data(self):
        gps_data_map=pexpect.spawn("chromium-browser map1.html")
        
    def StartHumanSensor(self):
        self.Label_Status_Human_Sensors_2=Label(text=with_lamp,bg = "green",).grid(row=row_default+11, column=2, sticky=Tkinter.W)
        
        
        parameter="gustav"
        self.humansensor=pexpect.spawn('nc -v 192.168.0.2 4444')
        self.humansensor.sendline('cd //home')
        self.humansensor.sendline('cd //home//odroid//Desktop//DVEM_Human_Odroid//maesurement')
        self.humansensor.sendline(str('python HumanSensorData.py '))
        self.proc_server=Process(target=server.server,args=('192.168.0.1',55606))
        self.proc_server.start()
        time.sleep(1)
         
root = Tk()
root.configure(bg="snow2")
my_gui = MainWindow(root)
root.mainloop()
