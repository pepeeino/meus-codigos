from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.primitives import padding
from troca_de_chaves import gerar_chave_compartilhada
import os

def encrypt_message(key, plaintext):
    iv = os.urandom(16)  # Vetor de inicialização
    cipher = Cipher(algorithms.AES(key), modes.CBC(iv))
    padder = padding.PKCS7(algorithms.AES.block_size).padder()
    padded_data = padder.update(plaintext) + padder.finalize()
    encryptor = cipher.encryptor()
    ciphertext = encryptor.update(padded_data) + encryptor.finalize()
    return iv + ciphertext

def decrypt_message(key, ciphertext):
    iv = ciphertext[:16]
    actual_ciphertext = ciphertext[16:]
    cipher = Cipher(algorithms.AES(key), modes.CBC(iv))
    decryptor = cipher.decryptor()
    padded_plaintext = decryptor.update(actual_ciphertext) + decryptor.finalize()
    unpadder = padding.PKCS7(algorithms.AES.block_size).unpadder()
    plaintext = unpadder.update(padded_plaintext) + unpadder.finalize()
    return plaintext

server_shared_key = gerar_chave_compartilhada()
shared_key = server_shared_key  # Chave derivada
message = b"Mensagem secreta"
encrypted_message = encrypt_message(shared_key, message)
print(f"Mensagem criptografada: {encrypted_message.hex()}")

decrypted_message = decrypt_message(shared_key, encrypted_message)
print(f"Mensagem decifrada: {decrypted_message.decode()}")
