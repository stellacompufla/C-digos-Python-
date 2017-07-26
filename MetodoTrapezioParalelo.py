'''
	Algoritmo Paralelo Para Derivação utilizando o Metodo dos Trapezios

	Desenvolvido por: Stella Marques

	Obs.: Caso este codigo ou parte dele seja utilizado por outro programador 
	o nome Stella Azevedo Marques deve ser citado desenvolvedora deste codigo.

	Uma breve explicação sobre o metodo dos Trapezios pode ser encontrada no vídeo disponivel no youtube neste link: 
	https://www.youtube.com/watch?v=mh7QpfupbjI
'''

import math       # para exp()
import threading
import time

#Vetor que ira receber o resultado de cada Trhead
vet = []
#Numero de Threads a ser geradas
tamThread = 100
#a - ponto inicial, b - ponto final
a = 0
b = 0
#aumenta ou diminui o numero de intevalos em cada Trhead
n = 10
#altura do trapezio global
h = 0
#Conta o numero de Threads que são criadas, e mostra o numero dela na tela (variavel de controle e debug)
contadorThread = 0

#Função a ser calculada
def f(x):
	return (x*x)
	#return ((x*x)+(2*x)+x)

#Função que gera as Trheads
def chamaTrhead(a,b):
	global n, contadorThread
	h = (b - a)/(n - 1)
	x = a
	soma = 0
	#Parte do codigo onde é calculado a area de cada trapezio global
	for i in range(1,n):
		soma = soma + f(x) + f(x + h)
		x = x + h
	soma = soma * h / 2
	vet.append(soma) 
	contadorThread += 1
	print ("Thread ",contadorThread," é: ",soma)
 
def main(args):
	
	#Entrada de dados. 
	print(" ----------- Algoritmo Paralelo --------------- \n")
	print("Calculo da Integral da função: (x*x) no intervalo [a,b] \n\n")
	global a, b
	a = int(input("Introduza limite inferior a = "))
	b = int(input("Introduza limite superior b (b>a) = "))
	#n = int(input("Introduza número de partições do intervalo (n>1) n = ")) 
	global h
	#Calcular dimensão de cada partição. 
	h = (b - a) / tamThread
	mini = a
	maxi = a+h
	soma = 0
	inicio = time.time()
	#Parte do codigo onde cada Thread é criada
	for i in range(1,(tamThread+1)):
		t = threading.Thread(target=chamaTrhead,args=(mini,maxi,))
		t.start()
		mini = maxi
		maxi = maxi+h
	#Verifica se as Treads ainda estão executando e espera (barreira) 
	
	while t.isAlive():
		tamanho = len(vet)
		#Percorre todo o valor com os resultados das Trheads e retorna no fim o calculo da área computado
		for i in range(0,tamanho):
			soma = soma+vet[i]
		#Resultado final do programa -  a área calculada
		print("Derivada da fucção é: ",soma)
		fim = time.time()
		print("Tempo de execução do Programa: ",(fim - inicio))
		return 0 

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
