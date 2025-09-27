import unittest

from collections import defaultdict

from directory_path_group_list import directory_path_group_list

from duplicated_subtrees_types import DirectoryMap

class TestDirectoryPathGroup(unittest.TestCase):
    def test_root_single_file(self):
        directory_map: DirectoryMap = defaultdict(list, {
            '/': [
                ('A', 0, 'a'),
            ],
        })

        result = \
            directory_path_group_list(directory_map)

        expected_result = [
            [
                '/',
            ],
        ]

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
            directory_path_group_list(directory_map)

        expected_result = [
            [
                '/0/0',
            ],
            [
                '/0',
            ],
            [
                '/',
            ],
        ]

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
            directory_path_group_list(directory_map)

        expected_result = [
            [
                '/0/0',
            ],
            [
                '/0',
            ],
            [
                '/',
            ],
        ]

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
            directory_path_group_list(directory_map)

        expected_result = [
            [
                '/1/0',
                '/0/0',
            ],
            [
                '/1',
                '/0',
            ],
            [
                '/',
            ],
        ]

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
            directory_path_group_list(directory_map)

        expected_result = [
            [
                '/0/0',
            ],
            [
                '/',
            ],
            [
                '/0',
            ],
        ]

        self.assertEqual(result, expected_result)

if __name__ == '__main__':
    unittest.main()
