from Cat.cat import Cat
import unittest


class CatTests(unittest.TestCase):

    name = "Pluto"

    def setUp(self):
        self.cat = Cat(self.name)

    def test_increasing_size__after_eat__expected_increased(self):
        # Cat's size is increased after eating
        expected_result = self.cat.size + 1
        self.cat.eat()
        actual_result = self.cat.size

        self.assertEqual(expected_result, actual_result)

    def test_cat_is_fed_after_eating__expected_True(self):
        # Cat is fed after eating
        self.cat.eat()

        self.assertEqual(self.cat.fed, True)

    def test_cat_cannot_eat_after_been_fed__expected_error(self):
        # Cat cannot eat if already fed, raises an error
        self.cat.eat()
        with self.assertRaises(Exception):
            self.cat.eat()

    def test_cat_cannot_sleep_before_been_fed_expected_error(self):
        # Cat cannot fall asleep if not fed, raises an error
        with self.assertRaises(Exception):
            self.cat.sleep()

    def test_cat_no_sleepy_after_sleeping_expecting_true(self):
        # Cat is not sleepy after sleeping
        expected_result = False
        self.cat.fed = True
        self.cat.sleep()
        actual_result = self.cat.sleepy

        self.assertEqual(expected_result, actual_result)


if __name__ == "__main__":
    unittest.main()
