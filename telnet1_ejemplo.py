import getpass
import telnetlib

HOST = "localhost"
user = input("Introduce tu usuario remoto (ej. alumno): ")
password = getpass.getpass("Introduce la contraseña: ")

# Conectamos
tn = telnetlib.Telnet(HOST)

# Esperamos a que pida el login y lo enviamos
tn.read_until(b"login: ")
tn.write(user.encode('utf-8') + b"\n")

# Si hemos escrito contraseña, esperamos a que la pida y la enviamos
if password:
    tn.read_until(b"Password: ")
    tn.write(password.encode('utf-8') + b"\n")

# Ejecutamos el comando modificado que pide la práctica (ls /home)
tn.write(b"ls -la /home\n")
tn.write(b"exit\n")

# Leemos todo hasta que se cierre la conexión y lo mostramos en pantalla
print(tn.read_all().decode('utf-8'))
