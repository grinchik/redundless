import unittest

from collections import defaultdict

from directory_path_to_file_entry_list_map import directory_path_to_file_entry_list_map
from directory_path_to_file_entry_list_map import DirectoryMap

class TestDirectoryPathToFileEntryListMap(unittest.TestCase):
    def test_root_single_file(self):
        directory_map: DirectoryMap = defaultdict(list)
        directory_path_to_file_entry_list_map(directory_map, ('A', 0, '/a'))

        expected_map: DirectoryMap = defaultdict(list, {
            '/': [
                ('A', 0, 'a'),
            ],
        })

        self.assertEqual(directory_map, expected_map)

    def test_nested_single_file(self):
        directory_map: DirectoryMap = defaultdict(list)
        directory_path_to_file_entry_list_map(directory_map, ('A', 0, '/0/0/a'))

        expected_map: DirectoryMap = defaultdict(list, {
            '/0/0': [
                ('A', 0, 'a'),
            ],
            '/0': [
                ('A', 0, '0/a'),
            ],
            '/': [
                ('A', 0, '0/0/a'),
            ],
        })

        self.assertEqual(directory_map, expected_map)

    def test_multiple_files_same_directory(self):
        directory_map: DirectoryMap = defaultdict(list)
        directory_path_to_file_entry_list_map(directory_map, ('A', 0, '/0/0/a'))
        directory_path_to_file_entry_list_map(directory_map, ('B', 0, '/0/0/b'))

        expected_map: DirectoryMap = defaultdict(list, {
            '/0/0': [
                ('A', 0, 'a'),
                ('B', 0, 'b'),
            ],
            '/0': [
                ('A', 0, '0/a'),
                ('B', 0, '0/b'),
            ],
            '/': [
                ('A', 0, '0/0/a'),
                ('B', 0, '0/0/b'),
            ],
        })

        self.assertEqual(directory_map, expected_map)

    def test_multiple_files_same_directory_preserve_order(self):
        directory_map1: DirectoryMap = defaultdict(list)
        directory_path_to_file_entry_list_map(directory_map1, ('A', 0, '/a'))
        directory_path_to_file_entry_list_map(directory_map1, ('B', 0, '/b'))

        directory_map2: DirectoryMap = defaultdict(list)
        directory_path_to_file_entry_list_map(directory_map2, ('B', 0, '/b'))
        directory_path_to_file_entry_list_map(directory_map2, ('A', 0, '/a'))

        expected_map1: DirectoryMap = defaultdict(list, {
            '/': [
                ('A', 0, 'a'),
                ('B', 0, 'b'),
            ],
        })

        expected_map2: DirectoryMap = defaultdict(list, {
            '/': [
                ('B', 0, 'b'),
                ('A', 0, 'a'),
            ],
        })

        self.assertEqual(directory_map1, expected_map1)
        self.assertEqual(directory_map2, expected_map2)

    def test_accumulating_entries_different_directories(self):
        directory_map: DirectoryMap = defaultdict(list)
        directory_path_to_file_entry_list_map(directory_map, ('A', 0, '/0/0/a'))
        directory_path_to_file_entry_list_map(directory_map, ('B', 0, '/0/1/b'))
        directory_path_to_file_entry_list_map(directory_map, ('C', 0, '/1/0/c'))

        expected_map: DirectoryMap = defaultdict(list, {
            '/0/0': [
                ('A', 0, 'a'),
            ],
            '/0/1': [
                ('B', 0, 'b'),
            ],
            '/0': [
                ('A', 0, '0/a'),
                ('B', 0, '1/b'),
            ],
            '/1/0': [
                ('C', 0, 'c'),
            ],
            '/1': [
                ('C', 0, '0/c'),
            ],
            '/': [
                ('A', 0, '0/0/a'),
                ('B', 0, '0/1/b'),
                ('C', 0, '1/0/c'),
            ],
        })

        self.assertEqual(directory_map, expected_map)

    def test_mutation_behavior(self):
        directory_map: DirectoryMap = defaultdict(list, {
            '/tmp': [
                ('A', 0, '/0/b'),
            ],
        })

        original_id = id(directory_map)

        directory_path_to_file_entry_list_map(directory_map, ('B', 0, '/0/b'))

        self.assertEqual(id(directory_map), original_id)

        self.assertIn(('B', 0, 'b'), directory_map['/0'])
        self.assertIn(('B', 0, '0/b'), directory_map['/'])

if __name__ == '__main__':
    unittest.main()
