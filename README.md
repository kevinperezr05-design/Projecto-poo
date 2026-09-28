# Kevin's Barbería - Sistema de Gestión POO

## Descripción del Negocio
La microempresa elegida es una Barbería denominada **Kevin's Barbería**. Es una barbería urbana y moderna enfocada en brindar una experiencia de estilizado masculino de alta calidad, especializada en cortes de cabello de tendencia, degradados, diseño y arreglo de barba, y tratamientos capilares.

---

##  Problema que Resuelve
Actualmente, el establecimiento maneja sus registros de clientes, agenda de citas y asignación de servicios de manera manual o desorganizada. Esto genera descontrol en la disponibilidad de agenda, duplicidad de datos, pérdidas de información de clientes frecuentes y falta de trazabilidad en los servicios agendados. 

Este sistema automatiza la gestión operativa de la barbería mediante una interfaz gráfica interactiva en Python (Tkinter) y persistencia de datos relacional (SQLite), permitiendo un control estructurado, rápido y sin errores.

---

## Módulos del Sistema (2 CRUDs)

### 1. CRUD de Clientes
Permite administrar el registro de los clientes de la barbería con persistencia en la base de datos `barberia.db`:
* **Create (Crear):** Registrar nuevos clientes con Cédula, Nombre y Teléfono.
* **Read (Leer):** Visualizar el listado actualizado de clientes en tiempo real dentro del `Listbox`.
* **Update (Actualizar):** Seleccionar un cliente de la lista y modificar su nombre o número telefónico.
* **Delete (Eliminar):** Borrar registros de clientes existentes con confirmación de seguridad.

### 2. CRUD de Citas y Servicios (`CitaBarberia`)
Permite agendar y controlar la atención y servicios asignados a los clientes mediante relaciones de agregación:
* **Create (Crear):** Programar una nueva cita asociando el cliente con el servicio solicitado (ej. Corte, Barba), fecha y hora.
* **Read (Leer):** Consultar el historial de citas programadas y los detalles del servicio asignado.
* **Update (Actualizar):** Reprogramar la fecha/hora de la cita o cambiar el servicio asignado.
* **Delete (Eliminar):** Cancelar o remover citas del sistema.

---

## Ejecución del Proyecto
 Para iniciar la aplicación con interfaz gráfica y base de datos SQLite, ejecuta el siguiente comando en tu terminal:

```bash
python proyectopoo.py 


 

