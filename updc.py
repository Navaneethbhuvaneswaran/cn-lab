

from socket import *
servername = '127.0.0.1'
serverport = 12000
clientsocket = socket(AF_INET,SOCK_DGRAM)
message = input('Input lowercase sentence:')
clientsocket.sendto(message.encode(),(servername, serverport))
modifiedmessage, serverAddress = clientsocket.recvfrom(2048)
print ('Uppercase Sentence : ',modifiedmessage.decode())
clientsocket.close()

