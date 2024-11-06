# Cifrar_SEG

Trabajo Final de Seguridad Informatica II - 2024 - Universidad de Mendoza - Sede San Rafael - Facultad de Ingenieria

## Cifrado y Descifrado de Mensajes en Python

Este proyecto implementa un sistema de cifrado y descifrado de mensajes utilizando algoritmos de cifrado simétrico (AES) y asimétrico (RSA) en Python. Además, permite firmar mensajes digitalmente y verificar firmas. La aplicación permite cifrar y descifrar mensajes en la terminal, así como guardar los mensajes cifrados en archivos para descifrarlos posteriormente.

### Estructura del Proyecto

. ├── archivos_cifrados # Carpeta donde se almacenan los archivos cifrados ├── aes_cipher.py # Módulo para generar claves y cifrar/descifrar con AES ├── rsa_cipher.py # Módulo para generar claves y cifrar/descifrar con RSA ├── digital_signature.py # Módulo para firmar y verificar mensajes ├── utils.py # Módulo de utilidades (funciones hash) └── main.py # Archivo principal del programa

## Requisitos

Para ejecutar este proyecto, necesitas tener instalado Python 3 y las siguientes bibliotecas:

pip install cryptography

## Instrucciones de Uso

1. Clona el repositorio:

    HTTPS:git clone https://github.com/Lucas16AR/Cifrar_SEG.git
    SSH: git clone git@github.com:Lucas16AR/Cifrar_SEG.git

    cd Cifrar_SEG

2. Ejecuta el programa:

    python main.py


## Funcionalidades

El programa ofrece diversas funcionalidades accesibles desde un menú principal.
1. Cifrar y Guardar en Archivo

    Descripción: Cifra un mensaje ingresado por el usuario utilizando AES y lo guarda en un archivo.
    Proceso:
        Ingresar el mensaje a cifrar.
        Especificar una contraseña para generar la clave de cifrado.
        Ingresar un nombre para el archivo cifrado, que se guardará en la carpeta archivos_cifrados.

2. Descifrar desde Archivo

    Descripción: Permite seleccionar un archivo cifrado previamente y descifrar su contenido utilizando la misma contraseña que se usó para cifrarlo.
    Proceso:
        El programa lista los archivos disponibles en la carpeta archivos_cifrados.
        Selecciona el archivo a descifrar.
        Introduce la contraseña para descifrar el archivo.
        Si la contraseña es incorrecta, el programa permite un segundo intento.
        Si ambos intentos fallan, se regresa al menú principal con un mensaje de error.

3. Cifrar y Descifrar en Terminal

    Descripción: Cifra un mensaje ingresado en la terminal y permite descifrarlo en la misma sesión.
    Proceso:
        Ingresar el mensaje y la contraseña para cifrarlo.
        El mensaje cifrado se muestra en la terminal.
        Opcionalmente, se ofrece descifrar el mensaje en la terminal.

4. Salir del Programa

    Descripción: Permite salir del programa desde el menú principal o tras cualquier operación.

Ejemplo de Uso
Cifrar un Mensaje y Guardarlo en un Archivo

    Al ejecutar el programa, selecciona la opción 1.
    Ingresa un mensaje, por ejemplo: "Este es un mensaje secreto."
    Define una contraseña, por ejemplo: ContraseñaSegura123
    Ingresa un nombre para el archivo, como mensaje_secreto.
    El mensaje cifrado se guarda en archivos_cifrados/mensaje_secreto.txt.

Descifrar un Mensaje desde un Archivo

    Selecciona la opción 2.
    Escoge el archivo mensaje_secreto.txt de la lista.
    Ingresa la contraseña: ContraseñaSegura123.
    Si la contraseña es correcta, el mensaje descifrado se muestra en la terminal.

Módulos del Proyecto

    aes_cipher.py
        Contiene funciones para generar una clave AES a partir de una contraseña y una sal. También incluye funciones para cifrar y descifrar mensajes utilizando el algoritmo AES.

    rsa_cipher.py
        Implementa la generación de claves RSA y permite cifrar y descifrar mensajes mediante RSA.

    digital_signature.py
        Permite firmar mensajes utilizando RSA y verificar la firma de los mensajes, asegurando la autenticidad.

    utils.py
        Incluye una función para generar un hash SHA-256 del mensaje, útil para integridad y autenticidad de los mensajes.

    main.py
        Archivo principal que gestiona el flujo del programa, con un menú de opciones que permite cifrar, descifrar, guardar y listar archivos cifrados.

Manejo de Errores

    Contraseña Incorrecta: En la opción de descifrado, si la contraseña es incorrecta, se permite un segundo intento. Si ambos intentos fallan, el programa muestra un mensaje de error y regresa al menú principal.
    Archivos Faltantes: Si no hay archivos disponibles para descifrar, el programa informa al usuario.
    Selección Inválida: Si se ingresa una opción incorrecta en el menú, se muestra un mensaje de error y se solicita una opción válida.