# ==========================================
# CLASE BASE
# ==========================================
class Persona:

    def __init__(self, nombre, telefono):
        self.nombre = nombre
        self.telefono = telefono

    def mostrar_contacto(self):
        return f"Nombre: {self.nombre} | Teléfono: {self.telefono}"


# ==========================================
# SUBCLASES
# ==========================================
class Cliente(Persona):

    def __init__(self, nombre, telefono, tipo_corte_favorito):
        super().__init__(nombre, telefono)
        self.tipo_corte_favorito = tipo_corte_favorito

    def agendar_cita(self, fecha, hora):
        return f"Cita agendada para {self.nombre} el {fecha} a las {hora}."


class Barbero(Persona):

    def __init__(self, nombre, telefono, especialidad):
        super().__init__(nombre, telefono)
        self.especialidad = especialidad

    def realizar_servicio(self, servicio):
        return f"El barbero {self.nombre} está realizando el servicio: {servicio}."


# ==========================================
# OBJETOS E IMPRESIÓN 
# ==========================================
cliente1 = Cliente("Carlos Gómez", "3205554433", "Corte con diseño y barba")
barbero1 = Barbero("Mateo Ríos", "3119876543", "Degradados y perfilado de barba")

print("--- DATOS HEREDADOS ---")
print(cliente1.mostrar_contacto())
print(barbero1.mostrar_contacto())

print("\n--- MÉTODOS Y ATRIBUTOS PROPIOS ---")
print(f"Preferencia: {cliente1.tipo_corte_favorito}")
print(cliente1.agendar_cita("15 de Octubre", "4:00 PM"))

print(f"Especialidad: {barbero1.especialidad}")
print(barbero1.realizar_servicio("Corte Fade + Barbería Premium"))