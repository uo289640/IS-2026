import socket
import sys

ip_servidor = sys.argv[1] if len(sys.argv) > 1 else "localhost"
puerto = int(sys.argv[2]) if len(sys.argv) > 2 else 9999

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((ip_servidor, puerto))

f = s.makefile(mode="r", encoding="utf8")

# Lista de mensajes de distinto tamaño
mensajes_a_enviar = ["HOLA", "ESTO ES UN MENSAJE LARGO", "FIN"]

for m in mensajes_a_enviar:
    # 1. Construimos el paquete: "longitud\nmensaje"
    paquete = f"{len(m)}\n{m}"
    print(f"Enviando al servidor: {repr(paquete)}")
    
    s.sendall(bytes(paquete, "utf8"))
    
    # 2. Leemos la respuesta del servidor (primero longitud, luego mensaje)
    linea_longitud = f.readline()
    if linea_longitud:
        longitud = int(linea_longitud.strip())
        respuesta = f.read(longitud)
        print(f"Respuesta del servidor: {respuesta}\n")

s.close()
print("Cliente finalizado.")