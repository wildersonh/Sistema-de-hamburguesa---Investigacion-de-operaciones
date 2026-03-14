import tkinter as tk
from tkinter import ttk, messagebox
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

# --- Constantes del negocio ---
PRECIO_VENTA = 1150
COSTO_VARIABLE = 950
COSTO_FIJO = 8000

class Aplicacion(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Sistema de Ventas y Reportes")
        self.geometry("650x700")
        self.resizable(False, False)

        # Contenedor central
        self.container = tk.Frame(self)
        self.container.pack(side="top", fill="both", expand=True)
        
        # Datos compartidos entre pantallas
        self.datos_reporte = [] 

        self.frames = {}
        for F in (PantallaGrafica, PantallaReporte):
            frame = F(self.container, self)
            self.frames[F] = frame
            frame.grid(row=0, column=0, sticky="nsew")

        self.mostrar_pantalla(PantallaGrafica)

    def mostrar_pantalla(self, pantalla):
        frame = self.frames[pantalla]
        # Si vamos a la pantalla de reporte, refrescamos su tabla
        if pantalla == PantallaReporte:
            frame.actualizar_tabla_reporte(self.datos_reporte)
        frame.tkraise()

class PantallaGrafica(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller
        
        tk.Label(self, text="ENTRADA DE DATOS SEMANALES", font=("Arial", 12, "bold")).pack(pady=10)

        # Entradas de datos
        entrada_frame = tk.Frame(self)
        entrada_frame.pack(pady=5)
        self.inputs = []
        for i in range(1, 5):
            f = tk.Frame(entrada_frame)
            f.pack(side="left", padx=10)
            tk.Label(f, text=f"Sem {i}").pack()
            ent = tk.Entry(f, width=7, justify="center")
            ent.insert(0, "0")
            ent.pack()
            self.inputs.append(ent)

        tk.Button(self, text="CALCULAR Y GRAFICAR", bg="#2196F3", fg="white", font=("Arial", 10, "bold"),
                  command=self.procesar_datos).pack(pady=15)

        # Canvas de Matplotlib
        self.fig, self.ax = plt.subplots(figsize=(5, 3), dpi=100)
        self.canvas = FigureCanvasTkAgg(self.fig, master=self)
        self.canvas.get_tk_widget().pack(fill="both", expand=True, padx=20)

        tk.Button(self, text="VER REPORTE DETALLADO →", bg="#607D8B", fg="white",
                  command=lambda: controller.mostrar_pantalla(PantallaReporte)).pack(pady=20)

    def procesar_datos(self):
        try:
            ventas = [int(e.get()) for e in self.inputs]
            self.controller.datos_reporte = [] # Limpiar reporte anterior
            
            # Generar datos para el reporte
            for i, unidad in enumerate(ventas):
                ingreso = unidad * PRECIO_VENTA
                costo = (unidad * COSTO_VARIABLE) + COSTO_FIJO
                balance = ingreso - costo
                estado = "Ganancia" if balance > 0 else "Pérdida" if balance < 0 else "Equilibrio"
                
                self.controller.datos_reporte.append((f"Semana {i+1}", unidad, f"${ingreso}", f"${costo}", estado))

            # Actualizar Gráfica
            self.ax.clear()
            self.ax.plot(range(1, 5), ventas, marker='s', color='#2196F3', linewidth=2)
            self.ax.set_title("Tendencia de Unidades Vendidas")
            self.ax.set_xticks(range(1, 5))
            self.ax.grid(True, alpha=0.3)
            self.canvas.draw()
            
        except ValueError:
            messagebox.showerror("Error", "Ingresa números válidos en todas las semanas.")

class PantallaReporte(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller
        
        tk.Label(self, text="REPORTE FINANCIERO MENSUAL", font=("Arial", 14, "bold")).pack(pady=15)

        # Configuración de la Tabla (Treeview)
        columnas = ("Semana", "Unidades", "Ingresos", "Costos", "Resultado")
        self.tabla = ttk.Treeview(self, columns=columnas, show="headings", height=8)
        
        for col in columnas:
            self.tabla.heading(col, text=col)
            self.tabla.column(col, width=120, anchor="center")
        
        self.tabla.pack(pady=10, padx=20, fill="x")

        # Resumen final
        self.lbl_resumen = tk.Label(self, text="", font=("Arial", 11, "italic"))
        self.lbl_resumen.pack(pady=10)

        tk.Button(self, text="← VOLVER A INICIO", command=lambda: controller.mostrar_pantalla(PantallaGrafica)).pack(pady=20)

    def actualizar_tabla_reporte(self, datos):
        # Limpiar tabla
        for item in self.tabla.get_children():
            self.tabla.delete(item)
        
        if not datos:
            self.lbl_resumen.config(text="No hay datos para mostrar. Regresa y genera la gráfica.")
            return

        # Insertar datos
        total_unidades = 0
        for fila in datos:
            self.tabla.insert("", "end", values=fila)
            total_unidades += fila[1]
        
        promedio = total_unidades / 4
        if promedio < 40: 
            self.lbl_resumen.config(text=f"Promedio Mensual: {promedio} unidades. Perdidas")
        elif promedio == 40:
            self.lbl_resumen.config(text=f"Promedio Mensual: {promedio} unidades. Equilibrio")
        else: 
            self.lbl_resumen.config(text=f"Promedio Mensual: {promedio} unidades. Ganancia")
if __name__ == "__main__":
    app = Aplicacion()
    app.mainloop()