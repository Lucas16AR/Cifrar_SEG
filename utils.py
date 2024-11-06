from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.backends import default_backend

def generar_hash(mensaje: bytes) -> bytes:
    digest = hashes.Hash(hashes.SHA256(), backend=default_backend())
    digest.update(mensaje)
    return digest.finalize()