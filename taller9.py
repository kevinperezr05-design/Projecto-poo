import sqlite3
import tkinter as tk
from tkinter import messagebox

DB_NAME = "barberia.db"


# ============================================================
#  CLASE CLIENTE Y PERSISTENCIA SQLITE 
# ============================================================
class Cliente:
    def __init__(self, nombre: str, telefono: str, cedula: str):
        self.nombre = nombre
        self.telefono = telefono
        self.cedula = cedula

    @staticmethod
    def crear_tabla():
        """Crea la tabla clientes si no existe en la BD."""
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

    def guardar(self):
        """Inserta un nuevo cliente en la base de datos."""
        with sqlite3.connect(DB_NAME) as conexion:
            cursor = conexion.cursor()
            cursor.execute(
                "INSERT INTO clientes (cedula, nombre, telefono) VALUES (?, ?, ?)",
                (self.cedula, self.nombre, self.telefono)
            )
            conexion.commit()

    @staticmethod
    def obtener_todos():
        """Recupera todos los registros almacenados en SQLite."""
        with sqlite3.connect(DB_NAME) as conexion:
            cursor = conexion.cursor()
            cursor.execute("SELECT cedula, nombre, telefono FROM clientes")
            registros = cursor.fetchall()
        return [Cliente(cedula=reg[0], nombre=reg[1], telefono=reg[2]) for reg in registros]

    def actualizar(self):
        """Actualiza los datos de un cliente según su cédula."""
        with sqlite3.connect(DB_NAME) as conexion:
            cursor = conexion.cursor()
            cursor.execute(
                "UPDATE clientes SET nombre = ?, telefono = ? WHERE cedula = ?",
                (self.nombre, self.telefono, self.cedula)
            )
            conexion.commit()

    @staticmethod
    def eliminar(cedula: str):
        """Elimina un cliente de la BD dada su cédula."""
        with sqlite3.connect(DB_NAME) as conexion:
            cursor = conexion.cursor()
            cursor.execute("DELETE FROM clientes WHERE cedula = ?", (cedula,))
            conexion.commit()


