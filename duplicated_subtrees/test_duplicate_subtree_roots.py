import unittest

from duplicate_subtree_roots import duplicate_subtree_roots

from duplicated_subtrees_types import FileEntryList

class TestDuplicateSubtreeRoots(unittest.TestCase):
    def test_empty_file_entry_list(self):
        file_entry_list: FileEntryList = []

        expected_result = []

        actual_result = duplicate_subtree_roots(file_entry_list)
        self.assertEqual(actual_result, expected_result)

    def test_single_file(self):
        file_entry_list: FileEntryList = [
            ('A', 0, '/a'),
        ]

        expected_result = []

        actual_result = duplicate_subtree_roots(file_entry_list)
        self.assertEqual(actual_result, expected_result)

    def test_root_level_two_duplicates(self):
        file_entry_list: FileEntryList = [
            ('A', 0, '/0/a'),
            ('A', 0, '/1/a'),
        ]

        expected_result = [
            (
                frozenset([
                    ('A', 0),
                ]),
                [
                    '/0',
                    '/1',
                ],
            ),
        ]

        actual_result = duplicate_subtree_roots(file_entry_list)
        self.assertEqual(actual_result, expected_result)

    def test_root_level_tree_duplicates(self):
        file_entry_list: FileEntryList = [
            ('A', 0, '/0/a'),
            ('A', 0, '/1/a'),
            ('A', 0, '/2/a'),
        ]

        expected_result = [
            (
                frozenset([
                    ('A', 0),
                ]),
                [
                    '/0',
                    '/1',
                    '/2',
                ],
            ),
        ]

        actual_result = duplicate_subtree_roots(file_entry_list)
        self.assertEqual(actual_result, expected_result)

    def test_duplicates_with_proxy_directory(self):
        file_entry_list: FileEntryList = [
            ('A', 0, '/0/0/a'),
            ('A', 0, '/0/1/a'),
        ]

        expected_result = [
            (
                frozenset([
                    ('A', 0),
                ]),
                [
                    '/0/0',
                    '/0/1',
                ],
            ),
        ]

        actual_result = duplicate_subtree_roots(file_entry_list)
        self.assertEqual(actual_result, expected_result)

    def test_multiple_duplicate_subtrees(self):
        file_entry_list: FileEntryList = [
            ('A', 0, '/0/a'),
            ('A', 0, '/1/a'),
            ('B', 0, '/2/b'),
            ('B', 0, '/3/b'),
        ]

        expected_result = [
            (
                frozenset([
                    ('A', 0),
                ]),
                [
                    '/0',
                    '/1',
                ],
            ),
            (
                frozenset([
                    ('B', 0),
                ]),
                [
                    '/2',
                    '/3',
                ],
            ),
        ]

        actual_result = duplicate_subtree_roots(file_entry_list)
        self.assertEqual(actual_result, expected_result)

    def test_duplicates_with_unique_directory(self):
        file_entry_list: FileEntryList = [
            ('A', 0, '/0/a'),
            ('A', 0, '/1/a'),
            ('B', 0, '/2/b'),
            ('C', 0, '/3/c'),
        ]

        expected_result = [
            (
                frozenset([
                    ('A', 0),
                ]),
                [
                    '/0',
                    '/1',
                ],
            ),
        ]

        actual_result = duplicate_subtree_roots(file_entry_list)
        self.assertEqual(actual_result, expected_result)

    def test_all_directories_are_unique(self):
        file_entry_list: FileEntryList = [
            ('A', 0, '/0/a'),
            ('B', 0, '/1/b'),
            ('C', 0, '/2/c'),
            ('D', 0, '/3/d'),
        ]

        expected_result = [
        ]

        actual_result = duplicate_subtree_roots(file_entry_list)
        self.assertEqual(actual_result, expected_result)

    def test_not_root_level_duplicate_subtrees(self):
        file_entry_list: FileEntryList = [
            ('A', 0, '/0/0/a'),
            ('B', 0, '/0/0/0/b'),
            ('A', 0, '/1/0/a'),
            ('B', 0, '/1/0/0/b'),
        ]

        expected_result = [
            (
                frozenset([
                    ('A', 0),
                    ('B', 0),
                ]),
                [
                    '/0/0',
                    '/1/0',
                ],
            ),
        ]

        actual_result = duplicate_subtree_roots(file_entry_list)
        self.assertEqual(actual_result, expected_result)

    def test_mixes_levels_duplicate_subtrees(self):
        file_entry_list: FileEntryList = [
            ('A', 0, '/0/0/a'),
            ('A', 0, '/0/0/0/a'),
            ('B', 0, '/0/0/0/0/b'),
            ('C', 0, '/0/0/0/1/c'),

            ('A', 0, '/0/1/a'),
            ('A', 0, '/0/1/0/a'),
            ('B', 0, '/0/1/0/0/b'),
            ('C', 0, '/0/1/0/1/c'),

            ('A', 0, '/0/0/0/0/1/a'),
            ('A', 0, '/0/0/0/0/1/0/a'),
            ('B', 0, '/0/0/0/0/1/0/0/b'),
            ('C', 0, '/0/0/0/0/1/0/1/c'),

            ('A', 0, '/1/0/a'),
            ('A', 0, '/1/0/0/a'),
            ('B', 0, '/1/0/0/0/b'),
            ('C', 0, '/1/0/0/1/c'),
        ]

        expected_result = [
            (
                frozenset([
                    ('A', 0),
                    ('B', 0),
                    ('C', 0),
                ]),
                [
                    '/0/1',
                    '/0/0/0/0/1',
                    '/1/0',
                ],
            ),
        ]

        actual_result = duplicate_subtree_roots(file_entry_list)
        self.assertEqual(actual_result, expected_result)

    # TODO: Different hashes, same file names
    # TODO: Different file names, same hashes

if __name__ == '__main__':
    unittest.main()
