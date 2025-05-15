from flask import Flask, request, render_template_string

app = Flask(__name__)

traduzir = {
    "sol": "sun",
    "lua": "moon",
    "estrela": "star"
}

html = """
<!DOCTYPE html>
<html>
<head>
    <title>Tradutor Simples</title>
</head>
<body>
    <h2>Digite uma palavra em português:</h2>
    <form method="post">
        <input type="text" name="palavra" required>
        <input type="submit" value="Traduzir">
    </form>
    {% if traducao %}
        <p><strong>Tradução:</strong> {{ traducao }}</p>
    {% endif %}
</body>
</html>
"""

@app.route("/", methods=["GET", "POST"])
def traduzir_palavra():
    traducao = None
    if request.method == "POST":
        palavra = request.form["palavra"].lower()
        traducao = traduzir.get(palavra, "Não encontrado")
    return render_template_string(html, traducao=traducao)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)