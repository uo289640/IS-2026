import ftplib
import getpass

# 1. Definimos la función "callback" que acumula las líneas que llegan
lista = []
def acumular(linea):
    lista.append(linea)

# 2. Pedimos usuario y clave
user = input("Introduce tu usuario FTP: ")
clave = getpass.getpass("Introduce tu clave FTP: ")

try:
    print("\nConectando al servidor FTP...")
    f = ftplib.FTP("localhost")
    f.login(user, clave)
    
    # 3. Nos movemos a la carpeta que acabamos de crear
    f.cwd("prueba-ftp")
    
    # 4. Enviamos el comando LIST y le decimos que use nuestra función 'acumular'
    resp = f.retrlines("LIST", acumular)
    
    print("\nRespuesta del protocolo:", resp)
    print("Contenidos de la carpeta remota:")
    for l in lista:
        print(l)
        
    f.quit()
except Exception as e:
    print(f"Error FTP: {e}")
