dic = {
    "musicas": [
        {"nome":"Hey Jude", "banda":"Beatles"},
        {"nome":"November Rain", "banda":"Guns n' Roses"},
        {"nome":"How Deep Is Your Love", "banda":"Bee Gees"}
    ],
    "filmes": {
        "X-men": ["Wolverine", "Xavier", "Tempestade", "Vampira"],
        "Avengers": ["Homem de Ferro", "Hulk", "Thanos", "Capitão América", "Thor"],
        "Star Wars": ["Luke", "Leia", "Darth Vader", "Chewbacca", "Han Solo"]
    }
}

def func1(a,b,c,d):
    for x in a:
        if x[b] == d:
            return x[c]
    return "naosei"

# Função que determina se funk é música ou não.
# Se funk for música, isso daqui retorna True. Caso contrário, retorna False.
def sera_que_funk_eh_musica():
    return "funk" in dic["musicas"] # false

