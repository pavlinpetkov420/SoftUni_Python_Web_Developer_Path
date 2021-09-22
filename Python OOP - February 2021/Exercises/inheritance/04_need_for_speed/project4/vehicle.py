class Vehicle:
    DEFAULT_FUEL_CONSUMPTION = 1.25

    def __init__(self, fuel: float, horse_power: int):
        """
        public constructor with 2 attributes upon initialization
        and default value for fuel consumption
        :param fuel:
        :param horse_power:
        """
        self.fuel = fuel
        self.horse_power = horse_power
        self.fuel_consumption = Vehicle.DEFAULT_FUEL_CONSUMPTION

    def check_fuel(self, kilometers):
        fuel_needed = kilometers * self.fuel_consumption
        return fuel_needed <= self.fuel, float(fuel_needed)

    def drive(self, kilometers):
        is_enough, fuel_needed = self.check_fuel(kilometers)
        if is_enough:
            self.fuel -= fuel_needed
