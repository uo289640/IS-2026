import ftplib
import getpass

user = input("Introduce tu usuario FTP: ")
clave = getpass.getpass("Introduce tu clave FTP: ")

# El nombre del archivo remoto que queremos descargar
archivo_a_descargar = "fichero1.txt"

try:
    print("\nConectando al servidor...")
    f = ftplib.FTP("localhost")
    f.login(user, clave)
    
    # Entramos en la carpeta donde están las pruebas
    f.cwd("prueba-ftp")
    
    # --- LA DESCARGA (Ejercicios 18 y 19) ---
    print(f"Descargando '{archivo_a_descargar}'...")
    
    # 1. Abrimos un archivo local con el mismo nombre en modo "Write Binary" (wb)
    with open(archivo_a_descargar, "wb") as archivo_local:
        # 2. Le decimos al servidor que recupere (RETR) el archivo y lo escriba en el nuestro
        # El tamaño del bloque (8192 bytes) suele ser el estándar por defecto.
        f.retrbinary(f"RETR {archivo_a_descargar}", archivo_local.write, 8192)
        
    print("¡Descarga completada con éxito!")
    f.quit()
    
except Exception as e:
    print(f"Error FTP: {e}")
