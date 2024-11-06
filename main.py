from aes_cipher import generar_clave_aes, cifrar_aes, descifrar_aes
from rsa_cipher import generar_claves_rsa, cifrar_rsa, descifrar_rsa
from digital_signature import firmar_mensaje, verificar_firma
from utils import generar_hash
import os

# Crear carpeta para archivos cifrados si no existe
CARPETA_ARCHIVOS = "archivos_cifrados"
if not os.path.exists(CARPETA_ARCHIVOS):
    os.makedirs(CARPETA_ARCHIVOS)

def cifrar_y_guardar():
    # Solicitar el mensaje y la contraseña
    mensaje = input("Ingrese el mensaje a cifrar: ").encode()
    password = input("Ingrese una contraseña para cifrado AES: ")
    
    # Generar clave AES y cifrar el mensaje
    salt = os.urandom(16)
    clave_aes = generar_clave_aes(password, salt)
    iv, mensaje_cifrado_aes = cifrar_aes(mensaje, clave_aes)
    
    # Solicitar nombre de archivo para guardar
    nombre_archivo = input("Ingrese el nombre del archivo para guardar (sin extensión): ")
    ruta_archivo = os.path.join(CARPETA_ARCHIVOS, f"{nombre_archivo}.txt")

    # Guardar en archivo
    with open(ruta_archivo, "wb") as file:
        file.write(salt + iv + mensaje_cifrado_aes)
    print(f"Mensaje cifrado y guardado en '{ruta_archivo}'.")

def listar_archivos():
    # Listar archivos en la carpeta de archivos cifrados
    archivos = [f for f in os.listdir(CARPETA_ARCHIVOS) if f.endswith(".txt")]
    if archivos:
        print("\nArchivos disponibles para descifrar:")
        for idx, archivo in enumerate(archivos, 1):
            print(f"{idx}. {archivo}")
    else:
        print("\nNo hay archivos disponibles en la carpeta.")
    return archivos

def descifrar_desde_archivo():
    archivos = listar_archivos()
    if not archivos:
        return
    
    # Seleccionar archivo
    try:
        opcion = int(input("\nSeleccione el número del archivo a descifrar: "))
        if opcion < 1 or opcion > len(archivos):
            print("Selección inválida.")
            return
        nombre_archivo = archivos[opcion - 1]
        ruta_archivo = os.path.join(CARPETA_ARCHIVOS, nombre_archivo)
    except ValueError:
        print("Entrada inválida.")
        return
    
    # Leer el archivo y extraer los datos
    with open(ruta_archivo, "rb") as file:
        contenido = file.read()
        salt = contenido[:16]
        iv = contenido[16:32]
        mensaje_cifrado_aes = contenido[32:]

    intentos = 2  # Número de intentos permitidos para ingresar la contraseña
    while intentos > 0:
        password = input("Ingrese la contraseña para descifrar AES: ")
        clave_aes = generar_clave_aes(password, salt)
        
        try:
            # Intentar descifrar el mensaje
            mensaje_descifrado_aes = descifrar_aes(iv, mensaje_cifrado_aes, clave_aes)
            print(f"\nMensaje descifrado: {mensaje_descifrado_aes.decode()}")
            return  # Salir de la función si el descifrado es exitoso
        except Exception:
            intentos -= 1
            if intentos > 0:
                print("Contraseña incorrecta. Inténtelo de nuevo.")
            else:
                print("Contraseña incorrecta.")

def cifrar_terminal():
    # Solicitar el mensaje y la contraseña
    mensaje = input("Ingrese el mensaje a cifrar: ").encode()
    password = input("Ingrese una contraseña para cifrado AES: ")
    
    # Generar clave AES y cifrar el mensaje
    salt = os.urandom(16)
    clave_aes = generar_clave_aes(password, salt)
    iv, mensaje_cifrado_aes = cifrar_aes(mensaje, clave_aes)
    
    print(f"\nMensaje cifrado (AES): {mensaje_cifrado_aes}")
    return salt, iv, mensaje_cifrado_aes, password

def descifrar_terminal(salt, iv, mensaje_cifrado_aes, password):
    # Generar clave AES y descifrar el mensaje
    clave_aes = generar_clave_aes(password, salt)
    mensaje_descifrado_aes = descifrar_aes(iv, mensaje_cifrado_aes, clave_aes)
    print(f"\nMensaje descifrado: {mensaje_descifrado_aes.decode()}")

def main():
    while True:
        print("\nOpciones disponibles:")
        print("1: Cifrar y Guardar en Archivo")
        print("2: Descifrar desde Archivo")
        print("3: Cifrar y Descifrar en Terminal")
        print("4: Salir")

        opcion = input("Seleccione una opción: ")
        
        if opcion == "1":
            cifrar_y_guardar()
        elif opcion == "2":
            descifrar_desde_archivo()
        elif opcion == "3":
            # Cifrado y Descifrado en Terminal
            salt, iv, mensaje_cifrado_aes, password = cifrar_terminal()
            if input("\n¿Desea descifrar el mensaje en la terminal ahora? (s/n): ").lower() == 's':
                descifrar_terminal(salt, iv, mensaje_cifrado_aes, password)
        elif opcion == "4":
            print("Saliendo del programa.")
            break
        else:
            print("Opción no válida.")

        # Preguntar si desea realizar otra operación
        continuar = input("\n¿Desea realizar otra operación? (s/n): ").lower()
        if continuar != 's':
            print("Saliendo del programa.")
            break

if __name__ == "__main__":
    main()