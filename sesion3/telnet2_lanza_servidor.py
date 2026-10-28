import telnetlib
import time

HOST = "localhost"

# 1. Nos conectamos a telnet con las credenciales incrustadas en el codigo
USER = "uo289640"
PASSWORD = "Fabarin.7" 

print(f"Conectando a {HOST}...")
tn = telnetlib.Telnet(HOST)

tn.read_until(b"login: ")
tn.write(USER.encode('utf-8') + b"\n")
tn.read_until(b"Password: ")
tn.write(PASSWORD.encode('utf-8') + b"\n")

# 2. Esperamos al prompt
tn.read_until(b"$")

# 3. Listamos los procesos del usuario
tn.write(b"ps -ef\n")

# 5. Esperamos al siguiente prompt y capturamos la respuesta en una variable
salida_ps = tn.read_until(b"$").decode('utf-8', errors='ignore')

# 6. Comprobamos si la respuesta contiene la cadena udp_servidor3_con_ok.py
if "udp_servidor3_con_ok.py" in salida_ps:
    print("El servidor ya está en ejecución")
else:
    # 6. Si la cadena no está, el servidor no está en ejecución, lo lanzamos
    print("El servidor NO está en ejecución. Lanzándolo ahora...")
    tn.write(b"nohup python3 ~/udp_servidor3_con_ok.py &\n")
    
    # 7. Esperamos un segundo a que el servidor arranque 
    time.sleep(1)

# 8. Terminamos la sesion telnet
tn.write(b"exit\n")

# 9. Mostramos la respuesta del servidor
salida_final = tn.read_all().decode('utf-8', errors='ignore')
print("\n--- SALIDA PARA DEPURACIÓN ---")
print(salida_final)
print("------------------------------")