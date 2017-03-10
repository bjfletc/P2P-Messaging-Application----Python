"""
#########################################################################################
# Author:    Brandon J. Fletcher                                                        #
# E-mail:    brandonjfletcher@gmail.com                                                 #
# GitHub:    https://github.com/bjfletc                                                 #
# File  :    cMessageApp.py is a client-side application to create a messaging app.     #
#                between two users. sMessageApp.py shall be the server-side.            #
#########################################################################################
"""

# Python File Imports:
import socket                  # socket module used for opening an internet socket
import sys                     # manages the sending of message for client
# import Tkinter               # Tkinter is a GUI module, to later be used

#########################################################################################

HOST = "localhost"             # client's IP Address
PORT = 04242                   # port of server we are connecting to (sMessageApp)

print('What would you like to send to the server?')

data = raw_input()

# Create socket for communication

cMessageSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
	# try connecting to the server...
	cMessageSocket.connect((HOST, PORT))
	cMessageSocket.sendall(data)

	sMessageResponse = cMessageSocket.recv(1024)
finally:
	cMessageSocket.close()

print('Sent: ' + data)
print('Received: {}'.format(sMessageResponse))