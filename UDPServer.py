from socket import *
serverPort = 12000
serverSocket = socket(AF_INET, SOCK_DGRAM)
serverSocket.bind(('', serverPort))
print("The server is ready to receive")
while True:
    messeage, clientAddress = serverSocket.recvfrom(2040)
    modifiedMessage = messeage.decode().upper()
    serverSocket.sendto(modifiedMessage.encode(), clientAddress)