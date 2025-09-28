import unittest

from collections import defaultdict

from directory_path_list_by_file_entity_list_set import directory_path_list_by_file_entity_list_set

from duplicated_subtrees_types import DirectoryMap

class TestDirectoryPathListByFileEntityListSet(unittest.TestCase):
    def test_root_single_file(self):
        directory_map: DirectoryMap = defaultdict(list, {
            '/': [
                ('A', 0, 'a'),
            ],
        })

        result = \
            directory_path_list_by_file_entity_list_set(directory_map)

        expected_result = {
            frozenset([
                ('A', 0, 'a'),
            ]): [
                '/',
            ],
        }

        self.assertEqual(result, expected_result)

    def test_nested_single_file(self):
        directory_map: DirectoryMap = defaultdict(list, {
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

        result = \
            directory_path_list_by_file_entity_list_set(directory_map)

        expected_result = {
            frozenset([
                ('A', 0, 'a'),
            ]): [
                '/0/0',
            ],
            frozenset([
                ('A', 0, '0/a'),
            ]): [
                '/0',
            ],
            frozenset([
                ('A', 0, '0/0/a'),
            ]): [
                '/',
            ],
        }

        self.assertEqual(result, expected_result)

    def test_multiple_files_same_directory_no_duplicates(self):
        directory_map: DirectoryMap = defaultdict(list, {
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

        result = \
            directory_path_list_by_file_entity_list_set(directory_map)

        expected_result = {
            frozenset([
                ('A', 0, 'a'),
                ('B', 0, 'b'),
            ]): [
                '/0/0',
            ],
            frozenset([
                ('A', 0, '0/a'),
                ('B', 0, '0/b'),
            ]): [
                '/0',
            ],
            frozenset([
                ('A', 0, '0/0/a'),
                ('B', 0, '0/0/b'),
            ]): [
                '/',
            ],
        }

        self.assertEqual(result, expected_result)

    def test_multiple_files_same_directory_with_duplicates(self):
        directory_map: DirectoryMap = defaultdict(list, {
            '/1/0': [
                ('A', 0, 'a'),
                ('B', 0, 'b'),
            ],
            '/1': [
                ('A', 0, '0/a'),
                ('B', 0, '0/b'),
            ],
            '/0/0': [
                ('A', 0, 'a'),
                ('B', 0, 'b'),
            ],
            '/0': [
                ('A', 0, '0/a'),
                ('B', 0, '0/b'),
            ],
            '/': [
                ('A', 0, '1/0/a'),
                ('B', 0, '1/0/b'),
                ('A', 0, '0/0/a'),
                ('B', 0, '0/0/b'),
            ],
        })

        result = \
            directory_path_list_by_file_entity_list_set(directory_map)

        expected_result = {
            frozenset([
                ('A', 0, 'a'),
                ('B', 0, 'b'),
            ]): [
                '/1/0',
                '/0/0',
            ],
            frozenset([
                ('A', 0, '0/a'),
                ('B', 0, '0/b'),
            ]): [
                '/1',
                '/0',
            ],
            frozenset([
                ('A', 0, '1/0/a'),
                ('B', 0, '1/0/b'),
                ('A', 0, '0/0/a'),
                ('B', 0, '0/0/b'),
            ]): [
                '/',
            ],
        }

        self.assertEqual(result, expected_result)

    def test_multiple_files_same_directory_preserve_order(self):
        directory_map: DirectoryMap = defaultdict(list, {
            '/0/0': [
                ('A', 0, 'a'),
                ('B', 0, 'b'),
            ],
            '/': [
                ('A', 0, '0/0/a'),
                ('B', 0, '0/0/b'),
            ],
            '/0': [
                ('A', 0, '0/a'),
                ('B', 0, '0/b'),
            ],
        })

        result = \
            directory_path_list_by_file_entity_list_set(directory_map)

        expected_result = {
            frozenset([
                ('A', 0, 'a'),
                ('B', 0, 'b'),
            ]): [
                '/0/0',
            ],
            frozenset([
                ('A', 0, '0/0/a'),
                ('B', 0, '0/0/b'),
            ]): [
                '/',
            ],
            frozenset([
                ('A', 0, '0/a'),
                ('B', 0, '0/b'),
            ]): [
                '/0',
            ],
        }

        self.assertEqual(result, expected_result)

if __name__ == '__main__':
    unittest.main()
