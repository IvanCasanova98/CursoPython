#!/bin/python3

#Primer print
print("String prueba")
print("Hola mundo")
print("""Probando String
de varias lineas """)

print('\n') #new line


#Math

print("Operadores")
print(50 + 50)
print(50 - 50)
print(50 * 50)
print(50 / 50)
print(50 ** 2)
print(50 // 6) #division sin resto

#Variables y metodos
quote= "En la guerra y el amor todo se vale"
print(len(quote))
print(quote.upper())
print(quote.lower())
print(quote.title())

#Funciones


print("Funciones")
def quien_soy():
	name="ivan"
	age=20
	print("Mi nombre es " + name + " y tengo " + str(age) + " años.")

quien_soy()
