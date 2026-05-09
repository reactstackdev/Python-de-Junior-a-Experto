# =============================================================================
# ENUNCIADO — Módulo: modelos/usuario.py
# Este fichero es un módulo dentro del paquete modelos. Define la clase
# Usuario con nombre y email. Se importa desde main.py con:
#   from modelos.usuario import Usuario
# =============================================================================

class Usuario:
    def __init__(self, nombre, email):
        self.nombre = nombre
        self.email = email

    def __str__(self):
        return f"El usuario se llama {self.nombre} y su email es {self.email}"
