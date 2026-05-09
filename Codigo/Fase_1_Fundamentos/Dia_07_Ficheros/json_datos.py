# =============================================================================
# ENUNCIADO
# Practica lectura y escritura de ficheros JSON en Python.
#   1. Crea un diccionario con datos de un usuario (nombre, edad, lenguajes).
#   2. Guárdalo en un fichero "usuario.json" usando el módulo json.
#   3. Léelo desde el fichero y reconstruye el diccionario.
#   4. Imprime el nombre y recorre la lista de lenguajes con un bucle.
# Usa json.dump() para escribir y json.load() para leer.
# =============================================================================

import json

usuario = {
    "nombre": "Sergio",
    "edad": 23,
    "lenguajes": ["Python", "Java", "C"]
}

with open ("usuario.json", "w") as f:
    json.dump(usuario, f, indent=4)
    
with open ("usuario.json", "r") as f:
    contenido = json.load(f)
    print(contenido["nombre"])
    for lenguaje in contenido["lenguajes"]:
        print(lenguaje)