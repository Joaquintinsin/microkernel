from kernel.internal.module_register_server import ModuleRegisterServer
from kernel.internal.error_handling_server import ErrorHandlingServer
from kernel.module_interface import ModuleInterface

class Microkernel:
    def __init__(self):
        self.modules = {}
        self.internal_register_server = ModuleRegisterServer(self.modules)
        self.internal_error_server = ErrorHandlingServer()

    def register_module(self, name, module: ModuleInterface):
        self.internal_register_server.register(name, module)

    def execute_module(self, name, *args):
        if name in self.modules:
            result = self.modules[name].run(*args)
            print(f"Resultado de {name}: {result}")
        else:
            self.internal_error_server.handle_error(name)
