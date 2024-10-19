from kernel.microkernel import Microkernel
from externals.addition_module import AdditionModule
from externals.subtraction_module import SubtractionModule

if __name__ == "__main__":
    kernel = Microkernel()

    # Registro de módulos
    kernel.register_module("suma", AdditionModule())
    kernel.register_module("resta", SubtractionModule())

    # Ejecución de módulos
    kernel.execute_module("suma", 10, 5)   # Resultado: 15
    kernel.execute_module("resta", 10, 5)  # Resultado: 5

    # Intento de ejecutar un módulo no registrado
    kernel.execute_module("multiplicacion", 10, 5)  # Error: el módulo no está registrado
