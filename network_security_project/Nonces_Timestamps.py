import time
import hmac
import os

def generate_nonce():
    return os.urandom(16)

def verify_nonce(nonce, used_nonces):
    if nonce in used_nonces:
        raise ValueError("Nonce já usado!")
    used_nonces.add(nonce)

def add_timestamp():
    return int(time.time())

def verify_timestamp(timestamp, window=5):
    current_time = int(time.time())
    if abs(current_time - timestamp) > window:
        raise ValueError("Timestamp fora do limite permitido!")

# Exemplo
used_nonces = set()
nonce = generate_nonce()
timestamp = add_timestamp()

# Verificando
verify_nonce(nonce, used_nonces)
verify_timestamp(timestamp)
print("Nonce e timestamp verificados!")
