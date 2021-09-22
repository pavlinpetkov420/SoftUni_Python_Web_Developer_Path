from problem_solving_2.need_for_speed.project.car import Car


class FamilyCar(Car):

    DEFAULT_FUEL_CONSUMPTION = Car.DEFAULT_FUEL_CONSUMPTION

    def __init__(self, fuel: float, horse_power: int):
        super().__init__(fuel, horse_power)
        self.fuel_consumption = FamilyCar.DEFAULT_FUEL_CONSUMPTION
