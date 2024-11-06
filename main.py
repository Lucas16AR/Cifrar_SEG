from aes_cipher import generar_clave_aes, cifrar_aes, descifrar_aes
from rsa_cipher import generar_claves_rsa, cifrar_rsa, descifrar_rsa
from digital_signature import firmar_mensaje, verificar_firma
from utils import generar_hash
import os

def main():
    # Datos de entrada
    mensaje = b"Este es un mensaje de prueba para cifrado y firma."

    # Cifrado y Descifrado AES
    password = "mi_contraseña_segura"
    salt = os.urandom(16)
    clave_aes = generar_clave_aes(password, salt)
    iv, mensaje_cifrado_aes = cifrar_aes(mensaje, clave_aes)
    mensaje_descifrado_aes = descifrar_aes(iv, mensaje_cifrado_aes, clave_aes)
    print(f"\nMensaje original: {mensaje}")
    print(f"Mensaje cifrado (AES): {mensaje_cifrado_aes}")
    print(f"Mensaje descifrado (AES): {mensaje_descifrado_aes}")

    # Generación de claves RSA
    clave_privada, clave_publica = generar_claves_rsa()

    # Cifrado y Descifrado RSA
    mensaje_cifrado_rsa = cifrar_rsa(mensaje, clave_publica)
    mensaje_descifrado_rsa = descifrar_rsa(mensaje_cifrado_rsa, clave_privada)
    print(f"\nMensaje cifrado (RSA): {mensaje_cifrado_rsa}")
    print(f"Mensaje descifrado (RSA): {mensaje_descifrado_rsa}")

    # Firma digital y verificación
    firma = firmar_mensaje(mensaje, clave_privada)
    es_valida = verificar_firma(mensaje, firma, clave_publica)
    print(f"\nFirma digital: {firma}")
    print(f"¿Firma válida?: {es_valida}")

    # Generación de hash
    hash_mensaje = generar_hash(mensaje)
    print(f"\nHash del mensaje: {hash_mensaje}")

if __name__ == "__main__":
    main()