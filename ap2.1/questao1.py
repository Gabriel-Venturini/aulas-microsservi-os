import requests
class AlgumaException(Exception):
    def __init__(self, sttus):
        # ... 
        pass

    def cadastrar(placa, modelo, cor):
        j = {
            "placa": placa,
            "modelo": modelo,
            "cor": cor
        }
        url = "http://example.com/carros"
        x = requests.post(url, json = j)
        code = x.status_code
        if code == 200:
            return x.json()
        else:
            raise AlgumaException(code)