import unittest
from unittest import mock

from validators import TypeValidator
from utills import Utills


class SampleTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        # For general logic for all test -> 1 execution
        print("setUpClass")

    @classmethod
    def tearDownClass(cls):
        # Logic here is executed when all test are executed
        print("TearDownClass..")

    def tearDown(self):
        # executes when execute all tests
        print("TearDown..")

    def setUp(self):
        # We can put general logic from all tests here.. -> tests count executions
        print("SetUp..")

    # test_names conventions
    # when_ints__utils_sum__expect_correct(pure AAA)
    # act__arrange__assert
    # assert arrange act

    # test_utilsSum_whenInts_expectCorrect
    @mock.patch('validators.TypeValidator.validate_type')
    def test_utils_my_sum__when_ints_expect_correct(self, validate_type_mock):
        # Arrange == prepare
        validator = validate_type_mock.return_value
        validator.validate_type.return_value = None
        utils = Utills()
        numbers = [1, 2, 3, 4, 5]

        # Act
        actual_result = utils.my_sum(numbers)

        # Assert
        expected_result = 15
        self.assertEqual(expected_result, actual_result)

    def test_my_sum__when_floats_expect_correct (self):
        # Arrange
        numbers = [1.0, 2.0, 3.0, 4.0, 5.3]
        utils = Utills()

        # Act
        actual_result = utils.my_sum(numbers)

        # Assert
        expected_result = 15.0
        self.assertEqual(expected_result, actual_result, "Actual result is not equal to expected!")

    def test_my_sum_when_strings__expected_value_exception(self):
        numbers = ['a', 'b', 'c']
        utils = Utills()

        with self.assertRaises(ValueError) as context:
            utils.my_sum(numbers)

        expected_message = '"numbers" should be ints or floats'
        actual_message = context.exception.args[0]

        self.assertEqual(expected_message, actual_message)


class SampleTest2(unittest.TestCase):

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
