class Cliente:

    # 1. ATRIBUTOS (Inicialización)
    def __init__(self, nombre, telefono, preferencias):
        self.nombre = nombre
        self.telefono = telefono
        self.preferencias = preferencias
        self.tiene_cita = False

    # 2. MÉTODOS (Acciones del cliente)
    def reservar_cita(self):
        self.tiene_cita = True
        print(f"{self.nombre} reservo una cita.")

    def cancelar_cita(self):
        self.tiene_cita = False
        print(f"{self.nombre} cancelo su cita.")

    def cambiar_preferencias(self, nueva_preferencia):
        self.preferencias = nueva_preferencia
        print(f"{self.nombre} actualizo su preferencia a: {self.preferencias}")

    # Método para retornar la información formateada
    def descripcion(self):
        estado_cita = "Con cita" if self.tiene_cita else "Sin cita"
        return f"Cliente: {self.nombre} | Telefono: {self.telefono} | Preferencia: {self.preferencias} | Estado: {estado_cita}"




# Inicialización de la lista
lista_clientes = []


lista_clientes.append(
    Cliente(
        nombre="Juan",
        telefono="3001234567",
        preferencias="Corte degradado"
    )
)

lista_clientes.append(
    Cliente(
        nombre="Maria",
        telefono="3109876543",
        preferencias="Tinte y peinado"
    )
)

lista_clientes.append(
    Cliente(
        nombre="Carlos",
        telefono="3205554433",
        preferencias="Corte con diseno y barba"
    )
)


lista_clientes[0].reservar_cita()
lista_clientes[1].cambiar_preferencias("Balayage y secado")

# Impresión con encabezado y separador
print("\nLISTA DE CLIENTES")
print("-" * 80)

# Recorrer la lista con un bucle for
for cliente in lista_clientes:
    print(cliente.descripcion())