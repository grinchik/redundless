import unittest

from subtree_root_list import subtree_root_list

class TestSubTreeRootList(unittest.TestCase):
    def test_multiple_duplicates_same_level(self):
        subtree_list = [
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

        expected_result = [
            [
                '/2',
                '/3',
                '/0',
            ],
        ]

        result = subtree_root_list(subtree_list)

        self.assertEqual(result, expected_result)

if __name__ == '__main__':
    unittest.main()
