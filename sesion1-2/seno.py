import math

def calcular_seno():
    "Calcula el seno de x desde 0 hasta pi en incrementos de 0.1 y lo devuelve en una lista."
    resultados = []
    x = 0.0
    
    # Mientras x sea menor o igual a pi
    while x <= math.pi:
        
        # Calculamos el seno y lo metemos en la lista
        resultados.append(math.sin(x))
        
        # Le sumamos 0.1 a la x 
        x += 0.1
        
    return resultados

if __name__ == "__main__":
    lista_senos = calcular_seno()
    print("La lista de senos es:")
    print(lista_senos)