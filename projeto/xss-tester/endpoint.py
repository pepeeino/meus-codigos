from flask import Flask, request, jsonify
import requests
from bs4 import BeautifulSoup

app = Flask(__name__)

def carregar_payloads(file_path):
    """Carrega payloads XSS de um arquivo."""
    try:
        with open(file_path, "r", encoding="utf-8") as file:
            return [line.strip() for line in file if line.strip()]
    except FileNotFoundError:
        return []
    except Exception as e:
        print(f"Erro ao carregar o arquivo: {str(e)}")
        return []

def test_xss_payloads(site, payloads):
    """Testa a vulnerabilidade XSS em um site usando uma lista de payloads."""
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
        except Exception as e:
            results[payload] = f"Erro inesperado: {str(e)}"
    return results

@app.route('/xss-tester', methods=['POST'])
def xss_tester():
    data = request.json  # Recebe dados enviados pelo Frontend
    url = data.get('url')
    file_path = data.get('file_path', 'payloads.txt')  # Caminho do arquivo de payloads

    if not url:
        return jsonify({"message": "URL não fornecida.", "status": "error"}), 400

    # Carrega os payloads
    payloads = carregar_payloads(file_path)
    if not payloads:
        return jsonify({"message": "Nenhum payload encontrado.", "status": "error"}), 400

    # Realiza os testes XSS
    resultados = test_xss_payloads(url, payloads)

    return jsonify({"message": "Teste concluído.", "status": "success", "resultados": resultados})

if __name__ == '__main__':
    app.run(debug=True)
