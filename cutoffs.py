from socket import *
serverport=12000
serverSocket=socket(AF_INET,SOCK_DGRAM)
serverSocket.bind(('',serverport))
print("The Server is Ready to Recieve")
while True:
    maths,clientAddress=serverSocket.recvfrom(2048)
    physics,clientAddress=serverSocket.recvfrom(2048)
    chemistry,clientAddress=serverSocket.recvfrom(2048)
    M1=maths.decode()
    M2=physics.decode()
    M3=chemistry.decode()
    Marks=int(M1)+(int(M2)/2)+(int(M3)/2)
    Marks=str(Marks)
    print("The Cutoff Marks is {}".format(Marks))
    serverSocket.sendto(Marks.encode(),clientAddress)