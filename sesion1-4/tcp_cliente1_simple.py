import socket
import sys

ip_servidor = sys.argv[1] if len(sys.argv) > 1 else "localhost"
puerto = int(sys.argv[2]) if len(sys.argv) > 2 else 9999

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((ip_servidor, puerto))

# Enviamos 5 veces el texto de exactamente 5 bytes
for i in range(5):
    print("Enviando 'ABCDE'...")
    s.send(b"ABCDE")

# Cerramos la comunicación
print("Enviando 'FINAL'...")
s.send(b"FINAL")
s.close()