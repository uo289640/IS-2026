import dns.resolver

# query() está obsoleto en dnspython 2.x; resolve() hace lo mismo
respuesta = dns.resolver.resolve('en.wikipedia.org')
print(respuesta[0].address)

# Respuesta del servidor en formato legible
print(respuesta.response)

# Y en el formato binario del protocolo (curiosidad)
print(respuesta.response.to_wire())
