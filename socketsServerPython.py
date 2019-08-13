#!/bin/python3

import socket
socket.setdefaulttimeout(2)
s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(("127.0.0.1",6666))
s.listen(5)
print("Servidor Chat\n")

while True:
	print("Esperando Conexion")
	sc, addr = s.accept()
	print("Cliente conectado desde: ", addr)
	
	while True:
		recibido= sc.recv(1024)
		if recibido == "quit":
			break
		print("Mensaje: ", recibido)
		
		respuesta= "Llego el mensaje perro"
		sc.send(respuesta.encode('utf-8'))

print("Chau")
sc.close()
s.close()

