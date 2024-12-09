#made with AI, probably contains some errors
# pip install requests beautifulsoup4
import requests
from bs4 import BeautifulSoup
import os

def carregar_payloads(file_path):
    """Carrega payloads XSS de um arquivo."""
    try:
        with open(file_path, "r", encoding="utf-8") as file:
            payloads = [line.strip() for line in file if line.strip()]
        if not payloads:
            print("O arquivo está vazio. Certifique-se de que contém payloads.")
            return []
        return payloads
    except FileNotFoundError:
        print(f"Arquivo não encontrado no caminho: {file_path}")
        return []
    except Exception as e:
        print(f"Erro ao carregar o arquivo: {str(e)}")
        return []

def validar_url(url):
    """Valida se a URL possui um formato básico correto."""
    if not url.startswith("http://") and not url.startswith("https://"):
        print("URL inválida. Certifique-se de incluir 'http://' ou 'https://'.")
        return False
    return True

def test_xss_payloads(site, payloads):
    """Testa a vulnerabilidade XSS em um site usando uma lista de payloads."""
    results = {}
    for payload in payloads:
        try:
            url = f"{site}?input={payload}"
            response = requests.get(url, timeout=5)  # Adicionado timeout
            response.raise_for_status()  # Verifica erros HTTP
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

def main():
    file_path = input("Digite o caminho completo do arquivo de payloads: ")
    xss_payloads = carregar_payloads(file_path)
    
    if not xss_payloads:
        print("Nenhum payload foi carregado. Encerrando o programa.")
        return

    site_testado = input("Digite o URL do site para testar: ")
    
    if not validar_url(site_testado):
        print("URL inválida. Encerrando o programa.")
        return

    print("\nIniciando os testes de XSS...")
    resultados = test_xss_payloads(site_testado, xss_payloads)
    
    print("\n--- Resultados ---")
    for payload, resultado in resultados.items():
        print(f"Payload: {payload}\nResultado: {resultado}\n")

if __name__ == "__main__":
    main()

