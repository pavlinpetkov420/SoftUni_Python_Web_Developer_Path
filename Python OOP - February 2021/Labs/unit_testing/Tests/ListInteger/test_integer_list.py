from List.extended_list import IntegerList
import unittest


class TestIntegerList(unittest.TestCase):

    nums = (1, 2, 3, 4, 5, 6, 7)

    def setUp(self):
        self.int_list = IntegerList(*self.nums)

    def test__integer_list_constructor__expected_return_integers(self):
        numbers = (1, 2, 3, 4, 5, 6.9)
        extended_list = IntegerList(*numbers)

        expected_result = [1, 2, 3, 4, 5]
        actual_result = extended_list.get_data()
        self.assertListEqual(expected_result, actual_result)

    def test__integer_list__when_add_int_expected_to_add_it(self):
        expected_result = [1, 2, 3, 4, 5, 6, 7, 8]
        actual_result = self.int_list.add(8)

        self.assertListEqual(expected_result, actual_result)

    def test__integer_list__when_add_float__expected_value_error(self):

        with self.assertRaises(ValueError):
            self.int_list.add(5.6)

    def test__integer_list_when_remove_index__expected_to_remove_it(self):
        expected_result = 4
        actual_result = self.int_list.remove_index(3)

        self.assertEqual(expected_result, actual_result)

    def test__integer_list_when_remove_index__expectedto_raise_index_error(self):
        with self.assertRaises(IndexError):
            self.int_list.remove_index(9)

    def test__integer_list_when_get__expected_to_return_element(self):
        expected_result = 5
        actual_result = self.int_list.get(4)

        self.assertEqual(expected_result, actual_result)

    def test__integer_list_when_get__expected_to_raise_index_error(self):
        with self.assertRaises(IndexError):
            self.int_list.get(19)

    def test__integer_list_when_insert_int_expected_to_insert_it(self):
        expected_result = [1, 2, 3, 4, 5, 69, 6, 7]
        self.int_list.insert(5, 69)
        actual_result = self.int_list.get_data()
        self.assertListEqual(expected_result, actual_result)

    def test__integer_list_when_insert_str__expected_value_error(self):
        with self.assertRaises(ValueError):
            self.int_list.insert(5, 'wrong_value')

    def test__integer_list_when_insert_wrong_index__expected_index_error(self):
        with self.assertRaises(IndexError):
            self.int_list.insert(819, 6)

    def test__integer_list_when_get_biggest__expected_biggest_number(self):
        expected_result = 7
        actual_result = self.int_list.get_biggest()

        self.assertEqual(expected_result, actual_result)

    def test__integer_list_when_get_index__expected_index(self):
        expected_result = 3
        actual_result = self.int_list.get_index(4)

        self.assertEqual(expected_result, actual_result)


if __name__ == '__main__':
    unittest.main()
