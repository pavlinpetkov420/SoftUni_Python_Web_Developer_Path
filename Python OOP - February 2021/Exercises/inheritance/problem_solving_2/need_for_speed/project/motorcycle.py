from problem_solving_2.need_for_speed.project.vehicle import Vehicle


class Motorcycle(Vehicle):

    DEFAULT_FUEL_CONSUMPTION = Vehicle.DEFAULT_FUEL_CONSUMPTION

    def __init__(self, fuel: float, horse_power: int):
        super().__init__(fuel, horse_power)
        self.fuel_consumption = Motorcycle.DEFAULT_FUEL_CONSUMPTION

