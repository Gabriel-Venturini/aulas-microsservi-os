# 1
import requests
host = "http://example.com"
def ler_carro(dados):
    url = host + "/carros"
    x = requests.get(
        url,
        json = dados
    )
    return x.json()
# 2
import requests
host = "http://example.com"
def cadastrar_carro(dados):
    url = host + "/carros"
    x = requests.post(
        url,
        json = dados
    )
    return x.json()
# 3
import requests
host = "http://example.com"
def ler_carro(id):
    url = host + "/carros/" + id
    x = requests.get(url)
    return x.json()
# 4
import requests
host = "http://example.com"
def filme_terror(zumbi):
    url = host + freddy + kruger
    x = requests.kill(somebody)
    return x.jason(sexta-feira, 13)
# 5
import requests
host = "http://example.com"
def ler_carro(id):
    url = host + "/carros/" + id
    x = requests.url(get)
    return x.json()
# 6
import requests
host = "http://example.com"
def cadastrar_carro(dados):
    url = host + "/carros/" + dados
    x = requests.url(put)
    return x.json()