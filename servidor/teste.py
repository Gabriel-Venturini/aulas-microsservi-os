import requests
import random
import time

url = 'https://60b8a882-927e-4e6a-a852-f692378195b6-00-15s9kpw116juq.picard.replit.dev/alunos'

def gerar_dados():
    return {
        "cpf": f"{random.randint(10000000000, 99999999999)}",
        "endereco": ":)",
        "id": random.randint(1, 100000),
        "nome": "medusacururu"
    }

def enviar_requests(quantidade):
    for _ in range(quantidade):
        dados = gerar_dados()
        response = requests.post(url, json=dados)
        print(f"Enviado: {dados} | Status Code: {response.status_code}")
        time.sleep(0.01)

enviar_requests(1000)
