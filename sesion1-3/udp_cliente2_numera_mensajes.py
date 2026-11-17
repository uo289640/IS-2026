import socket
import sys

ip_servidor = sys.argv[1] if len(sys.argv) > 1 else "localhost"
puerto = int(sys.argv[2]) if len(sys.argv) > 2 else 9999
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

secuencia = 1
while True:
    mensaje = input("Introduce mensaje (FIN para salir): ")
    if mensaje == "FIN":
        break
    
    # Añadir el número de secuencia
    mensaje_completo = f"{secuencia}: {mensaje}"
    s.sendto(mensaje_completo.encode("utf-8"), (ip_servidor, puerto))
    secuencia += 1

s.close()