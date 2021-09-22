from CarManager.car_manager import Car
import unittest


class CarTests(unittest.TestCase):

    make = 'SpaceCruiser'
    model = 'PickleRickAdventureCar v3.14'
    fuel_consumption = 3.14
    fuel_capacity = 130

    def setUp(self):
        self.pickle_rick_car = Car(self.make, self.model, self.fuel_consumption, self.fuel_capacity)

    def test__car_make_setter_empty__expected_exception(self):
        with self.assertRaises(Exception) as context:
            self.pickle_rick_car.make = ''

        self.assertEqual("Make cannot be null or empty!", str(context.exception))

    def test__car_make_setter__expected_new_make(self):
        expected_make = 'ScaryTerryFamilyVan'
        self.pickle_rick_car.make = 'ScaryTerryFamilyVan'
        actual_make = self.pickle_rick_car.make

        self.assertEqual(expected_make, actual_make)

    def test__car_model_setter_empty__expected_exception(self):
        with self.assertRaises(Exception) as context:
            self.pickle_rick_car.model = ''

        self.assertEqual("Model cannot be null or empty!", str(context.exception))

    def test__car_model_setter__expected_new_model(self):
        expected_model = "YouCanRunButYouCan'tHideBitch"
        self.pickle_rick_car.model = "YouCanRunButYouCan'tHideBitch"
        actuasl_model = self.pickle_rick_car.model

        self.assertEqual(expected_model, actuasl_model)

    def test__car_fuel_consumption_0_or_below_setter__expected_exception(self):
        with self.assertRaises(Exception) as context:
            self.pickle_rick_car.fuel_consumption = -3.14

        expected_result = "Fuel consumption cannot be zero or negative!"
        actual_result = str(context.exception)

        self.assertEqual(expected_result, actual_result)

    def test__car_fuel_consumption_setter__expected_diff_fuel_consumption(self):
        expected_result = 6.9
        self.pickle_rick_car.fuel_consumption = 6.9
        actual_result = self.pickle_rick_car.fuel_consumption

        self.assertEqual(expected_result, actual_result)

    def test__car_fuel_capacity_setter_0_or_below__expected_exception(self):
        with self.assertRaises(Exception) as context:
            self.pickle_rick_car.fuel_capacity = -3.14

        expected_result = "Fuel capacity cannot be zero or negative!"
        actual_result = str(context.exception)

        self.assertEqual(expected_result, actual_result)

    def test__car_fuel_capacity_setter__expected_fuel_capacity(self):
        expected_result = 6.9
        self.pickle_rick_car.fuel_capacity = 6.9
        actual_result = self.pickle_rick_car.fuel_capacity

        self.assertEqual(expected_result, actual_result)

    def test__car_refuel__when_fuel_lt_0_expected_exception(self):
        with self.assertRaises(Exception) as context:
            self.pickle_rick_car.refuel(-96)

        expected_result = "Fuel amount cannot be zero or negative!"
        actual_result = str(context.exception)
        self.assertEqual(expected_result, actual_result)

    def test__car_refuel__when_fuel_bt_0_and_lt_capacity_expected_refuel_tank(self):
        self.pickle_rick_car.refuel(19)
        self.assertEqual(19, self.pickle_rick_car.fuel_amount)

    def test__car_refuel__when_fuel_bt_0_and_bt_capacity_expected_refuel_tank(self):
        self.pickle_rick_car.refuel(314.69)
        self.assertEqual(130, self.pickle_rick_car.fuel_amount)

    def test__car_drive__when_needed_bt_amount_fuel__expected_exception(self):
        self.pickle_rick_car.refuel(3.0)

        with self.assertRaises(Exception) as context:
            self.pickle_rick_car.drive(130)

        expected_result = "You don't have enough fuel to drive!"
        actual_result = str(context.exception)

        self.assertEqual(expected_result, actual_result)

    def test__car_drive__when_needed_eq_amount_fuel__expected_drive_distance(self):
        expexted_result = 0

        self.pickle_rick_car.refuel(6.28)
        self.pickle_rick_car.drive(200)
        actual_result = self.pickle_rick_car.fuel_amount

        self.assertEqual(expexted_result, actual_result)

    def test__car_drive__when_needed_lt_amount_fuel_expected_drive_distance(self):
        expected_result = 3.14
        self.pickle_rick_car.refuel(6.28)
        self.pickle_rick_car.drive(100)

        actual_result = self.pickle_rick_car.fuel_amount

        self.assertEqual(expected_result, actual_result)


if __name__ == '__main__':
    unittest.main()
