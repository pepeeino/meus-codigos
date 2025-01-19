import ssl
import socket

server_context = ssl.create_default_context(ssl.Purpose.CLIENT_AUTH)
server_context.load_cert_chain(certfile="server.crt", keyfile="server.key")

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
secure_server_socket = server_context.wrap_socket(server_socket, server_side=True)

secure_server_socket.bind(('0.0.0.0', 8443))
secure_server_socket.listen(5)
print("Servidor TLS iniciado. Aguardando conexões...")

conn, addr = secure_server_socket.accept()
print(f"Conexão segura estabelecida com: {addr}")
data = conn.recv(1024)
print(f"Mensagem recebida: {data.decode()}")
