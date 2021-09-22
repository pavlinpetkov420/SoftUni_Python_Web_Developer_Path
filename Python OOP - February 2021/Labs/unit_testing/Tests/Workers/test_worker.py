
from Worker.worker import Worker
import unittest


class WorkerTests(unittest.TestCase):

    name = "Filip"
    salary = 3500.45
    energy = 68

    def setUp(self):
        self.worker = Worker(self.name, self.salary, self.energy)

    def test_init__when_correct_args_should_be_initialized(self):
        # Test if the worker is initialized with correct name, salary and energy
        # Assert
        self.assertEqual(self.name, self.worker.name)
        self.assertEqual(self.salary, self.worker.salary)
        self.assertEqual(self.energy, self.worker.energy)

    def test_is_energy_incremented__after_rest_method(self):
        # Test if the worker's energy is incremented after the rest method is called
        self.worker.rest()
        self.assertEqual(self.energy + 1, self.worker.energy)

    def test_is_error_raise__after_negative_energy(self):
        # Test if an error is raised if the worker tries to work with negative energy or equal to 0
        self.worker.energy = 0
        with self.assertRaises(Exception):
            self.worker.work()

    def test_is_money_increased__after_work_method(self):
        # Test if the worker's money is increased by his salary correctly after the work method is called

        self.worker.work()
        self.worker.work()

        self.assertEqual(self.salary * 2, self.worker.money)

    def test_is_energy_decrease__after_work_method_called(self):
        # Test if the worker's energy is decreased after the work method is called
        expected_result = self.energy - 1
        self.worker.work()
        actual_result = self.worker.energy

        self.assertEqual(expected_result, actual_result)

    def is__get_info__returns_correct_info(self):
        # Test if the get_info method returns the proper string with correct values
        expected = f'{self.name} has saved 0 money.'
        actual = self.worker.get_info()
        self.assertEqual(expected, actual)


if __name__ == '__main__':
    unittest.main()
