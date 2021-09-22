# from project.hero import Hero
import unittest
from hero.project.hero import Hero


class HeroTest(unittest.TestCase):

    def setUp(self):

        self.my_username = 'Sigma'
        self.my_level = 24
        self.my_health = 1840
        self.my_damage = 83

        self.enemy_username = "RoadHog"
        self.enemy_level = 23
        self.enemy_health = 1992
        self.enemy_damage = 80

        self.my_hero = Hero(self.my_username, self.my_level, self.my_health, self.my_damage)
        self.enemy_hero = Hero(self.enemy_username, self.enemy_level, self.enemy_health, self.enemy_damage)

    def test__hero_battle_when_both_usernames_are_eq__expected_exception(self):
        my_hero_copy = Hero(self.my_username, self.my_level, self.my_health, self.my_damage)

        with self.assertRaises(Exception) as context:
            self.my_hero.battle(my_hero_copy)

        expected_result = "You cannot fight yourself"
        actual_result = str(context.exception)

        self.assertEqual(expected_result, actual_result)

    def test__hero_battle_when_my_hero_hp_le_0__expected_exception(self):
        self.my_hero.health = 0
        expected_result = "Your health is lower than or equal to 0. You need to rest"

        with self.assertRaises(Exception) as context:
            self.my_hero.battle(self.enemy_hero)

        actual_result = str(context.exception)

        self.assertEqual(expected_result, actual_result)

    def test__hero_battle_when_enemy_hero_hp_le_0__expected_exception(self):
        expected_result = f"You cannot fight {self.enemy_hero.username}. He needs to rest"
        self.enemy_hero.health = -13

        with self.assertRaises(Exception) as context:
            self.my_hero.battle(self.enemy_hero)

        actual_result = str(context.exception)

        self.assertEqual(expected_result, actual_result)

    def test__hero_battle_when_both_heroes_hp_are_le_0_expected_draw(self):
        expected_result = "Draw"
        actual_result = self.my_hero.battle(self.enemy_hero)

        self.assertEqual(expected_result, actual_result)

    def test__hero_battle_when_my_hero_hp_lt_0__expected_lose(self):
        expected_result = "You lose"
        self.my_hero.damage = 79
        self.enemy_hero.damage = 99
        actual_result = self.my_hero.battle(self.enemy_hero)

        self.assertEqual(expected_result, actual_result)

    def test__hero_battle_when_enemy_hero_hp_lt_0__expected_lose(self):
        expected_result = "You win"

        self.enemy_hero.damage -= 10
        self.my_hero.damage += 10

        actual_result = self.my_hero.battle(self.enemy_hero)

        self.assertEqual(expected_result, actual_result)

    def test_hero_my_hero__str___expected_eq(self):
        expected_result = f"Hero {self.my_hero.username}: {self.my_hero.level} lvl\n" \
               f"Health: {self.my_hero.health}\n" \
               f"Damage: {self.my_hero.damage}\n"

        actual_result = self.my_hero.__str__()

        self.assertEqual(expected_result, actual_result)

    def test_hero_enemy_hero__str___expected_eq(self):
        expected_result = f"Hero {self.enemy_hero.username}: {self.enemy_hero.level} lvl\n" \
               f"Health: {self.enemy_hero.health}\n" \
               f"Damage: {self.enemy_hero.damage}\n"

        actual_result = self.enemy_hero.__str__()

        self.assertEqual(expected_result, actual_result)


if __name__ == "__main__":
    unittest.main()
