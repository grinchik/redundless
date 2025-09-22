import unittest

from multiline_file_entry_list import multiline_file_entry_list
from duplicated_subtree_list import duplicated_subtree_list

from duplicated_subtrees_types import FileEntryList
from duplicated_subtrees_types import DuplicatedSubTreeList

class TestDuplicatedSubtreeList(unittest.TestCase):
    # TODO: one/multiple level/s no duplicates
    # TODO: one/mupliple level/s multiple duplicates

    def test_one_level_sorted_two_duplicates(self):
        file_entry_list: FileEntryList = multiline_file_entry_list(
            [
                '\t'.join(['B', str(0), '/0/b']),
                '\t'.join(['C', str(0), '/0/c']),
                '\t'.join(['A', str(0), '/1/a']),
                '\t'.join(['B', str(0), '/1/b']),
                '\t'.join(['C', str(0), '/1/c']),
                '\t'.join(['D', str(0), '/1/d']),
                '\t'.join(['B', str(0), '/2/b']),
                '\t'.join(['C', str(0), '/2/c']),
            ]
        )

        result: DuplicatedSubTreeList = \
            duplicated_subtree_list(file_entry_list)

        expected_result = [
            [
                '/0',
                '/2',
            ],
        ]

        self.assertEqual(result, expected_result)

    def test_one_level_unsorted_duplicates(self):
        file_entry_list: FileEntryList = multiline_file_entry_list(
            [
                '\t'.join(['D', str(0), '/1/d']),
                '\t'.join(['C', str(0), '/0/c']),
                '\t'.join(['A', str(0), '/1/a']),
                '\t'.join(['B', str(0), '/2/b']),
                '\t'.join(['B', str(0), '/0/b']),
                '\t'.join(['C', str(0), '/1/c']),
                '\t'.join(['C', str(0), '/2/c']),
                '\t'.join(['B', str(0), '/1/b']),
            ]
        )

        result: DuplicatedSubTreeList = \
            duplicated_subtree_list(file_entry_list)

        expected_result = [
            [
                '/0',
                '/2',
            ],
        ]

        self.assertEqual(result, expected_result)

    def test_multi_levels_sorted_duplicates(self):
        file_entry_list: FileEntryList = multiline_file_entry_list(
            [
                '\t'.join(['B', str(0), '/0/b']),
                '\t'.join(['C', str(0), '/0/1/c']),
                '\t'.join(['D', str(0), '/0/1/2/d']),

                '\t'.join(['D', str(0), '/1/d']),
                '\t'.join(['A', str(0), '/1/a']),
                '\t'.join(['B', str(0), '/1/b']),
                '\t'.join(['C', str(0), '/1/c']),

                '\t'.join(['B', str(0), '/2/b']),
                '\t'.join(['C', str(0), '/2/1/c']),
                '\t'.join(['D', str(0), '/2/1/2/d']),

                '\t'.join(['B', str(0), '/3/b']),
                '\t'.join(['C', str(0), '/3/1/c']),
                '\t'.join(['D', str(0), '/3/1/2/d']),
            ]
        )

        result: DuplicatedSubTreeList = \
            duplicated_subtree_list(file_entry_list)

        expected_result = [
            [
                '/0',
                '/2',
                '/3',
            ],
            [
                '/0/1',
                '/2/1',
                '/3/1',
            ],
            [
                '/0/1/2',
                '/2/1/2',
                '/3/1/2',
            ],
        ]

        self.assertEqual(result, expected_result)

    def test_multi_levels_unsorted_duplicates(self):
        file_entry_list: FileEntryList = multiline_file_entry_list(
            [
                '\t'.join(['D', str(0), '/1/d']),
                '\t'.join(['B', str(0), '/1/b']),

                '\t'.join(['B', str(0), '/2/b']),
                '\t'.join(['C', str(0), '/2/1/c']),
                '\t'.join(['D', str(0), '/2/1/2/d']),

                '\t'.join(['A', str(0), '/1/a']),
                '\t'.join(['C', str(0), '/1/c']),

                '\t'.join(['B', str(0), '/3/b']),
                '\t'.join(['C', str(0), '/3/1/c']),
                '\t'.join(['D', str(0), '/3/1/2/d']),

                '\t'.join(['B', str(0), '/0/b']),
                '\t'.join(['C', str(0), '/0/1/c']),
                '\t'.join(['D', str(0), '/0/1/2/d']),
            ]
        )

        result: DuplicatedSubTreeList = \
            duplicated_subtree_list(file_entry_list)

        expected_result = [
            [
                '/2',
                '/3',
                '/0',
            ],
            [
                '/2/1',
                '/3/1',
                '/0/1',
            ],
            [
                '/2/1/2',
                '/3/1/2',
                '/0/1/2',
            ],
        ]

        self.assertEqual(result, expected_result)

    def test_multi_levels_with_proxy_sorted_duplicates(self):
        file_entry_list: FileEntryList = multiline_file_entry_list(
            [
                '\t'.join(['G', str(0), '/0/0/1/g']),
                '\t'.join(['G', str(0), '/0/0/2/g']),
                '\t'.join(['G', str(0), '/0/1/1/g']),
                '\t'.join(['G', str(0), '/0/1/2/g']),
            ]
        )

        result: DuplicatedSubTreeList = \
            duplicated_subtree_list(file_entry_list)

        expected_result = [
            [
                '/0/0/1',
                '/0/0/2',
                '/0/1/1',
                '/0/1/2',
            ],
            [
                '/0/0',
                '/0/1',
            ],
        ]

        self.assertEqual(result, expected_result)

    def test_multi_levels_with_proxy_unsorted_duplicates(self):
        file_entry_list: FileEntryList = multiline_file_entry_list(
            [
                '\t'.join(['G', str(0), '/0/0/2/g']),
                '\t'.join(['G', str(0), '/0/1/1/g']),
                '\t'.join(['G', str(0), '/0/0/1/g']),
                '\t'.join(['G', str(0), '/0/1/2/g']),
            ]
        )

        result: DuplicatedSubTreeList = \
            duplicated_subtree_list(file_entry_list)

        expected_result = [
            [
                '/0/0/2',
                '/0/1/1',
                '/0/0/1',
                '/0/1/2'
            ],
            [
                '/0/0',
                '/0/1'
            ],
        ]

        self.assertEqual(result, expected_result)

if __name__ == '__main__':
    unittest.main()
