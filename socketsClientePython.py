#!/bin/python3

import socket

socket_cliente = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
socket_cliente.connect(("127.0.0.1", 6666))

while True:
	mensaje = str(input(">> "))
	socket_cliente.send(mensaje.encode('utf-8'))

	recibido = socket_cliente.recv(1024)
	print("Recibido: ", recibido)


print("Chau")
socket_cliente.close()
