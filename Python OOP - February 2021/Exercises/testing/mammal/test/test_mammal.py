from project.mammal import Mammal
from unittest import TestCase, main


class TestMammal(TestCase):

    def setUp(self):
        self.mammal = Mammal("Toby", "Dolphin", "prrrrr-prrrrrrr-prr")

    def test_mammal_contructor_expected_correct(self):
        mammal2 = Mammal("Toby", "Dolphin", "prrrrr-prrrrrrr-prr")

        self.assertEqual("Toby", mammal2.name)
        self.assertEqual("Dolphin", mammal2.type)
        self.assertEqual("prrrrr-prrrrrrr-prr", mammal2.sound)
        self.assertEqual("animals", mammal2.get_kingdom())

    def test__mammal_make_sound__expect_correct(self):
        expected_result = f"Toby makes prrrrr-prrrrrrr-prr"
        actual_result = self.mammal.make_sound()

        self.assertEqual(expected_result, actual_result)

    def test__mammal_get_kingdom_expected_corect(self):
        expected_result = "animals"
        actual_result = self.mammal.get_kingdom()

        self.assertEqual(expected_result, actual_result)

    def test__mammal_info_expected_correct(self):
        expected_result = f"Toby is of type Dolphin"
        actual_result = self.mammal.info()

        self.assertEqual(expected_result, actual_result)

if __name__ == "__main__":
    main()