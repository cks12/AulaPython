from random import randint

def bubble_sort(lista):
    n = len(lista)
    for i in range(0, n-1):
        for j in range(0, n-1-i):
            if lista[j] > lista[j+1]:           # compara elementos consecutivos
                aux = lista[j]                  # realiza a troca
                lista[j] = lista[j+1]
                lista[j+1] = aux


def selection_sort(lista):
    n = len(lista)
    for i in range(0, n-1):
        menor = i
        for j in range(i + 1, n):               # encontra o menor elemento
            if lista[j] < lista[menor]:
                menor = j
        aux = lista[i]                          # realiza a troca
        lista[i] = lista[menor]
        lista[menor] = aux


def insertion_sort(lista):
    n = len(lista)
    for i in range(1, n):
        j = i
        while j > 0 and lista[j] < lista[j-1]:  # compara elemento com os anteriores
            aux = lista[j]                      # realiza a troca
            lista[j] = lista[j-1]
            lista[j-1] = aux
            j -= 1


def intercala(lista, inicio, meio, fim):
    aux = []                                    # lista auxiliar
    esq = inicio
    dir = meio + 1
    while(esq <= meio and dir <= fim):          # enquanto não avaliou completamente
        if (lista[esq] <= lista[dir]):          # uma das sublistas, copia o menor
            aux.append(lista[esq])              # elemento para lista auxiliar
            esq += 1
        else:
            aux.append(lista[dir])
            dir += 1
    while(esq <= meio):                         # copia o resto da primeira sub-lista
        aux.append(lista[esq])
        esq += 1
    while(dir <= fim):                          # copia o resto da segunda sub-lista
        aux.append(lista[dir])
        dir += 1
    lista[inicio:fim+1] = aux                   # copia a lista auxiliar ordenada para a lista
    return lista


def merge_sort(lista, inicio, fim):
    meio = (fim + inicio) // 2
    if (inicio < fim):
        merge_sort(lista, inicio, meio)         # primeira metade da lista
        merge_sort(lista, meio + 1, fim)        # segunda metade da lista
        intercala(lista, inicio, meio, fim)     # realiza intercalação das duas metades


def particiona(lista, inicio, fim):
    indice = randint(inicio, fim,)              # seleciona um pivô aleatório
    aux = lista[inicio]                         # pivô aleatório troca de posição com primeiro elemento
    lista[inicio] = lista[indice]
    lista[indice] = aux

    pivo = lista[inicio]                        # considera primeiro elemento como pivo
    i = inicio                                  # armazena índice do pivo
    for j in range(inicio + 1, fim + 1):        
        if lista[j] <= pivo:                    # ao encontrar elemento menor que pivo
            i += 1                              # incrementa variável i (índice do pivô)
            aux = lista[i]                      # troca elemento de posição
            lista[i] = lista[j]
            lista[j] = aux

    aux = lista[inicio]                         # troca pivô de posição
    lista[inicio] = lista[i]
    lista[i] = aux
    return i                                    # retorna índice atual do pivo


def quick_sort(lista, inicio, fim):
    if (inicio < fim):                          # enquanto tem pelo menos 2 elementos
        posicao = particiona(lista, inicio, fim)
        quick_sort(lista, inicio, posicao - 1)  # lista à esquerda do pivô
        quick_sort(lista, posicao + 1, fim)     # lista à direita do pivo