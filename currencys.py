from socket import *
serverport=12000
serverSocket=socket(AF_INET,SOCK_STREAM)
serverSocket.bind(('',serverport))
serverSocket.listen(1)
print("The Server is Ready to Recieve")
while True:
    connectionSocket, addr=serverSocket.accept()
    R=connectionSocket.recv(1024).decode()
    R=int(R)
    D=(R/82)
    P=(R/90)
    print('Entered Indian Rupee in Dollar is ',D)
    print('Entered Indian Rupee in Pound is ',P)
    D=str(D)
    P=str(P)
    connectionSocket.send(D.encode())
    connectionSocket.send(P.encode())
    connectionSocket.close()