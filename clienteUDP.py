#Referencias para el codigo
#https://pythontic.com/modules/socket/udp-client-server-example
import socket

# Create a UDP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

server_address = ('172.17.37.100', 10000)
message = b"hola desde cliente"

try:

    # Send data
    print('sending {!r}'.format(message))
    sent = sock.sendto(message, server_address)

    # Receive responsesci
    print('waiting to receive')
    data, server = sock.recvfrom(1024)
    print('received {!r}'.format(data))

finally:
    print('closing socket')
    sock.close()
