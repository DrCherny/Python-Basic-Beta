from abc import ABC
from homework_02.exceptions import LowFuelError, NotEnoughFuel

class Vehicle(ABC):

    def __init__(self, weight: int = 500, fuel: int = 50, fuel_consumption: int = 5):
        self.weight = weight
        self.fuel = fuel
        self.fuel_consumption = fuel_consumption
        self.started = False

    def start(self):
    ## проверка топлива
        if self.fuel > 0:
            self.started = True
        elif self.fuel <= 0:
            raise LowFuelError()

    def move(self, km: int):
        self.distance = km
        consumption = self.distance * self.fuel_consumption
        if self.fuel >= consumption:
            self.fuel = self.fuel - consumption
            return self.fuel
        else:
            raise NotEnoughFuel()