#!/usr/bin/python           # This is server.py file

import socket               # Import socket module
import time
# simulator ip: 192.168.0.104
# orgin  ip: 192.168.0.1
def server(ip='192.168.0.1',port=55606):
    s = socket.socket()         # Create a socket object
    s.bind((ip, port))        # Bind to the port
    print"server is online"
    while True:
       s.listen(5)                 # Now wait for client connection.
       c, addr = s.accept()     # Establish connection with client
       c.send(str(time.time()))
       c.close()                # Close the connection

if __name__=="__main__":
    #server("192.168.0.104",55606) for simulator
    server()
    