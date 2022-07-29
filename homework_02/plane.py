"""
создайте класс `Plane`, наследник `Vehicle`
"""
from homework_02.base import Vehicle
from homework_02.exceptions import CargoOverload

class Plane(Vehicle):
    # cargo: int = 0
    # max_cargo: int = 0

    def __init__(self, weight, fuel, fuel_consumption, max_cargo):
        super().__init__(weight,fuel,fuel_consumption)
        self.max_cargo = max_cargo
        self.cargo = 0

    def load_cargo(self, load):
        if load + self.cargo <= self.max_cargo:
            self.cargo += load
            return f'Общий загруженный вес {self.cargo}.'
        else:
            raise CargoOverload()

    def remove_all_cargo(self):
        cc = self.cargo
        self.cargo = 0
        return cc