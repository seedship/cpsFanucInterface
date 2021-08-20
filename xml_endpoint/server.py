# Echo server program
import socket
import time

HOST = '127.0.0.1'
PORT = 8000
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((HOST, PORT))
print('Server startup')

xml_single_str = r'<?xml version="1.0" encoding="ASCII"?>' \
                 r'<struct_tag int_val="10" float_val="-2.7" string_val="abc"/>'
xml_varlist_str = r'<?xml version="1.0" encoding="ASCII"?>' \
                  r'<list_tag>' \
                  r'<struct_tag int_val="10" float_val="-2.7" string_val="abc"/>' \
                  r'<struct_tag int_val="9" float_val="-2.6" string_val="def"/>' \
                  r'<struct_tag int_val="8" float_val="-2.5" string_val="ghi"/>' \
                  r'</list_tag>'

while(True):
    s.listen(1)
    conn, addr = s.accept()
    print ('Connected by', addr)

    # block until incoming client msg
    msg = conn.recv(1024)
    print(msg)

    conn.sendall(xml_varlist_str.encode("ascii"))
    print ('Send message')