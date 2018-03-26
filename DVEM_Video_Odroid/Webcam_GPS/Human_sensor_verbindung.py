#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Tue Dec 19 16:50:16 2017

@author: odroid
"""

import pexpect
import os
import time
#=====================
parameter="jago"
humansensor=pexpect.spawn("nc -v 192.168.0.2 4444")
humansensor.sendline('cd //home')
humansensor.sendline('cd //home//odroid//DVEM//maesurement')
humansensor.sendline('python HumanSensorData.py {}'.format(parameter))

#===================== Der nachfolgende Befehl kill den Prozess
#humansensor.send('\003')




