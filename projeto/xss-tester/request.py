from flask import Flask, request, jsonify
import requests
from bs4 import BeautifulSoup

app = Flask(__name__)

@app.route('/xss-tester', methods=['POST'])
def xss_tester():
    data = request.json  # Recebe dados enviados pelo fetch
    url = data.get('url')
    # Aqui, processa a lógica com o URL enviado
    if "xss" in url.lower():
        return jsonify({"message": "XSS encontrado!", "status": "danger"})
    return jsonify({"message": "Nenhum XSS detectado.", "status": "safe"})

if __name__ == '__main__':
    app.run(debug=True)
