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
            response = requests.get(url)   
            soup = BeautifulSoup(response.text, 'html.parser')
            if payload in soup.prettify():
                results[payload] = "Vulnerável (XSS detectado)"
            else:
                results[payload] = "Não vulnerável (XSS não detectado)"        
        except Exception as e:
            results[payload] = f"Erro ao testar: {str(e)}"   
    return results

# Endpoint para receber a URL e testar os payloads
@app.route('/process', methods=['POST'])
def process():
    data = request.get_json()
    site = data.get('input')
    
    # Carregar payloads (exemplo de lista de payloads)
    xss_payloads = ["<script>alert(1)</script>", "<img src=x onerror=alert(1)>"]
    
    if not site:
        return jsonify({"status": "error", "message": "URL não fornecida"})
    
    resultados = test_xss_payloads(site, xss_payloads)

    return jsonify({"status": "success", "result": resultados})

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
