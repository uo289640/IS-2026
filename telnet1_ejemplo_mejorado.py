import getpass
import telnetlib

HOST = "localhost"
user = input("Introduce tu usuario remoto: ")
password = getpass.getpass("Introduce la contraseña: ")

tn = telnetlib.Telnet(HOST)

tn.read_until(b"login: ")
tn.write(user.encode('utf-8') + b"\n")

if password:
    tn.read_until(b"Password: ")
    tn.write(password.encode('utf-8') + b"\n")

# --- LA MEJORA ESTÁ AQUÍ ---
# Leemos y descartamos todo el texto de bienvenida hasta el primer prompt ($)
tn.read_until(b"$")

# Ahora sí, enviamos el comando y salimos
tn.write(b"ls -la /home\n")
tn.write(b"exit\n")

# Leemos y mostramos el resultado limpio
print(tn.read_all().decode('utf-8'))
