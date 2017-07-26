'''
	Algoritimo Sequencial que calcula a área de uma função 
	utilizando o metodo numerico denominado Metodo do Trapezio.

	Desenvolvido por: Stella Marques

	Obs.: Caso este codigo ou parte dele seja utilizado por outro programador 
	o nome Stella Azevedo Marques deve ser citado desenvolvedora deste codigo.

	Uma breve explicação sobre o metodo dos Trapezios pode ser encontrada no vídeo disponivel no youtube neste link: 
	https://www.youtube.com/watch?v=mh7QpfupbjI
'''

import math # para exp()
import time

def f(x):
	#return math.exp(x)
	return (x*x)

def main(args):
	# Declaração de variáveis.
	i = 0
	n = 0
	# Limites do intervalo de integração.
	a = 0 
	b = 0
	soma = 0   #Valor do integral.
	h = 0
	x = 0

	#Entrada de dados. 
	print(" ----------- Algoritimo sequencial ----------- \n")
	print("Calculo da Integral de:\n (x*x) no intervalo [a,b] \n\n")
	a = int(input("Introduza limite inferior a = "))
	b = int(input("Introduza limite superior b (b>a) = "))
	#n = int(input("Introduza número de partições do intervalo (n>1) n = "))
	inicio = time.time()
	n = 1000
	#Calcular dimensão de cada partição. 
	h = (b - a) / (n - 1)
	
	#Inicializar x.
	x = a
	
	resultado = 0
	#Ciclo de cálculo.
	for i in range(1,n):
		soma = soma + f(x) + f(x + h)
		x = x + h
	resultado = soma * h / 2
 
	#Escrita do resultado.
	print("O resultado da soma é: ", resultado, "\n")
	fim = time.time()
	print("Tempo de execução do Programa: ",(fim - inicio))
	return 0 

if __name__ == '__main__':
	import sys
	sys.exit(main(sys.argv))
