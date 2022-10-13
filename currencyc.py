from socket import *
serverName='127.0.0.1'
serverport=12000
clientSocket=socket(AF_INET,SOCK_STREAM)
clientSocket.connect((serverName,serverport))
R=input("Enter the Money in Rupees(Indian Currency) : ")
clientSocket.send(R.encode())
C1 = clientSocket.recv(1024)
C2=clientSocket.recv(1024)
print(R," Rupee in Dollar is ",C1.decode())
print(R," Rupee in Pound is ",C2.decode())
clientSocket.close()