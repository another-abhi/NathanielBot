import socket               # Import socket module
import sys
s = socket.socket()         # Create a socket object
host = "13.126.106.19"  # Get local machine name
port = 1234                # Reserve a port for your service.
s.connect((host, port))
while True:
    inp=input("User:")
    s.send(inp.encode('ascii'))
    recv=s.recv(1024)
    if recv=='stop':
        s.close
        sys.exit()
        break
    print ("Nathaniel:",recv.decode('ascii'))
s.close                     # Close the socket when done