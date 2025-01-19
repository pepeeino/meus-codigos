import ssl
import os
import socket

client_context = ssl.create_default_context()
client_context.load_verify_locations(cafile="ca.crt")
if not os.path.exists("ca.crt"):
    raise FileNotFoundError("O arquivo ca.crt não foi encontrado. Verifique o caminho.")


secure_client_socket = client_context.wrap_socket(socket.socket(socket.AF_INET), server_hostname="server")

secure_client_socket.connect(('127.0.0.1', 8443))
secure_client_socket.sendall("Olá, servidor seguro!".encode("utf-8"))

