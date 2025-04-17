  #ũsr/bin/python3

import sys

def soma(numero1, numero2):

	return numero1 + numero2

def divisao(numero1, numero2):

	try:

		resultado =  numero1 / numero2

	except ZeroDivisionError:

		resultado = "indefinida"

	return resultado

if len(sys.argv) >= 3:

	if sys.argv[1].isdigit() and sys.argv[2].isdigit():

		primeiro_numero = int(sys.argv[1])
		segundo_numero = int(sys.argv[2])

		print("A soma do primeiro número com o segundo é", soma(primeiro_numero, segundo_numero))
		print("A divisão do primeiro número com o segundo é", divisao(primeiro_numero, segundo_numero))

	else:

		print("Os valores precisam ser numericos")

else:

	print("Passe como argumento dois números")

