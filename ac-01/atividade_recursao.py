# Análise e Projeto de Algoritmos
# AC1: Ciência da Computação
#
# Email Impacta: caio.fresneda@aluno.faculdadeimpacta.com.br


def somatorio(n:int) -> int:
	
	if n <= 0:
		return n

	if n == 0:
		return n

	else:
		return n + somatorio(n-1)

def potencia_de_2(n:int) -> bool:

    if n == 1:
        return True

    elif n % 2 == 1:
        return False

    else:
        return potencia_de_2(n // 2)


def qtd_digitos(n:int) -> int:
	if n < 10:
		return 1
	else: 
		return 1 + qtd_digitos(n//10)


def soma_digitos(n: int) -> int:
	if n < 10:
		return n
	else:
		return n % 10 + soma_digitos(n // 10)


def soma_lista(lista:list, i:int) -> int: 

	if i == len(lista) - 1:
		return lista[i]
	else:
		return lista[i] + soma_lista(lista, i + 1)