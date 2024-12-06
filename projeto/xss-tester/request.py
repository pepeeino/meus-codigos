#made with AI, probably contains some errors
from flask import Flask, request, jsonify
import requests
from bs4 import BeautifulSoup

app = Flask(__name__)

# Função de teste de vulnerabilidade XSS
def test_xss_payloads(site, payloads):
    results = {}
    for payload in payloads:
        try:
            url = f"{site}?input={payload}"
            response = requests.get(url, timeout=5)
            response.raise_for_status()
            soup = BeautifulSoup(response.text, 'html.parser')
            if payload in soup.prettify():
                results[payload] = "Vulnerável (XSS detectado)"
            else:
                results[payload] = "Não vulnerável (XSS não detectado)"
        except requests.exceptions.RequestException as e:
            results[payload] = f"Erro na requisição: {str(e)}"
    return results

# Endpoint para receber a URL e testar os payloads
@app.route('/process', methods=['POST'])
def process():
    data = request.get_json()
    site = data.get('input')
    payloads = data.get('payloads', [])

    if not site or not payloads:
        return jsonify({"status": "error", "message": "URL ou payloads não fornecidos"})

    resultados = test_xss_payloads(site, payloads)
    return jsonify({"status": "success", "result": resultados})

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
