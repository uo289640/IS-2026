import socket
import sys

# Configuración de IP y puerto
ip_servidor = sys.argv[1] if len(sys.argv) > 1 else "localhost"
puerto = int(sys.argv[2]) if len(sys.argv) > 2 else 9999

# Crear el socket UDP
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

while True:
    mensaje = input("Introduce mensaje (FIN para salir): ")
    if mensaje == "FIN":
        break
    
    # Enviar datagrama convertido a bytes
    s.sendto(mensaje.encode("utf-8"), (ip_servidor, puerto))

s.close()