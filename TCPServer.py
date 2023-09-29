from socket import *
serverPort = 12000
serverSocket = socket(AF_INET, SOCK_STREAM)
serverSocket.bind(('', 12000))
serverSocket.listen(1)
while 1:
    connectionSocket, addr = serverSocket.accept()
    sentence = connectionSocket.recv(1024).decode()
    modifiedSentence = sentence.upper()
    connectionSocket.send(modifiedSentence.encode())
    connectionSocket.close()