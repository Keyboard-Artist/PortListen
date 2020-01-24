import socket

# Every function or method is created by the keyword def 
# Following the keyword def is the name of the method
def main():

	# First we need to create a socket obect
	sock = socket.socket()
	sock2 = socket.socket()
	sock3 = socket.socket()
	sock4 = socket.socket()

	# We then get the local hosts name
	host = socket.gethostname()

	# We now set the port we will be using
	port = 22
	port2 = 80
	port3= 443
	port4= 21

	# Next we need to bind the port and reserve it on the system
	sock.bind((host, port))
	sock2.bind((host, port2))
	sock3.bind((host, port3))
	sock4.bind((host, port4))

	# We will now listen for any connection with a max of 5 
	sock.listen(5)
	sock2.listen(5)
	sock3.listen(5)
	sock4.listen(5)

	print('Starting Server!')

	# We now run the while loop to consistantly check for connections and send back a response
	while True:

		# Establish a connection with the client
		client, address = sock.accept()
		client, address1 = sock2.accept()
		client, address2 = sock3.accept()
		client, address3 = sock4.accept()

		print('Connection From {0}'.format(address))
		print('Connection From {0}'.format(address1))
		print('Connection From {0}'.format(address2))
		print('Connection From {0}'.format(address3))

		output = 'Thank you for connecting'
		# We now send data over to the client
		client.sendall(output.encode('utf-8'))

		# We now close the connection
		client.close()




# When running a .py file that specific file willl create a special variable called __name__
# It will set  __name__ to the value __main__ to let the code know this is the file used to 
# Run the python script
if __name__ == '__main__':

	# This will call a function main() that we created above this
	main()