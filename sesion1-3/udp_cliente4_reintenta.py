import socket
import sys

ip_servidor = sys.argv[1] if len(sys.argv) > 1 else "localhost"
puerto = int(sys.argv[2]) if len(sys.argv) > 2 else 9999
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

secuencia = 1
while True:
    mensaje = input("Introduce mensaje (FIN para salir): ")
    if mensaje == "FIN":
        break
    
    mensaje_completo = f"{secuencia}: {mensaje}"
    datos_envio = mensaje_completo.encode("utf-8")
    
    timeout_actual = 0.5
    confirmado = False
    
    while not confirmado and timeout_actual <= 2.0:
        s.settimeout(timeout_actual)
        print(f"Enviando '{mensaje_completo}' (Timeout: {timeout_actual}s)")
        s.sendto(datos_envio, (ip_servidor, puerto))
        
        try:
            respuesta, origen = s.recvfrom(1024)
            if respuesta.decode("utf-8") == "OK":
                print("Confirmación recibida.")
                confirmado = True
        except socket.timeout:
            print("Timeout expirado, reintentando...")
            timeout_actual *= 2  # Duplicar el timeout en cada reintento
            
    if not confirmado:
        print("Puede que el servidor esté caído. Inténtelo más tarde.")
        sys.exit(1)
        
    secuencia += 1

s.close()