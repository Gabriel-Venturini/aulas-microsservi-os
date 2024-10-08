'''
Defina uma função merge que faz o seguinte:
    Dadas duas listas ordenadas L1 e L2, 
    retorna uma lista ordenada com todos os números de L1 e L2.

    A função NAO deve usar o método sort do python.

    Em vez disso, faça o seguinte:
       * Crie um indice i1 para a lista L1 e um i2 para L2
       * Inicialize i1 e i2 com 0
       * Compare L1[i1] com L2[i2] e coloque o menor dos dois
       na lista de resposta. Se o menor era L1[i1], aumente i1.
       Caso contrário, aumente i2
       * Assim, L1[i1] e L2[i2] são sempre os menores elementos
       de L1 e L2, e um  deles é sempre o proximo que deve entrar 
       na resposta
       * Continue fazendo isso até adicionar todos os elementos
       de L1 e L2 na resposta
'''

def merge(lista1, lista2):
    i1 = 0
    i2 = 0
    novaLista = []
    range1 = len(lista1)
    range2 = len(lista2)

    while i1 < range1 and i2 < range2:
        if lista1[i1] < lista2[i2]:
            novaLista.append(lista1[i1])
            i1 += 1
        else:
            novaLista.append(lista2[i2])
            i2 += 1

    # Adiciona os elementos restantes de lista1, se houver
    if i1 < range1:
        novaLista.extend(lista1[i1:])
    
    # Adiciona os elementos restantes de lista2, se houver
    if i2 < range2:
        novaLista.extend(lista2[i2:])

    return novaLista