from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.backends import default_backend
import os

def generar_clave_aes(password: str, salt: bytes) -> bytes:
    kdf = PBKDF2HMAC(
        algorithm=hashes.SHA256(),
        length=32,
        salt=salt,
        iterations=100000,
        backend=default_backend()
    )
    return kdf.derive(password.encode())

def cifrar_aes(mensaje: bytes, clave: bytes) -> (bytes, bytes):
    iv = os.urandom(16)
    cipher = Cipher(algorithms.AES(clave), modes.CFB(iv), backend=default_backend())
    encryptor = cipher.encryptor()
    cifrado = encryptor.update(mensaje) + encryptor.finalize()
    return iv, cifrado

def descifrar_aes(iv: bytes, cifrado: bytes, clave: bytes) -> bytes:
    cipher = Cipher(algorithms.AES(clave), modes.CFB(iv), backend=default_backend())
    decryptor = cipher.decryptor()
    return decryptor.update(cifrado) + decryptor.finalize()