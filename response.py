from socket import *
import sys
serverPort = 12000
serverSocket = socket(AF_INET, SOCK_STREAM)
serverSocket.bind(('', serverPort))
serverSocket.listen(1)
while 1:
    connectionSocket, addr = serverSocket.accept()
    connectionSocket.send("Input request message : ")
    requestBytes = connectionSocket.recv(1024)
    methodMessage = requestBytes.decode().split(' ')[0]
    if methodMessage == 'GET':
        connectionSocket.send('HTTP/0.1 200 OK\n')
        connectionSocket.send("size : ", sys.getsizeof(requestBytes))
    if methodMessage == 
    
