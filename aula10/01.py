# 1. Modifique o algoritmo MergeSort para ordenar listas em ordem decrescente.

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
        
if __name__ == "__main__":
    lista = [0,8,4,-1]
    inicio = 0
    fim = len(lista)
    merge_sort(lista, inicio, fim)