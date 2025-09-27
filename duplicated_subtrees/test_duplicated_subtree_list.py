import unittest

from duplicated_subtree_list import duplicated_subtree_list

from duplicated_subtrees_types import DirectoryPathGroupList

class TestDuplicatedSubtreeList(unittest.TestCase):
    def test_no_groups_with_duplicates(self):
        input: DirectoryPathGroupList = [
            [
                '/0',
            ],
            [
                '/1',
            ],
        ]

        result = duplicated_subtree_list(input)

        expected_result = [
        ]

        self.assertEqual(result, expected_result)

    def test_mixed_groups(self):
        input: DirectoryPathGroupList = [
            [
                '/0',
                '/2',
            ],
            [
                '/1',
            ],
        ]

        result = duplicated_subtree_list(input)

        expected_result = [
            [
                '/0',
                '/2',
            ],
        ]

        self.assertEqual(result, expected_result)

    def test_multiple_groups_with_duplicates(self):
        input: DirectoryPathGroupList = [
            [
                '/0',
                '/2',
            ],
            [
                '/1',
                '/3',
            ],
        ]

        result = duplicated_subtree_list(input)

        expected_result = [
            [
                '/0',
                '/2',
            ],
            [
                '/1',
                '/3',
            ]
        ]

        self.assertEqual(result, expected_result)

if __name__ == '__main__':
    unittest.main()
