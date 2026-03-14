Esta es la documentación técnica profesional para el proyecto, estructurada bajo estándares de la industria y optimizada para la legibilidad.

---

## 1. README.md

# Hamburguesas

**Hamburguesas** es una herramienta de automatización para el cálculo de estados financieros mensuales. Resuelve la necesidad de procesar ingresos, costos variables y fijos de forma rápida, transformando datos de ventas semanales en reportes de rentabilidad (Ganancia/Pérdida/Equilibrio) sin necesidad de hojas de cálculo complejas.

### Requisitos previos

* **Python:** 3.8 o superior.
* **Sistema Operativo:** Independiente (Windows, macOS, Linux).

### Instalación

```bash
# 1. Clonar el repositorio
git clone https://github.com/wildersonh/Sistema-de-hamburguesa---Investigacion-de-operaciones.git

# 2. Acceder al directorio
cd Sistema-de-hamburguesa---Investigacion-de-operaciones

```

### Ejemplo de uso rápido

Para iniciar la captura de datos y generación del reporte, ejecute el script principal:

```bash
python hamburguesas2.py

```

### Estructura del proyecto

```text
.
├── hamburguesas2.py              # Script principal y lógica de negocio
├── README.md            # Documentación general
└── .gitignore           # Archivos excluidos de Git

```

### Constantes de Configuración

Actualmente, el sistema utiliza constantes harcodeadas para la lógica de negocio. Estas deben modificarse directamente en `main.py` antes de la ejecución:

| Variable | Descripción | Ejemplo | Obligatorio |
| --- | --- | --- | --- |
| `PRECIO_VENTA` | Valor unitario de venta al público | `1150` | Sí |
| `COSTO_VARIABLE` | Costo de producción por unidad | `950` | Sí |
| `COSTO_FIJO` | Gastos operativos mensuales fijos | `8000` | Sí |

### Pruebas

Actualmente, las pruebas se realizan mediante validación manual de entradas. Se planea la implementación de `pytest` para la lógica de cálculo en la v1.1.0.

### Contribución

1. Haga un Fork del proyecto.
2. Cree una rama para su mejora (`git checkout -b feature/MejoraLogica`).
3. Realice un Commit de sus cambios (`git commit -m 'Add: nueva funcionalidad'`).
4. Haga un Push a la rama (`git push origin feature/MejoraLogica`).
5. Abra un Pull Request.

---

## 2. Documentación Inline

A continuación se presenta el código con la implementación de **Docstrings** bajo el estándar de Google, incluyendo manejo de excepciones y ejemplos de uso.

```python
# --- Constantes del negocio ---
PRECIO_VENTA = 1150
COSTO_VARIABLE = 950
COSTO_FIJO = 8000

def calcular_reporte():
    """
    Ejecuta el flujo completo de captura, procesamiento y visualización del reporte financiero.

    La función solicita por consola las unidades vendidas durante 4 semanas,
    valida que los datos sean enteros y calcula el balance financiero basado en 
    las constantes PRECIO_VENTA, COSTO_VARIABLE y COSTO_FIJO.

    Args:
        None

    Returns:
        None: Imprime el reporte directamente en la salida estándar (stdout).

    Raises:
        ValueError: Si el usuario ingresa caracteres no numéricos durante la captura.
        ZeroDivisionError: Si se modifica la lógica de semanas y el divisor resulta en cero.

    Example:
        >>> # Al ejecutar, el sistema pedirá entradas:
        >>> # Ingrese unidades vendidas en la Semana 1: 50
        >>> # ... (repite para 4 semanas)
        >>> calcular_reporte()
        REPORTE FINANCIERO MENSUAL
        Semana 1 | 50 | $57500 | $55500 | Ganancia
    """
    print("--- ENTRADA DE DATOS SEMANALES ---")
    ventas = []
    
    # Captura de datos con validación de tipo
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
        # Lógica de negocio: Ingresos vs Egresos
        ingreso = unidad * PRECIO_VENTA
        costo = (unidad * COSTO_VARIABLE) + COSTO_FIJO
        balance = ingreso - costo
        
        # Evaluación de estado financiero
        if balance > 0:
            estado = "Ganancia"
        elif balance < 0:
            estado = "Pérdida"
        else:
            estado = "Equilibrio"

        print(f"Semana {i+1:<5} | {unidad:<10} | ${ingreso:<11} | ${costo:<11} | {estado}")
        
        total_unidades += unidad

    # Resumen final de métricas
    promedio = total_unidades / 4
    print("-" * 60)
    print(f"Promedio Mensual: {promedio:.2f} unidades.")
    print("="*60)

if __name__ == "__main__":
    calcular_reporte()

```
