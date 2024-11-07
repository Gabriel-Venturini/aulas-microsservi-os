#essa parte é sempre igual, nao encana
from flask import Flask, request
app = Flask(__name__)
#fim da burocracia


#tudo que voce precisa de flask
@app.route("/proximo/<int:n>", methods=['GET'])
def proximo(n):
    if n < 10:
        return ({"erro":"numero muito pequeno"}),400
    return {"proximo numero":n+1}


@app.route("/receba", methods=['PUT',"POST"])
def receberei():
    print(request.json)
    return 'veja no cmd'

@app.route("/hello", methods=['GET'])
def hello_world():
    print(request.json)
    return 'Hello world!', 200

@app.route("/mensagem/<string:n>", methods=['GET'])
def mensagem(n):
    print(request.json)
    return n

# essa parte é sempre igual, nao encana    
if __name__ == "__main__":
    app.run(debug=True)
#fim da burocracia