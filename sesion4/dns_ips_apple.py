# Muestra todas las IPs (registros A) de apple.com
import dns.resolver

respuesta = dns.resolver.resolve('apple.com')
for registro in respuesta:
    print(registro.address)
