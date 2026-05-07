# Escribe una función llamada clasificar_numero que reciba un número entero y devuelva un string: "positivo", "negativo" o "cero". 
# Luego, desde fuera de la función, crea una lista con al menos 5 números (positivos, negativos y el cero), 
# recórrela con un bucle, llama a la función con cada número e imprime algo como: "El número 3 es positivo".

def clasificar_numero(num):
    if num > 0:
        return "positivo"
    elif num < 0:
        return "negativo"
    else:
        return "cero"

lista = [0, 2, -3, 4, -5, 6, -7, -8, 9, 10]

for num in lista:
    print(f"El numero: {num} es {clasificar_numero(num)}")


