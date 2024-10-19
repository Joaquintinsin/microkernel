class ModuleRegisterServer:
    def __init__(self, modules):
        self.modules = modules

    def register(self, name, module):
        self.modules[name] = module
        print(f"Módulo '{name}' registrado.")
