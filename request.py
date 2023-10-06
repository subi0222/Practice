from socket import *
import sys
serverName = '127.0.0.1'
serverPort = 12000
clientSocket = socket(AF_INET, SOCK_STREAM)
clientSocket.connect((serverName, serverPort))
requesetMessage = input(clientSocket.recv(1024).decode())
clientSocket.send(requesetMessage)
method = requesetMessage.split(' ')[0]
