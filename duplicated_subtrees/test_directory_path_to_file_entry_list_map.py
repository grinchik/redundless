import unittest

from directory_path_to_file_entry_list_map import directory_path_to_file_entry_list_map
from directory_path_to_file_entry_list_map import DirectoryMap
from directory_path_to_file_entry_list_map import FileTuple

class TestDirectoryPathToFileEntryListMap(unittest.TestCase):
    def test_root_single_file(self):
        file_entry: FileTuple = ('A', 0, '/a')

        directory_map: DirectoryMap = {}
        directory_path_to_file_entry_list_map(directory_map, file_entry)

        expected_map: DirectoryMap = {
            '/': [
                file_entry,
            ],
        }

        self.assertEqual(directory_map, expected_map)

    def test_nested_single_file(self):
        file_entry: FileTuple = ('A', 0, '/0/0/a')

        directory_map: DirectoryMap = {}
        directory_path_to_file_entry_list_map(directory_map, file_entry)

        expected_map: DirectoryMap = {
            '/0/0': [
                file_entry,
            ],
            '/0': [
                file_entry,
            ],
            '/': [
                file_entry,
            ],
        }

        self.assertEqual(directory_map, expected_map)

    def test_multiple_files_same_directory(self):
        file_entry1: FileTuple = ('A', 0, '/0/0/a')
        file_entry2: FileTuple = ('B', 0, '/0/0/b')

        directory_map: DirectoryMap = {}
        directory_path_to_file_entry_list_map(directory_map, file_entry1)
        directory_path_to_file_entry_list_map(directory_map, file_entry2)

        expected_map: DirectoryMap = {
            '/0/0': [
                file_entry1,
                file_entry2,
            ],
            '/0': [
                file_entry1,
                file_entry2,
            ],
            '/': [
                file_entry1,
                file_entry2,
            ],
        }

        self.assertEqual(directory_map, expected_map)

    def test_multiple_files_same_directory_preserve_order(self):
        file_entry1: FileTuple = ('A', 0, '/a')
        file_entry2: FileTuple = ('B', 0, '/b')

        directory_map1: DirectoryMap = {}
        directory_path_to_file_entry_list_map(directory_map1, file_entry1)
        directory_path_to_file_entry_list_map(directory_map1, file_entry2)

        directory_map2: DirectoryMap = {}
        directory_path_to_file_entry_list_map(directory_map2, file_entry2)
        directory_path_to_file_entry_list_map(directory_map2, file_entry1)

        expected_map1: DirectoryMap = {
            '/': [
                file_entry1,
                file_entry2,
            ],
        }

        expected_map2: DirectoryMap = {
            '/': [
                file_entry2,
                file_entry1,
            ],
        }

        self.assertEqual(directory_map1, expected_map1)
        self.assertEqual(directory_map2, expected_map2)

    def test_accumulating_entries_different_directories(self):
        file_entry1: FileTuple = ('A', 0, '/0/0/a')
        file_entry2: FileTuple = ('B', 0, '/0/1/b')
        file_entry3: FileTuple = ('C', 0, '/1/0/c')

        directory_map: DirectoryMap = {}
        directory_path_to_file_entry_list_map(directory_map, file_entry1)
        directory_path_to_file_entry_list_map(directory_map, file_entry2)
        directory_path_to_file_entry_list_map(directory_map, file_entry3)

        expected_map: DirectoryMap = {
            '/0/0': [
                file_entry1,
            ],
            '/0/1': [
                file_entry2,
            ],
            '/0': [
                file_entry1,
                file_entry2,
            ],
            '/1/0': [
                file_entry3,
            ],
            '/1': [
                file_entry3,
            ],
            '/': [
                file_entry1,
                file_entry2,
                file_entry3,
            ],
        }

        self.assertEqual(directory_map, expected_map)

    def test_mutation_behavior(self):
        file_entry1: FileTuple = ('A', 0, '/0/b')

        directory_map: DirectoryMap = {
            '/tmp': [
                file_entry1
            ],
        }

        original_id = id(directory_map)

        file_entry2: FileTuple = ('B', 0, '/0/b')

        directory_path_to_file_entry_list_map(directory_map, file_entry2)

        self.assertEqual(id(directory_map), original_id)

        self.assertIn(file_entry2, directory_map['/0'])
        self.assertIn(file_entry2, directory_map['/'])

if __name__ == '__main__':
    unittest.main()
