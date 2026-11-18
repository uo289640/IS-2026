# Muestra los servidores MX de gmail.com, con su IP,
# en el orden en que un MTA los probaría (menor preference primero)
import dns.resolver

respuesta = dns.resolver.resolve('gmail.com', 'MX')
for registro in sorted(respuesta, key=lambda r: r.preference):
    nombre = registro.exchange
    ip = dns.resolver.resolve(nombre, 'A')[0].address
    print(registro.preference, nombre, ip)
