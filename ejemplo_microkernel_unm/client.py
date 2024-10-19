# Microkernel
class Microkernel:
    def __init__(self):
        self.modules = {}
        # Servidores internos
        self.internal_register_server = ModuleRegisterServer(self.modules)
        self.internal_error_server = ErrorHandlingServer()

    # Adaptador que registra módulos en el servidor interno correspondiente
    def register_module(self, name, module):
        self.internal_register_server.register(name, module)

    # Adaptador que ejecuta los módulos a través del microkernel
    def execute_module(self, name, *args):
        if name in self.modules:
            # Adaptador que llama al servidor correspondiente (el módulo)
            result = self.modules[name].run(*args)
            print(f"Resultado de {name}: {result}")
        else:
            # Llama al servidor de errores si el módulo no existe
            self.internal_error_server.handle_error(name)


# Servidor interno para registrar módulos
class ModuleRegisterServer:
    def __init__(self, modules):
        self.modules = modules

    def register(self, name, module):
        self.modules[name] = module
        print(f"Módulo '{name}' registrado.")


# Servidor interno para manejar errores
class ErrorHandlingServer:
    def handle_error(self, module_name):
        print(f"Error: el módulo '{module_name}' no está registrado.")


# Interfaz para los módulos (servidores externos)
class Module:
    def run(self, *args):
        raise NotImplementedError("Este método debe ser implementado por subclases.")


# Módulos (Servidores Externos)
class AdditionModule(Module):
    def run(self, a, b):
        return a + b


class SubtractionModule(Module):
    def run(self, a, b):
        return a - b


# Agregar un servidor externo para que se comunique con el microkernel
# Nunca tocamos directamente el microkernel, solamente tenemos que registrarlo y ya podemos usarlo
# class MultiplicationModule(Module):
#     def run(self, a, b):
#         return a * b


# Clase principal (Cliente)
if __name__ == "__main__":
    # Inicialización del Microkernel
    kernel = Microkernel()

    # Registro de módulos (a través del adaptador)
    kernel.register_module("suma", AdditionModule())
    kernel.register_module("resta", SubtractionModule())

    # Ejecución de los módulos registrados
    kernel.execute_module("suma", 10, 5)  # Resultado: 15
    kernel.execute_module("resta", 10, 5)  # Resultado: 5

    # Intento de ejecutar un módulo no registrado
    kernel.execute_module(
        "multiplicacion", 10, 5
    )  # Error: el módulo no está registrado

    # kernel.register_module("multiplicacion", MultiplicationModule())
    # kernel.execute_module("multiplicacion", 100, 7)  # Resultado: 700
