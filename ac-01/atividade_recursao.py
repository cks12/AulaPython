# Análise e Projeto de Algoritmos
# AC1: Ciência da Computação
#
# Email Impacta: __________@aluno.faculdadeimpacta.com.br


def somatorio(n:int) -> int:
	
	if n <= 0:
		return n

	if n == 0:
		return n

	else:
		return n + somatorio(n-1)

def potencia_de_2(n):

    if n == 1:
        return True

    elif n % 2 == 1:
        return False

    else:
        return potencia_de_2(n // 2)


def qtd_digitos(n):
	
	"""
	Função recursiva que recebe um valor inteiro n >= 1, e devolve um valor inteiro
	indicando o número de dígitos de n.

	Exemplos:
	------------
	qtd_digitos(4) devolve 1, pois 4 contém somente 1 dígito;
	qtd_digitos(9) devolve 1, pois 9 contém somente 1 dígito;
	qtd_digitos(10) devolve 2, pois 10 contém 2 dígitos;
	qtd_digitos(99) devolve 2, pois 99 contém 2 dígitos;
	qtd_digitos(1071) devolve 4, pois 1071 contém 4 dígitos;

	Retorno:
	------------
	int: número de digitos de n.
	"""
	pass


def soma_digitos(n):
	"""
	Função recursiva que recebe um valor inteiro n >= 1, e devolve o somatório de
	todos os dígitos de n.

	Exemplo:
	------------
	soma_digitos(4) devolve 4;
	soma_digitos(45) devolve 9, pois 4+5 = 9;
	soma_digitos(451) devolve 10, pois 4+5+1 = 10;
	soma_digitos(2345) devolve 14, pois 2+3+4+5 = 14;

	Retorno:
	------------
	int: soma dos dígitos de n.
	"""
	pass


def soma_lista(lista, i):
	"""
	Função recursiva que recebe uma lista com números inteiros (tipo list do Python) e
	um valor inteiro i >= 0, que representa um índice da lista.

	A função devolve o somatório de todos os números da lista a partir do índice i
	até o final da lista.

	Exemplo:
	------------
	Caso lista = [1,2,3,4] e i = 0,
		o retorno deve ser: 10, pois lista[0]+lista[1]+lista[2]+lista[3] = 10.
	Caso lista = [1,2,3,4] e i = 2,
		o retorno deve ser: 7, pois lista[2]+lista[3] = 7.
	Caso lista = [22, 33, 44, 55] e i = 1,
		o retorno deve ser 132, pois lista[1]+lista[2]+lista[3] = 132.
	
	Retorno:
	------------
	int: soma dos valores da lista.	
	"""
	pass

