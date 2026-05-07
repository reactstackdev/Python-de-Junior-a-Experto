# Escribe una función resumir_lista(numeros) que reciba una lista de números y devuelva un diccionario con este formato:
# {"positivos": 5, "negativos": 3, "ceros": 2}
# Luego llámala con tu lista de antes e imprime el resultado con f-strings de forma legible, algo como:
# Positivos: 5 | Negativos: 3 | Ceros: 2

lista = [-1 ,-2, 5, 0, 7, 3, 0, 0, 1, 1, 1]
numeros = {}

def resumir_lista(num):
    countPos, countNeg, countCer = 0, 0, 0

    for num in lista:
        if num > 0:
            countPos+=1
        elif num < 0:
            countNeg+=1
        else:
            countCer+=1

    numeros["Positivos"] = countPos
    numeros["Negativos"] = countNeg
    numeros["Ceros"] = countCer

    return numeros

print(f"{resumir_lista(lista)}")
    
        
