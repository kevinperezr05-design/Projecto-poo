class Cliente:

    # 1. ATRIBUTOS (Datos que guardamos del cliente)
    def __init__(self, nombre, telefono, preferencias):
        self.nombre = nombre
        self.telefono = telefono
        self.preferencias = preferencias
        self.tiene_cita = False

    # 2. MÉTODOS (Acciones que puede realizar)
    def reservar_cita(self):
        self.tiene_cita = True
        print(f"{self.nombre} reservó una cita.")

    def cancelar_cita(self):
        self.tiene_cita = False
        print(f"{self.nombre} canceló su cita.")

    def cambiar_preferencias(self, nueva_preferencia):
        self.preferencias = nueva_preferencia
        print(f"{self.nombre} actualizó su preferencia a: {self.preferencias}")


# --- PRUEBA DE EJECUCIÓN ---
obj = Cliente("Juan", "3001234567", "Corte degradado")

# Probamos los métodos
obj.reservar_cita()
obj.cambiar_preferencias("Corte con diseño y barba")
obj.cancelar_cita()

# Imprimimos un atributo para verificar
print("Cliente registrado:", obj.nombre)



class Barbero:

    # 1. ATRIBUTOS
    def __init__(self, nombre, especialidad, comision):
        self.nombre = nombre
        self.especialidad = especialidad
        self.comision = comision
        self.disponible = True

    # 2. MÉTODOS
    def cambiar_especialidad(self, nueva_especialidad):
        self.especialidad = nueva_especialidad
        print(f"{self.nombre} ahora se especializa en: {self.especialidad}")

    def actualizar_comision(self, nueva_comision):
        self.comision = nueva_comision
        print(f"La nueva comisión de {self.nombre} es: {self.comision}%")

    def atender_cliente(self):
        self.disponible = False
        print(f"{self.nombre} está atendiendo a un cliente.")


# Ejemplo de uso
obj_barbero = Barbero("Kevin", "Corte clásico", 15)

# Ejecución de métodos
obj_barbero.cambiar_especialidad("Degradados y Barba")
obj_barbero.actualizar_comision(20)
obj_barbero.atender_cliente()

print("Barbero:", obj_barbero.nombre)
