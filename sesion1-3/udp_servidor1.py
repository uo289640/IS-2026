import socket
import sys

# Configuración del puerto
puerto = int(sys.argv[1]) if len(sys.argv) > 1 else 9999

# Crear el socket UDP
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.bind(("", puerto))

print(f"Servidor UDP escuchando en el puerto {puerto}...")

while True:
    # Recibir datagrama (máximo 1024 bytes)
    datagrama, origen = s.recvfrom(1024)
    texto = datagrama.decode("utf-8")
    print(f"Recibido de {origen}: {texto}")
    
