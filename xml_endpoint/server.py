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
                  r'<struct_tag int_val="9" float_val="-1.6" string_val="def"/>' \
                  r'<struct_tag int_val="8" float_val="0.5" string_val="ghi"/>' \
                  r'<struct_tag int_val="10" float_val="-2.7" string_val="abc"/>' \
                  r'<struct_tag int_val="9" float_val="-1.6" string_val="def"/>' \
                  r'<struct_tag int_val="8" float_val="0.5" string_val="ghi"/>'\
                  r'<struct_tag int_val="10" float_val="-2.7" string_val="abc"/>' \
                  r'<struct_tag int_val="9" float_val="-1.6" string_val="def"/>' \
                  r'<struct_tag int_val="8" float_val="0.5" string_val="ghi"/>' \
                  r'<struct_tag int_val="10" float_val="-2.7" string_val="abc"/>' \
                  r'<struct_tag int_val="9" float_val="-1.6" string_val="def"/>' \
                  r'<struct_tag int_val="8" float_val="0.5" string_val="ghi"/>' \
                  r'<struct_tag int_val="10" float_val="-2.7" string_val="abc"/>' \
                  r'<struct_tag int_val="9" float_val="-1.6" string_val="def"/>' \
                  r'<struct_tag int_val="8" float_val="0.5" string_val="ghi"/>' \
                  r'<struct_tag int_val="10" float_val="-2.7" string_val="abc"/>' \
                  r'<struct_tag int_val="10" float_val="-2.7" string_val="abc"/>' \
                  r'</list_tag>'

from xml.etree.ElementTree import Element, SubElement, tostring
root = Element('list_tag')
for i in range(15):
     x = SubElement(root, 'struct_tag', {'int_val': str(i), 'float_val': str(-3.5+i), 'string_val': "abc" if i%2==0 else "def"})

print(tostring(root))

rootStr = tostring(root)

while(True):
    print ('Listening')
    s.listen(1)
    conn, addr = s.accept()
    print ('Connected by', addr)
    for x in range(100):
        # block until incoming client msg
        msg = conn.recv(1024)
        print(msg.decode("ascii"))

        conn.sendall(str(rootStr).encode("ascii"))
        print ('Send message')