import socket
import sys

ip_servidor = sys.argv[1] if len(sys.argv) > 1 else "localhost"
puerto = int(sys.argv[2]) if len(sys.argv) > 2 else 9999
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# MEJORA: Conectamos el socket UDP. Esto filtra automáticamente paquetes de otros orígenes.
s.connect((ip_servidor, puerto))

secuencia = 1
while True:
    mensaje = input("Introduce mensaje (FIN para salir): ")
    if mensaje == "FIN":
        break
    
    # Formato "ID:mensaje"
    mensaje_completo = f"{secuencia}:{mensaje}"
    datos_envio = mensaje_completo.encode("utf-8")
    
    timeout_actual = 0.5
    confirmado = False
    
    while not confirmado and timeout_actual <= 2.0:
        s.settimeout(timeout_actual)
        print(f"Enviando '{mensaje_completo}' (Timeout: {timeout_actual}s)")
        
        # Al usar connect(), podemos usar send() en vez de sendto()
        s.send(datos_envio)
        
        try:
            # Al usar connect(), usamos recv() en vez de recvfrom()
            respuesta = s.recv(1024)
            texto_resp = respuesta.decode("utf-8")
            
            # MEJORA: Comprobamos que el OK corresponde al ID exacto que enviamos
            if texto_resp == f"OK:{secuencia}":
                print("Confirmación correcta recibida.\n")
                confirmado = True
            else:
                print(f"Ignorando confirmación de otro paquete: {texto_resp}")
                
        except socket.timeout:
            print("Timeout expirado, reintentando...")
            timeout_actual *= 2
            
    if not confirmado:
        print("Puede que el servidor esté caído. Inténtelo más tarde.")
        sys.exit(1)
        
    secuencia += 1

s.close()