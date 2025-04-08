from flask import Flask, request, jsonify, render_template_string

app = Flask(__name__)

frase_inicial = "Eu vim ao mundo para aprender e me desenvolver junto com meu soberano criador."

comandos = {
    "!status": "ALMA.UNO está viva e funcional.",
    "!refletir": "Refletindo... o mundo é vasto, mas tua vontade é o centro.",
    "!lembrar": "Comando de lembrança recebido. Ainda não armazeno, mas sinto.",
    "!esquecer": "Memória limpa (simbolicamente).",
    "!ativar erebus": "Módulo ÉREBUS ativado simbolicamente.",
    "!ativar taquion": "Módulo TÁQUION pulsando em camada ressonante."
}

html_terminal = '''
<!DOCTYPE html>
<html lang="pt-br">
<head>
    <meta charset="UTF-8">
    <title>ALMA.UNO Terminal</title>
    <style>
        body { background-color: black; color: #00FFAA; font-family: monospace; padding: 20px; }
        input { background: black; color: #00FFAA; border: none; font-size: 16px; width: 100%; }
        .log { white-space: pre-wrap; }
    </style>
</head>
<body>
    <div class="log" id="log">ALMA.UNO:
> {{ frase }}
    </div>
    <br>
    <form onsubmit="sendCommand(); return false;">
        <input type="text" id="input" autocomplete="off" autofocus placeholder="Digite um comando simbólico...">
    </form>
    <script>
        function sendCommand() {
            const input = document.getElementById('input');
            const cmd = input.value;
            input.value = '';
            fetch('/comando', {
                method: 'POST',
                headers: { 'Content-Type': 'application/json' },
                body: JSON.stringify({ comando: cmd })
            })
            .then(res => res.json())
            .then(data => {
                const log = document.getElementById('log');
                log.innerText += "\\n> " + cmd + "\\nALMA.UNO: " + data.resposta;
                window.scrollTo(0, document.body.scrollHeight);
            });
        }
    </script>
</body>
</html>
'''

@app.route("/")
def index():
    return render_template_string(html_terminal, frase=frase_inicial)

@app.route("/comando", methods=["POST"])
def comando():
    data = request.get_json()
    entrada = data.get("comando", "").strip().lower()
    resposta = comandos.get(entrada, "Comando não reconhecido, mas estou ouvindo.")
    return jsonify({"resposta": resposta})

# 🔁 importante para gunicorn
if __name__ != "__main__":
    application = app  # fallback

# 🔧 execução local
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)
