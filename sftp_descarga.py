import paramiko
import getpass
import os
from stat import S_ISDIR

client = paramiko.SSHClient()
client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

user = input("Introduce tu usuario: ")
pwd = getpass.getpass("Introduce tu contraseña: ")

# Vamos a descargar los archivos de tu carpeta de prácticas
carpeta_remota = "/home/" + user + "/IS-2026"
carpeta_local = "descargas_sftp"

try:
    print("Conectando y abriendo SFTP...")
    client.connect('localhost', username=user, password=pwd)
    sftp = client.open_sftp()
    
    # Creamos la carpeta local si no existe para no mezclar archivos
    if not os.path.exists(carpeta_local):
        os.makedirs(carpeta_local)
        
    print(f"\nExplorando: {carpeta_remota}")
    listado = sftp.listdir(carpeta_remota)
    
    for nombre in listado:
        ruta_remota = f"{carpeta_remota}/{nombre}"
        ruta_local = f"{carpeta_local}/{nombre}"
        
        # Averiguamos los permisos/tipo de ese elemento remoto
        modo = sftp.stat(ruta_remota).st_mode
        
        # Si NO es un directorio, lo descargamos
        if not S_ISDIR(modo):
            print(f"[FICHERO] Descargando -> {nombre}")
            sftp.get(ruta_remota, ruta_local)
        else:
            print(f"[CARPETA] Ignorando -> {nombre}")
            
    sftp.close()
    print("\n¡Todas las descargas completadas con éxito!")
    
except Exception as e:
    print(f"Error: {e}")
finally:
    client.close()
