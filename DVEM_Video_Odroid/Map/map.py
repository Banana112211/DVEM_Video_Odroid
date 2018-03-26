import folium
import numpy as np
import pandas as pd
import numpy.ma as ma
import base64
import matplotlib.pyplot as plt
from folium import IFrame
 
txt_gps = open("gps2.txt")
gps_data=[]
for i in txt_gps:
   line=i.split(",")
   gps_data.append(line)
   

 
resolution, width, height = 75, 7, 3

map1=folium.Map(location=[49.1234218333,9.2100], zoom_start=6,tiles="Mapbox Bright")
 
encoded = base64.b64encode(open('marker.png', 'rb').read()).decode()
 
html = '<img src="data:image/png;base64,{}">'.format
iframe = IFrame(html(encoded), width=632+20, height=420+20)
popup = folium.Popup(iframe, max_width=2650)


fg=folium.FeatureGroup(name="MyMap")
icon1 = folium.Icon(color="red", icon="ok")

icon2 = folium.Icon(color="red", icon="ok")

marker = folium.Marker(location=[35.50,9.20], popup=popup, icon=icon1)
fg.add_child(marker);

marker1 = folium.Marker(location=[49.1234218333,9.21006966667], popup="hellO", icon=icon2)
fg.add_child(marker1);

map1.add_child(fg)
map1.save("map1.html")



fg=folium.FeatureGroup(name="My Map")


