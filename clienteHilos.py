#Referencias del codigo
#April 10, 2022 by Digamber
#https://www.positronx.io/create-socket-server-with-multiple-clients-in-python/
import socket
ClientMultiSocket = socket.socket()
host = '172.17.37.100'
port = 2004
print('Esperando coneccion de respuesta')
try:
    ClientMultiSocket.connect((host, port))
except socket.error as e:
    print(str(e))
res = ClientMultiSocket.recv(1024)
while True:
    Input = input('Hey there: ')
    ClientMultiSocket.send(str.encode(Input))
    res = ClientMultiSocket.recv(1024)
    print(res.decode('utf-8'))
ClientMultiSocket.close()
