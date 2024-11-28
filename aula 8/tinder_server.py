from flask import Flask, jsonify, request
import estrutura_interesses as i
import json
from dados import getSystemInfo

app = Flask(__name__)
app.url_map.strict_slashes = False

@app.route("/meupc", methods=['GET'])
def infoPc():
    return json.loads(getSystemInfo())

@app.route("/")
def ola():
    return "servidor do tinder"
    

@app.route('/pessoas', methods=['GET'])
def f():
    return i.todas_as_pessoas()

@app.route("/pessoas/<int:n>", methods=['GET'])
def pessoa_por_id(n):
    try:
        return i.localiza_pessoa(n)
    except i.NotFoundError:
        return {"erro": "id invalida"}, 404

@app.route("/pessoas", methods=['POST'])
def adiciona_pessoa():
    dicionario_enviado = request.json
    i.adiciona_pessoa(dicionario_enviado)
    return i.todas_as_pessoas()

@app.route("/pessoas/reseta", methods=['GET'])
def reseta_pessoas():
    i.reseta()
    return i.todas_as_pessoas()

@app.route("/sinalizar_interesse/<int:p1>/<int:p2>", methods=['PUT'])
def add_like(p1, p2):
    try:
        i.adiciona_interesse(p1, p2)
        d = {f"interesses {p1}": i.consulta_interesses(p1)}
        return d
    except i.NotFoundError:
        return {"erro": "id invalida"}, 404

if __name__ == '__main__':
    app.run(host='localhost', port=5003, debug=True)