import unittest


def validate_type(value, types):
    if type(value) not in types:
        raise ValueError('"numbers" should be numbers')


def my_sum(numbers):
    [validate_type(x, [int, float]) for x in numbers]
    return sum(numbers)


class SampleTest3(unittest.TestCase):

    def test_my_sum__when_ints_expect_to_be_equal(self):
        numbers = [1, 2, 3, 4, 5]
        actual_result = my_sum(numbers)
        expected_result = 15

        self.assertEqual(expected_result, actual_result)

    def test_my_sum__when_floats_expect_to_be_equal(self):
        numbers = [1.0, 2.0, 3.0, 4.0, 5.0]
        actual_result = my_sum(numbers)
        expected_result = 15

        self.assertEqual(expected_result, actual_result)

    def test_my_sum_when_strings__expected_value_exception(self):
        numbers = ['a', 'b', 'c']
        with self.assertRaises(ValueError) as context:
            my_sum(numbers)


class SampleTest4(unittest.TestCase):

    def test_my_sum__when_ints_expect_to_be_equal(self):
        numbers = [1, 2, 3, 4, 5]
        actual_result = my_sum(numbers)
        expected_result = 15

        self.assertEqual(expected_result, actual_result)

    def test_my_sum__when_floats_expect_to_be_equal(self):
        numbers = [1.0, 2.0, 3.0, 4.0, 5.0]
        actual_result = my_sum(numbers)
        expected_result = 15

        self.assertEqual(expected_result, actual_result)

    def test_my_sum_when_strings__expected_value_exception(self):
        numbers = ['a', 'b', 'c']
        with self.assertRaises(ValueError) as context:
            my_sum(numbers)