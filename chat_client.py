from socket import *

#setup socket to connect to server
serverName = 'localhost'
serverPort = input("Enter port number: ")
serverPort = 43500
clientSocket = socket(AF_INET, SOCK_STREAM) #TCP socket
clientSocket.connect((serverName, serverPort))

#receive message from server, print it, close connection
message = clientSocket.recv(1024).decode('utf-8')
print(message)
sentence = ""
#sentence != "quit"
while True:
	while (clientSocket.recv(1024).decode('utf-8') ==""):
			if (clientSocket.recv(1024).decode('utf-8') !=""):
				break
			sentence = input("You: ")
			if (sentence == "quit"):
				break
			clientSocket.send(sentence.encode('utf-8'))
	if(sentence == "quit"):
		break
	message = clientSocket.recv(1024).decode('utf-8')
	print("Stranger: ", message)

print("Disconnected")
clientSocket.close()
