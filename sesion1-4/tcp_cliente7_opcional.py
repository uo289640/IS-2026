import socket
import sys
import struct

def recvall(sock, n):
    buffer = b""
    while len(buffer) < n:
        chunk = sock.recv(n - len(buffer))
        if not chunk:
            return b""
        buffer += chunk
    return buffer

ip_servidor = sys.argv[1] if len(sys.argv) > 1 else "localhost"
puerto = int(sys.argv[2]) if len(sys.argv) > 2 else 9999

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((ip_servidor, puerto))

mensajes_a_enviar = ["HOLA", "ESTO ES UN MENSAJE CON BINARIO", "FIN"]

for m in mensajes_a_enviar:
    datos = m.encode("utf8")
    
    # 1. Convertimos la longitud de los datos a 2 bytes binarios
    bytes_longitud = struct.pack(">H", len(datos))
    
    # 2. Enviamos todo de golpe (cabecera de 2 bytes + el mensaje)
    print(f"Enviando al servidor: {m}")
    s.sendall(bytes_longitud + datos)
    
    # 3. Recibimos la respuesta: leemos los 2 primeros bytes
    bytes_long_resp = recvall(s, 2)
    if bytes_long_resp:
        # Desempaquetamos la longitud
        longitud = struct.unpack(">H", bytes_long_resp)[0]
        
        # Leemos el texto
        datos_resp = recvall(s, longitud)
        respuesta = datos_resp.decode("utf8")
        print(f"Respuesta del servidor: {respuesta}\n")

s.close()
print("Cliente finalizado.")