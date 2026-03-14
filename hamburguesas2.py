# --- Constantes del negocio ---
PRECIO_VENTA = 1150
COSTO_VARIABLE = 950
COSTO_FIJO = 8000

def calcular_reporte():
    print("--- ENTRADA DE DATOS SEMANALES ---")
    ventas = []
    
    # Captura de datos
    for i in range(1, 5):
        while True:
            try:
                unidad = int(input(f"Ingrese unidades vendidas en la Semana {i}: "))
                ventas.append(unidad)
                break
            except ValueError:
                print("Error: Por favor, ingrese un número entero válido.")

    print("\n" + "="*70)
    print(f"{'REPORTE FINANCIERO MENSUAL':^60}")
    print("="*70)
    
    # Encabezados de la tabla
    print(f"{'Semana':<12} | {'Unidades':<10} | {'Ingresos':<12} | {'Costos':<12} | {'Resultado'}")
    print("-" * 70)

    total_unidades = 0
    
    # Procesamiento y salida de datos
    for i, unidad in enumerate(ventas):
        ingreso = unidad * PRECIO_VENTA
        costo = (unidad * COSTO_VARIABLE) + COSTO_FIJO
        balance = ingreso - costo
        
        if balance > 0:
            estado = "Ganancia"
        elif balance < 0:
            estado = "Pérdida"
        else:
            estado = "Equilibrio"

        print(f"Semana {i+1:<5} | {unidad:<10} | ${ingreso:<11} | ${costo:<11} | {estado}")
        
        total_unidades += unidad

    # Resumen final
    promedio = total_unidades / 4
    print("-" * 60)
    print(f"Promedio Mensual: {promedio:.2f} unidades.")
    print("="*60)

if __name__ == "__main__":
    calcular_reporte()