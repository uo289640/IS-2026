import paramiko
import getpass
import base64

client = paramiko.SSHClient()

# --- SOLUCIÓN EJERCICIO 10 ---
# 1. Ya NO ponemos set_missing_host_key_policy. Por defecto, Paramiko 
#    ahora rechazará cualquier conexión desconocida.

# 2. Codificamos la clave pública real de tu servidor
clave_b64 = b'AAAAC3NzaC1lZDI1NTE5AAAAIFNw02TtoFCf2XhKd4+RB260u67QjJwjQT3odZLyy6ag'
key = paramiko.Ed25519Key(data=base64.b64decode(clave_b64))

# 3. Añadimos esta clave a la caja fuerte interna de Paramiko
client.get_host_keys().add('localhost', 'ssh-ed25519', key)

user = input("Introduce tu usuario: ")
pwd = getpass.getpass("Introduce tu contraseña: ")

try:
    print("Conectando de forma 100% segura...")
    client.connect('localhost', username=user, password=pwd)
    print("¡Conectado con éxito! Ningún impostor a la vista.")
except paramiko.SSHException as e:
    print(f"Alarma de seguridad (conexión rechazada): {e}")
finally:
    client.close()
