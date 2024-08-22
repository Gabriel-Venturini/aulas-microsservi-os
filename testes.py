def maior(*args):
    numeros = list(args)
    maior = 0
    
    for numero in numeros:
        if numero > maior:
            maior = numero

    return maior