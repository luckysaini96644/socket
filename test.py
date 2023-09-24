import socket
import sys
s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

# ip = socket.gethostbyname('www.google.com')
print("Socket Successfully connected")

port = 1234

s.bind(('',port))
print("socket binded to %s" %(port))

s.listen(5)
print("socket is listening")

while True:
    c,addr = s.accept()
    print("got connect  from ",addr)

    c.send("you get terminal".encode())
    c.close()
    break