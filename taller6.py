# ==========================================
# DEFINICIÓN DE CLASES
# ==========================================
class Cliente:

    def __init__(self, cedula, nombre, telefono, servicio_habitual):
        self.cedula = cedula
        self.nombre = nombre
        self.telefono = telefono
        self.servicio_habitual = servicio_habitual

    def calcular_total(self, monto):
        return monto

    def __str__(self):
        return (
            f"[Regular] Cédula: {self.cedula} | Nombre: {self.nombre} | "
            f"Tel: {self.telefono} | Servicio: {self.servicio_habitual}"
        )


class ClienteVIP(Cliente):

    def __init__(
        self, cedula, nombre, telefono, servicio_habitual, descuento=0.15
    ):
        super().__init__(cedula, nombre, telefono, servicio_habitual)
        self.descuento = descuento

    def calcular_total(self, monto):
        return monto * (1 - self.descuento)

    def __str__(self):
        return (
            f"[VIP {int(self.descuento * 100)}% OFF] Cédula: {self.cedula} | "
            f"Nombre: {self.nombre} | Tel: {self.telefono} | "
            f"Servicio: {self.servicio_habitual}"
        )



def mostrar_lista_clientes(lista):
    print("--------------------------------------------------")
    if not lista:
        print("La lista de clientes está vacía.")
    else:
        for cliente in lista:
            print(cliente)
    print("--------------------------------------------------\n")


# Lista principal para almacenar clientes
clientes = []

# ==========================================
# 1. CREAR 
# ==========================================
print("=== 1. CREAR CLIENTES ===")
c1 = Cliente("1012345678", "Carlos Gómez", "3205554433", "Corte Fade")
c2 = ClienteVIP(
    "1023456789",
    "Juan Pérez",
    "3109876543",
    "Corte + Barba Premium",
    descuento=0.20,
)
c3 = Cliente("1034567890", "Andrés López", "3151112233", "Perfilado de Barba")

clientes.extend([c1, c2, c3])
print("Estado de la lista tras la CREACIÓN de 3 clientes:")
mostrar_lista_clientes(clientes)


# ==========================================
# 2. LEER 
# ==========================================
print("=== 2. LEER CLIENTES ===")
print("Consulta general de la lista de clientes activos:")
mostrar_lista_clientes(clientes)


# ==========================================
# 3. ACTUALIZAR 
# ==========================================
print("=== 3. ACTUALIZAR CLIENTE ===")
cedula_buscar = "1012345678"
print(f"Buscando cliente con cédula {cedula_buscar} para modificar datos...")

for cliente in clientes:
    if cliente.cedula == cedula_buscar:
        cliente.servicio_habitual = "Corte Fade + Diseño con navaja"
        cliente.telefono = "3209990000"
        print(f"Cliente '{cliente.nombre}' actualizado con éxito.")
        break

print("\nEstado de la lista tras la ACTUALIZACIÓN:")
mostrar_lista_clientes(clientes)


# ==========================================
# 4. BORRAR 
# ==========================================
print("=== 4. BORRAR CLIENTE ===")
cedula_eliminar = "1034567890"
print(f"Eliminando cliente con cédula {cedula_eliminar}...")

for cliente in clientes:
    if cliente.cedula == cedula_eliminar:
        clientes.remove(cliente)
        print("Cliente eliminado correctamente.")
        break

print("\nEstado de la lista tras la ELIMINACIÓN:")
mostrar_lista_clientes(clientes)


# ==========================================
# DEMOSTRACIÓN FINAL DE POLIMORFISMO
# ==========================================
print("=== DEMOSTRACIÓN DE POLIMORFISMO EN COBRO ===")
monto_servicio = 50000
for cliente in clientes:
    total = cliente.calcular_total(monto_servicio)
    print(f"{cliente.nombre} paga: ${total:.0f}")