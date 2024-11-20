from locust import HttpUser, task, between
import random

class LoadTest(HttpUser):
    wait_time = between(0.1, 0.5)  # Tempo de espera entre requisições

    @task
    def enviar_request(self):
        dados = {
            "cpf": f"{random.randint(10000000000, 99999999999)}",
            "endereco": ":)",
            "id": random.randint(1, 100000),
            "nome": "medusacururu"
        }
        self.client.post("/alunos", json=dados)