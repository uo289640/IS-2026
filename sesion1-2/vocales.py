def contar_vocales(cadena):
    # Inicializamos el diccionario con todas las vocales a 0
    vocales = {'a': 0, 'e': 0, 'i': 0, 'o': 0, 'u': 0}
    
    # Recorremos la frase letra a letra pasándola a minúsculas
    for letra in cadena.lower():
        
        # Si la letra está en nuestro diccionario, le sumamos 1
        if letra in vocales:
            vocales[letra] += 1
            
    return vocales

if __name__ == "__main__":
    txt = "Esto es una prueba. Esta cadena contiene vocales variadas"
    result = contar_vocales(txt)
    print("Frase analizada:", txt)
    print("Recuento de vocales:", result)