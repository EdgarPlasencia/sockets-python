#Importamos las librerias
import socket
from _thread import *
import threading

print_lock = threading.Lock()

#Hilos
def threaded(c):
	while True:

		# Informacion que recive del cliente
		data = c.recv(1024)
		if not data:
			print('Bye')
			
			# Liberar
			print_lock.release()
			break

		data = data[::-1]
		c.send(data)

	#Cerrar conexion
	c.close()


def Main():
    #localhost para el servidor
	host = ""
	port = 12345
	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	s.bind((host, port))
	print("socket binded to port", port)

	#Escuchar
	s.listen(5)
	print("el socket esta escuchando")

	#Bucle para el cliente
	while True:

		#Establecer con el cliente
		c, addr = s.accept()

		# lock acquired by client
		print_lock.acquire()
		print('Connected to :', addr[0], ':', addr[1])

		# Iniciar nuevo hilo y devolver el identificador
		start_new_thread(threaded, (c,))
	s.close()


if __name__ == '__main__':
	Main()
