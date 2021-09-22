from problem_solving_2.need_for_speed.project.motorcycle import Motorcycle


class CrossMotorcycle(Motorcycle):

    DEFAULT_FUEL_CONSUMPTION = Motorcycle.DEFAULT_FUEL_CONSUMPTION

    def __init__(self, fuel: float, horse_power: int):
        super().__init__(fuel, horse_power)
