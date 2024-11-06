from cryptography.hazmat.primitives.asymmetric import rsa, padding
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.backends import default_backend

def generar_claves_rsa():
    clave_privada = rsa.generate_private_key(
        public_exponent=65537,
        key_size=2048,
        backend=default_backend()
    )
    clave_publica = clave_privada.public_key()
    return clave_privada, clave_publica

def cifrar_rsa(mensaje: bytes, clave_publica) -> bytes:
    return clave_publica.encrypt(
        mensaje,
        padding.OAEP(
            mgf=padding.MGF1(algorithm=hashes.SHA256()),
            algorithm=hashes.SHA256(),
            label=None
        )
    )

def descifrar_rsa(cifrado: bytes, clave_privada) -> bytes:
    return clave_privada.decrypt(
        cifrado,
        padding.OAEP(
            mgf=padding.MGF1(algorithm=hashes.SHA256()),
            algorithm=hashes.SHA256(),
            label=None
        )
    )