#pip install requests beautifulsoup4
import requests
from bs4 import BeautifulSoup

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


file_path = "C:/Users/HP/Desktop/save/xss2_modified/"
try:
    with open(file_path, "r", encoding="utf-8") as file:
        xss_payloads = [line.strip() for line in file if line.strip()]
except FileNotFoundError:
    print(f"Arquivo não encontrado no caminho: {file_path}")
    xss_payloads = []


if not xss_payloads:
    print("Nenhum payload foi carregado. Certifique-se de que o arquivo contém os payloads.")
else:
    site_testado = input("Digite o URL do site para testar: ")

    resultados = test_xss_payloads(site_testado, xss_payloads)

    for payload, resultado in resultados.items():
        print(f"Payload: {payload}\nResultado: {resultado}\n")
