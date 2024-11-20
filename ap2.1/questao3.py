
# 1
@app.route("/imoveis/<int:id>",
    methods = ["GET"])
def obter_imovel():
    # ...

# 2 ESSE
@app.route("/imoveis/<int:id>",
    methods = ["GET"])
def obter_imovel(id):
    # ...

# 3
@app.route("/imoveis/",
    methods = ["GET"])
def obter_imovel(id):
    # ...

# 4
def app.flask("/futebol/<bola>",
              methods = ["CHUT"])
@gol(bola):
    # ...

# 5
@app.route("/imoveis/",
    methods = ["POST"])
def obter_imovel():
    # ...

# 6
@app.route("/imoveis/<int:id>",
    methods = ["POST"])
def obter_imovel(id):
    # ...