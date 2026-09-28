class Cliente:

    def __init__(self, nombre, telefono, preferencias):

        self.nombre = nombre

        self.telefono = telefono

        self.preferencias = preferencias


# Ejemplo de uso
cliente1 = Cliente("Juan", "3001234567", "Corte degradado")

print(f"Cliente: {cliente1.nombre} - Preferencia: {cliente1.preferencias}")