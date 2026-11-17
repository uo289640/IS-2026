import socket
import sys

puerto = int(sys.argv[1]) if len(sys.argv) > 1 else 9999

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
s.bind(("", puerto))
s.listen(5)
print(f"Servidor Oche (Longitud ASCII) escuchando en puerto {puerto}...")

while True:
    print("Esperando cliente...")
    sd, origen = s.accept()
    print(f"Cliente conectado desde {origen}")
    
    # Abrimos el socket como fichero en modo lectura ("r")
    f = sd.makefile(mode="r", encoding="utf8")
    
    while True:
        # 1. Leemos solo la primera línea (que contiene el número de la longitud)
        linea_longitud = f.readline()
        
        if not linea_longitud:
            print("Cliente desconectado.")
            break
            
        # 2. Convertimos ese texto a un número entero (strip quita el \n)
        longitud = int(linea_longitud.strip())
        
        # 3. Leemos EXACTAMENTE esa cantidad de caracteres
        mensaje = f.read(longitud)
        print(f"Recibido mensaje de {longitud} caracteres: {mensaje}")
        
        # 4. Le damos la vuelta
        mensaje_invertido = mensaje[::-1]
        
        # 5. Preparamos la respuesta con el mismo formato: "longitud\nrespuesta"
        respuesta_completa = f"{len(mensaje_invertido)}\n{mensaje_invertido}"
        sd.sendall(bytes(respuesta_completa, "utf8"))
        
    sd.close()