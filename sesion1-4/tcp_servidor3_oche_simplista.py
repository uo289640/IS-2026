import socket
import sys
import time  # Importamos time para el experimento

puerto = int(sys.argv[1]) if len(sys.argv) > 1 else 9999
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(("", puerto))
s.listen(5)

print(f"Servidor Oche escuchando en puerto {puerto}...")

while True:
    print("Esperando un cliente...")
    sd, origen = s.accept()
    
    # EXPERIMENTO: Retardo de 1 segundo para forzar la acumulación de mensajes en TCP
    time.sleep(1)
    
    print(f"Nuevo cliente conectado desde {origen}")
    
    while True:
        # 1. Recibir mensaje (asumimos max 80 bytes y que llega 1 sola línea)
        datos = sd.recv(80)
        if not datos:
            print("El cliente ha cerrado la conexión.")
            sd.close()
            break
            
        mensaje = datos.decode("utf-8")
        
        # 2. Quitar el \r\n final (los dos últimos caracteres)
        linea = mensaje[:-2]
        
        # 3. Darle la vuelta al texto
        linea_invertida = linea[::-1]
        
        # 4. Enviar respuesta añadiendo de nuevo el \r\n
        respuesta = linea_invertida + "\r\n"
        sd.sendall(respuesta.encode("utf-8"))