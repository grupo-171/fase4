# hola mundo 
# esta es una prueba que estamos conectados al repositorio para empezar a trabajar 
"""_summary_
crearemos la clase 

"""
class Finanzas:
    """
    Clase para gestionar ingresos, gastos y saldo del sistema.
    """
 
    def __init__(self):
        self.ingresos = []
        self.gastos = []
 
    def agregar_ingreso(self, descripcion, valor):
        if valor <= 0:
            print("El ingreso debe ser mayor que cero.")
            return
 
        ingreso = {
            "descripcion": descripcion,
            "valor": valor
        }
 
        self.ingresos.append(ingreso)
        print("Ingreso agregado correctamente.")
 
    def agregar_gasto(self, descripcion, valor):
        if valor <= 0:
            print("El gasto debe ser mayor que cero.")
            return
 
        gasto = {
            "descripcion": descripcion,
            "valor": valor
        }
 
        self.gastos.append(gasto)
        print("Gasto agregado correctamente.")
 
    def calcular_total_ingresos(self):
        total = 0
        for ingreso in self.ingresos:
            total += ingreso["valor"]
        return total
 
    def calcular_total_gastos(self):
        total = 0
        for gasto in self.gastos:
            total += gasto["valor"]
        return total
 
    def calcular_saldo(self):
        return self.calcular_total_ingresos() - self.calcular_total_gastos()
 
    def mostrar_reporte(self):
        print("====== REPORTE FINANCIERO ======")
 
        print("\nIngresos:")
        if len(self.ingresos) == 0:
            print("No hay ingresos registrados.")
        else:
            for ingreso in self.ingresos:
                print(f"- {ingreso['descripcion']}: ${ingreso['valor']}")
 
        print("\nGastos:")
        if len(self.gastos) == 0:
            print("No hay gastos registrados.")
        else:
            for gasto in self.gastos:
                print(f"- {gasto['descripcion']}: ${gasto['valor']}")
 
        print("\nResumen:")
        print(f"Total ingresos: ${self.calcular_total_ingresos()}")
        print(f"Total gastos: ${self.calcular_total_gastos()}")
        print(f"Saldo actual: ${self.calcular_saldo()}")
