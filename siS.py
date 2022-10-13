from socket import *
serverPort=12000
serverSocket=socket(AF_INET,SOCK_STREAM)
serverSocket.bind(('',serverPort))
serverSocket.listen(1)
print("The server is ready to listen")
while True:
    connectionSocket,addr=serverSocket.accept()
    p=connectionSocket.recv(1024).decode()
    n=connectionSocket.recv(1024).decode()
    r=connectionSocket.recv(1024).decode()
    print("Recieved:","P:",p,"N:",n,"R:",r,sep="\n")
    ans=int(p)*int(n)*int(r)/100
    connectionSocket.send(str(ans).encode())
    connectionSocket.close()