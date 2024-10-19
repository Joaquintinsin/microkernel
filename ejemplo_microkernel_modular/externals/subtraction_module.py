from kernel.module_interface import ModuleInterface

class SubtractionModule(ModuleInterface):
    def run(self, a, b):
        return a - b
