"""
#########################################################################################
# Author:    Brandon J. Fletcher                                                        #
# E-mail:    brandonjfletcher@gmail.com                                                 #
# GitHub:    https://github.com/bjfletc                                                 #
# File  :    sMessageApp.py is a server-side application to create a messaging app.     #
#                between two users. cMessageApp.py shall be the client-side.            #
#########################################################################################
"""

# Python File Imports:
import SocketServer            # socket module used for opening an internet socket
# import Tkinter               # Tkinter is a GUI module, to later be used

#########################################################################################

# Server-Side Variables

# HOST = "localhost"             # initiate server's host
# PORT = 424242                  # initiate server's port (can be any number)

# Create Server-Side Script

class sMessageApp(SocketServer.BaseRequestHandler):
	"""
	##############################################
        The request handler class for our server.
        ##############################################
	"""

	def handle(self):
		# self.request is the TCP socket connected to the client
		# 1024 below simply means a single line of input data
		self.data = self.request.recv(1024).strip()
		print('{} wrote: '.format(self.client_address[0]))
		print(self.data)

		# going to respond by sending "Ahh... Thank you..."
		self.request.sendall('Ahh... Thank you...')

if __name__ == "__main__":

	HOST = "localhost"             # initiate server's host
	PORT = 04242                   # initiate server's port (can be any number)

	# Create the server, binding it to localhost on port 424242
	server = SocketServer.TCPServer((HOST, PORT), sMessageApp)

	# Activate the server; will run until Ctrl-C
	server.serve_forever()
