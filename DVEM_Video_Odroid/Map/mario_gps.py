# -*- coding: utf-8 -*-
"""
Created on Thu Dec 21 08:02:03 2017

@author: Gustav Willig
"""

import folium
import numpy as np
import pandas as pd
import numpy.ma as ma
import base64
import matplotlib.pyplot as plt
from folium import IFrame
 

#1.Step: read gps_data from txt
txt_gps = open("gustav_gps2.txt")
gps_data=[]

for i in txt_gps:
   line=i.split(",")
   gps_data.append(line)
#2.Step: remove \n from each element 
#gustav=2681
#mario=93
length=290
gps_data.remove(['\n'])
for row in range(0,length):
    row_element= gps_data[row]
    for element in range(0,2):
        gps_data[row][element]=gps_data[row][element].strip("\n")


       
 
resolution, width, height = 75, 7, 3
lon, lat = 9.21006966667, 49.1234218333
map1 = folium.Map(location=[lat, lon], zoom_start=3)
 
encoded = base64.b64encode(open('marker.png', 'rb').read()).decode()
 
html = '<img src="data:image/png;base64,{}">'.format
iframe = IFrame(html(encoded), width=632+20, height=420+20)
popup = folium.Popup(iframe, max_width=2650)


fg=folium.FeatureGroup(name="MyMap")

icon1 = folium.Icon(color="red", icon="ok")

icon2 = folium.Icon(color="red", icon="ok")

#marker = folium.Marker(location=[49.05, 9.20], popup=popup, icon=icon1)
test1=float(gps_data[row][0].strip("'"))
test2=float(gps_data[row][1].strip("'"))

#marker = folium.Marker(location=[test1, test2], popup=popup, icon=icon1)
#fg.add_child(marker);
#2681
for row in range(0,length):
    for element in range(0,1):
       test1=float(gps_data[row][element].strip("'"))
       test2=float(gps_data[row][element+1].strip("'"))
       fg.add_child(folium.Marker(location=[test1,test2], popup="hellO", icon=folium.Icon(color='green')));

map1.add_child(fg)
map1.save("map2.html")



