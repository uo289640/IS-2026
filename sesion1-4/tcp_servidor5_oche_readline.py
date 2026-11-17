import socket
import sys
import time

puerto = int(sys.argv[1]) if len(sys.argv) > 1 else 9999

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
s.bind(("", puerto))
s.listen(5)
print(f"Servidor Oche (readline) escuchando en puerto {puerto}...")

while True:
    print("Esperando cliente...")
    sd, origen = s.accept()
    print(f"Cliente conectado desde {origen}")
    
    # Retardo provocado para que se acumulen los mensajes del cliente
    time.sleep(1)
    
    # MAGIA AQUÍ: Convertimos el socket a modo fichero de texto
    f = sd.makefile(encoding="utf8", newline="\r\n")
    
    while True:
        # Lee hasta encontrar el \r\n (y lo incluye en el resultado)
        mensaje = f.readline()
        
        if not mensaje:  # Retorna cadena vacía si el cliente cierra la conexión
            print("Cliente desconectado.")
            break
            
        print(f"Recibido: {repr(mensaje)}")
        
        # Le quitamos los 2 últimos caracteres (\r\n) y le damos la vuelta
        linea = mensaje[:-2][::-1]
        
        # Volvemos a añadir el \r\n y lo enviamos
        respuesta = linea + "\r\n"
        sd.sendall(bytes(respuesta, "utf8"))
        
    sd.close()