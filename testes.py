def cria_naipe(naipe): # o naipe deve ser === naipes para ser aceito
    naipes = ['o','p','c','e']
    cartas = ['A','2','3','4','5','6','7','8','9','10','J','Q','K']
    cartaCorreta = []
    if naipe not in naipes:
        pass
    else:
        for carta in cartas:
            cartaCorreta += [carta + naipe]
    return cartaCorreta