import ftplib
import getpass

lista = []
def acumular(linea):
    lista.append(linea)

user = input("Introduce tu usuario FTP: ")
clave = getpass.getpass("Introduce tu clave FTP: ")

try:
    f = ftplib.FTP("localhost")
    f.login(user, clave)
    f.cwd("prueba-ftp")
    
    # 1. Usamos MLSD en lugar de LIST
    f.retrlines("MLSD", acumular)
    
    print("\nArchivos encontrados (nombres limpios):")
    for l in lista:
        # 2. Ignoramos los directorios actual (.) y padre (..)
        if "type=cdir" in l or "type=pdir" in l:
            continue
            
        # 3. La línea de MLSD tiene este formato: "datos_estandarizados; nombre_del_fichero"
        # Usamos split para romper la frase por el primer espacio en blanco
        partes = l.split(" ", 1)
        if len(partes) == 2:
            nombre = partes[1]
            print(f"- {nombre}")
            
    f.quit()
except Exception as e:
    print(f"Error FTP: {e}")
