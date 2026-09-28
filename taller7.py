# ==========================================
# CLASES BASE Y HERENCIA
# ==========================================

class Usuario:
    def __init__(self, nombre: str, email: str):
        self.nombre = nombre
        self.email = email

    def descripcion(self):
        return f"Usuario: {self.nombre} ({self.email})"


class Administrador(Usuario):
    def __init__(self, nombre: str, email: str, nivel_acceso: int):
        super().__init__(nombre, email)
        self.nivel_acceso = nivel_acceso


class Barbero(Usuario):
    def __init__(self, nombre: str, email: str, meta_cortes: int):
        super().__init__(nombre, email)
        self.meta_cortes = meta_cortes


class Cliente:
    def __init__(self, nombre: str, telefono: str, cedula: str):
        self.nombre = nombre
        self.telefono = telefono
        self.cedula = cedula

    def calcular_total(self, monto_base: float) -> float:
        return monto_base


class ClienteVIP(Cliente):
    def __init__(self, nombre: str, telefono: str, cedula: str, descuento: float):
        super().__init__(nombre, telefono, cedula)
        self.descuento = descuento

    def calcular_total(self, monto_base: float) -> float:
        return monto_base * (1 - self.descuento)


# ==========================================
# AGREGACION Y COMPOSICION
# ==========================================

class Servicio:
    def __init__(self, nombre: str, precio: float):
        self.nombre = nombre
        self.precio = precio


class Factura:
    def __init__(self, numero_factura: int, total: float):
        self.numero_factura = numero_factura
        self.total = total

    def imprimir(self):
        print(f"Factura #{self.numero_factura} | Total a pagar: ${self.total:,.0f} COP")


class CitaBarberia:
    def __init__(self, numero_cita: int, cliente: Cliente, barbero: Barbero):
        self.numero_cita = numero_cita
        self.cliente = cliente
        self.barbero = barbero
        self.servicios = []  # Agregacion: Lista de objetos Servicio
        self.factura = None  # Composicion: La factura nace con la cita

    def agregar_servicio(self, servicio: Servicio):
        self.servicios.append(servicio)

    def cerrar_cita(self):
        monto_base = sum(s.precio for s in self.servicios)
        total_final = self.cliente.calcular_total(monto_base)
        self.factura = Factura(numero_factura=self.numero_cita + 1000, total=total_final)
        return self.factura


# ==========================================
# PRUEBA DE EJECUCION (SALIDA EN CONSOLA)
# ==========================================
if __name__ == "__main__":
    print("========================================")
    print("    KEVIN'S BARBERIA -      ")
    print("========================================\n")

    # 1. Creamos el cliente VIP y el Barbero
    cliente = ClienteVIP("Carlos Gomez", "3001234567", "1018222333", descuento=0.10)
    barbero = Barbero("Kevin Perez", "kevin@barberia.com", meta_cortes=20)

    # 2. Creamos la cita
    cita = CitaBarberia(numero_cita=1, cliente=cliente, barbero=barbero)

    # 3. Agregamos servicios (Agregacion)
    corte = Servicio("Corte de Cabello Tradicional", 25000)
    barba = Servicio("Perfilado de Barba", 15000)
    cita.agregar_servicio(corte)
    cita.agregar_servicio(barba)

    # 4. Cerramos cita e imprimimos comprobante
    factura = cita.cerrar_cita()

    print(f"Cliente: {cliente.nombre} (Descuento VIP: {int(cliente.descuento * 100)}%)")
    print(f"Atendido por: {barbero.nombre}")
    print("Servicios consumidos:")
    for s in cita.servicios:
        print(f"  - {s.nombre}: ${s.precio:,.0f} COP")
    print("----------------------------------------")
    factura.imprimir()
    print("========================================")