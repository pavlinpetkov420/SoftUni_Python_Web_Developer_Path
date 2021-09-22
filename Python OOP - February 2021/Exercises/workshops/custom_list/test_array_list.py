from unittest import TestCase

from custom_list.array_list import ArrayList


class TestArrayList(TestCase):

    def setUp(self):
        self.al = ArrayList()

    def test_append__when_list_is_empty__expect_append_to_the_end(self):
        self.al.append(1)
        values = list(self.al)

        self.assertListEqual([1], values)

    def test_append__expect_to_return_the_list(self):
        result = self.al.append(1)

        self.assertEqual(self.al, result)

    def test_append__1024_values__expect_append_to_the_end(self):

        values = [x for x in range(1024)]
        [self.al.append(x) for x in values]
        list_values = list(self.al)

        self.assertListEqual(values, list_values)

    def test_remove__when__index_is_valid__expect_remove_value_and_return_it(self):
        values_to_append = [1, 2, 3, 4, 5]
        for x in values_to_append:
            self.al.append(x)

        result = self.al.remove(2)

        self.assertListEqual([1, 2, 4, 5], list(self.al))
        self.assertEqual(3, result)

    def test_remove__when__index_is_invalid__expect_to_raise(self):
        values_to_append = [1, 2, 3, 4]
        for x in values_to_append:
            self.al.append(x)

        with self.assertRaises(IndexError):
            self.al.remove(self.al.size())

    def test_get__when__index_is_valid__expect_remove_value_and_return_it(self):
        values_to_append = [1, 2, 3, 4, 5]
        for x in values_to_append:
            self.al.append(x)

        result = self.al.get(2)

        self.assertListEqual([1, 2, 3, 4, 5], list(self.al))
        self.assertEqual(3, result)

    def test_get__when__index_is_invalid__expect_to_raise(self):
        values_to_append = [1, 2, 3, 4]
        for x in values_to_append:
            self.al.append(x)

        with self.assertRaises(IndexError):
            self.al.get(self.al.size())

    def test_extend__with_empty_iterable__expect_to_be_same(self):
        self.al.append(1)

        self.al.extend([])

        self.assertListEqual([1], list(self.al))

    def test_extend__with_list__expect_to_append_to_list(self):
        self.al.append(1)

        self.al.extend([2, 3])

        self.assertListEqual([1, 2, 3], list(self.al))

    def test_extend__with_generator__expect_to_be_same(self):
        self.al.append(1)

        self.al.extend(x for x in range(2, 3))

        self.assertListEqual([1, 2], list(self.al))

    def test_extend__when_empty__expect_to_append_to_the_list(self):

        self.al.extend(x for x in range(1, 3))

        self.assertListEqual([1, 2], list(self.al))

    def test_extend__with_not_iterable__expect_to_raise(self):
        self.al.append(1)

        with self.assertRaises(ValueError):
            self.al.extend(2)

    def test_insert__when__index_is_valid__expect_place_value_at_index(self):
        values_to_append = [1, 2, 4, 5, 6, 7, 8, 9]
        for x in values_to_append:
            self.al.append(x)

        self.al.insert(2, 33)

        self.assertListEqual([1, 2, 33, 4, 5, 6, 7, 8, 9], list(self.al))

    def test_insert__when__index_is_invalid__expect_to_raise(self):
        values_to_append = [1, 2, 3, 4]
        for x in values_to_append:
            self.al.append(x)

        with self.assertRaises(IndexError):
            self.al.remove(self.al.size())

    def test_pop__expect_to_remove_last_element(self):
        values_to_append = [1, 2, 3, 4]
        for x in values_to_append:
            self.al.append(x)

        result = self.al.pop()

        self.assertEqual(4, result)
        self.assertListEqual([1, 2, 3], list(self.al))

    def test_pop__when_empty__expect_to_raise(self):

        with self.assertRaises(IndexError):
            self.al.pop()

    def test_clear__expect_to_be_empty(self):
        [self.al.append(x) for x in range(15)]

        self.al.clear()
        self.assertListEqual([], list(self.al))

    def test_index__when_item_is_present__expect_return_correct_item(self):
        [self.al.append(x) for x in range(15)]

        index = self.al.index(5)

        self.assertEqual(5, index)

    def test_index__when_item_is_not_present__expect_raise(self):
        [self.al.append(x) for x in range(15)]

        with self.assertRaises(ValueError):
            self.al.index(17)

    def test_count__when_item_is_present_one_time__expect_return_1(self):
        [self.al.append(x) for x in range(15)]

        expected_count = 1
        actual_count = self.al.count(5)
        self.assertEqual(expected_count, actual_count)

    def test_count__when_item_is_present_multiple_times__expect_to_return_correct_count(self):
        [self.al.append(x) for x in range(15)]
        self.al.insert(3, 5)
        self.al.insert(14, 5)
        self.al.insert(7, 5)
        self.al.insert(10, 5)
        self.al.append(5)
        self.al.pop()

        expected_count = 5
        actual_count = self.al.count(5)
        self.assertEqual(expected_count, actual_count)

    def test_count__when_item_is_present_multiple_times_and_once_popped__expect_to_return_correct_count(self):
        [self.al.append(x) for x in range(15)]
        self.al.append(5)
        self.al.insert(3, 5)
        self.al.insert(14, 5)
        self.al.insert(7, 5)
        self.al.insert(10, 5)

        expected_count = 6
        actual_count = self.al.count(5)
        self.assertEqual(expected_count, actual_count)

    def test_count__when_item_is_not_present_times__expect_to_return_0(self):
        [self.al.append(x) for x in range(15)]

        expected_count = 0
        actual_count = self.al.count(55)
        self.assertEqual(expected_count, actual_count)

    def test_reverse__expect_in_reversed_order(self):
        [self.al.append(x) for x in range(5)]

        expected = [x for x in range(4, -1, -1)]
        actual = self.al.reverse()
        self.assertListEqual(expected, actual)

    def test_copy__expect_to_return_another_list_with_same_values(self):
        [self.al.append(x) for x in range(5)]

        copied_list = self.al.copy()

        expected = [x for x in range(5)]
        actual_result = list(copied_list)

        self.assertNotEqual(copied_list, self.al)
        self.assertListEqual(expected, actual_result)
