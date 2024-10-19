from kernel.module_interface import ModuleInterface

class AdditionModule(ModuleInterface):
    def run(self, a, b):
        return a + b
