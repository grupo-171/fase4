from abc import ABC, abstractmethod
import logging

# CONFIGURACIÓN DE LOGS
logging.basicConfig(
    filename="sistema.log",
    level=logging.ERROR,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

# =========================
# EXCEPCIONES PERSONALIZADAS
# =========================
class SistemaError(Exception):
    pass

class ValidacionError(SistemaError):
    pass

class ReservaError(SistemaError):
    pass


# =========================
# CLASE ABSTRACTA BASE
# =========================
class Entidad(ABC):
    @abstractmethod
    def mostrar_info(self):
        pass


# =========================
# CLIENTE
# =========================
class Cliente(Entidad):
    def __init__(self, nombre, edad, email):
        try:
            if not nombre or not isinstance(nombre, str):
                raise ValidacionError("Nombre inválido")
            if edad < 18:
                raise ValidacionError("El cliente debe ser mayor de edad")
            if "@" not in email:
                raise ValidacionError("Email inválido")

            self.__nombre = nombre
            self.__edad = edad
            self.__email = email

        except Exception as e:
            logging.error(e)
            raise

    def mostrar_info(self):
        return f"Cliente: {self.__nombre}, Edad: {self.__edad}, Email: {self.__email}"


# =========================
# SERVICIO ABSTRACTO
# =========================
class Servicio(ABC):
    def __init__(self, nombre, precio_base):
        self.nombre = nombre
        self.precio_base = precio_base

    @abstractmethod
    def calcular_costo(self, *args):
        pass

    @abstractmethod
    def descripcion(self):
        pass


# =========================
# SERVICIOS DERIVADOS
# =========================
class ServicioHotel(Servicio):
    def calcular_costo(self, dias=1, impuesto=0):
        return (self.precio_base * dias) * (1 + impuesto)

    def descripcion(self):
        return "Servicio de hospedaje"


class ServicioTransporte(Servicio):
    def calcular_costo(self, distancia=1):
        return self.precio_base * distancia

    def descripcion(self):
        return "Servicio de transporte"


class ServicioTour(Servicio):
    def calcular_costo(self, personas=1, descuento=0):
        total = self.precio_base * personas
        return total - (total * descuento)

    def descripcion(self):
        return "Servicio turístico"
    # =========================
# RESERVA
# =========================
class Reserva:
    def __init__(self, cliente, servicio, duracion):
        try:
            if not isinstance(cliente, Cliente):
                raise ReservaError("Cliente inválido")
            if not isinstance(servicio, Servicio):
                raise ReservaError("Servicio inválido")
            if duracion <= 0:
                raise ReservaError("Duración inválida")
 
            self.cliente = cliente
            self.servicio = servicio
            self.duracion = duracion
            self.estado = "pendiente"
 
        except Exception as e:
            logging.error(e)
            raise
 
    def confirmar(self):
        try:
            if self.estado != "pendiente":
                raise ReservaError("Reserva ya procesada")
            self.estado = "confirmada"
            print("Reserva confirmada")
 
        except Exception as e:
            logging.error(e)
            print("Error al confirmar:", e)
 
    def cancelar(self):
        try:
            if self.estado == "cancelada":
                raise ReservaError("Ya está cancelada")
            self.estado = "cancelada"
            print("Reserva cancelada")
 
        except Exception as e:
            logging.error(e)
            print("Error al cancelar:", e)
 
    def procesar_pago(self):
        try:
            costo = self.servicio.calcular_costo(self.duracion)
        except TypeError:
            try:
                costo = self.servicio.calcular_costo()
            except Exception as e:
                logging.error(e)
                raise ReservaError("Error en cálculo") from e
        else:
            print(f"Costo calculado: {costo}")
        finally:
            print("Proceso de pago finalizado")
 
 
# =========================
# SIMULACIÓN (10 OPERACIONES)
# =========================
clientes = []
servicios = []
reservas = []
 
def ejecutar_sistema():
    operaciones = [
        lambda: clientes.append(Cliente("Ana", 25, "ana@mail.com")),
        lambda: clientes.append(Cliente("", 20, "mal")),  # ERROR
        lambda: servicios.append(ServicioHotel("Hotel", 100)),
        lambda: servicios.append(ServicioTransporte("Bus", 5)),
        lambda: servicios.append(ServicioTour("Tour", 50)),
        lambda: reservas.append(Reserva(clientes[0], servicios[0], 3)),
        lambda: reservas.append(Reserva("fake", servicios[0], 2)),  # ERROR
        lambda: reservas[0].confirmar(),
        lambda: reservas[0].procesar_pago(),
        lambda: reservas[0].cancelar()
    ]
 
    for i, op in enumerate(operaciones):
        try:
            print(f"\nOperación {i+1}")
            op()
        except Exception as e:
            print("Error controlado:", e)
 
 
# EJECUCIÓN
if __name__ == "__main__":
    ejecutar_sistema()