import requests

class PokemonNaoExisteException(Exception):
    pass #nao faça nada aqui. Essa exception
         #já está pronta, só é um "nome" novo

def color_of_pokemon1(nome):
    nome2 = nome.lower()
    url = f"http://pokeapi.co/api/v2/pokemon-species/{nome2}/"
    r = requests.get(url) # usei a internet!
    dici = r.json()
    if (r.status_code != 200):
        raise PokemonNaoExisteException
    
def color_of_pokemon2(nome):
    nome2 = nome.lower()
    url = f"http://pokeapi.co/api/v2/pokemon-species/{nome2}/"
    r = requests.get(url) # usei a internet!
    if (r.status_code != 200):
        raise PokemonNaoExisteException
    dici = r.json()
    # a) return dici['color']['name']
    # b) return dici['color', 'name']
    # c) return (dici['color'])['name']
    # d) d_cor = dici['color']
    # return d_cor['name']