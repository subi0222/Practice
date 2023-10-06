from socket import *
import sys
servName = '127.0.0.1'
servPort = 12000
clientSocket = socket(AF_INET, SOCK_STREAM)
clientSocket.connect((servName, servPort))
requestUrl = sys.argv[1]
if len(sys.argv) < 2:
    print('URL must be presented')
    sys.exit()
clientSocket.send(requestUrl)
