import folium
import numpy as np
import pandas as pd
import numpy.ma as ma
import base64
import matplotlib.pyplot as plt
from folium import IFrame
 

#1.Step: read gps_data from txt
txt_gps = open("gps2.txt")
gps_data=[]

for i in txt_gps:
   line=i.split(",")
   gps_data.append(line)
#2.Step: remove \n from each element 
gps_data.remove(['\n'])
for row in range(0,2681):
    row_element= gps_data[row]
    for element in range(0,2):
        gps_data[row][element]=gps_data[row][element].strip("\n")


       
 
resolution, width, height = 75, 7, 3
lon, lat = 9.21006966667, 49.1234218333
map1 = folium.Map(location=[lat, lon], zoom_start=5)
 
encoded = base64.b64encode(open('marker.png', 'rb').read()).decode()
 
html = '<img src="data:image/png;base64,{}">'.format
iframe = IFrame(html(encoded), width=632+20, height=420+20)
popup = folium.Popup(iframe, max_width=2650)


fg=folium.FeatureGroup(name="MyMap")

icon1 = folium.Icon(color="red", icon="ok")

icon2 = folium.Icon(color="red", icon="ok")

marker = folium.Marker(location=[49.05, 9.20], popup=popup, icon=icon1)
fg.add_child(marker);




map1.add_child(fg)
map1.save("map1.html")


fg=folium.FeatureGroup(name="My Map")


