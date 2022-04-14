import socket

HOST="172.17.37.100"
PORT=65432

with socket.socket(socket.AF_INET,socket.SOCK_STREAM) as s:
    s.connect((HOST,PORT))
    s.sendall(b'hola desde cliente')
    data=s.recv(1024)
    print(f"recibido {data!r}")
    