from flask import Flask, request, render_template, redirect
import random
from string import digits, punctuation, ascii_letters


def gerar_senha(parametros_senha: dict) -> str:
    simbolos = ""
    rand = random.SystemRandom()
    
    if parametros_senha['letras']:
        simbolos += ascii_letters
    if parametros_senha['digitos']:
        simbolos += digits
    if parametros_senha['ponctuation']:
        simbolos += punctuation
    
    if simbolos != "":
        return "".join(rand.choice(simbolos) for i in range(parametros_senha['tamanho']))

def convert_data(data: str) -> dict:
    info = dict(tamanho=20, letras=True, digitos=True, ponctuation=True)

    info['tamanho'] = int(data.split("&")[0].split("=")[1])
    
    if 'letras' not in data:
        info['letras'] = False
    if 'digitos' not in data:
        info['digitos'] = False
    if 'ponctuation' not in data:
        info['ponctuation'] = False

    return info

app = Flask(__name__)


@app.route("/senha", methods=['GET', 'POST'])
def senha():
    parametros_senha = dict(tamanho=20, letras=True, digitos=True, ponctuation=True)
    senha="sua senha"
    if request.method == 'POST':
        data = request.get_data(as_text=True)

        parametros_senha = convert_data(data)

        senha = gerar_senha(parametros_senha)
    return render_template("index.html", senha=senha, parametros_senha=parametros_senha)


@app.route("/", methods=['GET'])
def index():
    return redirect("/senha")
    

if __name__ == "__main__":
    app.run(debug=True)
