import socket
import sys

ip_servidor = sys.argv[1] if len(sys.argv) > 1 else "localhost"
puerto = int(sys.argv[2]) if len(sys.argv) > 2 else 9999

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((ip_servidor, puerto))

for i in range(5):
    print("Enviando 'ABCD' con sendall...")
    s.sendall(b"ABCD")

print("Enviando 'FINAL'...")
s.sendall(b"FINAL")
s.close()