# ============================================================
# INTERFAZ GRÁFICA TKINTER (TALLER 9)
# ============================================================
class BarberiaGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Kevin's Barbería - Gestión de Clientes")
        self.root.geometry("520x500")
        self.root.resizable(False, False)

        # Inicializar la base de datos
        Cliente.crear_tabla()

        # ---------- SECCIÓN DE FORMULARIO (GRID) ----------
        frame_form = tk.LabelFrame(self.root, text=" Datos del Cliente ", padx=15, pady=15)
        frame_form.pack(fill="x", padx=15, pady=10)

        # Cajas de entrada ordenadas según el wireframe
        tk.Label(frame_form, text="Nombre:").grid(row=0, column=0, sticky="e", pady=5)
        self.txt_nombre = tk.Entry(frame_form, width=32)
        self.txt_nombre.grid(row=0, column=1, pady=5, padx=5)

        tk.Label(frame_form, text="Cédula:").grid(row=1, column=0, sticky="e", pady=5)
        self.txt_cedula = tk.Entry(frame_form, width=32)
        self.txt_cedula.grid(row=1, column=1, pady=5, padx=5)

        tk.Label(frame_form, text="Teléfono:").grid(row=2, column=0, sticky="e", pady=5)
        self.txt_telefono = tk.Entry(frame_form, width=32)
        self.txt_telefono.grid(row=2, column=1, pady=5, padx=5)

        # ---------- SECCIÓN DE BOTONES ----------
        frame_botones = tk.Frame(self.root)
        frame_botones.pack(fill="x", padx=15, pady=5)

        tk.Button(frame_botones, text="Guardar", bg="#4CAF50", fg="white", width=10, command=self.guardar_cliente).grid(row=0, column=0, padx=4)
        tk.Button(frame_botones, text="Actualizar", bg="#2196F3", fg="white", width=10, command=self.actualizar_cliente).grid(row=0, column=1, padx=4)
        tk.Button(frame_botones, text="Eliminar", bg="#f44336", fg="white", width=10, command=self.eliminar_cliente).grid(row=0, column=2, padx=4)
        tk.Button(frame_botones, text="Limpiar", bg="#9E9E9E", fg="white", width=10, command=self.limpiar_campos).grid(row=0, column=3, padx=4)

        # ---------- SECCIÓN LISTA (LISTBOX) ----------
        frame_lista = tk.LabelFrame(self.root, text=" Clientes Registrados ", padx=15, pady=10)
        frame_lista.pack(fill="both", expand=True, padx=15, pady=10)

        self.listbox = tk.Listbox(frame_lista, font=("Consolas", 10))
        self.listbox.pack(side="left", fill="both", expand=True)

        scrollbar = tk.Scrollbar(frame_lista, orient="vertical", command=self.listbox.yview)
        scrollbar.pack(side="right", fill="y")
        self.listbox.config(yscrollcommand=scrollbar.set)

        # Evento al seleccionar un ítem de la lista
        self.listbox.bind("<<ListboxSelect>>", self.seleccionar_cliente)

        # Cargar registros en pantalla al iniciar
        self.listar_clientes()

    # ---------- MÉTODOS DE CONTROL DE LA INTERFAZ ----------
    def limpiar_campos(self):
        """Limpia los inputs y habilita el campo cédula."""
        self.txt_cedula.config(state="normal")
        self.txt_nombre.delete(0, tk.END)
        self.txt_cedula.delete(0, tk.END)
        self.txt_telefono.delete(0, tk.END)

    def listar_clientes(self):
        """Vacia el Listbox y vuelve a cargar los clientes desde SQLite."""
        self.listbox.delete(0, tk.END)
        clientes = Cliente.obtener_todos()
        for cli in clientes:
            self.listbox.insert(tk.END, f"{cli.nombre} - CC {cli.cedula} - Tel {cli.telefono}")

    def guardar_cliente(self):
        """Obtiene datos de la UI y los inserta en la BD."""
        nombre = self.txt_nombre.get().strip()
        cedula = self.txt_cedula.get().strip()
        telefono = self.txt_telefono.get().strip()

        if not nombre or not cedula or not telefono:
            messagebox.showwarning("Atención", "Todos los campos son obligatorios.")
            return

        try:
            nuevo = Cliente(nombre, telefono, cedula)
            nuevo.guardar()
            messagebox.showinfo("Éxito", f"Cliente '{nombre}' guardado correctamente.")
            self.limpiar_campos()
            self.listar_clientes()
        except sqlite3.IntegrityError:
            messagebox.showerror("Error", f"La cédula '{cedula}' ya está registrada.")

    def seleccionar_cliente(self, event):
        """Al hacer clic en un cliente de la lista, auto-completa el formulario."""
        seleccion = self.listbox.curselection()
        if seleccion:
            item = self.listbox.get(seleccion[0])
            partes = item.split(" - ")
            nombre = partes[0]
            cedula = partes[1].replace("CC ", "")
            telefono = partes[2].replace("Tel ", "")

            self.limpiar_campos()
            self.txt_nombre.insert(0, nombre)
            self.txt_cedula.insert(0, cedula)
            self.txt_telefono.insert(0, telefono)
            
            # Bloquea el campo cédula durante la edición (Clave Primaria)
            self.txt_cedula.config(state="disabled")

    def actualizar_cliente(self):
        """Actualiza los datos del cliente seleccionado en la BD."""
        self.txt_cedula.config(state="normal")
        nombre = self.txt_nombre.get().strip()
        cedula = self.txt_cedula.get().strip()
        telefono = self.txt_telefono.get().strip()

        if not cedula or not nombre or not telefono:
            messagebox.showwarning("Atención", "Selecciona un cliente para actualizar.")
            return

        cliente = Cliente(nombre, telefono, cedula)
        cliente.actualizar()
        messagebox.showinfo("Éxito", "Datos del cliente actualizados correctamente.")
        self.limpiar_campos()
        self.listar_clientes()

    def eliminar_cliente(self):
        """Borra el cliente seleccionado previa confirmación."""
        self.txt_cedula.config(state="normal")
        cedula = self.txt_cedula.get().strip()

        if not cedula:
            messagebox.showwarning("Atención", "Selecciona un cliente de la lista para eliminar.")
            return

        confirmar = messagebox.askyesno("Confirmar", "¿Deseas eliminar este cliente de la base de datos?")
        if confirmar:
            Cliente.eliminar(cedula)
            messagebox.showinfo("Éxito", "Cliente eliminado correctamente.")
            self.limpiar_campos()
            self.listar_clientes()


# ============================================================
# EJECUCIÓN PRINCIPAL
# ============================================================
if __name__ == "__main__":
    root = tk.Tk()
    app = BarberiaGUI(root)
    root.mainloop()