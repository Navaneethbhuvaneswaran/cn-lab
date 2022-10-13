from socket import *
serverName = 'localhost'
serverPort = 12000
clientSocket = socket(AF_INET, SOCK_DGRAM)
clientSocket.connect((serverName, serverPort))
maths = input('Enter the Maths Mark : ')
physics = input('Enter the Physics Mark : ')
chemistry = input('Enter the Chemistry Mark : ')
clientSocket.sendto(maths.encode(), (serverName, serverPort))
clientSocket.sendto(physics.encode(), (serverName, serverPort))
clientSocket.sendto(chemistry.encode(), (serverName, serverPort))
Marks, serverAddress = clientSocket.recvfrom(2048)
print("Cutoff Marks Calculated is ",Marks.decode())
clientSocket.close()