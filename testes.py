def cria_baralho():
    baralho=[]
    naipes = ['c','e','o','p']
    cartas = ['A','2','3','4','5','6','7','8','9','10','J','Q','K']

    for naipe in naipes:
        for carta in cartas:
            baralho += [carta + naipe]

    return  baralho