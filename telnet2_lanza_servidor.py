import telnetlib
import time

HOST = "localhost"
USER = b"uo289640"
PASS = b"Fabarin.7"

print("Conectando al servidor...")
tn = telnetlib.Telnet(HOST)

# 1. Autenticación automática (mala práctica de seguridad, pero es lo que pide el guion)
tn.read_until(b"login: ")
tn.write(USER + b"\n")
tn.read_until(b"Password: ")
tn.write(PASS + b"\n")

# 3. Esperamos el primer prompt
tn.read_until(b"$")

# 4. Enviamos el comando para ver los procesos
tn.write(b"ps -ef\n")

# 5. Capturamos todo hasta el siguiente prompt
salida = tn.read_until(b"$").decode('utf-8')

# 6 y 7. Comprobamos si el servidor está en la lista de procesos
if "udp_servidor3_con_ok.py" in salida:
    print("El servidor ya está en ejecución")
else:
    print("El servidor no estaba corriendo. Lanzándolo...")
    tn.write(b"nohup python3 udp_servidor3_con_ok.py &\n")
    # 8. Esperamos 1 segundo a que arranque
    time.sleep(1)

# 9. Cerramos sesión
tn.write(b"exit\n")

# 10. Imprimimos el rastro final para depurar
print("\n--- Rastro de la sesión ---")
print(tn.read_all().decode('utf-8'))
