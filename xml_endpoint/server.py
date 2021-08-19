# Echo server program
import socket
import time

HOST = '127.0.0.1'
PORT = 8000
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((HOST, PORT))
print('Server startup')

s.listen(1)
conn, addr = s.accept()
print ('Connected by', addr)

conn.sendall('Hello, AIsmart!'.encode("ascii"))
print ('Send message')
conn.close()