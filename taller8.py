import sqlite3

DB_NAME = "barberia.db"


class Cliente:
    def __init__(self, nombre: str, telefono: str, cedula: str):
        self.nombre = nombre
        self.telefono = telefono
        self.cedula = cedula

    # ============================================================
    # 0. INICIALIZACIÓN DE LA BASE DE DATOS
    # ============================================================
    @staticmethod
    def crear_tabla():
        """Crea la tabla clientes si no existe."""
        with sqlite3.connect(DB_NAME) as conexion:
            cursor = conexion.cursor()
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS clientes (
                    cedula TEXT PRIMARY KEY,
                    nombre TEXT NOT NULL,
                    telefono TEXT NOT NULL
                )
            """)
            conexion.commit()
        print("[BD] Tabla 'clientes' verificada / creada exitosamente.")

    # ============================================================
    # 1. CREAR (INSERTAR CLIENTE)
    # ============================================================
    def guardar(self):
        """Inserta el cliente actual en la base de datos."""
        try:
            with sqlite3.connect(DB_NAME) as conexion:
                cursor = conexion.cursor()
                cursor.execute(
                    "INSERT INTO clientes (cedula, nombre, telefono) VALUES (?, ?, ?)",
                    (self.cedula, self.nombre, self.telefono)
                )
                conexion.commit()
            print(f"[INSERT] Cliente '{self.nombre}' guardado con exito.")
        except sqlite3.IntegrityError:
            print(f"[INFO] La cedula '{self.cedula}' ya existe en la base de datos.")

    # ============================================================
    # 2. LEER (LISTAR TODOS Y BUSCAR POR CÉDULA)
    # ============================================================
    @staticmethod
    def obtener_todos():
        """Retorna todos los clientes registrados."""
        with sqlite3.connect(DB_NAME) as conexion:
            cursor = conexion.cursor()
            cursor.execute("SELECT cedula, nombre, telefono FROM clientes")
            registros = cursor.fetchall()

        clientes = []
        for reg in registros:
            clientes.append(Cliente(cedula=reg[0], nombre=reg[1], telefono=reg[2]))
        return clientes

    @staticmethod
    def buscar_por_cedula(cedula: str):
        """Busca un cliente especifico por su cedula."""
        with sqlite3.connect(DB_NAME) as conexion:
            cursor = conexion.cursor()
            cursor.execute("SELECT cedula, nombre, telefono FROM clientes WHERE cedula = ?", (cedula,))
            reg = cursor.fetchone()

        if reg:
            return Cliente(cedula=reg[0], nombre=reg[1], telefono=reg[2])
        return None

    # ============================================================
    # 3. ACTUALIZAR
    # ============================================================
    def actualizar(self):
        """Actualiza el nombre y telefono del cliente."""
        with sqlite3.connect(DB_NAME) as conexion:
            cursor = conexion.cursor()
            cursor.execute(
                "UPDATE clientes SET nombre = ?, telefono = ? WHERE cedula = ?",
                (self.nombre, self.telefono, self.cedula)
            )
            conexion.commit()
        print(f"[UPDATE] Cliente con cedula '{self.cedula}' actualizado correctamente.")

    # ============================================================
    # 4. ELIMINAR
    # ============================================================
    @staticmethod
    def eliminar(cedula: str):
        """Elimina un cliente de la BD usando su cedula."""
        with sqlite3.connect(DB_NAME) as conexion:
            cursor = conexion.cursor()
            cursor.execute("DELETE FROM clientes WHERE cedula = ?", (cedula,))
            conexion.commit()
        print(f"[DELETE] Cliente con cedula '{cedula}' eliminado de la base de datos.")


# ============================================================
# PRUEBA Y VERIFICACIÓN COMPLETA DEL CRUD
# ============================================================
if __name__ == "__main__":
    print("==================================================")
    print("   KEVIN'S BARBERIA - TALLER 8 (SQLITE CRUD)      ")
    print("==================================================\n")

    # Step 0: Crear la tabla
    Cliente.crear_tabla()

    # Step 1: INSERTAR CLIENTES (CREATE)
    print("\n--- 1. INSERTANDO CLIENTES ---")
    c1 = Cliente("Andres Felipe Silva", "3158889900", "1014235890")
    c2 = Cliente("Santiago Ospina", "3124567890", "1022458963")
    c3 = Cliente("Mateo Bermudez", "3017654321", "1033652147")
    
    c1.guardar()
    c2.guardar()
    c3.guardar()

    # Step 2: LISTAR CLIENTES (READ)
    print("\n--- 2. LISTANDO CLIENTES REGISTRADOS ---")
    lista = Cliente.obtener_todos()
    for cli in lista:
        print(f"-> Cedula: {cli.cedula} | Nombre: {cli.nombre} | Tel: {cli.telefono}")

    # Step 3: ACTUALIZAR CLIENTE (UPDATE)
    print("\n--- 3. ACTUALIZANDO DATOS DE UN CLIENTE ---")
    c1.nombre = "Andres Felipe Silva Gomez"
    c1.telefono = "3159990011"
    c1.actualizar()

    # Verificamos la actualizacion buscando por cedula
    cli_actualizado = Cliente.buscar_por_cedula("1014235890")
    if cli_actualizado:
        print(f" Verificacion Update: {cli_actualizado.nombre} - Tel: {cli_actualizado.telefono}")

    # Step 4: ELIMINAR CLIENTE (DELETE)
    print("\n--- 4. ELIMINANDO UN CLIENTE ---")
    Cliente.eliminar("1022458963")

    # Lista final para verificar
    print("\n--- LISTA FINAL EN BASE DE DATOS ---")
    lista_final = Cliente.obtener_todos()
    for cli in lista_final:
        print(f"-> Cedula: {cli.cedula} | Nombre: {cli.nombre} | Tel: {cli.telefono}")

    print("\n==================================================")