#UDP
from socket import *
serverName = '127.0.0.1'
serverPort = 12000
while True:
    clientSocket = socket(AF_INET,SOCK_DGRAM)
    message = input('Enter message to send to server : ')
    clientSocket.sendto(message.encode(),(serverName, serverPort))
    receivedMessage, serverAddress = clientSocket.recvfrom(2048)
    print ('Received message from server : ',receivedMessage.decode())
    clientSocket.close()
