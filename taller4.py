
# Definición de la clase base
class Cliente:
    def __init__(self, id_cliente, nombre, servicio, precio):
        self.id_cliente = id_cliente
        self.nombre = nombre
        self.servicio = servicio
        self.precio = precio

    def __str__(self):
        return f"ID: {self.id_cliente} | Nombre: {self.nombre} | Servicio: {self.servicio} | Precio: ${self.precio}"


# Lista principal para almacenar los objetos
clientes = []

# ==========================================
# 1. CREAR (Create): 
# ==========================================
print("--- 1. CREAR ---")
cliente1 = Cliente(1, "Carlos Gómez", "Corte de cabello", 25000)
cliente2 = Cliente(2, "María Rodríguez", "Tintura de cabello", 80000)
cliente3 = Cliente(3, "Andrés Pérez", "Arreglo de barba", 20000)

clientes.append(cliente1)
clientes.append(cliente2)
clientes.append(cliente3)
print("Se han agregado 3 clientes exitosamente.\n")


# ==========================================
# 2. LEER (Read): Muéstralos con un for
# ==========================================
print("--- 2. LEER ---")
print("Lista de clientes registrados:")
for cliente in clientes:
    print(cliente)
print()


# ==========================================
# 3. ACTUALIZAR (Update): Busca uno y actualiza
# ==========================================
print("--- 3. ACTUALIZAR ---")
id_buscar = 2
for cliente in clientes:
    if cliente.id_cliente == id_buscar:
        print(f"Cliente encontrado: {cliente.nombre}")
        cliente.servicio = "Tintura + Cepillado"
        cliente.precio = 95000
        print(f"Datos actualizados: {cliente}\n")
        break


# ==========================================
# 4. BORRAR (Delete): Elimina uno de la lista
# ==========================================
print("--- 4. BORRAR ---")
id_eliminar = 1
for cliente in clientes:
    if cliente.id_cliente == id_eliminar:
        clientes.remove(cliente)
        print(f"Cliente con ID {id_eliminar} eliminado correctamente.\n")
        break


# ==========================================
# VERIFICACIÓN FINAL
# ==========================================
print("--- LISTA FINAL DE CLIENTES ---")
for cliente in clientes:
    print(cliente)