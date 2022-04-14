# importamos el modulo socket
import socket


def Main():
	# local host IP ''
	host = '172.17.37.100'

	# definimos los puertos
	port = 12345

	s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

	# conecccion del servidor :v
	s.connect((host,port))

	# servidor mensaje 
	message = "Hola desde el cliente"
	while True:

		# 
		s.send(message.encode('ascii'))

		# 
		data = s.recv(1024)

		# escribe el mensaje recivido
		# aquí sería un reverso del mensaje enviado
		print('Received from the server :',str(data.decode('ascii')))

		# Preguntar a la clienta si quiere continuar
		ans = input('\nQuieres continuar(y/n) :')
		if ans == 'y':
			continue
		else:
			break
	# close the connection
	s.close()

if __name__ == '__main__':
	Main()
