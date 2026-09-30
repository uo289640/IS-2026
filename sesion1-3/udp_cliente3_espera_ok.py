import socket
import sys

ip_servidor = sys.argv[1] if len(sys.argv) > 1 else "localhost"
puerto = int(sys.argv[2]) if len(sys.argv) > 2 else 9999
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Establecer timeout de 0.5 segundos para recepciones
s.settimeout(0.5)

secuencia = 1
while True:
    mensaje = input("Introduce mensaje (FIN para salir): ")
    if mensaje == "FIN":
        break
    
    mensaje_completo = f"{secuencia}: {mensaje}"
    s.sendto(mensaje_completo.encode("utf-8"), (ip_servidor, puerto))
    
    # Esperar confirmación
    try:
        respuesta, origen = s.recvfrom(1024)
        if respuesta.decode("utf-8") == "OK":
            print("Confirmación recibida.")
        else:
            print("Respuesta inesperada.")
    except socket.timeout:
        print("ERROR. El datagrama de confirmación no llega.")
        
    secuencia += 1

s.close()