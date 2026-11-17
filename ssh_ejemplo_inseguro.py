import paramiko
import time
import getpass

client = paramiko.SSHClient()

# --- SOLUCIÓN EJERCICIO 8 ---
# Política insegura: aceptamos automáticamente cualquier host key (fingerprint) desconocido
client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

user = input("Introduce tu usuario (ej. uo289640): ")
pwd = getpass.getpass("Introduce tu contraseña (la normal de inicio de sesión): ")

try:
    print("Conectando...")
    client.connect('localhost', username=user, password=pwd)
    print("¡Conectado con éxito!")

    # Ejecutamos el comando ls de forma remota
    stdin, stdout, stderr = client.exec_command('ls')

    # Mostramos el resultado limpio (rstrip quita los saltos de línea sobrantes)
    print("\n--- Resultado de 'ls' ---")
    for line in stdout:
        print(line.rstrip())

    time.sleep(1) # Damos tiempo a que se vacíen los buffers
except paramiko.AuthenticationException:
    print("Error: Autenticación fallida (contraseña incorrecta).")
except Exception as e:
    print(f"Error inesperado: {e}")
finally:
    client.close()
