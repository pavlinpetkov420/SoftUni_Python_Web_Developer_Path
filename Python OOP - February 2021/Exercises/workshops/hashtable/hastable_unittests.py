from hastable import HashTable
from unittest import TestCase, main


class TestHashTable(TestCase):

    def setUp(self):
        self.hash_table = HashTable()

    def test_attribtes(self):
        self.assertEqual(4, len(self.hash_table.keys))
        self.assertEqual(4, len(self.hash_table.values))
        self.assertEqual(4, self.hash_table.max_capacity)

    def test_add_with_available_space(self):
        self.hash_table.add('test_key_1', 'Value_1')
        self.assertEqual(1, self.hash_table.actual_lenght)
        self.assertEqual(4, self.hash_table.max_capacity)
        self.assertEqual('Value_1', self.hash_table['test_key_1'])

    def test_add_with_no_available_space_resize_lists(self):
        for number in range(1, self.hash_table.max_capacity + 1):
            self.hash_table.add(f'Test_Key_{number}', f'Value_{number**2}')

        self.assertEqual(4, self.hash_table.actual_lenght)
        self.assertEqual(4, self.hash_table.max_capacity)

        # Here we are overload the dict and it should resize

        self.hash_table.add('Test_Key_5', 'Value_5')
        self.assertEqual(5, self.hash_table.actual_lenght)
        self.assertEqual(8, self.hash_table.max_capacity)
        self.assertIn('Test_Key_5', self.hash_table.keys)

    def test_value_is_replaced_when_key_exist(self):
        self.hash_table.add('test_key', 'Value')
        self.assertEqual('Value', self.hash_table['test_key'])
        self.hash_table['test_key'] = 'New_Value'
        self.assertEqual('New_Value', self.hash_table['test_key'])

    def test_get_with_existing_key(self):
        self.hash_table.add('test_key', 'value')
        self.assertEqual('value', self.hash_table.get('test_key'))

    def test_get_without_existing_key(self):
        self.hash_table.add('test_key', 'value')
        self.assertIsNone(None, self.hash_table.get('diff_key'))

    def test_get_without_existing_key_with_default_value(self):
        self.hash_table.add('test_key', 'value')
        self.assertEqual('DEFAULT', self.hash_table.get('not_existing', 'DEFAULT'))

    def test_representation(self):
        self.hash_table.add('test_key_1', 'value_1')
        self.assertEqual('{test_key_1: value_1}', str(self.hash_table))

    def test_collision_set_next_available_index(self):
        self.hash_table["name"] = 'Peter'
        self.assertEqual(1, self.hash_table.keys.index('name'))
        # collision with index 1
        self.hash_table['age'] = 25
        self.assertEqual(2, self.hash_table.keys.index('age'))

    def test_collision_set_next_available_index_at_0(self):
        self.hash_table["name"] = 'Peter'
        self.assertEqual(1, self.hash_table.keys.index('name'))

        # collision with index 1
        self.hash_table['age'] = 25
        self.assertEqual(2, self.hash_table.keys.index('age'))

        self.hash_table['car'] = 'Tesla Model S'
        self.assertEqual(3, self.hash_table.keys.index('car'))

        # Go back to index 0, no other is available
        self.hash_table['favourite food'] = 'Duner Box from City Food <3'
        self.assertEqual(0, self.hash_table.keys.index('favourite food'))
