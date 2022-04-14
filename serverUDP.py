import socket

# Crear un socket UDP
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEPORT, 1)
# Configurar socket
HOST=""
PORT=10000
print(f"Iniciando servidor en port {PORT}")
sock.bind((HOST,PORT))

while True:
    print('\nEsperando mensaje')
    data, address = sock.recvfrom(1024)

    print(f"Conectado al cliente from {address}")
    print(data)

    if data:
        sent = sock.sendto(data, address)
        print(f"Respuesta enviada a {address}")
    
    break
