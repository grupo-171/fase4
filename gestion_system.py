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