from problem_solving_2.need_for_speed.project.motorcycle import Motorcycle


class RaceMotorcycle(Motorcycle):

    DEFAULT_FUEL_CONSUMPTION = 8

    def __init__(self, fuel: float, horse_power: int):
        super().__init__(fuel, horse_power)