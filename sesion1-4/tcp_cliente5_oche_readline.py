import socket
import sys

ip_servidor = sys.argv[1] if len(sys.argv) > 1 else "localhost"
puerto = int(sys.argv[2]) if len(sys.argv) > 2 else 9999

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((ip_servidor, puerto))

# Convertimos también el socket en fichero para leer las respuestas
f = s.makefile(encoding="utf8", newline="\r\n")

# Enviamos 3 mensajes de golpe
mensajes_a_enviar = ["UNO\r\n", "DOS\r\n", "TRES\r\n"]
for m in mensajes_a_enviar:
    print(f"Enviando: {repr(m)}")
    s.sendall(bytes(m, "utf8"))

# Ahora recibimos las 3 respuestas usando readline()
for i in range(3):
    respuesta = f.readline()
    print(f"Respuesta del servidor: {repr(respuesta)}")

s.close()
print("Cliente finalizado.")