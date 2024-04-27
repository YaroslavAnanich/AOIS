import unittest
import table

class TestHashTable(unittest.TestCase):
    def setUp(self):
        self.hash_table = table.HashTable(10)

    def test_insert_and_search(self):
        self.hash_table.insert('key1', 'value1')
        self.assertEqual(self.hash_table.search('key1'), 'value1')

    def test_delete(self):
        self.hash_table.insert('key2', 'value2')
        self.hash_table.delete('key2')
        self.assertIsNone(self.hash_table.search('key2'))

    def test_insert_collision(self):
        self.hash_table.insert('key3', 'value3')
        self.hash_table.insert('key4', 'value4')
        self.assertEqual(self.hash_table.search('key3'), 'value3')
        self.assertEqual(self.hash_table.search('key4'), 'value4')