import socket
import sys
sys.path.append('../')
from DNN_chatbot.chatbot_engine import response
import chatbot_config as cfg
threadList = []

def server():
    print("server:ON")
    serverSocket = socket.socket()
    serverSocket.settimeout(10)
    serverSocket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    serverSocket.setsockopt( socket.IPPROTO_TCP, socket.TCP_NODELAY, 1 )
    host = socket.gethostname() #ip
    port = cfg.port
    serverSocket.bind( (host,port) )
    try:
        serverSocket.listen(cfg.n_connection)
        flag=0
        clientConnection, clientAddress = serverSocket.accept()
        print("recieved connection from :", clientAddress)
        while True:
            msg=str(clientConnection.recv(1024).decode('ascii'))
            print ('Recieved Message : ',msg)
            if msg=="":
                if flag==1:
                    break
                flag=1
                continue
            if msg=="stop":
                clientConnection.send('stop'.encode('ascii'))
                break
            resp=str(response(msg))
            print (resp)
            if(resp!=""):
                clientConnection.send(resp.encode('ascii'))
            else:
                clientConnection.send('empty'.encode('ascii'))
        clientConnection.close()
    except KeyboardInterrupt:
        #serverSocket.shutdown(socket.SHUT_RDWR)
        serverSocket.close()
        sys.exit()
    except socket.timeout:
        print("restarting server")
        print("server:OFF")
        serverSocket.close()    
    finally:
        #serverSocket.shutdown(socket.SHUT_RDWR)
        serverSocket.close()


print ('#######################')
print ('# Nathaniel SERVER #')
print ('#######################')
while True:
    try:
        server()
    except KeyboardInterrupt:
        print ('Stopping server...')
        print ('server:OFF')
        break


