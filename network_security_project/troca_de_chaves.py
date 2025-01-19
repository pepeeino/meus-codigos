from cryptography.hazmat.primitives.asymmetric import dh
from cryptography.hazmat.primitives.asymmetric import ec
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.hkdf import HKDF
from cryptography.hazmat.primitives.serialization import Encoding, PublicFormat, load_pem_public_key
import os

# Gerando os parâmetros DH (somente no servidor)
parameters = dh.generate_parameters(generator=2, key_size=2048)

def generate_dh_keys(parameters):
    private_key = parameters.generate_private_key()
    public_key = private_key.public_key()
    return private_key, public_key

def derive_shared_key(private_key, peer_public_key):
    shared_key = private_key.exchange(peer_public_key)
    derived_key = HKDF(
        algorithm=hashes.SHA256(),
        length=32,
        salt=None,
        info=b'handshake data'
    ).derive(shared_key)
    return derived_key

# No servidor
server_private_key, server_public_key = generate_dh_keys(parameters)

# No cliente (parâmetros devem ser enviados do servidor)
client_private_key, client_public_key = generate_dh_keys(parameters)

# Exchanging public keys and deriving shared key
server_shared_key = derive_shared_key(server_private_key, client_public_key)
client_shared_key = derive_shared_key(client_private_key, server_public_key)

assert server_shared_key == client_shared_key, "As chaves derivadas não coincidem!"
print(f"Chave compartilhada derivada: {server_shared_key.hex()}")

def gerar_chave_compartilhada():
    # Exemplo simples (não seguro para produção)
    return b"minha_chave_secreta_1234"
