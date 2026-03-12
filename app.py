#alterar app.py para servir html
#render template manda o html para o navegador

from flask import Flask, render_template, jsonify
from caca_palavras import gerar_caca_palavras,temas


app = Flask( __name__)

    
@app.route("/")
def home():
    return render_template ("template_index.html")

@app.route("/jogo/<tema>")
def jogo(tema):
    tema = tema.upper()

    if tema not in temas:
         return jsonify({"erro":"Tema não existe"})
    
    palavras = temas[tema]

    matriz = gerar_caca_palavras(1, palavras)[0]

    return jsonify({
        "matriz": matriz,
        "palavras": palavras
    })
if __name__ == "__main__":
    app.run(#debug=True
        )

    