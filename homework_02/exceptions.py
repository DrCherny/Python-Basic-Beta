"""
Объявите следующие исключения:
- LowFuelError
- NotEnoughFuel
- CargoOverload
"""
class LowFuelError(Exception):
    pass
    # print("Ошибка топливного насоса")

class NotEnoughFuel(Exception):
    pass
    # print("Топлива не достаточно")

class CargoOverload(Exception):
    pass
    # print("Машина перегружена")
