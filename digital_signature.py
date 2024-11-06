from cryptography.hazmat.primitives.asymmetric import padding
from cryptography.hazmat.primitives import hashes

def firmar_mensaje(mensaje: bytes, clave_privada) -> bytes:
    return clave_privada.sign(
        mensaje,
        padding.PSS(
            mgf=padding.MGF1(hashes.SHA256()),
            salt_length=padding.PSS.MAX_LENGTH
        ),
        hashes.SHA256()
    )

def verificar_firma(mensaje: bytes, firma: bytes, clave_publica) -> bool:
    try:
        clave_publica.verify(
            firma,
            mensaje,
            padding.PSS(
                mgf=padding.MGF1(hashes.SHA256()),
                salt_length=padding.PSS.MAX_LENGTH
            ),
            hashes.SHA256()
        )
        return True
    except:
        return False