# -*- coding: utf-8 -*-
"""
Created on Tue Oct  3 18:08:16 2017

@author: root
"""

def logfile_schreiben(datensatz,name_txtfile,dir_path):
    with open(dir_path+"/"+name_txtfile+".csv", "a") as myfile:
        myfile.write(datensatz+"\n")
