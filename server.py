from audioop import add
import socket

HOST=""
PORT=65432
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as S:
    print("Esperando conexion")
    S.bind((HOST,PORT))
    S.listen()
    conn,addr=S.accept()
    with conn:
        print(f"Conectado al cliente {addr}")
        while True:
            data=conn.recv(1024)
            if not data:
                break
            conn.sendall(data)