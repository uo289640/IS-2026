import paramiko
import getpass

client = paramiko.SSHClient()
client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

user = input("Introduce tu usuario: ")
pwd = getpass.getpass("Introduce tu contraseña: ")

try:
    print("Estableciendo túnel SSH...")
    client.connect('localhost', username=user, password=pwd)
    
    print("Abriendo canal SFTP...")
    sftp = client.open_sftp()
    
    print("\n--- Contenido de tu carpeta (SFTP) ---")
    listado = sftp.listdir() 
    for nombre in listado:
        print(nombre)
        
    sftp.close() 
except Exception as e:
    print(f"Error: {e}")
finally:
    client.close()
