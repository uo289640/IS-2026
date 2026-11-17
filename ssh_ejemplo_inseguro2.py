import paramiko
import getpass

client = paramiko.SSHClient()

# --- SOLUCIÓN EJERCICIO 9 ---
# Usamos WarningPolicy: entra igual, pero avisa del peligro
client.set_missing_host_key_policy(paramiko.WarningPolicy())

user = input("Introduce tu usuario: ")
pwd = getpass.getpass("Introduce tu contraseña: ")

try:
    print("Conectando...")
    client.connect('localhost', username=user, password=pwd)
    print("¡Conectado con éxito!")
finally:
    client.close()
