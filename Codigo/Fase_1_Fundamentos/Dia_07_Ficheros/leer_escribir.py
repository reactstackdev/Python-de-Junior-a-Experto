# =============================================================================
# ENUNCIADO
# Practica lectura y escritura de ficheros de texto en Python.
#   1. Crea un fichero llamado "notas.txt" y escribe en él tres líneas de texto.
#   2. Léelo completo e imprime su contenido.
#   3. Añade una cuarta línea sin borrar las anteriores.
#   4. Léelo de nuevo para confirmar que las cuatro líneas están.
# Usa open() con los modos "w", "r" y "a". Cierra siempre el fichero con close()
# o usando el bloque with.
# =============================================================================

# w es para escribir, r es para leer y a es para añadir sin borrar lo anterior

with open ("texto.txt", "w") as f:
    f.write("Hola soy Sergio\n")
    f.write("Estoy haciendo pruebas\n")
    f.write("Para poder aprender python\n")

with open ("texto.txt", "r") as f:
    contenido = f.read()
    print(contenido)
    
with open ("texto.txt", "a") as f:
    f.write("Y esto es una nueva linea\n")
    
with open ("texto.txt", "r") as f:
    contenido = f.read()
    print(contenido)