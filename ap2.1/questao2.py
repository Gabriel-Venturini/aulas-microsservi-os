dic = {
    "musicas": [
        {"nome": "Hey Jude", "banda": "Beatles"},
        {"nome": "November Rain", "banda": "Guns n' Roses"},
        {"nome": "How Deep Is Your Love", "banda": "Bee Gees"}
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
    
