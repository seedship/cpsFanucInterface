# Echo server program
import socket
import time

HOST = '127.0.0.1'
PORT = 65531
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((HOST, PORT))

s.listen(1)
conn, addr = s.accept()
print ('Connected by', addr)

conn.sendall('Hello, AIsmart!'.encode())
print ('Send message')
conn.close()